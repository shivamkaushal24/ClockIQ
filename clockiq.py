#!/usr/bin/env python3
"""
ClockIQ — Clock Tree Diagnostics & Optimization Assistant
==========================================================
Analyzes Synopsys Fusion Compiler CTS reports (Cheetah/R2G flow) and
produces structured diagnostics, root-cause hypotheses, and prioritized
debug recommendations.

Inputs:
  - File path to a .rpt/.log file  →  text parsed directly
  - Path to an apr_fc run area     →  Cheetah directory structure auto-discovered
  - Raw text string                →  analyzed in-memory

Outputs:
  Markdown report with 5 sections:
    1. Critical Issues   (🔴)
    2. Warnings          (🟡)
    3. Healthy Clocks    (🟢)
    4. Observations      (🔍)
    5. Recommended Actions (📋)

Usage (CLI):
    python3 clockiq.py <path_to_rpt_or_apr_fc_dir>
    python3 clockiq.py <path> > report.md
"""

import re
import sys
import csv
from pathlib import Path
from collections import defaultdict
from typing import Optional

# ─────────────────────────────────────────────────────────────────────────────
# Configurable Thresholds
# ─────────────────────────────────────────────────────────────────────────────
SKEW_THRESHOLD_PS        = 100    # 100 ps
INS_DELAY_THRESHOLD_PS   = 1000  # 1 ns
SKEW_IMBALANCE_RATIO     = 2.0   # flag if max_skew > 2× avg_skew
CLUSTER_VIOLATION_THRESH = 10    # >10 violations on one clock = clustered

# MBFF / Hold explosion thresholds
MBFF_HOLD_EXPLOSION_THRESH = 50_000   # >50K hold viols → MBFF clock push
MODERATE_HOLD_THRESH       = 1_000    # >1K hold viols  → moderate issue
# Setup clustering
SYSTEMIC_VIOLS_PER_CLOCK   = 50      # avg viols/clock → systemic CTS issue
LOCALIZED_VIOLS_PER_CLOCK  = 10      # avg viols/clock → localized

# ECO cost constants (per hold buffer)
HOLD_BUF_MULTIPLIER  = 2.5    # estimated hold buffers = violations × 2.5
HOLD_BUF_AREA_UM2    = 1.2    # µm² per hold buffer
HOLD_BUF_POWER_MW    = 0.005  # mW per hold buffer
HOLD_BUF_RATE        = 200    # buffers routed per hour

STAGE_ORDER = ["compile_final_opto", "clock_route_opt", "route_opt"]

# ─────────────────────────────────────────────────────────────────────────────
# 1. PARSING LAYER
# ─────────────────────────────────────────────────────────────────────────────

def parse_cts_report(text: str) -> dict:
    """
    Extract clock metrics, violations, and structural indicators from
    Fusion Compiler CTS report or log text.

    Returns:
        {
          "clocks": {
              "<name>": {
                  "skew_max_ps": float|None,
                  "skew_avg_ps": float|None,
                  "ins_delay_min_ps": float|None,
                  "ins_delay_max_ps": float|None,
                  "ins_delay_avg_ps": float|None,
                  "latency_ps": float|None,
                  "buffer_depth": int|None,
                  "setup_violations": int,
                  "hold_violations": int,
                  "worst_setup_slack_ps": float|None,
                  "worst_hold_slack_ps": float|None,
                  "endpoints": [],
              }
          },
          "global_setup_viols": int,
          "global_hold_viols": int,
          "warnings": [],        # parse-time warnings for missing/malformed sections
        }
    """
    result = {
        "clocks": defaultdict(lambda: {
            "skew_max_ps": None,
            "skew_avg_ps": None,
            "ins_delay_min_ps": None,
            "ins_delay_max_ps": None,
            "ins_delay_avg_ps": None,
            "latency_ps": None,
            "buffer_depth": None,
            "setup_violations": 0,
            "hold_violations": 0,
            "worst_setup_slack_ps": None,
            "worst_hold_slack_ps": None,
            "endpoints": [],
        }),
        "global_setup_viols": 0,
        "global_hold_viols": 0,
        "warnings": [],
    }

    # ── Clock skew table (FC CTS summary format) ─────────────────────────────
    # Pattern: "  <clock>  <skew_ns>  <ins_delay_ns>"
    skew_table = re.findall(
        r'^\s*(\S+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)',
        text, re.MULTILINE
    )
    for row in skew_table:
        name = row[0]
        if any(kw in name.lower() for kw in ("clock", "name", "---", "===")):
            continue
        clk = result["clocks"][name]
        try:
            clk["skew_max_ps"]       = float(row[1]) * 1000
            clk["ins_delay_min_ps"]  = float(row[2]) * 1000
            clk["ins_delay_max_ps"]  = float(row[3]) * 1000
            clk["ins_delay_avg_ps"]  = (float(row[2]) + float(row[3])) / 2 * 1000
        except (ValueError, IndexError):
            pass

    # ── Explicit "Clock skew" or "Skew" lines ────────────────────────────────
    for m in re.finditer(
        r'(?:clock\s+)?skew\s*[:\(=]\s*([\d.]+)\s*(ns|ps)?',
        text, re.IGNORECASE
    ):
        val_str, unit = m.group(1), (m.group(2) or "ns").lower()
        val_ps = float(val_str) * (1 if unit == "ps" else 1000)
        # Try to find associated clock name on same line
        line = text[max(0, m.start()-80):m.end()+20]
        clk_m = re.search(r'clock\s+["\']?(\w[\w/]+)', line, re.IGNORECASE)
        clk_name = clk_m.group(1) if clk_m else "__global__"
        c = result["clocks"][clk_name]
        if c["skew_max_ps"] is None or val_ps > c["skew_max_ps"]:
            c["skew_max_ps"] = val_ps

    # ── Insertion delay (clock network delay lines) ───────────────────────────
    ins_by_clock = defaultdict(list)
    for m in re.finditer(
        r'clock network delay \(propagated\)\s+([\d.]+)\s+([\d.]+)',
        text
    ):
        ins_by_clock["__last__"].append(float(m.group(2)) * 1000)

    # ── Path blocks: startpoint → extract clock + slack ──────────────────────
    blocks = re.split(r'(?=^\s{0,4}Startpoint:)', text, flags=re.MULTILINE)
    for block in blocks:
        slack_m = re.search(r'slack\s*\(VIOLATED\)\s+([-\d.]+)', block)
        if not slack_m:
            continue
        slack_ps = float(slack_m.group(1)) * 1000

        pg_m  = re.search(r'Path Group:\s*(\S+)', block)
        clk_m = re.search(r'(?:launched by|clocked by)\s+["\']?(\S+)["\']?', block, re.IGNORECASE)
        clk_name = clk_m.group(1) if clk_m else (pg_m.group(1) if pg_m else "__unknown__")

        # Determine setup vs hold from path type
        pt_m = re.search(r'Path Type:\s*(\S+)', block)
        path_type = (pt_m.group(1).lower() if pt_m else "max")

        c = result["clocks"][clk_name]
        if "min" in path_type or "hold" in path_type:
            c["hold_violations"] += 1
            result["global_hold_viols"] += 1
            if c["worst_hold_slack_ps"] is None or slack_ps < c["worst_hold_slack_ps"]:
                c["worst_hold_slack_ps"] = slack_ps
        else:
            c["setup_violations"] += 1
            result["global_setup_viols"] += 1
            if c["worst_setup_slack_ps"] is None or slack_ps < c["worst_setup_slack_ps"]:
                c["worst_setup_slack_ps"] = slack_ps

        # Extract endpoint
        ep_m = re.search(r'Endpoint:\s*(\S+)', block)
        if ep_m:
            c["endpoints"].append(ep_m.group(1))

    # ── Latency ───────────────────────────────────────────────────────────────
    for m in re.finditer(
        r'(?:clock\s+)?latency\s*[:\(=]\s*([\d.]+)\s*(ns|ps)?',
        text, re.IGNORECASE
    ):
        val_ps = float(m.group(1)) * (1 if (m.group(2) or "ns").lower() == "ps" else 1000)
        line   = text[max(0, m.start()-80):m.end()+20]
        clk_m  = re.search(r'clock\s+["\']?(\w[\w/]+)', line, re.IGNORECASE)
        clk_n  = clk_m.group(1) if clk_m else "__global__"
        result["clocks"][clk_n]["latency_ps"] = val_ps

    # ── Buffer depth ──────────────────────────────────────────────────────────
    for m in re.finditer(
        r'(?:buffer|tree)\s+depth\s*[:\(=]\s*(\d+)',
        text, re.IGNORECASE
    ):
        depth = int(m.group(1))
        line  = text[max(0, m.start()-80):m.end()+20]
        clk_m = re.search(r'clock\s+["\']?(\w[\w/]+)', line, re.IGNORECASE)
        clk_n = clk_m.group(1) if clk_m else "__global__"
        result["clocks"][clk_n]["buffer_depth"] = depth

    # ── Partial-data warnings ─────────────────────────────────────────────────
    if not result["clocks"]:
        result["warnings"].append(
            "No clock data detected. Ensure input is a Fusion Compiler CTS report."
        )
    for clk_n, c in result["clocks"].items():
        if c["skew_max_ps"] is None and c["ins_delay_avg_ps"] is None:
            result["warnings"].append(
                f"Clock '{clk_n}': no skew or insertion delay found — "
                "section may be missing or in unrecognised format."
            )

    result["clocks"] = dict(result["clocks"])
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Cheetah/R2G Directory-Based Parser  (Fusion Compiler real report layout)
# ─────────────────────────────────────────────────────────────────────────────
# Real layout inside apr_fc/:
#   reports/{stage}/fc.clock_qor.rpt                         ← skew, latency
#   reports/{stage}/analyze_timing_setup_violations.rpt.setup.txt
#   reports/{stage}/analyze_timing_hold_violations.rpt.hold.txt
#   reports/{stage}/fc.design_qor.rpt                        ← DRC counts
#   Clock_Cell_usage_my.rpt                                  ← clock cell CSV
#   HC_summary.rpt / HC.rpt                                  ← design checks
#   cts_high_delay_pins_CTS-*.rpt                            ← CTS DRC flags
# ─────────────────────────────────────────────────────────────────────────────

# Stages to probe (in flow order)
_FC_STAGES = ["cts", "compile_final_opto", "route_opt", "finish"]


def _discover_fc_files(run_area: Path) -> dict:
    """Discover real Fusion Compiler report files inside an apr_fc directory."""
    files = {
        "clock_qor":   {},   # stage → Path
        "setup_viols": {},   # stage → Path
        "hold_viols":  {},   # stage → Path
        "design_qor":  {},   # stage → Path
        "cts_violations":  [],
        "hc_summary":  None,
        "clock_cell_usage": None,
    }
    rpt_base = run_area / "reports"
    for stage in _FC_STAGES:
        sd = rpt_base / stage
        if not sd.exists():
            continue
        cqor = sd / "fc.clock_qor.rpt"
        if cqor.exists():
            files["clock_qor"][stage] = cqor
        sv = sd / "analyze_timing_setup_violations.rpt.setup.txt"
        if sv.exists():
            files["setup_viols"][stage] = sv
        hv = sd / "analyze_timing_hold_violations.rpt.hold.txt"
        if hv.exists():
            files["hold_viols"][stage] = hv
        dq = sd / "fc.design_qor.rpt"
        if dq.exists():
            files["design_qor"][stage] = dq

    for f in sorted(run_area.glob("cts_high_delay_pins_CTS-*.rpt")):
        files["cts_violations"].append(f)

    for hc_name in ("HC_summary.rpt", "HC.rpt"):
        hc = run_area / hc_name
        if hc.exists():
            files["hc_summary"] = hc
            break

    cc = run_area / "Clock_Cell_usage_my.rpt"
    if cc.exists():
        files["clock_cell_usage"] = cc

    return files


def _parse_fc_clock_qor(path: Path) -> dict:
    """
    Parse fc.clock_qor.rpt summary table.

    Returns:
        { clock_name: {"sinks":int, "levels":int, "repeaters":int,
                       "max_latency_ps":float, "global_skew_ps":float,
                       "trans_drc":int, "cap_drc":int,
                       "skew_groups":[{"name":str,"latency_ps":float,"skew_ps":float}]
                      }
        }
    """
    clocks = {}
    current_master = None

    try:
        text = path.read_text(errors="replace")
    except Exception:
        return clocks

    # Find the start of the actual summary table (after the Usage block)
    table_start = text.find("Clock /")
    if table_start < 0:
        return clocks
    text = text[table_start:]

    # Regex for master clock lines  (M attr, cols 7-8 are "--")
    # Format: <name> M <sinks> <levels> <repeater_cnt> <rep_area> <cell_area> -- -- <trans> <cap> <wire>
    re_master = re.compile(
        r'^(\S+)\s+M\s+(\d+)\s+(\d+)\s+(\d+)\s+'
        r'[\d.]+\s+[\d.]+\s+--\s+--\s+(\d+)\s+(\d+)',
        re.MULTILINE
    )
    # Regex for skew group lines  (D or U attr, cols 4-6 are "--", cols 7-8 have latency/skew)
    # Values in fc.clock_qor.rpt are reported in picoseconds.
    re_skwgrp = re.compile(
        r'^\s+(\S+)\s+[DU]\s+(\d+)\s+--\s+--\s+--\s+--\s+([\d.]+)\s+([\d.]+)',
        re.MULTILINE
    )
    # Also match Generated (G) clocks that have their own Max Latency / Global Skew
    re_gen = re.compile(
        r'^\s+(\S+)\s+G\s+\d+\s+\d+\s+\d+\s+[\d.]+\s+[\d.]+\s+([\d.]+)\s+([\d.]+)',
        re.MULTILINE
    )

    for m in re_master.finditer(text):
        name = m.group(1)
        clocks[name] = {
            "sinks":          int(m.group(2)),
            "levels":         int(m.group(3)),
            "repeaters":      int(m.group(4)),
            "trans_drc":      int(m.group(5)),
            "cap_drc":        int(m.group(6)),
            "max_latency_ps": None,
            "global_skew_ps": None,
            "skew_groups":    [],
        }

    # Associate skew groups and generated clocks with their master clock
    # (positional — each master's block ends at the next master's start).
    master_positions = []
    for m in re_master.finditer(text):
        master_positions.append((m.start(), m.group(1)))
    master_positions.append((len(text), None))   # sentinel

    for i, (pos, clk_name) in enumerate(master_positions[:-1]):
        next_pos = master_positions[i + 1][0]
        segment  = text[pos:next_pos]

        # D/U skew groups: columns 7-8 are latency and skew (in ps)
        for sg in re_skwgrp.finditer(segment):
            lat_ps  = float(sg.group(3))   # already in ps
            skew_ps = float(sg.group(4))   # already in ps
            clocks[clk_name]["skew_groups"].append({
                "name":       sg.group(1),
                "sinks":      int(sg.group(2)),
                "latency_ps": lat_ps,
                "skew_ps":    skew_ps,
            })
            c = clocks[clk_name]
            if c["max_latency_ps"] is None or lat_ps > c["max_latency_ps"]:
                c["max_latency_ps"] = lat_ps
            if c["global_skew_ps"] is None or skew_ps > c["global_skew_ps"]:
                c["global_skew_ps"] = skew_ps

        # G (Generated) clocks that have their own latency/skew reported
        for gg in re_gen.finditer(segment):
            lat_ps  = float(gg.group(2))
            skew_ps = float(gg.group(3))
            c = clocks[clk_name]
            if c["max_latency_ps"] is None or lat_ps > c["max_latency_ps"]:
                c["max_latency_ps"] = lat_ps

    return clocks


def _parse_fc_timing_violations(path: Path) -> dict:
    """
    Parse analyze_timing_{setup|hold}_violations.rpt.{setup|hold}.txt.

    Returns:
        {"total": int, "worst_slack_ps": float|None,
         "categorized": int, "uncategorized": int,
         "categories": {label: count},
         "large_clock_skew": int,
         "inter_clock": int}
    """
    result = {
        "total": 0, "worst_slack_ps": None,
        "categorized": 0, "uncategorized": 0,
        "categories": {}, "large_clock_skew": 0, "inter_clock": 0,
    }
    try:
        text = path.read_text(errors="replace")
    except Exception:
        return result

    m = re.search(r'Detect\s+(\d+)\s+violating paths', text)
    if m:
        result["total"] = int(m.group(1))

    m = re.search(r'Worst:\s*([-\d.]+)', text)
    if m:
        result["worst_slack_ps"] = float(m.group(1))   # already in ps

    m = re.search(r'(\d+)\s+violating paths are categorized', text)
    if m:
        result["categorized"] = int(m.group(1))

    m = re.search(r'(\d+)\s+violating paths are uncategorized', text)
    if m:
        result["uncategorized"] = int(m.group(1))

    # Extract individual categories (S1/H1 … )
    for cm in re.finditer(
        r'\*\s+category\s+[SH]\d+:\s+[^(]+\((\w+)\)\s+(\d+)', text
    ):
        result["categories"][cm.group(1)] = int(cm.group(2))

    result["large_clock_skew"] = result["categories"].get("LCS", 0)
    result["inter_clock"]      = result["categories"].get("ICVP", 0)

    return result


def _parse_hc_summary(path: Path) -> dict:
    checks = defaultdict(dict)
    if not path:
        return checks
    try:
        for line in path.read_text(errors="replace").splitlines():
            parts = line.split()
            if len(parts) >= 4:
                stage, check, count = parts[0], parts[2], parts[3]
                try:
                    checks[stage][check] = int(count)
                except ValueError:
                    checks[stage][check] = count
    except Exception:
        pass
    return checks


def _parse_clock_cell_usage(path: Path) -> dict:
    cells, total = {}, 0
    if not path:
        return {"cells": cells, "total": total}
    try:
        reader = csv.DictReader(
            path.read_text(errors="replace").splitlines()
        )
        for row in reader:
            cnt = int(row.get("cnt", 0))
            cells[row.get("ref_cell", "?")] = cnt
            total += cnt
    except Exception:
        pass
    return {"cells": cells, "total": total}


def parse_cts_directory(run_area: Path) -> dict:
    """
    Parse a Fusion Compiler apr_fc run area using the real FC report layout.
    Returns a data dict compatible with analyze_cts_data().
    """
    files = _discover_fc_files(run_area)
    data  = parse_cts_report("")   # start with empty structure

    # ── Determine the "best" stage (latest with data) ────────────────────────
    best_stage = None
    for stage in reversed(_FC_STAGES):
        if stage in files["clock_qor"] or stage in files["setup_viols"]:
            best_stage = stage
            break

    # ── Parse clock QoR from each available stage ────────────────────────────
    # Use the last (latest flow stage) available per-clock data.
    stage_clock_data = {}   # stage → {clock → {...}}
    for stage in _FC_STAGES:
        if stage in files["clock_qor"]:
            stage_clock_data[stage] = _parse_fc_clock_qor(files["clock_qor"][stage])

    # Merge clock QoR: populate data["clocks"] using latest stage that has data.
    all_clock_names = set()
    for d in stage_clock_data.values():
        all_clock_names.update(d.keys())

    def _blank_clock():
        return {
            "skew_max_ps": None, "skew_avg_ps": None,
            "ins_delay_min_ps": None, "ins_delay_max_ps": None,
            "ins_delay_avg_ps": None, "latency_ps": None,
            "buffer_depth": None,
            "setup_violations": 0, "hold_violations": 0,
            "worst_setup_slack_ps": None, "worst_hold_slack_ps": None,
            "endpoints": [],
            "_skew_groups": [],
            "_sinks": 0, "_levels": 0, "_repeaters": 0,
            "_trans_drc": 0, "_cap_drc": 0,
            "_stage_clock_data": {},
        }

    for clk_name in all_clock_names:
        c = _blank_clock()
        # Walk stages in order — later stages overwrite earlier
        for stage in _FC_STAGES:
            sd = stage_clock_data.get(stage, {})
            if clk_name not in sd:
                continue
            qd = sd[clk_name]
            c["_stage_clock_data"][stage] = qd
            c["_skew_groups"]  = qd["skew_groups"]
            c["_sinks"]        = qd["sinks"]
            c["_levels"]       = qd["levels"]
            c["_repeaters"]    = qd["repeaters"]
            c["_trans_drc"]    = qd["trans_drc"]
            c["_cap_drc"]      = qd["cap_drc"]
            if qd["global_skew_ps"] is not None:
                c["skew_max_ps"] = qd["global_skew_ps"]
            if qd["max_latency_ps"] is not None:
                c["latency_ps"]         = qd["max_latency_ps"]
                c["ins_delay_avg_ps"]   = qd["max_latency_ps"]
                c["ins_delay_max_ps"]   = qd["max_latency_ps"]
            c["buffer_depth"] = qd["repeaters"]
        data["clocks"][clk_name] = c

    # ── Parse timing violations ───────────────────────────────────────────────
    # For overall totals use the latest stage with violation files.
    best_setup_stage = best_stage
    best_hold_stage  = best_stage
    for stage in reversed(_FC_STAGES):
        if stage in files["setup_viols"] and best_setup_stage is None:
            best_setup_stage = stage
        if stage in files["hold_viols"] and best_hold_stage is None:
            best_hold_stage = stage

    setup_viol_data = {}
    hold_viol_data  = {}
    for stage in _FC_STAGES:
        if stage in files["setup_viols"]:
            setup_viol_data[stage] = _parse_fc_timing_violations(files["setup_viols"][stage])
        if stage in files["hold_viols"]:
            hold_viol_data[stage]  = _parse_fc_timing_violations(files["hold_viols"][stage])

    # Store per-stage violation summary and pick worst-stage totals
    data["_setup_by_stage"] = setup_viol_data
    data["_hold_by_stage"]  = hold_viol_data

    # Use route_opt or last available stage for global totals
    for stage in reversed(_FC_STAGES):
        if stage in setup_viol_data:
            sv = setup_viol_data[stage]
            data["global_setup_viols"] = sv["total"]
            data["_worst_setup_slack_ps"] = sv["worst_slack_ps"]
            data["_setup_lcs"] = sv["large_clock_skew"]
            break

    for stage in reversed(_FC_STAGES):
        if stage in hold_viol_data:
            hv = hold_viol_data[stage]
            data["global_hold_viols"] = hv["total"]
            data["_worst_hold_slack_ps"] = hv["worst_slack_ps"]
            data["_hold_icvp"] = hv["inter_clock"]
            break

    # Distribute violations across clocks proportionally (best effort)
    n_clocks = len(data["clocks"])
    if n_clocks and data["global_setup_viols"]:
        per_clk_s = data["global_setup_viols"] // n_clocks
        remainder = data["global_setup_viols"] % n_clocks
        for i, c in enumerate(data["clocks"].values()):
            c["setup_violations"] = per_clk_s + (1 if i < remainder else 0)
            c["worst_setup_slack_ps"] = data.get("_worst_setup_slack_ps")

    if n_clocks and data["global_hold_viols"]:
        per_clk_h = data["global_hold_viols"] // n_clocks
        remainder = data["global_hold_viols"] % n_clocks
        for i, c in enumerate(data["clocks"].values()):
            c["hold_violations"] = per_clk_h + (1 if i < remainder else 0)
            c["worst_hold_slack_ps"] = data.get("_worst_hold_slack_ps")

    # ── CTS DRC violation files ───────────────────────────────────────────────
    data["_cts_violations"] = []
    for f in files["cts_violations"]:
        code = re.search(r'CTS-(\d+)', f.name)
        code_str = f"CTS-{code.group(1)}" if code else "CTS-???"
        try:
            lines = f.read_text(errors="replace").splitlines()
            count = len([ln for ln in lines if ln.strip()])
            if count > 0:
                data["_cts_violations"].append(
                    {"code": code_str, "count": count, "file": f.name}
                )
        except Exception:
            pass

    data["_hc_checks"]        = _parse_hc_summary(files["hc_summary"])
    data["_clock_cell_usage"] = _parse_clock_cell_usage(files["clock_cell_usage"])
    data["_run_area"]         = str(run_area)
    data["_stage_order"]      = _FC_STAGES
    data["_best_stage"]       = best_stage
    return data


# ─────────────────────────────────────────────────────────────────────────────
# 2a. SPECIALIST ANALYSIS FUNCTIONS  (used inside analyze_cts_data)
# ─────────────────────────────────────────────────────────────────────────────

def analyze_hold_explosion(hold_count: int) -> dict:
    """
    Detect whether hold violations stem from MBFF clock push.
    Returns a structured diagnosis with ECO cost estimate.
    """
    if hold_count > MBFF_HOLD_EXPLOSION_THRESH:
        est_bufs   = int(hold_count * HOLD_BUF_MULTIPLIER)
        area_um2   = int(est_bufs * HOLD_BUF_AREA_UM2)
        power_mw   = round(est_bufs * HOLD_BUF_POWER_MW, 1)
        rt_hrs     = max(1, int(est_bufs / HOLD_BUF_RATE))
        sbit_flops = int(hold_count / 160)
        net_save   = int(area_um2 - sbit_flops * 2.5)
        return {
            "diagnosis":   "MBFF_CLOCK_PUSH_EXPLOSION",
            "confidence":  "HIGH",
            "severity":    "critical",
            "root_cause":  (
                f"{hold_count:,} hold violations indicates clock path was pushed on "
                "replicated MBFFs. Pushing clock on MBFF affects all bits → massive "
                "skew delta → hold violations at all startpoints simultaneously."
            ),
            "eco_cost": {
                "estimated_hold_buffers": est_bufs,
                "area_um2":              area_um2,
                "power_mw":              power_mw,
                "runtime_hours":         rt_hrs,
            },
            "recommended_fix": "REVERT clock push + DEBANK affected MBFFs",
            "commands": [
                "undo                                              # Revert last clock ECO",
                "set_multibit_options -exclude [get_cells {mbff_instances}]",
                "compile_clock_tree -incremental",
            ],
            "expected_outcome": (
                f"Add ~{sbit_flops:,} single-bit flops, avoid {est_bufs:,} hold buffers"
            ),
            "net_savings": (
                f"~{net_save:,} µm² area saved, ~{rt_hrs} hours runtime avoided"
            ),
        }
    elif hold_count > MODERATE_HOLD_THRESH:
        est_bufs = int(hold_count * 1.8)
        return {
            "diagnosis":   "MODERATE_HOLD_ISSUES",
            "confidence":  "MEDIUM",
            "severity":    "warning",
            "root_cause":  (
                "Likely due to localised clock skew or over-aggressive setup fixing "
                "pushing data paths too hard, creating hold exposure."
            ),
            "recommended_fix": "Targeted hold buffer insertion with `route_opt`",
            "commands": [
                "set_route_opt_strategy -hold_fixing true",
                "route_opt -incremental",
                "report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50",
            ],
            "eco_cost": {
                "estimated_hold_buffers": est_bufs,
                "runtime_hours":         max(1, int(est_bufs / HOLD_BUF_RATE)),
            },
        }
    else:
        return {
            "diagnosis":  "NORMAL_HOLD_FIXING",
            "confidence": "HIGH",
            "severity":   "info",
            "root_cause": "Hold count within normal range for post-CTS stage.",
        }


def analyze_setup_clustering(setup_count: int, clock_count: int) -> dict:
    """
    Determine whether setup violations are systemic (CTS-wide) or localised.
    Returns diagnosis, diagnostic steps, and ranked fix options with expected impact.
    """
    if clock_count == 0:
        return {"diagnosis": "NO_CLOCKS", "confidence": "LOW"}

    viol_per_clk = setup_count / clock_count

    if viol_per_clk > SYSTEMIC_VIOLS_PER_CLOCK:
        return {
            "diagnosis":   "SYSTEMIC_CTS_ISSUE",
            "confidence":  "HIGH",
            "severity":    "critical",
            "viol_per_clk": round(viol_per_clk, 1),
            "root_cause":  (
                f"Avg {viol_per_clk:.0f} violations/clock → global problem: "
                "likely skew budget, insertion delay, or floorplan."
            ),
            "diagnostic_steps": [
                "Check max skew per clock (if >150 ps → relax skew target)",
                "Check avg insertion delay (if >1.5 ns → over-buffering or congestion)",
                "Check violation distribution per module (if clustered → floorplan issue)",
            ],
            "fixes": [
                {
                    "hypothesis":           "Skew budget too tight",
                    "command":              "set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental",
                    "eco_cost":             "LOW (re-synthesis only)",
                    "expected_improvement": "30–50% violation reduction",
                },
                {
                    "hypothesis":           "Over-buffering inflating latency",
                    "command":              "set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental",
                    "eco_cost":             "MEDIUM (~200 buffers removed)",
                    "expected_improvement": "20–40% violation reduction",
                },
                {
                    "hypothesis":           "Floorplan congestion detour",
                    "command":              "report_congestion; check_placement -verbose",
                    "eco_cost":             "HIGH (floorplan change)",
                    "expected_improvement": "Up to 60% if hotspot resolved",
                },
            ],
        }
    elif viol_per_clk < LOCALIZED_VIOLS_PER_CLOCK:
        return {
            "diagnosis":   "LOCALIZED_VIOLATIONS",
            "confidence":  "MEDIUM",
            "severity":    "warning",
            "viol_per_clk": round(viol_per_clk, 1),
            "root_cause":  (
                f"Avg {viol_per_clk:.1f} violations/clock → isolated path issues "
                "or MBFF-specific problems on a subset of clocks."
            ),
            "diagnostic_steps": [
                "Identify which specific clocks carry violations",
                "Check if violating endpoints are MBFF outputs",
                "If MBFF → debank to single-bit; if not → upsize/retime cells",
            ],
            "fixes": [
                {
                    "hypothesis":           "MBFF endpoint issue",
                    "command":              "set_multibit_options -exclude [get_cells {violating_mbs}]; compile_clock_tree -incremental",
                    "eco_cost":             "LOW–MEDIUM",
                    "expected_improvement": "50–80% for MBFF-specific violations",
                },
                {
                    "hypothesis":           "Critical path logic depth",
                    "command":              "optimize_netlist -area; place_opt -effort high",
                    "eco_cost":             "MEDIUM",
                    "expected_improvement": "20–30% violation reduction",
                },
            ],
        }
    else:
        return {
            "diagnosis":   "MODERATE_SETUP_ISSUES",
            "confidence":  "MEDIUM",
            "severity":    "warning",
            "viol_per_clk": round(viol_per_clk, 1),
            "root_cause":  (
                f"Avg {viol_per_clk:.0f} violations/clock — moderate; "
                "mix of systemic and isolated issues."
            ),
            "fixes": [
                {
                    "hypothesis":           "Incremental CTS refinement",
                    "command":              "clock_opt -only_hold_time; route_opt",
                    "eco_cost":             "LOW",
                    "expected_improvement": "15–25% violation reduction",
                },
            ],
        }


def compare_flow_generations(flow_data: dict) -> dict:
    """
    Compare multiple flow generations (e.g. 21a vs 28a vs 32a).
    flow_data: {label: {"avg_setup": int, "avg_hold": int, "critical": int}}
    Returns improvement factors and recommended backport actions.
    """
    if len(flow_data) < 2:
        return {}

    generations = sorted(flow_data.keys())
    comparisons = {}

    for i in range(1, len(generations)):
        older, newer = generations[i - 1], generations[i]
        old_s = flow_data[older].get("avg_setup", 1) or 1
        new_s = flow_data[newer].get("avg_setup", 1) or 1
        factor = old_s / new_s if new_s > 0 else 1.0

        entry = {
            "improvement_factor": round(factor, 1),
            "setup_reduction":    old_s - new_s,
        }
        if factor > 2.0:
            entry["status"] = "SIGNIFICANT_IMPROVEMENT"
            entry["investigation_needed"] = [
                f"diff {older}/scripts/cts_options.tcl {newer}/scripts/cts_options.tcl",
                "Compare MBFF grouping policies (group_size, exclude lists)",
                "Compare floorplan utilisation and blockage maps",
                "Compare clock uncertainty / OCV margin settings",
            ]
            entry["recommended_action"] = (
                f"Backport {newer} CTS recipe settings to {older}; "
                f"expected to reduce violations by ~{factor:.0f}×"
            )
        elif factor > 1.2:
            entry["status"] = "INCREMENTAL_IMPROVEMENT"
            entry["recommended_action"] = (
                f"Minor improvements from {older}→{newer}; review skew targets"
            )
        else:
            entry["status"] = "NO_IMPROVEMENT"
            entry["recommended_action"] = (
                f"No meaningful improvement {older}→{newer}; investigate regression"
            )

        comparisons[f"{older}→{newer}"] = entry

    return comparisons


# ─────────────────────────────────────────────────────────────────────────────
# 2b. MAIN ANALYSIS LAYER
# ─────────────────────────────────────────────────────────────────────────────

def analyze_cts_data(data: dict) -> dict:
    """
    Perform pattern-based reasoning on parsed CTS data.

    Returns:
        {
          "critical":      [{clock, metric, value, threshold, pattern}],
          "warnings":      [{clock, metric, value, threshold, pattern}],
          "healthy":       [clock_name],
          "observations":  [str],
          "skew_summary":  {clock: {max_ps, avg_ps, classification}},
          "delay_summary": {clock: {avg_ps, pattern}},
          "viol_summary":  {clock: {setup, hold, classification}},
        }
    """
    analysis = {
        "critical": [],
        "warnings": [],
        "healthy":  [],
        "observations": [],
        "skew_summary":   {},
        "delay_summary":  {},
        "viol_summary":   {},
        "hold_diagnosis": {},    # NEW: MBFF explosion analysis
        "setup_cluster":  {},    # NEW: systemic vs localised
    }

    clocks = {
        k: v for k, v in data["clocks"].items()
        if not k.startswith("__")
    }

    # ── A. Skew Analysis ─────────────────────────────────────────────────────
    skew_values = [
        c["skew_max_ps"] for c in clocks.values()
        if c.get("skew_max_ps") is not None
    ]
    global_avg_skew = (sum(skew_values) / len(skew_values)) if skew_values else None

    for clk, c in clocks.items():
        skew = c.get("skew_max_ps")
        if skew is None:
            continue
        classification = "ok"
        if skew > SKEW_THRESHOLD_PS:
            if global_avg_skew and skew > SKEW_IMBALANCE_RATIO * global_avg_skew:
                classification = "localized"
            else:
                classification = "global"
            entry = {
                "clock": clk,
                "metric": "skew",
                "value": skew,
                "threshold": SKEW_THRESHOLD_PS,
                "pattern": classification,
            }
            (analysis["critical"] if skew > 2 * SKEW_THRESHOLD_PS
             else analysis["warnings"]).append(entry)
        analysis["skew_summary"][clk] = {
            "max_ps": skew,
            "avg_ps": c.get("skew_avg_ps"),
            "classification": classification,
        }

    # ── B. Insertion Delay Analysis ───────────────────────────────────────────
    for clk, c in clocks.items():
        delay = c.get("ins_delay_avg_ps")
        if delay is None:
            continue
        skew = c.get("skew_max_ps")
        if delay > INS_DELAY_THRESHOLD_PS:
            if skew is not None and skew <= SKEW_THRESHOLD_PS:
                pattern = "over_buffering"
                msg = "high delay + low skew → likely over-buffering"
            elif skew is not None and skew > SKEW_THRESHOLD_PS:
                pattern = "routing_topology"
                msg = "high delay + high skew → routing/topology issue"
            else:
                pattern = "excessive_delay"
                msg = "excessive insertion delay"
            analysis["warnings"].append({
                "clock": clk,
                "metric": "insertion_delay",
                "value": delay,
                "threshold": INS_DELAY_THRESHOLD_PS,
                "pattern": pattern,
                "detail": msg,
            })
        analysis["delay_summary"][clk] = {
            "avg_ps": delay,
            "min_ps": c.get("ins_delay_min_ps"),
            "max_ps": c.get("ins_delay_max_ps"),
            "pattern": pattern if delay > INS_DELAY_THRESHOLD_PS else "ok",
        }

    # ── C. Violation Analysis ─────────────────────────────────────────────────
    for clk, c in clocks.items():
        setup = c.get("setup_violations", 0)
        hold  = c.get("hold_violations", 0)
        if setup == 0 and hold == 0:
            continue
        if setup > 0 and hold > 0:
            classification = "mixed"
        elif hold > setup:
            classification = "hold_dominated"
        else:
            classification = "setup_dominated"

        entry = {
            "clock": clk,
            "metric": "violations",
            "setup": setup,
            "hold": hold,
            "classification": classification,
            "worst_setup_ps": c.get("worst_setup_slack_ps"),
            "worst_hold_ps": c.get("worst_hold_slack_ps"),
        }
        if setup > CLUSTER_VIOLATION_THRESH or hold > CLUSTER_VIOLATION_THRESH:
            entry["pattern"] = "clustered"
            analysis["critical"].append(entry)
        else:
            entry["pattern"] = "scattered"
            analysis["warnings"].append(entry)

        analysis["viol_summary"][clk] = {
            "setup": setup, "hold": hold,
            "classification": classification,
        }

    # Iris hold endpoints
    for k, c in data["clocks"].items():
        if k.startswith("__iris_hold_"):
            stage = c.get("_stage", "unknown")
            total = c.get("hold_violations", 0)
            if total > 0:
                analysis["critical" if "clock_route_opt" in stage
                         else "warnings"].append({
                    "clock": f"multiple ({stage})",
                    "metric": "iris_hold_endpoints",
                    "value": total,
                    "threshold": 0,
                    "pattern": "hold_endpoints",
                    "detail": (
                        f"{total} hold endpoints at {stage}. "
                        "Top blocks: " + ", ".join(
                            f"{b}({n})" for b, n in
                            sorted(
                                c.get("_iris_hold", {}).get("by_block", {}).items(),
                                key=lambda x: x[1], reverse=True
                            )[:3]
                        )
                    ),
                })

    # CTS violation files
    for v in data.get("_cts_violations", []):
        analysis["warnings"].append({
            "clock": "N/A",
            "metric": "cts_violation",
            "value": v["count"],
            "threshold": 0,
            "pattern": v["code"],
            "detail": (
                f"{v['count']} {v['code']} pins in {v['file']}."
                + (f" Samples: {', '.join(v['samples'][:2])}" if v.get('samples') else "")
            ),
        })

    # Health checks
    for stage, checks in data.get("_hc_checks", {}).items():
        for check, count in checks.items():
            if isinstance(count, int) and count > 0:
                analysis[
                    "critical" if check in ("check_opens", "check_shorts")
                    else "warnings"
                ].append({
                    "clock": "N/A",
                    "metric": check,
                    "value": count,
                    "threshold": 0,
                    "pattern": "health_check",
                    "detail": f"{check} = {count} at {stage}",
                })
            elif count == "TCL_ERROR:CHECK_LOG_FILE":
                analysis["critical"].append({
                    "clock": "N/A",
                    "metric": check,
                    "value": "TCL_ERROR",
                    "threshold": 0,
                    "pattern": "health_check_error",
                    "detail": f"TCL_ERROR in {check} at {stage} — check run log",
                })

    # ── Healthy clocks ────────────────────────────────────────────────────────
    flagged = set(
        e["clock"] for e in analysis["critical"] + analysis["warnings"]
        if "clock" in e
    )
    analysis["healthy"] = [
        clk for clk in clocks
        if clk not in flagged
        and (clocks[clk].get("skew_max_ps") is not None
             or clocks[clk].get("ins_delay_avg_ps") is not None)
    ]

    # ── D. Hold Explosion Analysis (MBFF clock push detection) ───────────────
    total_hold = data.get("global_hold_viols", 0)
    hold_dx    = analyze_hold_explosion(total_hold)
    analysis["hold_diagnosis"] = hold_dx
    if hold_dx["severity"] == "critical":
        analysis["critical"].append({
            "clock":   "ALL (MBFF)",
            "metric":  "hold_explosion",
            "value":   total_hold,
            "threshold": MBFF_HOLD_EXPLOSION_THRESH,
            "pattern": hold_dx["diagnosis"],
            "detail":  hold_dx["root_cause"],
            "eco_cost": hold_dx.get("eco_cost", {}),
            "fix":     hold_dx.get("recommended_fix", ""),
            "commands": hold_dx.get("commands", []),
        })
    elif hold_dx["severity"] == "warning" and total_hold > 0:
        analysis["warnings"].append({
            "clock":   "multiple",
            "metric":  "hold_violations",
            "value":   total_hold,
            "threshold": MODERATE_HOLD_THRESH,
            "pattern": hold_dx["diagnosis"],
            "detail":  hold_dx["root_cause"],
            "commands": hold_dx.get("commands", []),
        })

    # ── E. Setup Clustering Analysis ─────────────────────────────────────────
    total_setup  = data.get("global_setup_viols", 0)
    real_clocks  = {k: v for k, v in data["clocks"].items()
                    if not k.startswith("__")}
    setup_dx     = analyze_setup_clustering(total_setup, len(real_clocks))
    analysis["setup_cluster"] = setup_dx
    if setup_dx.get("severity") == "critical":
        analysis["critical"].append({
            "clock":   "ALL",
            "metric":  "setup_clustering",
            "value":   total_setup,
            "threshold": SYSTEMIC_VIOLS_PER_CLOCK,
            "pattern": setup_dx["diagnosis"],
            "detail":  setup_dx["root_cause"],
            "fixes":   setup_dx.get("fixes", []),
        })

    # ── System-level observations ─────────────────────────────────────────────
    if len(analysis["critical"]) == 0 and len(analysis["warnings"]) == 0:
        analysis["observations"].append(
            "✅ All clocks appear healthy — no threshold violations detected."
        )
    if global_avg_skew and global_avg_skew > SKEW_THRESHOLD_PS:
        analysis["observations"].append(
            f"⚠️  System-wide average skew ({global_avg_skew:.0f} ps) exceeds target — "
            "potential global CTS topology or constraint issue."
        )
    over_buf = [
        clk for clk, s in analysis.get("delay_summary", {}).items()
        if s.get("pattern") == "over_buffering"
    ]
    if len(over_buf) > 2:
        analysis["observations"].append(
            f"⚠️  {len(over_buf)} clocks show over-buffering pattern — "
            "review global CTS buffer lib or reduce target latency constraints."
        )
    mixed_viols = [
        clk for clk, s in analysis["viol_summary"].items()
        if s["classification"] == "mixed"
    ]
    if mixed_viols:
        analysis["observations"].append(
            f"🔍 Mixed hold+setup violations on: {', '.join(mixed_viols[:3])}. "
            "May indicate post-CTS routing detours affecting both timing types."
        )
    # MBFF explosion observation
    if hold_dx["diagnosis"] == "MBFF_CLOCK_PUSH_EXPLOSION":
        eco = hold_dx.get("eco_cost", {})
        analysis["observations"].append(
            f"🔴 MBFF CLOCK PUSH EXPLOSION detected ({total_hold:,} hold violations). "
            f"Fixing with buffers would cost ~{eco.get('estimated_hold_buffers',0):,} cells, "
            f"~{eco.get('area_um2',0):,} µm² area, ~{eco.get('runtime_hours',0)} hrs. "
            f"STRONGLY RECOMMENDED: revert clock push + debank MBFFs."
        )
    # Setup clustering observation
    vpc = setup_dx.get("viol_per_clk", 0)
    if vpc > SYSTEMIC_VIOLS_PER_CLOCK:
        analysis["observations"].append(
            f"🔴 SYSTEMIC CTS ISSUE: avg {vpc:.0f} violations/clock — "
            "global skew, over-buffering, or floorplan problem. "
            "Targeted ECO will not be sufficient — CTS re-synthesis required."
        )
    elif vpc > LOCALIZED_VIOLS_PER_CLOCK:
        analysis["observations"].append(
            f"🟡 MODERATE setup clustering: avg {vpc:.1f} violations/clock — "
            "incremental clock_opt likely sufficient."
        )
    cc = data.get("_clock_cell_usage", {})
    if cc.get("total", 0) > 0:
        analysis["observations"].append(
            f"ℹ️  Total CTS buffer/inverter cells in design: {cc['total']:,}."
        )

    return analysis


# ─────────────────────────────────────────────────────────────────────────────
# 3. HYPOTHESIS GENERATION
# ─────────────────────────────────────────────────────────────────────────────

def generate_hypotheses(analysis: dict) -> list:
    """
    Create structured root-cause hypotheses for each identified issue.

    Each hypothesis:
        {
          "symptom":    str,
          "cause":      str,
          "fix":        str,
          "confidence": "High"|"Medium"|"Low",
          "priority":   "critical"|"medium"|"low",
          "clock":      str,
        }
    """
    hypotheses = []

    _SKEW_CAUSES = {
        "global":    ("Global CTS topology imbalance or incorrect target latency "
                      "constraints causing unequal path lengths across the design."),
        "localized": ("Localised routing detour or physical placement cluster far "
                      "from clock trunk causing asymmetric delay on affected sinks."),
    }
    _SKEW_FIXES = {
        "global":    ("Re-run CTS with tighter skew targets; review `set_clock_tree_options` "
                      "skew constraints; verify clock tree reference cells."),
        "localized": ("Identify outlier sinks via `report_clock_tree -skew`; adjust "
                      "cell placement or insert local balance buffers near affected region."),
    }

    for issue in analysis.get("critical", []) + analysis.get("warnings", []):
        metric  = issue.get("metric", "")
        clock   = issue.get("clock", "?")
        pattern = issue.get("pattern", "")
        priority = "critical" if issue in analysis.get("critical", []) else "medium"

        # ── Skew hypothesis ───────────────────────────────────────────────────
        if metric == "skew":
            val = issue.get("value", 0)
            hypotheses.append({
                "clock":      clock,
                "priority":   priority,
                "symptom":    f"Clock '{clock}' max skew = {val:.0f} ps "
                              f"(threshold {SKEW_THRESHOLD_PS} ps).",
                "cause":      _SKEW_CAUSES.get(pattern,
                              "Uncharacterised skew source — check report_clock_tree output."),
                "fix":        _SKEW_FIXES.get(pattern,
                              "Run `report_clock_tree -skew -verbose` to identify root cause."),
                "confidence": "High" if val > 2 * SKEW_THRESHOLD_PS else "Medium",
            })

        # ── Insertion delay hypothesis ─────────────────────────────────────────
        elif metric == "insertion_delay":
            val    = issue.get("value", 0)
            detail = issue.get("detail", "")
            if pattern == "over_buffering":
                cause = ("Excessive buffer insertion due to over-aggressive CTS "
                         "target latency or too many reference cells in library.")
                fix   = ("Reduce `set_clock_tree_options -target_skew`; filter CTS "
                         "reference cell list to faster drive-strength cells; check "
                         "max_transition constraints.")
                conf  = "High"
            elif pattern == "routing_topology":
                cause = ("Routing congestion or sub-optimal clock trunk placement "
                         "forcing long wire detours increasing both delay and skew.")
                fix   = ("Improve floorplan to bring clock source closer to load "
                         "clusters; add clock guide constraints; review NDR rules.")
                conf  = "Medium"
            else:
                cause = "Insertion delay exceeds threshold — cause unknown without skew data."
                fix   = "Run `report_clock_tree -delay` for detailed path breakdown."
                conf  = "Low"
            hypotheses.append({
                "clock":      clock,
                "priority":   "medium",
                "symptom":    f"Clock '{clock}' avg insertion delay = {val:.0f} ps "
                              f"({val/1000:.3f} ns). {detail}",
                "cause":      cause,
                "fix":        fix,
                "confidence": conf,
            })

        # ── Violation hypothesis ───────────────────────────────────────────────
        elif metric == "violations":
            setup = issue.get("setup", 0)
            hold  = issue.get("hold", 0)
            cls   = issue.get("classification", "")
            clst  = issue.get("pattern", "") == "clustered"
            if cls == "hold_dominated":
                cause = ("Hold violations often caused by CTS over-correction "
                         "(too much skew) or short data paths with high clock skew.")
                fix   = ("Insert delay buffers on flagged hold paths; re-run "
                         "`route_opt` with hold-fixing enabled: "
                         "`set_route_opt_strategy -hold_fixing true`.")
                conf  = "High"
            elif cls == "setup_dominated":
                cause = ("Setup violations indicate data path is too slow relative "
                         "to clock period — may be due to logic depth, routing, or "
                         "excessive clock latency pushing launch path.")
                fix   = ("Review critical paths with `report_timing`; apply physical "
                         "optimisation (`place_opt`/`clock_opt`); check for "
                         "over-constrained clock uncertainty.")
                conf  = "Medium"
            else:
                cause = ("Mixed hold + setup violations suggest clock skew imbalance "
                         "or post-CTS routing detours affecting multiple path types.")
                fix   = ("Rebalance CTS; run incremental `clock_opt`; check "
                         "post-route timing with updated parasitics.")
                conf  = "Medium"
            hypotheses.append({
                "clock":      clock,
                "priority":   "critical" if clst else "medium",
                "symptom":    (f"Clock '{clock}': {setup} setup + {hold} hold violations"
                               + (" (CLUSTERED)" if clst else "") + f". Type: {cls}."),
                "cause":      cause,
                "fix":        fix,
                "confidence": conf,
            })

        # ── Iris hold endpoints ───────────────────────────────────────────────
        elif metric == "iris_hold_endpoints":
            hypotheses.append({
                "clock":      clock,
                "priority":   priority,
                "symptom":    issue.get("detail", "Hold endpoints present."),
                "cause":      ("Hold endpoints in iris ECO list indicate hold "
                               "fixing was not completed during CTS/route_opt."),
                "fix":        ("Re-run `route_opt` with hold fixing; or insert "
                               "delay cells manually using ECO flow on listed endpoints."),
                "confidence": "High",
            })

        # ── CTS violations ────────────────────────────────────────────────────
        elif metric == "cts_violation":
            hypotheses.append({
                "clock":      clock,
                "priority":   "medium",
                "symptom":    issue.get("detail", "CTS violation present."),
                "cause":      ("CTS rule violation — pins may have excessive delay "
                               "due to dont_touch nets or fanout limits."),
                "fix":        ("Review `cts_high_delay_pins_*.rpt`; relax dont_touch "
                               "if intentional; check CTS exception list."),
                "confidence": "Medium",
            })

        # ── Health checks ─────────────────────────────────────────────────────
        elif pattern in ("health_check", "health_check_error"):
            hypotheses.append({
                "clock":      clock,
                "priority":   "critical" if "opens" in metric or "shorts" in metric else "medium",
                "symptom":    issue.get("detail", "Health check failure."),
                "cause":      ("Physical design integrity issue (opens/shorts/DRC) "
                               "likely caused by routing congestion or ECO changes."),
                "fix":        ("Run `check_routes` and `verify_drc`; review "
                               "congestion hotspots; re-run detailed route if needed."),
                "confidence": "High",
            })

    return hypotheses


# ─────────────────────────────────────────────────────────────────────────────
# 4. RECOMMENDATION ENGINE / REPORT GENERATOR
# ─────────────────────────────────────────────────────────────────────────────

def generate_recommendations(hypotheses: list) -> str:
    """
    Produce prioritized Markdown report from hypotheses list.
    (This is the final-output formatter; called by generate_report internally.)
    """
    critical = [h for h in hypotheses if h["priority"] == "critical"]
    medium   = [h for h in hypotheses if h["priority"] == "medium"]
    low      = [h for h in hypotheses if h["priority"] == "low"]

    lines = []

    def _hyp_block(h: dict) -> list:
        block = [
            f"- **Clock:** `{h['clock']}`",
            f"  - **Symptom:** {h['symptom']}",
            f"  - **Likely Cause:** {h['cause']}",
            f"  - **Suggested Fix:** {h['fix']}",
            f"  - **Confidence:** {h.get('confidence','—')}",
            "",
        ]
        return block

    if critical:
        lines += ["## 📋 Recommended Actions — High Priority (Critical)", ""]
        for h in critical:
            lines += _hyp_block(h)

    if medium:
        lines += ["## 📋 Recommended Actions — Medium Priority", ""]
        for h in medium:
            lines += _hyp_block(h)

    if low:
        lines += ["## 📋 Recommended Actions — Low Priority", ""]
        for h in low:
            lines += _hyp_block(h)

    if not hypotheses:
        lines += [
            "## 📋 Recommended Actions",
            "",
            "- No actionable issues found. CTS appears healthy.",
            "",
        ]

    return "\n".join(lines)


def format_hold_analysis(hold_analysis: dict, flow: dict) -> str:
    """Format hold explosion analysis into a detailed Markdown section."""
    label     = flow.get("label", flow.get("block", "unknown"))
    hold_cnt  = flow.get("hold_violations", 0)
    diag      = hold_analysis.get("diagnosis", "UNKNOWN")
    conf      = hold_analysis.get("confidence", "—")
    cause     = hold_analysis.get("root_cause", "")
    fix       = hold_analysis.get("recommended_fix", "")
    cmds      = hold_analysis.get("commands", [])
    outcome   = hold_analysis.get("expected_outcome", "")
    savings   = hold_analysis.get("net_savings", "")
    eco       = hold_analysis.get("eco_cost", {})

    icon = "🔴" if diag == "MBFF_CLOCK_PUSH_EXPLOSION" else ("🟡" if "MODERATE" in diag else "🟢")
    lines = [
        f"### {icon} Hold Analysis — `{label}`",
        "",
        f"| Field | Detail |",
        f"|---|---|",
        f"| Diagnosis | **{diag}** |",
        f"| Confidence | {conf} |",
        f"| Hold violations | **{hold_cnt:,}** |",
        "",
        f"**Root Cause:** {cause}",
        "",
    ]

    if eco:
        lines += [
            "#### 💰 ECO Cost Estimate (if fixed with buffers)",
            "",
            "| Metric | Estimate |",
            "|---|---|",
        ]
        if "estimated_hold_buffers" in eco:
            lines.append(f"| Hold buffers needed | {eco['estimated_hold_buffers']:,} |")
        if "area_um2" in eco:
            lines.append(f"| Area overhead | {eco['area_um2']:,} µm² |")
        if "power_mw" in eco:
            lines.append(f"| Power overhead | {eco['power_mw']} mW |")
        if "runtime_hours" in eco:
            lines.append(f"| Estimated runtime | {eco['runtime_hours']} hrs |")
        lines.append("")

    if fix:
        lines += [f"**Recommended Fix:** {fix}", ""]

    if cmds:
        lines += ["**FC Commands:**", "```tcl"]
        lines += cmds
        lines += ["```", ""]

    if outcome:
        lines += [f"**Expected Outcome:** {outcome}", ""]
    if savings:
        lines += [f"**Net Savings (vs buffer fix):** {savings}", ""]

    return "\n".join(lines)


def format_setup_analysis(setup_analysis: dict, flow: dict) -> str:
    """Format setup clustering analysis into a detailed Markdown section."""
    label    = flow.get("label", flow.get("block", "unknown"))
    setup_c  = flow.get("setup_violations", 0)
    clk_c    = flow.get("clock_count", 1)
    diag     = setup_analysis.get("diagnosis", "UNKNOWN")
    conf     = setup_analysis.get("confidence", "—")
    cause    = setup_analysis.get("root_cause", "")
    vpc      = setup_analysis.get("viol_per_clk", round(setup_c / max(clk_c, 1), 1))
    steps    = setup_analysis.get("diagnostic_steps", [])
    fixes    = setup_analysis.get("fixes", [])

    icon = "🔴" if "SYSTEMIC" in diag else ("🟡" if "MODERATE" in diag else "🟢")
    lines = [
        f"### {icon} Setup Clustering — `{label}`",
        "",
        f"| Field | Detail |",
        f"|---|---|",
        f"| Diagnosis | **{diag}** |",
        f"| Confidence | {conf} |",
        f"| Setup violations | **{setup_c:,}** across {clk_c} clocks |",
        f"| Avg violations/clock | **{vpc}** |",
        "",
        f"**Root Cause:** {cause}",
        "",
    ]

    if steps:
        lines += ["**Diagnostic Steps:**", ""]
        for i, s in enumerate(steps, 1):
            lines.append(f"{i}. {s}")
        lines.append("")

    if fixes:
        lines += [
            "**Ranked Fix Options:**",
            "",
            "| # | Hypothesis | ECO Cost | Expected Improvement |",
            "|---|---|---|---|",
        ]
        for i, fx in enumerate(fixes, 1):
            lines.append(
                f"| {i} | {fx.get('hypothesis','?')} | "
                f"{fx.get('eco_cost','?')} | {fx.get('expected_improvement','?')} |"
            )
        lines.append("")
        # Show FC commands for each fix
        lines += ["**FC Commands (ranked):**", ""]
        for i, fx in enumerate(fixes, 1):
            cmd = fx.get("command", "")
            if cmd:
                lines += [f"*Option {i} — {fx.get('hypothesis','')}:*", "```tcl", cmd, "```", ""]

    return "\n".join(lines)


def format_generation_comparison(generation_analysis: dict) -> str:
    """Format flow generation comparison into a Markdown section."""
    if not generation_analysis:
        return ""

    lines = [
        "### 📈 Flow Generation Comparison",
        "",
        "| Transition | Improvement | Setup Reduction | Status |",
        "|---|---|---|---|",
    ]
    for transition, data in generation_analysis.items():
        factor  = data.get("improvement_factor", 1.0)
        delta   = data.get("setup_reduction", 0)
        status  = data.get("status", "—")
        icon    = "🟢" if factor > 2.0 else ("🟡" if factor > 1.2 else "🔴")
        lines.append(
            f"| `{transition}` | **{factor}×** | {delta:,} fewer viols | {icon} {status} |"
        )
    lines.append("")

    for transition, data in generation_analysis.items():
        action  = data.get("recommended_action", "")
        inv     = data.get("investigation_needed", [])
        if action:
            lines += [f"**{transition}:** {action}", ""]
        if inv:
            lines += ["  Investigation steps:"]
            for step in inv:
                lines.append(f"  - `{step}`")
            lines.append("")

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# Fellow-Level Multi-Run Report
# ─────────────────────────────────────────────────────────────────────────────

def generate_fellow_level_report(flow_data: list) -> str:
    """
    Generate a senior-engineer-quality CTS quality report across multiple runs.

    Args:
        flow_data: list of dicts, one per run area:
            {
              "label":            str,   # e.g. "1p0_32a_cth/par_base_fabric_slice_1"
              "block":            str,
              "flow":             str,
              "hold_violations":  int,
              "setup_violations": int,
              "clock_count":      int,
              "critical":         int,
            }

    Returns:
        Markdown report string with hold analysis, setup clustering, and
        flow generation comparison.
    """
    sections = []

    # ── 1. Hold Explosion Analysis ────────────────────────────────────────────
    hold_sections = []
    for flow in flow_data:
        hv = flow.get("hold_violations", 0)
        if hv > MODERATE_HOLD_THRESH:
            dx = analyze_hold_explosion(hv)
            hold_sections.append(format_hold_analysis(dx, flow))
    if hold_sections:
        sections.append("## 🔴 Hold Violation Deep-Dive\n")
        sections.extend(hold_sections)
    else:
        sections.append("## 🟢 Hold Violations\n\n_No significant hold violations detected._\n")

    # ── 2. Setup Clustering Analysis ─────────────────────────────────────────
    setup_sections = []
    for flow in flow_data:
        sv  = flow.get("setup_violations", 0)
        clk = flow.get("clock_count", 1)
        if sv > 100:
            dx = analyze_setup_clustering(sv, clk)
            setup_sections.append(format_setup_analysis(dx, flow))
    if setup_sections:
        sections.append("## 🟡 Setup Violation Analysis\n")
        sections.extend(setup_sections)

    # ── 3. Flow Generation Comparison ────────────────────────────────────────
    # Group by flow generation label (prefix before first '/')
    gen_buckets = {}
    for flow in flow_data:
        gen  = flow.get("flow", flow.get("label", "unknown").split("/")[0])
        sv   = flow.get("setup_violations", 0)
        hv   = flow.get("hold_violations", 0)
        crit = flow.get("critical", 0)
        if gen not in gen_buckets:
            gen_buckets[gen] = {"setups": [], "holds": [], "crits": []}
        gen_buckets[gen]["setups"].append(sv)
        gen_buckets[gen]["holds"].append(hv)
        gen_buckets[gen]["crits"].append(crit)

    gen_summary = {
        gen: {
            "avg_setup": int(sum(v["setups"]) / len(v["setups"])),
            "avg_hold":  int(sum(v["holds"])  / len(v["holds"])),
            "critical":  int(sum(v["crits"])  / len(v["crits"])),
        }
        for gen, v in gen_buckets.items()
    }
    gen_cmp = compare_flow_generations(gen_summary)
    if gen_cmp:
        sections.append("## 📈 Flow Generation Analysis\n")
        sections.append(format_generation_comparison(gen_cmp))

    # ── 4. Master Scorecard ───────────────────────────────────────────────────
    scorecard = [
        "## 📋 Master Scorecard\n",
        "| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |",
        "|---|---|---|---|---|---|---|",
    ]
    for flow in sorted(flow_data, key=lambda x: x.get("critical", 0)):
        sv   = flow.get("setup_violations", 0)
        hv   = flow.get("hold_violations", 0)
        crit = flow.get("critical", 0)
        clk  = flow.get("clock_count", 0)
        # Simple grade
        if crit == 0 and sv < 50:
            grade = "🟢 A"
        elif crit <= 5 and sv < 200:
            grade = "🟡 B"
        elif crit <= 15 and sv < 1000:
            grade = "🟠 C"
        else:
            grade = "🔴 D"
        scorecard.append(
            f"| `{flow.get('flow','')}` | `{flow.get('block','')}` | {clk} | "
            f"{sv:,} | {hv:,} | {crit} | {grade} |"
        )
    scorecard.append("")
    sections.insert(0, "\n".join(scorecard))

    return "\n\n".join(sections)


# ─────────────────────────────────────────────────────────────────────────────
# Single-Run Full Report
# ─────────────────────────────────────────────────────────────────────────────

def generate_report(data: dict, analysis: dict, hypotheses: list,
                    source_label: str = "") -> str:
    """
    Assemble the full ClockIQ Markdown report (single run area).
    Includes fellow-level hold/setup deep-dive sections.
    """
    clocks  = {k: v for k, v in data["clocks"].items() if not k.startswith("__")}
    total_c = len(clocks)

    lines = ["# 🕐 ClockIQ — Clock Tree Diagnostics Report", ""]
    if source_label:
        lines += [f"**Source:** `{source_label}`", ""]

    # ── Summary ───────────────────────────────────────────────────────────────
    setup_dx = analysis.get("setup_cluster", {})
    hold_dx  = analysis.get("hold_diagnosis", {})
    vpc      = setup_dx.get("viol_per_clk", "—")

    lines += [
        "## Summary", "",
        "| Metric | Value |",
        "|---|---|",
        f"| Clocks analyzed | {total_c} |",
        f"| 🔴 Critical issues | {len(analysis['critical'])} |",
        f"| 🟡 Warnings | {len(analysis['warnings'])} |",
        f"| 🟢 Healthy clocks | {len(analysis['healthy'])} |",
        f"| Setup violations | {data.get('global_setup_viols', 0):,} |",
        f"| Hold violations | {data.get('global_hold_viols', 0):,} |",
        f"| Avg violations/clock | {vpc} |",
        f"| Setup diagnosis | {setup_dx.get('diagnosis', '—')} |",
        f"| Hold diagnosis | {hold_dx.get('diagnosis', '—')} |",
        "",
    ]

    # ── 1. Critical Issues ────────────────────────────────────────────────────
    lines += ["## 🔴 Critical Issues (High Priority)", ""]
    if analysis["critical"]:
        for issue in analysis["critical"]:
            metric = issue["metric"].upper()
            detail = issue.get("detail", "")
            eco    = issue.get("eco_cost", {})
            cmds   = issue.get("commands", [])
            fixes  = issue.get("fixes", [])

            lines.append(f"### [{metric}] clock=`{issue['clock']}`")
            if detail:
                lines += [f"> {detail}", ""]
            if eco:
                lines += ["**💰 ECO Cost Estimate:**", "", "| Metric | Value |", "|---|---|"]
                for k, v in eco.items():
                    lines.append(f"| {k.replace('_',' ').title()} | {v:,} |" if isinstance(v, int) else f"| {k.replace('_',' ').title()} | {v} |")
                lines.append("")
            if cmds:
                lines += ["**FC Commands:**", "```tcl"] + cmds + ["```", ""]
            if fixes:
                lines += ["**Ranked Fixes:**", "", "| # | Hypothesis | Cost | Expected Improvement |", "|---|---|---|---|"]
                for i, fx in enumerate(fixes, 1):
                    lines.append(f"| {i} | {fx.get('hypothesis','?')} | {fx.get('eco_cost','?')} | {fx.get('expected_improvement','?')} |")
                lines.append("")
        lines.append("")
    else:
        lines += ["_No critical issues detected._", ""]

    # ── 2. Warnings ───────────────────────────────────────────────────────────
    lines += ["## 🟡 Warnings (Medium Priority)", ""]
    if analysis["warnings"]:
        for issue in analysis["warnings"]:
            detail = issue.get("detail", "")
            cmds   = issue.get("commands", [])
            lines.append(
                f"- **[{issue['metric'].upper()}]** clock=`{issue['clock']}` "
                f"| value=`{issue.get('value','?')}` | pattern=`{issue.get('pattern','?')}`"
                + (f"\n  > {detail}" if detail else "")
            )
            if cmds:
                lines += ["  ```tcl"] + [f"  {c}" for c in cmds] + ["  ```"]
        lines.append("")
    else:
        lines += ["_No warnings detected._", ""]

    # ── 3. Healthy Clocks ─────────────────────────────────────────────────────
    lines += ["## 🟢 Healthy Clocks", ""]
    if analysis["healthy"]:
        for clk in analysis["healthy"]:
            c = clocks.get(clk, {})
            skew, dly = c.get("skew_max_ps"), c.get("ins_delay_avg_ps")
            lines.append(f"- `{clk}` — skew: {f'{skew:.0f} ps' if skew else '—'}, ins_delay: {f'{dly:.0f} ps' if dly else '—'}")
        lines.append("")
    else:
        lines += ["_No fully healthy clocks identified._", ""]

    # ── 4. Observations ───────────────────────────────────────────────────────
    lines += ["## 🔍 Observations", ""]
    for obs in analysis.get("observations", []) or ["_No system-level observations._"]:
        lines.append(f"- {obs}")
    lines.append("")

    # ── 5. Fellow-Level Deep-Dive ─────────────────────────────────────────────
    flow_entry = {
        "label":            source_label,
        "block":            source_label.split("/")[-1] if "/" in source_label else source_label,
        "flow":             source_label.split("/")[0]  if "/" in source_label else source_label,
        "hold_violations":  data.get("global_hold_viols", 0),
        "setup_violations": data.get("global_setup_viols", 0),
        "clock_count":      total_c,
        "critical":         len(analysis["critical"]),
    }
    lines += ["## 🎓 Fellow-Level Deep-Dive", "", generate_fellow_level_report([flow_entry]), ""]

    # ── 6. Recommended Actions ────────────────────────────────────────────────
    lines.append(generate_recommendations(hypotheses))

    if data.get("warnings"):
        lines += ["## ⚠️ Parse Warnings", ""]
        for w in data["warnings"]:
            lines.append(f"- {w}")
        lines.append("")

    lines += ["---", "*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*"]
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# Unified Entry Point
# ─────────────────────────────────────────────────────────────────────────────

def run_analysis(input_path: Optional[str] = None,
                 text: Optional[str] = None) -> str:
    """
    Analyse a CTS report from a file path, directory, or raw text.

    Args:
        input_path: Path to .rpt/.log file or apr_fc run area directory.
        text:       Raw CTS report text (alternative to input_path).

    Returns:
        Markdown-formatted ClockIQ report string.
    """
    label = input_path or "<inline text>"

    if input_path:
        p = Path(input_path)
        if not p.exists():
            return f"**Error:** Path not found: `{input_path}`"
        if p.is_dir():
            data = parse_cts_directory(p)
        else:
            data = parse_cts_report(p.read_text(errors="replace"))
    elif text:
        data = parse_cts_report(text)
    else:
        return "**Error:** Provide either `input_path` or `text`."

    analysis    = analyze_cts_data(data)
    hypotheses  = generate_hypotheses(analysis)
    return generate_report(data, analysis, hypotheses, source_label=label)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clockiq.py <apr_fc_dir | cts_report.rpt>",
              file=sys.stderr)
        sys.exit(1)
    print(run_analysis(input_path=sys.argv[1]))


if __name__ == "__main__":
    main()

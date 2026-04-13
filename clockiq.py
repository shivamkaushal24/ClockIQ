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
SKEW_THRESHOLD_PS        = 100     # 100 ps
INS_DELAY_THRESHOLD_PS   = 1000   # 1 ns
SKEW_IMBALANCE_RATIO     = 2.0    # flag if max_skew > 2× avg_skew
CLUSTER_VIOLATION_THRESH = 10     # >10 violations on one clock = clustered

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
# Cheetah/R2G Directory-Based Parser (supplements text parser)
# ─────────────────────────────────────────────────────────────────────────────

def _discover_cheetah_files(run_area: Path) -> dict:
    """Walk an apr_fc run area and return categorised file lists."""
    files = {
        "timing_rpts":    defaultdict(list),
        "iris_hold":      defaultdict(list),
        "iris_setup":     defaultdict(list),
        "cts_violations": [],
        "cts_dont_touch": None,
        "hc_summary":     None,
        "clock_cell_usage": None,
    }
    for stage in STAGE_ORDER:
        stage_dir = run_area / f"ch_reports_{stage}"
        if stage_dir.exists():
            for f in sorted(stage_dir.glob("func_max_low_*.rpt")):
                files["timing_rpts"][stage].append(f)
        iris_base = run_area / f"iris_report_fc_{stage}"
        if iris_base.exists():
            for merge_dir in iris_base.rglob("merge"):
                for sub in merge_dir.iterdir():
                    if not sub.is_dir():
                        continue
                    for f in sub.glob("*.pteco_endpoints.hold.rpt"):
                        files["iris_hold"][stage].append(f)
                    for f in sub.glob("*.pteco_endpoints.setup.rpt"):
                        files["iris_setup"][stage].append(f)
    for f in sorted(run_area.glob("cts_high_delay_pins_CTS-*.rpt")):
        files["cts_violations"].append(f)
    dt = run_area / "cts_dont_touch_nets_CTS-055.rpt"
    if dt.exists():
        files["cts_dont_touch"] = dt
    hc = run_area / "HC_summary.rpt"
    if hc.exists():
        files["hc_summary"] = hc
    cc = run_area / "Clock_Cell_usage_my.rpt"
    if cc.exists():
        files["clock_cell_usage"] = cc
    return files


def _parse_cheetah_timing_report(path: Path) -> dict:
    clock = re.sub(r'^func_max_low_', '', path.stem)
    stage = path.parent.name.replace("ch_reports_", "")
    text  = path.read_text(errors="replace")
    data  = {"clock": clock, "stage": stage, "violations": [],
             "ins_delays": [], "worst_slack": None}
    for block in re.split(r'(?=^\s+Startpoint:)', text, flags=re.MULTILINE):
        m = re.search(r'slack\s*\(VIOLATED\)\s+([-\d.]+)', block)
        if not m:
            continue
        slack = float(m.group(1))
        sp_m  = re.search(r'Startpoint:\s+(\S+)', block)
        ep_m  = re.search(r'Endpoint:\s+(\S+)', block)
        pg_m  = re.search(r'Path Group:\s+(\S+)', block)
        mo_m  = re.search(r'Mode:\s+(\S+)', block)
        data["violations"].append({
            "slack":      slack,
            "startpoint": sp_m.group(1) if sp_m else "unknown",
            "endpoint":   ep_m.group(1) if ep_m else "unknown",
            "path_group": pg_m.group(1) if pg_m else clock,
            "mode":       mo_m.group(1) if mo_m else "unknown",
        })
    for m in re.finditer(
        r'clock network delay \(propagated\)\s+([\d.]+)\s+([\d.]+)', text
    ):
        data["ins_delays"].append(float(m.group(2)) * 1000)
    if data["violations"]:
        data["worst_slack"] = min(v["slack"] for v in data["violations"]) * 1000
    return data


def _parse_iris_endpoints(paths: list) -> dict:
    endpoints = []
    for p in paths:
        try:
            lines = p.read_text(errors="replace").splitlines()
            endpoints += [l.strip() for l in lines if l.strip()]
        except Exception:
            pass
    blocks = defaultdict(int)
    for ep in endpoints:
        block = ep.split("/")[0] if "/" in ep else ep
        blocks[block] += 1
    return {"total": len(endpoints), "by_block": dict(blocks)}


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
    Parse a Cheetah apr_fc run area directory and return a unified data dict
    compatible with analyze_cts_data().
    """
    files = _discover_cheetah_files(run_area)
    data  = parse_cts_report("")   # start with empty structure

    for stage in STAGE_ORDER:
        stage_ins = defaultdict(list)
        for rpt_path in files["timing_rpts"].get(stage, []):
            rpt = _parse_cheetah_timing_report(rpt_path)
            clk = rpt["clock"]
            c   = data["clocks"].setdefault(clk, {
                "skew_max_ps": None, "skew_avg_ps": None,
                "ins_delay_min_ps": None, "ins_delay_max_ps": None,
                "ins_delay_avg_ps": None, "latency_ps": None,
                "buffer_depth": None,
                "setup_violations": 0, "hold_violations": 0,
                "worst_setup_slack_ps": None, "worst_hold_slack_ps": None,
                "endpoints": [],
                "_stage_data": defaultdict(dict),
            })
            c.setdefault("_stage_data", defaultdict(dict))[stage] = rpt
            for v in rpt["violations"]:
                c["setup_violations"] += 1
                data["global_setup_viols"] += 1
                if (c["worst_setup_slack_ps"] is None or
                        v["slack"] * 1000 < c["worst_setup_slack_ps"]):
                    c["worst_setup_slack_ps"] = v["slack"] * 1000
                c["endpoints"].append(v["endpoint"])
            stage_ins[clk].extend(rpt["ins_delays"])

        # Aggregate insertion delays per clock
        for clk, delays in stage_ins.items():
            if delays:
                avg = sum(delays) / len(delays)
                c   = data["clocks"].get(clk, {})
                if c.get("ins_delay_avg_ps") is None or avg > c["ins_delay_avg_ps"]:
                    c["ins_delay_avg_ps"] = avg
                    c["ins_delay_min_ps"] = min(delays)
                    c["ins_delay_max_ps"] = max(delays)

        # Hold violations from iris reports
        hold_paths = files["iris_hold"].get(stage, [])
        if hold_paths:
            hd = _parse_iris_endpoints(hold_paths)
            if hd["total"] > 0:
                # Store in __iris_hold__ pseudo-clock for analysis
                data["clocks"].setdefault(f"__iris_hold_{stage}__", {
                    "skew_max_ps": None, "skew_avg_ps": None,
                    "ins_delay_min_ps": None, "ins_delay_max_ps": None,
                    "ins_delay_avg_ps": None, "latency_ps": None,
                    "buffer_depth": None,
                    "setup_violations": 0, "hold_violations": hd["total"],
                    "worst_setup_slack_ps": None, "worst_hold_slack_ps": None,
                    "endpoints": list(hd["by_block"].keys()),
                    "_iris_hold": hd,
                    "_stage": stage,
                })
                data["global_hold_viols"] += hd["total"]

    # CTS violation files
    data["_cts_violations"] = []
    for f in files["cts_violations"]:
        code = re.search(r'CTS-(\d+)', f.name)
        code_str = f"CTS-{code.group(1)}" if code else "CTS-???"
        try:
            lines = f.read_text(errors="replace").splitlines()
            count = len([l for l in lines if l.strip()])
            samples = []
            for l in lines[:3]:
                nm = re.search(r"(?:net|pin)\s+'([^']+)'", l)
                if nm:
                    samples.append(nm.group(1))
            if count > 0:
                data["_cts_violations"].append(
                    {"code": code_str, "count": count, "file": f.name,
                     "samples": samples}
                )
        except Exception:
            pass

    data["_hc_checks"]       = _parse_hc_summary(files["hc_summary"])
    data["_clock_cell_usage"] = _parse_clock_cell_usage(files["clock_cell_usage"])
    data["_run_area"]         = str(run_area)
    return data


# ─────────────────────────────────────────────────────────────────────────────
# 2. ANALYSIS LAYER
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
        "skew_summary":  {},
        "delay_summary": {},
        "viol_summary":  {},
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
                f"{v['count']} {v['code']} pins in {v['file']}. "
                f"Samples: {', '.join(v['samples'][:2])}"
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

    # ── System-level observations ─────────────────────────────────────────────
    if len(analysis["critical"]) == 0 and len(analysis["warnings"]) == 0:
        analysis["observations"].append(
            "✅ All clocks appear healthy with no threshold violations."
        )
    if global_avg_skew and global_avg_skew > SKEW_THRESHOLD_PS:
        analysis["observations"].append(
            f"System-wide average skew ({global_avg_skew:.0f} ps) exceeds target — "
            "potential global CTS topology or constraint issue."
        )
    over_buf = [
        clk for clk, s in analysis.get("delay_summary", {}).items()
        if s.get("pattern") == "over_buffering"
    ]
    if len(over_buf) > 2:
        analysis["observations"].append(
            f"{len(over_buf)} clocks show over-buffering pattern — "
            "consider reviewing global CTS buffer lib or target latency constraints."
        )
    mixed_viols = [
        clk for clk, s in analysis["viol_summary"].items()
        if s["classification"] == "mixed"
    ]
    if mixed_viols:
        analysis["observations"].append(
            f"Mixed hold+setup violations on: {', '.join(mixed_viols[:3])}. "
            "May indicate post-CTS routing detours affecting both timing types."
        )
    cc = data.get("_clock_cell_usage", {})
    if cc.get("total", 0) > 0:
        analysis["observations"].append(
            f"Total CTS buffer/inverter cells in design: {cc['total']}."
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


def generate_report(data: dict, analysis: dict, hypotheses: list,
                    source_label: str = "") -> str:
    """
    Assemble the full ClockIQ Markdown report.
    """
    clocks  = {k: v for k, v in data["clocks"].items() if not k.startswith("__")}
    total_c = len(clocks)

    lines = [
        "# 🕐 ClockIQ — Clock Tree Diagnostics Report",
        "",
    ]
    if source_label:
        lines += [f"**Source:** `{source_label}`", ""]

    lines += [
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Clocks analyzed | {total_c} |",
        f"| Critical issues | {len(analysis['critical'])} |",
        f"| Warnings        | {len(analysis['warnings'])} |",
        f"| Healthy clocks  | {len(analysis['healthy'])} |",
        f"| Global setup violations | {data.get('global_setup_viols', 0)} |",
        f"| Global hold violations  | {data.get('global_hold_viols', 0)} |",
        "",
    ]

    # ── 1. Critical Issues ────────────────────────────────────────────────────
    lines += ["## 🔴 Critical Issues (High Priority)", ""]
    if analysis["critical"]:
        for issue in analysis["critical"]:
            detail = issue.get("detail", "")
            lines.append(
                f"- **[{issue['metric'].upper()}]** clock=`{issue['clock']}` "
                f"value=`{issue.get('value','?')}` pattern=`{issue.get('pattern','?')}`"
                + (f"\n  > {detail}" if detail else "")
            )
        lines.append("")
    else:
        lines += ["_No critical issues detected._", ""]

    # ── 2. Warnings ───────────────────────────────────────────────────────────
    lines += ["## 🟡 Warnings (Medium Priority)", ""]
    if analysis["warnings"]:
        for issue in analysis["warnings"]:
            detail = issue.get("detail", "")
            lines.append(
                f"- **[{issue['metric'].upper()}]** clock=`{issue['clock']}` "
                f"value=`{issue.get('value','?')}` pattern=`{issue.get('pattern','?')}`"
                + (f"\n  > {detail}" if detail else "")
            )
        lines.append("")
    else:
        lines += ["_No warnings detected._", ""]

    # ── 3. Healthy Clocks ─────────────────────────────────────────────────────
    lines += ["## 🟢 Healthy Clocks", ""]
    if analysis["healthy"]:
        for clk in analysis["healthy"]:
            c    = clocks.get(clk, {})
            skew = c.get("skew_max_ps")
            dly  = c.get("ins_delay_avg_ps")
            lines.append(
                f"- `{clk}` — skew: {f'{skew:.0f} ps' if skew else '—'}, "
                f"ins_delay: {f'{dly:.0f} ps' if dly else '—'}"
            )
        lines.append("")
    else:
        lines += ["_No fully healthy clocks identified (or no skew data available)._", ""]

    # ── 4. Observations ───────────────────────────────────────────────────────
    lines += ["## 🔍 Observations (System-level Insights)", ""]
    if analysis["observations"]:
        for obs in analysis["observations"]:
            lines.append(f"- {obs}")
        lines.append("")
    else:
        lines += ["_No system-level observations._", ""]

    # ── 5. Recommended Actions ────────────────────────────────────────────────
    lines.append(generate_recommendations(hypotheses))

    # ── Parse warnings ────────────────────────────────────────────────────────
    if data.get("warnings"):
        lines += ["## ⚠️ Parse Warnings", ""]
        for w in data["warnings"]:
            lines.append(f"- {w}")
        lines.append("")

    lines += [
        "---",
        "*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*",
    ]
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

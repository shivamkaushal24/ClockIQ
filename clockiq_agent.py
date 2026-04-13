#!/usr/bin/env python3
"""
ClockIQ - Clock Tree Diagnostics & Optimization Assistant
Analyzes Synopsys Fusion Compiler CTS reports and generates structured
diagnostics, root-cause hypotheses, and prioritized debug recommendations.
"""

import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# ─── Configurable Thresholds ────────────────────────────────────────────────
SKEW_THRESHOLD_PS            = 100.0   # ps
INSERTION_DELAY_THRESHOLD_NS = 1.0    # ns
VIOLATION_CLUSTER_THRESHOLD  = 10     # violations on a single clock


# ─── Data Structures ────────────────────────────────────────────────────────
@dataclass
class ClockMetrics:
    name: str
    max_skew_ps:          Optional[float] = None
    avg_skew_ps:          Optional[float] = None
    insertion_delay_min:  Optional[float] = None
    insertion_delay_max:  Optional[float] = None
    insertion_delay_avg:  Optional[float] = None
    latency:              Optional[float] = None
    setup_violations:     int = 0
    hold_violations:      int = 0
    buffer_depth:         Optional[int] = None
    tree_balance:         Optional[str] = None
    endpoints:            int = 0
    raw_lines:            list = field(default_factory=list)


# ─── 1. PARSING LAYER ────────────────────────────────────────────────────────
def parse_cts_report(text: str) -> dict:
    """
    Extract clock metrics, violations, and structural data from CTS report text.
    Returns a dict: { clock_name -> ClockMetrics, '_warnings': [str] }
    """
    clocks: dict[str, ClockMetrics] = {}
    warnings: list[str] = []

    lines = text.splitlines()

    # ── Pattern library ──────────────────────────────────────────────────────
    # Clock section header  e.g.  "Clock: CLK_CORE"  /  "Clock 'CLK_CORE'"
    RE_CLOCK_HDR     = re.compile(r"(?:^|\s)Clock[:\s]+['\"]?(\w[\w/\-\.]+)['\"]?", re.I)

    # Skew:  "Max Skew : 0.123 ns"  or  "max_skew 123.4 ps"
    RE_MAX_SKEW      = re.compile(r"max[_\s]?skew\s*[:\s]\s*([\d.]+)\s*(ps|ns)", re.I)
    RE_AVG_SKEW      = re.compile(r"(?:avg|average|mean)[_\s]?skew\s*[:\s]\s*([\d.]+)\s*(ps|ns)", re.I)

    # Insertion delay:  "Insertion Delay (min/max/avg) : 0.5 / 1.2 / 0.8 ns"
    RE_INS_DELAY_MMM = re.compile(
        r"insertion[_\s]delay.*?([\d.]+)\s*/\s*([\d.]+)\s*/\s*([\d.]+)\s*(ps|ns)", re.I)
    RE_INS_DELAY_MAX = re.compile(r"(?:max)[_\s]?insertion[_\s]delay\s*[:\s]\s*([\d.]+)\s*(ps|ns)", re.I)
    RE_INS_DELAY_MIN = re.compile(r"(?:min)[_\s]?insertion[_\s]delay\s*[:\s]\s*([\d.]+)\s*(ps|ns)", re.I)
    RE_INS_DELAY_AVG = re.compile(r"(?:avg|average)[_\s]?insertion[_\s]delay\s*[:\s]\s*([\d.]+)\s*(ps|ns)", re.I)

    # Latency
    RE_LATENCY       = re.compile(r"(?:clock[_\s])?latency\s*[:\s]\s*([\d.]+)\s*(ps|ns)", re.I)

    # Violations
    RE_SETUP_VIOL    = re.compile(r"setup\s+(?:violations?|failing\s+paths?)\s*[:\s]\s*(\d+)", re.I)
    RE_HOLD_VIOL     = re.compile(r"hold\s+(?:violations?|failing\s+paths?)\s*[:\s]\s*(\d+)", re.I)

    # Buffer depth
    RE_BUF_DEPTH     = re.compile(r"(?:buffer|buf)[_\s]depth\s*[:\s]\s*(\d+)", re.I)
    RE_ENDPOINTS     = re.compile(r"(?:sink|endpoint)s?\s*[:\s]\s*(\d+)", re.I)
    RE_BALANCE       = re.compile(r"balance[d]?\s*[:\s]\s*(\w+)", re.I)

    # ── Fallback: summary table  "CLK_CORE   0.080  0.050  0.920  1.100 ..."
    RE_SUMMARY_ROW   = re.compile(
        r"^(\w[\w/\-\.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)", re.M)

    current_clock: Optional[str] = None

    def to_ps(value: float, unit: str) -> float:
        return value * 1000.0 if unit.lower() == "ns" else value

    def to_ns(value: float, unit: str) -> float:
        return value / 1000.0 if unit.lower() == "ps" else value

    def get_or_create(name: str) -> ClockMetrics:
        if name not in clocks:
            clocks[name] = ClockMetrics(name=name)
        return clocks[name]

    # ── Line-by-line pass ────────────────────────────────────────────────────
    for line in lines:
        # Detect clock context
        m = RE_CLOCK_HDR.search(line)
        if m:
            current_clock = m.group(1)
            get_or_create(current_clock)

        if current_clock:
            cm = get_or_create(current_clock)
            cm.raw_lines.append(line)

        # Skew
        m = RE_MAX_SKEW.search(line)
        if m and current_clock:
            get_or_create(current_clock).max_skew_ps = to_ps(float(m.group(1)), m.group(2))

        m = RE_AVG_SKEW.search(line)
        if m and current_clock:
            get_or_create(current_clock).avg_skew_ps = to_ps(float(m.group(1)), m.group(2))

        # Insertion delay  (min / max / avg in one line)
        m = RE_INS_DELAY_MMM.search(line)
        if m and current_clock:
            cm = get_or_create(current_clock)
            unit = m.group(4)
            cm.insertion_delay_min = to_ns(float(m.group(1)), unit)
            cm.insertion_delay_max = to_ns(float(m.group(2)), unit)
            cm.insertion_delay_avg = to_ns(float(m.group(3)), unit)
        else:
            for pat, attr in [
                (RE_INS_DELAY_MAX, "insertion_delay_max"),
                (RE_INS_DELAY_MIN, "insertion_delay_min"),
                (RE_INS_DELAY_AVG, "insertion_delay_avg"),
            ]:
                m = pat.search(line)
                if m and current_clock:
                    setattr(get_or_create(current_clock), attr,
                            to_ns(float(m.group(1)), m.group(2)))

        # Latency
        m = RE_LATENCY.search(line)
        if m and current_clock:
            get_or_create(current_clock).latency = to_ns(float(m.group(1)), m.group(2))

        # Violations
        m = RE_SETUP_VIOL.search(line)
        if m and current_clock:
            get_or_create(current_clock).setup_violations += int(m.group(1))

        m = RE_HOLD_VIOL.search(line)
        if m and current_clock:
            get_or_create(current_clock).hold_violations += int(m.group(1))

        # Structural
        m = RE_BUF_DEPTH.search(line)
        if m and current_clock:
            get_or_create(current_clock).buffer_depth = int(m.group(1))

        m = RE_ENDPOINTS.search(line)
        if m and current_clock:
            get_or_create(current_clock).endpoints = int(m.group(1))

        m = RE_BALANCE.search(line)
        if m and current_clock:
            get_or_create(current_clock).tree_balance = m.group(1)

    # ── Fallback summary-table scan (no clock header found) ─────────────────
    if not clocks:
        warnings.append("No explicit 'Clock:' headers found – attempting summary-table parse.")
        for m in RE_SUMMARY_ROW.finditer(text):
            name = m.group(1)
            if name.lower() in ("clock", "name", "clk", "total"):
                continue
            cm = get_or_create(name)
            cm.max_skew_ps          = float(m.group(2)) * 1000  # assume ns
            cm.insertion_delay_min  = float(m.group(3))
            cm.insertion_delay_max  = float(m.group(4))
            cm.insertion_delay_avg  = float(m.group(5))

    if not clocks:
        warnings.append("Could not parse any clock data. Check report format.")

    return {"clocks": clocks, "_warnings": warnings}


# ─── 2. ANALYSIS LAYER ───────────────────────────────────────────────────────
def analyze_cts_data(data: dict) -> dict:
    """
    Perform pattern-based reasoning and classify issues per clock.
    Returns dict with classified results and aggregate stats.
    """
    clocks: dict[str, ClockMetrics] = data.get("clocks", {})

    critical:  list[dict] = []
    warnings_out: list[dict] = []
    healthy:   list[str]  = []
    total_setup = total_hold = 0

    for name, cm in clocks.items():
        issues: list[str] = []
        skew_ps = cm.max_skew_ps
        ins_max = cm.insertion_delay_max

        # ── Skew analysis ────────────────────────────────────────────────────
        if skew_ps is not None:
            if skew_ps > SKEW_THRESHOLD_PS * 2:
                issues.append(f"CRITICAL_SKEW:{skew_ps:.1f}ps")
            elif skew_ps > SKEW_THRESHOLD_PS:
                issues.append(f"HIGH_SKEW:{skew_ps:.1f}ps")

            if cm.avg_skew_ps is not None:
                variance = skew_ps - cm.avg_skew_ps
                if variance > SKEW_THRESHOLD_PS:
                    issues.append("SKEW_DISTRIBUTION_WIDE")

        # ── Insertion delay analysis ─────────────────────────────────────────
        if ins_max is not None:
            if ins_max > INSERTION_DELAY_THRESHOLD_NS * 2:
                issues.append(f"EXCESSIVE_INSERTION_DELAY:{ins_max:.3f}ns")
            elif ins_max > INSERTION_DELAY_THRESHOLD_NS:
                issues.append(f"HIGH_INSERTION_DELAY:{ins_max:.3f}ns")

        # Correlation: over-buffering vs topology issue
        if ins_max is not None and skew_ps is not None:
            if ins_max > INSERTION_DELAY_THRESHOLD_NS and skew_ps <= SKEW_THRESHOLD_PS:
                issues.append("PATTERN:OVER_BUFFERING")
            elif ins_max > INSERTION_DELAY_THRESHOLD_NS and skew_ps > SKEW_THRESHOLD_PS:
                issues.append("PATTERN:ROUTING_TOPOLOGY_ISSUE")

        # ── Violation analysis ───────────────────────────────────────────────
        sv, hv = cm.setup_violations, cm.hold_violations
        total_setup += sv
        total_hold  += hv
        total_viol   = sv + hv

        if total_viol > VIOLATION_CLUSTER_THRESHOLD:
            issues.append(f"VIOLATION_CLUSTER:{sv}S/{hv}H")
        elif sv > 0 and hv == 0:
            issues.append(f"SETUP_DOMINATED:{sv}")
        elif hv > 0 and sv == 0:
            issues.append(f"HOLD_DOMINATED:{hv}")
        elif sv > 0 and hv > 0:
            issues.append(f"MIXED_VIOLATIONS:{sv}S/{hv}H")

        # ── Classify ─────────────────────────────────────────────────────────
        crit_tags = [i for i in issues if i.startswith("CRITICAL") or "CLUSTER" in i]
        warn_tags = [i for i in issues if i not in crit_tags]

        if crit_tags:
            critical.append({"clock": name, "metrics": cm, "issues": issues})
        elif warn_tags:
            warnings_out.append({"clock": name, "metrics": cm, "issues": issues})
        else:
            healthy.append(name)

    return {
        "critical": critical,
        "warnings": warnings_out,
        "healthy":  healthy,
        "parse_warnings": data.get("_warnings", []),
        "stats": {
            "total_clocks":  len(clocks),
            "total_setup_v": total_setup,
            "total_hold_v":  total_hold,
        },
    }


# ─── 3. ROOT CAUSE HYPOTHESIS GENERATION ────────────────────────────────────
def generate_hypotheses(analysis: dict) -> list:
    """
    Create root-cause hypotheses for each identified issue.
    Returns list of hypothesis dicts.
    """
    hypotheses: list[dict] = []

    all_entries = analysis["critical"] + analysis["warnings"]

    for entry in all_entries:
        clock   = entry["clock"]
        cm: ClockMetrics = entry["metrics"]
        issues  = entry["issues"]

        for issue in issues:
            hyp = {"clock": clock, "symptom": issue}

            if "CRITICAL_SKEW" in issue or "HIGH_SKEW" in issue:
                skew_val = issue.split(":")[1]
                hyp.update({
                    "symptom":       f"High clock skew ({skew_val}) on '{clock}'",
                    "likely_cause":  "Clock tree imbalance due to uneven buffer placement, "
                                     "congestion-driven detours, or floorplan mismatch.",
                    "suggested_fix": "Re-run CTS with tighter skew targets; check CTS "
                                     "clustering constraints; verify NDR rules on clock nets; "
                                     "review floorplan for macro blockages affecting clock routing.",
                    "confidence":    "High" if "CRITICAL" in issue else "Medium",
                })

            elif "SKEW_DISTRIBUTION_WIDE" in issue:
                hyp.update({
                    "symptom":       f"Wide skew distribution on '{clock}' (large max–avg gap)",
                    "likely_cause":  "Localized skew issue: a subset of sinks have long paths "
                                     "due to detour routing or isolated high-load nets.",
                    "suggested_fix": "Identify outlier sinks using clock path reports; "
                                     "add shielding or local buffering; adjust CTS sink clustering.",
                    "confidence":    "Medium",
                })

            elif "OVER_BUFFERING" in issue:
                delay_val = cm.insertion_delay_max
                hyp.update({
                    "symptom":       f"Excessive insertion delay ({delay_val:.3f}ns) with acceptable skew on '{clock}'",
                    "likely_cause":  "Over-buffering: too many buffer levels inflating latency "
                                     "without benefit to skew. Possibly overly tight skew targets.",
                    "suggested_fix": "Relax CTS skew target slightly; reduce max buffer count; "
                                     "use higher-drive buffers to reduce depth; "
                                     "review CTS library cells for better drive strength options.",
                    "confidence":    "High",
                })

            elif "ROUTING_TOPOLOGY_ISSUE" in issue:
                hyp.update({
                    "symptom":       f"Both high insertion delay and high skew on '{clock}'",
                    "likely_cause":  "Routing congestion forcing long detours on clock nets, "
                                     "or poor clock source placement relative to sink cluster.",
                    "suggested_fix": "Improve floorplan: move clock source closer to centroid; "
                                     "reduce routing congestion in critical regions; "
                                     "use NDR (non-default routing rules) with wider spacing.",
                    "confidence":    "High",
                })

            elif "EXCESSIVE_INSERTION_DELAY" in issue or "HIGH_INSERTION_DELAY" in issue:
                delay_val = cm.insertion_delay_max
                hyp.update({
                    "symptom":       f"High insertion delay ({delay_val:.3f}ns) on '{clock}'",
                    "likely_cause":  "Long clock path from source to sinks; possible routing detour "
                                     "or insufficient drive strength in buffer chain.",
                    "suggested_fix": "Use higher-drive buffers near source; check for long wire "
                                     "segments in clock path; review CTS buffer library selection.",
                    "confidence":    "Medium",
                })

            elif "VIOLATION_CLUSTER" in issue:
                sv, hv = cm.setup_violations, cm.hold_violations
                hyp.update({
                    "symptom":       f"Violation cluster on '{clock}': {sv} setup / {hv} hold",
                    "likely_cause":  "Systemic timing issue on this clock domain – likely skew-induced "
                                     "or a common path group with insufficient margin.",
                    "suggested_fix": "Run targeted path-group analysis; check common paths; "
                                     "consider clock uncertainty adjustments; "
                                     "review SDC constraints for over/under-constraining.",
                    "confidence":    "High",
                })

            elif "SETUP_DOMINATED" in issue:
                hyp.update({
                    "symptom":       f"Setup violations ({cm.setup_violations}) on '{clock}'",
                    "likely_cause":  "Critical path(s) missing timing due to late arrival or "
                                     "excessive clock latency to launch flip-flop.",
                    "suggested_fix": "Reduce insertion delay on launch path; size up cells on "
                                     "critical data path; check for false paths masking real violations.",
                    "confidence":    "Medium",
                })

            elif "HOLD_DOMINATED" in issue:
                hyp.update({
                    "symptom":       f"Hold violations ({cm.hold_violations}) on '{clock}'",
                    "likely_cause":  "Capture clock arriving too late or data path too short; "
                                     "common after CTS rebalancing.",
                    "suggested_fix": "Insert hold buffers on short data paths post-CTS; "
                                     "verify CTS did not over-reduce latency on capture side; "
                                     "check for missing hold uncertainty margins in SDC.",
                    "confidence":    "High",
                })

            elif "MIXED_VIOLATIONS" in issue:
                hyp.update({
                    "symptom":       f"Mixed violations ({cm.setup_violations}S/{cm.hold_violations}H) on '{clock}'",
                    "likely_cause":  "Competing constraints or multiple independent path groups "
                                     "with different slack conditions on same clock.",
                    "suggested_fix": "Segment analysis by path group; fix hold violations first "
                                     "(buffer insertion); then address setup via sizing/restructuring.",
                    "confidence":    "Medium",
                })

            else:
                continue  # skip internal tags not mapped above

            if "symptom" in hyp and "likely_cause" in hyp:
                hypotheses.append(hyp)

    return hypotheses


# ─── 4. RECOMMENDATION ENGINE + REPORT GENERATION ────────────────────────────
def generate_recommendations(hypotheses: list, analysis: dict) -> str:
    """
    Produce a prioritized Markdown diagnostic report.
    """
    stats   = analysis["stats"]
    healthy = analysis["healthy"]
    parse_w = analysis.get("parse_warnings", [])

    high:   list[str] = []
    medium: list[str] = []
    low:    list[str] = []
    obs:    list[str] = []

    for h in hypotheses:
        conf  = h.get("confidence", "Medium")
        clock = h["clock"]
        sym   = h.get("symptom", "")
        cause = h.get("likely_cause", "")
        fix   = h.get("suggested_fix", "")

        entry = (
            f"**`{clock}`** – {sym}\n"
            f"  - 🔍 *Likely Cause:* {cause}\n"
            f"  - 🔧 *Fix:* {fix}\n"
            f"  - *Confidence:* {conf}"
        )

        if conf == "High" and ("CRITICAL" in sym.upper() or "CLUSTER" in sym.upper()
                               or "ROUTING" in sym.upper() or "OVER_BUFF" in sym.upper()
                               or "HOLD" in sym.upper()):
            high.append(entry)
        elif conf == "High" or conf == "Medium":
            medium.append(entry)
        else:
            low.append(entry)

    # ── System-level observations ─────────────────────────────────────────────
    total_v = stats["total_setup_v"] + stats["total_hold_v"]
    if stats["total_hold_v"] > stats["total_setup_v"]:
        obs.append("Hold violations dominate – typical post-CTS artifact; "
                   "prioritize hold-buffer insertion before setup optimization.")
    elif stats["total_setup_v"] > stats["total_hold_v"]:
        obs.append("Setup violations dominate – review critical path constraints "
                   "and CTS insertion delay targets.")
    if len(analysis["critical"]) > len(clocks := analysis.get("critical", [])) // 2 + 1:
        obs.append("More than half of analyzed clocks are in critical state – "
                   "consider a global CTS re-run with revised constraints.")
    if any("OVER_BUFFERING" in str(e["issues"]) for e in analysis["warnings"]):
        obs.append("Over-buffering pattern detected on at least one clock – "
                   "review CTS max-buffer and skew-target settings globally.")

    # ── Markdown assembly ─────────────────────────────────────────────────────
    lines = ["# 🕐 ClockIQ — CTS Diagnostic Report", ""]

    # Summary stats
    lines += [
        "## Summary Statistics",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total clocks analyzed | {stats['total_clocks']} |",
        f"| Critical clocks       | {len(analysis['critical'])} |",
        f"| Warning clocks        | {len(analysis['warnings'])} |",
        f"| Healthy clocks        | {len(healthy)} |",
        f"| Total setup violations | {stats['total_setup_v']} |",
        f"| Total hold violations  | {stats['total_hold_v']} |",
        "",
    ]

    # Parse warnings (if any)
    if parse_w:
        lines += ["> ⚠️ **Parser Notices:**"]
        for w in parse_w:
            lines.append(f"> - {w}")
        lines.append("")

    # Critical
    lines += ["---", "## 🔴 Critical Issues (High Priority)", ""]
    if high:
        for item in high:
            lines += [f"- {item}", ""]
    else:
        lines.append("_No critical issues detected._\n")

    # Warnings
    lines += ["---", "## 🟡 Warnings (Medium Priority)", ""]
    if medium:
        for item in medium:
            lines += [f"- {item}", ""]
    else:
        lines.append("_No medium-priority warnings._\n")

    # Low priority
    lines += ["---", "## 🔵 Low Priority / Validation", ""]
    low_defaults = [
        "Validate all clock uncertainty (setup/hold jitter) margins in SDC.",
        "Verify CTS target latency values reflect actual PVT corners.",
        "Fine-tune `set_clock_uncertainty` if post-CTS skew is within target.",
    ]
    for item in (low or low_defaults):
        lines += [f"- {item}", ""]

    # Healthy
    lines += ["---", "## 🟢 Healthy Clocks", ""]
    if healthy:
        for c in healthy:
            lines.append(f"- `{c}` — All metrics within target thresholds.")
    else:
        lines.append("_No clocks fully meeting all targets._")
    lines.append("")

    # Observations
    lines += ["---", "## 🔭 Observations (System-level Insights)", ""]
    if obs:
        for o in obs:
            lines += [f"- {o}", ""]
    else:
        lines.append("_No system-level patterns identified beyond per-clock findings._\n")

    return "\n".join(lines)


# ─── MAIN ENTRY POINT ────────────────────────────────────────────────────────
def run(input_path: Optional[str] = None, text: Optional[str] = None) -> str:
    """
    Orchestrate the full analysis pipeline.
    Accepts either a file path or raw text.
    """
    if text is None:
        if input_path is None:
            raise ValueError("Provide either input_path or text.")
        p = Path(input_path)
        if not p.exists():
            raise FileNotFoundError(f"File not found: {input_path}")
        text = p.read_text(errors="replace")

    data       = parse_cts_report(text)
    analysis   = analyze_cts_data(data)
    hypotheses = generate_hypotheses(analysis)
    report     = generate_recommendations(hypotheses, analysis)
    return report


def main():
    parser = argparse.ArgumentParser(
        prog="clockiq",
        description="ClockIQ – CTS Diagnostics & Optimization Assistant",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--report", "-r", metavar="FILE",
                       help="Path to CTS report (.rpt / .log / text)")
    group.add_argument("--stdin", action="store_true",
                       help="Read CTS report text from STDIN")
    parser.add_argument("--output", "-o", metavar="FILE",
                        help="Write Markdown report to FILE (default: stdout)")
    args = parser.parse_args()

    if args.stdin:
        text = sys.stdin.read()
        result = run(text=text)
    else:
        result = run(input_path=args.report)

    if args.output:
        Path(args.output).write_text(result)
        print(f"[ClockIQ] Report written to {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()

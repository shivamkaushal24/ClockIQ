#!/usr/bin/env python3
"""
ClockIQ MCP Server
-------------------
Exposes the ClockIQ clock-tree diagnostic engine as MCP tools so Copilot CLI
can call them like any other agent (r2g, debug, hsd, etc.).

Tools:
  analyze_clock_tree(path, text)     — full ClockIQ analysis
  get_clock_critical_issues(path)    — critical issues only (fast triage)
  get_clock_timing_summary(path)     — per-clock metrics table
"""

import sys
import importlib.util
from pathlib import Path

# ── Load clockiq core engine ──────────────────────────────────────────────────
_AGENT_PATH = Path(__file__).parent / "clockiq.py"
_spec = importlib.util.spec_from_file_location("clockiq", _AGENT_PATH)
_ciq  = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_ciq)

# ── MCP server setup ──────────────────────────────────────────────────────────
from autobots_sdk.base.mcp.servers.base_server import AutobotsMCPStdioServer

mcp_clockiq = AutobotsMCPStdioServer(name="clockiq")


# ─────────────────────────────────────────────────────────────────────────────
# Tool 1: Full ClockIQ analysis
# ─────────────────────────────────────────────────────────────────────────────

@mcp_clockiq.tool()
def analyze_clock_tree(path: str = "", text: str = "") -> dict:
    """
    Run full ClockIQ analysis on a Fusion Compiler CTS report or run area.

    Accepts either a file/directory path or raw report text.
    Supports Cheetah/R2G apr_fc run area directories and single .rpt/.log files.

    Performs:
      - Clock metrics extraction (skew, insertion delay, latency, violations)
      - Pattern-based reasoning (over-buffering, routing issues, hold/setup classification)
      - Root-cause hypothesis generation (Symptom / Cause / Fix / Confidence)
      - Prioritized recommendations

    Args:
        path (str): Path to apr_fc run area directory OR a .rpt/.log file.
                    Example: /nfs/site/disks/<disk>/<user>/<block>/runs/<step>/apr_fc
        text (str): Raw CTS report text (alternative to path).

    Returns:
        dict: {
            "success": bool,
            "report": str,              # Full Markdown ClockIQ report
            "critical_count": int,
            "warning_count": int,
            "healthy_clocks": list[str],
            "critical_issues": list[str],
            "warnings": list[str],
            "observations": list[str],
        }
    """
    if not path and not text:
        return {"success": False,
                "error": "Provide either 'path' (file/directory) or 'text' (raw report)."}
    try:
        if path:
            p = Path(path)
            if not p.exists():
                return {"success": False, "error": f"Path not found: {path}"}
            data = (_ciq.parse_cts_directory(p) if p.is_dir()
                    else _ciq.parse_cts_report(p.read_text(errors="replace")))
        else:
            data = _ciq.parse_cts_report(text)

        analysis   = _ciq.analyze_cts_data(data)
        hypotheses = _ciq.generate_hypotheses(analysis)
        report     = _ciq.generate_report(data, analysis, hypotheses,
                                          source_label=path or "<inline>")

        def _fmt(issue):
            detail = issue.get("detail", "")
            return (f"[{issue.get('metric','?').upper()}] clock={issue.get('clock','?')} "
                    f"value={issue.get('value','?')} pattern={issue.get('pattern','?')}"
                    + (f" — {detail}" if detail else ""))

        return {
            "success":        True,
            "report":         report,
            "critical_count": len(analysis["critical"]),
            "warning_count":  len(analysis["warnings"]),
            "healthy_clocks": analysis["healthy"],
            "critical_issues": [_fmt(i) for i in analysis["critical"]],
            "warnings":        [_fmt(i) for i in analysis["warnings"]],
            "observations":    analysis["observations"],
        }
    except Exception as exc:
        return {"success": False, "error": str(exc)}


# ─────────────────────────────────────────────────────────────────────────────
# Tool 2: Critical issues only (fast triage)
# ─────────────────────────────────────────────────────────────────────────────

@mcp_clockiq.tool()
def get_clock_critical_issues(path: str) -> dict:
    """
    Return only critical issues from a CTS run area (fast triage).

    Args:
        path (str): Path to apr_fc run area or .rpt/.log file.

    Returns:
        dict: {
            "success": bool,
            "critical_count": int,
            "issues": list[{clock, metric, value, pattern, hypothesis}],
        }
    """
    p = Path(path)
    if not p.exists():
        return {"success": False, "error": f"Path not found: {path}"}
    try:
        data       = (_ciq.parse_cts_directory(p) if p.is_dir()
                      else _ciq.parse_cts_report(p.read_text(errors="replace")))
        analysis   = _ciq.analyze_cts_data(data)
        hypotheses = _ciq.generate_hypotheses(analysis)

        crit_hyps = {h["clock"]: h for h in hypotheses if h["priority"] == "critical"}
        issues = []
        for issue in analysis["critical"]:
            clk  = issue.get("clock", "?")
            hyp  = crit_hyps.get(clk, {})
            issues.append({
                "clock":      clk,
                "metric":     issue.get("metric", "?"),
                "value":      issue.get("value"),
                "pattern":    issue.get("pattern", "?"),
                "detail":     issue.get("detail", ""),
                "hypothesis": hyp.get("cause", ""),
                "fix":        hyp.get("fix", ""),
                "confidence": hyp.get("confidence", "—"),
            })

        return {
            "success":        True,
            "critical_count": len(issues),
            "issues":         issues,
        }
    except Exception as exc:
        return {"success": False, "error": str(exc)}


# ─────────────────────────────────────────────────────────────────────────────
# Tool 3: Per-clock metrics table
# ─────────────────────────────────────────────────────────────────────────────

@mcp_clockiq.tool()
def get_clock_timing_summary(path: str) -> dict:
    """
    Get a per-clock metrics table for a CTS run area.

    Shows skew, insertion delay, and violation counts per clock in both
    structured form and as a Markdown table.

    Args:
        path (str): Path to apr_fc run area or .rpt/.log file.

    Returns:
        dict: {
            "success": bool,
            "total_clocks": int,
            "summary": list[{clock, skew_max_ps, ins_delay_avg_ps,
                              setup_viols, hold_viols, status}],
            "table": str,   # Markdown table
        }
    """
    p = Path(path)
    if not p.exists():
        return {"success": False, "error": f"Path not found: {path}"}
    try:
        data     = (_ciq.parse_cts_directory(p) if p.is_dir()
                    else _ciq.parse_cts_report(p.read_text(errors="replace")))
        analysis = _ciq.analyze_cts_data(data)

        healthy_set = set(analysis["healthy"])
        critical_set = {i.get("clock") for i in analysis["critical"]}

        summary = []
        for clk, c in data["clocks"].items():
            if clk.startswith("__"):
                continue
            if clk in critical_set:
                status = "🔴 Critical"
            elif clk not in healthy_set:
                status = "🟡 Warning"
            else:
                status = "🟢 Healthy"
            summary.append({
                "clock":           clk,
                "skew_max_ps":     c.get("skew_max_ps"),
                "ins_delay_avg_ps": c.get("ins_delay_avg_ps"),
                "setup_viols":     c.get("setup_violations", 0),
                "hold_viols":      c.get("hold_violations", 0),
                "status":          status,
            })

        rows = [
            "| Clock | Max Skew (ps) | Ins Delay avg (ps) | Setup Viols | Hold Viols | Status |",
            "|---|---|---|---|---|---|",
        ]
        for r in sorted(summary, key=lambda x: x["clock"]):
            sk = f"{r['skew_max_ps']:.0f}" if r["skew_max_ps"] is not None else "—"
            dl = f"{r['ins_delay_avg_ps']:.0f}" if r["ins_delay_avg_ps"] is not None else "—"
            rows.append(
                f"| `{r['clock']}` | {sk} | {dl} | "
                f"{r['setup_viols']} | {r['hold_viols']} | {r['status']} |"
            )

        return {
            "success":      True,
            "total_clocks": len(summary),
            "summary":      summary,
            "table":        "\n".join(rows),
        }
    except Exception as exc:
        return {"success": False, "error": str(exc)}


# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp_clockiq.run()

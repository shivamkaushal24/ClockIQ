# 🕐 ClockIQ — Clock Tree Diagnostics & Optimization Assistant

**ClockIQ** is a GitHub Copilot skill that analyzes **Synopsys Fusion Compiler CTS (Clock Tree Synthesis)** reports and generates structured diagnostics, root-cause hypotheses, and prioritized debug recommendations — reasoning like an experienced physical design engineer.

---

## Features

- 📊 **Parsing Layer** — Extracts clock metrics (skew, insertion delay, latency, violations, buffer depth) from `.rpt` / `.log` / `.txt` files using robust regex with graceful fallback
- 🧠 **Analysis Layer** — Pattern-based reasoning: detects over-buffering, routing topology issues, violation clustering, skew distribution problems
- 🔍 **Root Cause Hypotheses** — Symptom → Likely Cause → Suggested Fix with Confidence Level
- 📋 **Prioritized Markdown Report** — 🔴 Critical / 🟡 Warnings / 🟢 Healthy / 🔭 Observations

---

## Usage

```bash
# Analyze a CTS report file
python3 clockiq_agent.py --report path/to/cts.rpt

# Save output to a Markdown file
python3 clockiq_agent.py --report cts.rpt --output report.md

# Pipe from stdin
cat cts.log | python3 clockiq_agent.py --stdin
```

---

## Sample Output

```
# 🕐 ClockIQ — CTS Diagnostic Report

## Summary Statistics
| Metric | Value |
|--------|-------|
| Total clocks analyzed | 4 |
| Critical clocks       | 2 |
| Healthy clocks        | 2 |
| Total hold violations | 62 |

## 🔴 Critical Issues (High Priority)
- **`CLK_IO`** – Violation cluster: 22 setup / 15 hold
  - 🔍 Likely Cause: Systemic timing issue, skew-induced or common path group...
  - 🔧 Fix: Run targeted path-group analysis; check common paths...

## 🟢 Healthy Clocks
- `CLK_MEM` — All metrics within target thresholds.
- `CLK_SCAN` — All metrics within target thresholds.
```

---

## Analysis Rules

| Pattern | Diagnosis |
|---------|-----------|
| High skew (>100ps) | Clock tree imbalance, floorplan/routing issue |
| High delay + low skew | Over-buffering |
| High delay + high skew | Routing congestion / topology issue |
| >10 violations on one clock | Violation cluster — systemic issue |
| Hold-dominated violations | Post-CTS artifact — insert hold buffers |

---

## Configurable Thresholds

Edit the constants at the top of `clockiq_agent.py`:

```python
SKEW_THRESHOLD_PS            = 100.0   # ps
INSERTION_DELAY_THRESHOLD_NS = 1.0     # ns
VIOLATION_CLUSTER_THRESHOLD  = 10      # violations per clock
```

---

## File Structure

```
ClockIQ/
├── clockiq_agent.py   # Main agent (Python 3, stdlib only)
├── skill.yaml         # Skill metadata
├── sample_cts.rpt     # Sample Fusion Compiler CTS report
└── README.md
```

---

## Requirements

- Python 3.8+
- No external dependencies — fully offline capable

---

## Input Format

Supports Synopsys Fusion Compiler CTS reports (Cheetah flow) with sections like:

```
Clock: CLK_CORE
  Max Skew          : 0.215 ns
  Insertion Delay (min / max / avg) : 0.820 / 1.450 / 1.105 ns
  Setup Violations  : 0
  Hold Violations   : 47
```

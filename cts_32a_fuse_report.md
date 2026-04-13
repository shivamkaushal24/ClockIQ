# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_32a_cth/par_base_fuse`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 12 |
| 🔴 Critical issues | **22** |
| 🔴 Warnings | **20** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 105 |
| Hold violations | 403 |
| Avg violations/clock | 8.8 |
| Setup diagnosis | LOCALIZED_VIOLATIONS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 20 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `oddccfclk`, `N/A`, `sbclk_right`
> **Metrics flagged:** CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PDN_PG_CUTS, CHECK_PDFX_CONTENT, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_NETSPEC_LSPEC, CHECK_DANGLING_USER_SHAPES, INSERTION_DELAY, CHECK_DANGLING_PORTS_PINS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_IO_PLACEMENT, CHECK_HALO_LOCATIONS, CTS_VIOLATION, CHECK_PLACEMENT_LEGALITY, CHECK_PWR_INTEG, SKEW, CHECK_PDN_POLYGONS, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_NETSPEC_MISSING_SHIELD, CHECK_STD_CELL_POWER_HOOKUP
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`tapclk`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`roclk`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`sbclk_right`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`tapclk`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`visaclk`
### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 1740 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `oddccfclk` | `141 ps` | `100 ps` | global |
| 2 | **INSERTION_DELAY** | `sbclk_right` | `1130 ps` | `1000 ps` | routing_topology |
| 3 | **CTS_VIOLATION** | `N/A` | `29 ps` | `0 ps` | CTS-997 |
| 4 | **CHECK_PWR_INTEG** | `N/A` | `754 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDN_PG_CUTS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 6 | **CHECK_IO_PLACEMENT** | `N/A` | `17 ps` | `0 ps` | health_check |
| 7 | **CHECK_PDFX_CONTENT** | `N/A` | `22 ps` | `0 ps` | health_check |
| 8 | **CHECK_PDN_POLYGONS** | `N/A` | `1004 ps` | `0 ps` | health_check |
| 9 | **CHECK_NETSPEC_LSPEC** | `N/A` | `2 ps` | `0 ps` | health_check |
| 10 | **CHECK_HALO_LOCATIONS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 11 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `34 ps` | `0 ps` | health_check |
| 12 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `343 ps` | `0 ps` | health_check |
| 13 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `461 ps` | `0 ps` | health_check |
| 14 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `20 ps` | `0 ps` | health_check |
| 15 | **CHECK_STD_CELL_POWER_HOOKUP** | `N/A` | `2 ps` | `0 ps` | health_check |
| 16 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `4 ps` | `0 ps` | health_check |
| 17 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 18 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 19 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `11 ps` | `0 ps` | health_check |
| 20 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `9 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk` |
| Measured value | `140.6 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 2 — [INSERTION_DELAY] `sbclk_right`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_right` |
| Measured value | `1130.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_right}
```

#### ⚠️ Warning 3 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `29.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 29 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `754.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 754 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 8 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `17.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 17 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `22.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 22 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1004.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1004 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 2 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 8 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `34.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 34 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `343.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 343 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `461.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 461 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `20.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 20 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_STD_CELL_POWER_HOOKUP] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_STD_CELL_POWER_HOOKUP` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_std_cell_power_hookup = 2 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `4.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 4 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `5.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 5 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 2 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 19 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `11.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 11 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `9.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 9 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (408 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: oddccf_l2tclk, tapclk_sys, xtalclk. May indicate post-CTS routing detours affecting both timing types.
- ℹ️  Total CTS buffer/inverter cells in design: 16,259.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_32a_cth` | `par_base_fuse` | 12 | 105 | 403 | 22 | 🔴 D |


## 🟢 Hold Violations

_No significant hold violations detected._


## 🟡 Setup Violation Analysis


### 🟢 Setup Clustering — `1p0_32a_cth/par_base_fuse`

| Field | Detail |
|---|---|
| Diagnosis | **LOCALIZED_VIOLATIONS** |
| Confidence | MEDIUM |
| Setup violations | **105** across 12 clocks |
| Avg violations/clock | **8.8** |

**Root Cause:** Avg 8.8 violations/clock → isolated path issues or MBFF-specific problems on a subset of clocks.

**Diagnostic Steps:**

1. Identify which specific clocks carry violations
2. Check if violating endpoints are MBFF outputs
3. If MBFF → debank to single-bit; if not → upsize/retime cells

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | MBFF endpoint issue | LOW–MEDIUM | 50–80% for MBFF-specific violations |
| 2 | Critical path logic depth | MEDIUM | 20–30% violation reduction |

**FC Commands (ranked):**

*Option 1 — MBFF endpoint issue:*
```tcl
set_multibit_options -exclude [get_cells {violating_mbs}]; compile_clock_tree -incremental
```

*Option 2 — Critical path logic depth:*
```tcl
optimize_netlist -area; place_opt -effort high
```


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 469 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk' max skew = 637 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk' max skew = 566 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 583 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 513 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 581 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 551 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 818 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 9 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 9 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 1740 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 141 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1130 ps (1.130 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** 29 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 754 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 17 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 22 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1004 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 2 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 34 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 343 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 461 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 20 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_std_cell_power_hookup = 2 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 4 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 5 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 2 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 11 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 9 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 29  |  **Priority:** MEDIUM

**Message pattern:**  
> Failed sizing pre-existing cell '{cell}' with CTS reference cell.

**Root Cause:**  
CTS attempted to resize a pre-existing clock cell (from a previous compile or ECO) to a reference cell from the CTS library, but could not find a legal substitution. Causes: (a) the cell type is not in the CTS reference list (`set_clock_tree_references`), (b) the cell has `dont_touch` or `dont_size` attribute, (c) the cell is inside a read-only or hierarchical boundary block, or (d) the cell is a DFX/secure plugin that must remain as-is.

**Impact:**  
The cell retains its original drive strength, which may be mismatched for the current fanout. This can cause: (a) transition-time DRC on downstream nets, (b) latency imbalance in the branch driven by this cell, (c) hold/setup violations at sinks driven by the mis-sized cell. High occurrence counts (>100) indicate a systematic library or dont_touch issue.

**Recommended Fixes:**

  **Fix 1:** Confirm the cell is a protected DFX cell — waive if so
  _DFX/secure plugin cells — intentional, safe to waive_
  ```tcl
  # These cells are typically intentional dont_touch in DFX stacks.
  # Verify by checking cell names for 'dfxsecure', 'ctmi_', 'stap_':
  report_attribute [get_cells {cell}] dont_touch
  ```

  **Fix 2:** Add the required reference cell to the CTS reference list
  _Cell missing from CTS reference list_
  ```tcl
  set_clock_tree_references -references [list {existing} {missing_ref}] -clock {clk}
  compile_clock_tree -incremental
  ```

  **Fix 3:** Remove dont_touch if safe, then allow CTS to resize
  _Cell has dont_touch attribute preventing resize_
  ```tcl
  remove_attribute [get_cells {cell}] dont_touch
  compile_clock_tree -incremental
  ```

**Related codes:** `CTS-055`

---

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*
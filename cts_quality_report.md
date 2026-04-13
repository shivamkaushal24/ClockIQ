# ClockIQ — CTS Quality Report (Improved Agent)

**Scan area:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb`  
**Runs analysed:** 14  

---

## Multi-Run Fellow-Level Analysis

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_21a_cth` | `par_base_fuse` | 1 | 0 | 0 | 0 | 🟢 A |
| `1p0_21a_cth` | `par_base_fabric_slice_1` | 1 | 0 | 0 | 0 | 🟢 A |
| `1p0_28a_cth` | `par_base_fuse` | 1 | 0 | 0 | 0 | 🟢 A |
| `1p0_28a_cth` | `par_base_fabric_slice_1` | 1 | 0 | 0 | 0 | 🟢 A |
| `1p0_28a_cth_new` | `par_base_fuse` | 1 | 0 | 0 | 0 | 🟢 A |
| `1p0_28a_cth_new` | `par_base_fabric_slice_1` | 51 | 6,871 | 9,273 | 0 | 🔴 D |
| `1p0_28a_cth_pc` | `par_base_fabric_slice_1` | 1 | 0 | 0 | 0 | 🟢 A |
| `1p0_32a_cth` | `par_base_fuse` | 12 | 105 | 403 | 0 | 🟡 B |
| `1p0_32a_cth` | `par_base_fabric_slice_1` | 1 | 6,892 | 112,722 | 0 | 🔴 D |
| `1p0_35a_cth` | `par_base_fuse` | 12 | 99 | 460 | 0 | 🟡 B |
| `1p0_35a_cth` | `par_base_fabric_slice_1` | 51 | 6,026 | 9,642 | 0 | 🔴 D |
| `1p0_35a_cth_pc` | `par_base_fabric_slice_1` | 51 | 6,026 | 9,642 | 0 | 🔴 D |
| `1p0_39a_cth` | `par_base_fuse` | 22 | 6,026 | 9,642 | 0 | 🔴 D |
| `1p0_39a_cth` | `par_base_fabric_slice_1` | 20 | 0 | 0 | 0 | 🟢 A |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,273** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 16,691 |
| Estimated runtime | 83 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


### 🔴 Hold Analysis — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **MBFF_CLOCK_PUSH_EXPLOSION** |
| Confidence | HIGH |
| Hold violations | **112,722** |

**Root Cause:** 112,722 hold violations indicates clock path was pushed on replicated MBFFs. Pushing clock on MBFF affects all bits → massive skew delta → hold violations at all startpoints simultaneously.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 281,805 |
| Area overhead | 338,166 µm² |
| Power overhead | 1409.0 mW |
| Estimated runtime | 1409 hrs |

**Recommended Fix:** REVERT clock push + DEBANK affected MBFFs

**FC Commands:**
```tcl
undo                                              # Revert last clock ECO
set_multibit_options -exclude [get_cells {mbff_instances}]
compile_clock_tree -incremental
```

**Expected Outcome:** Add ~704 single-bit flops, avoid 281,805 hold buffers

**Net Savings (vs buffer fix):** ~336,406 µm² area saved, ~1409 hours runtime avoided


### 🟡 Hold Analysis — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,642** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 17,355 |
| Estimated runtime | 86 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


### 🟡 Hold Analysis — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,642** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 17,355 |
| Estimated runtime | 86 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


### 🟡 Hold Analysis — `par_base_fuse`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,642** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 17,355 |
| Estimated runtime | 86 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟡 Setup Violation Analysis


### 🔴 Setup Clustering — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,871** across 51 clocks |
| Avg violations/clock | **134.7** |

**Root Cause:** Avg 135 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


### 🟢 Setup Clustering — `par_base_fuse`

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


### 🔴 Setup Clustering — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,892** across 1 clocks |
| Avg violations/clock | **6892.0** |

**Root Cause:** Avg 6892 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


### 🔴 Setup Clustering — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,026** across 51 clocks |
| Avg violations/clock | **118.2** |

**Root Cause:** Avg 118 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


### 🔴 Setup Clustering — `par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,026** across 51 clocks |
| Avg violations/clock | **118.2** |

**Root Cause:** Avg 118 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


### 🔴 Setup Clustering — `par_base_fuse`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,026** across 22 clocks |
| Avg violations/clock | **273.9** |

**Root Cause:** Avg 274 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


## 📈 Flow Generation Analysis


### 📈 Flow Generation Comparison

| Transition | Improvement | Setup Reduction | Status |
|---|---|---|---|
| `1p0_21a_cth→1p0_28a_cth` | **1.0×** | 0 fewer viols | 🔴 NO_IMPROVEMENT |
| `1p0_28a_cth→1p0_28a_cth_new` | **0.0×** | -3,434 fewer viols | 🔴 NO_IMPROVEMENT |
| `1p0_28a_cth_new→1p0_28a_cth_pc` | **3435.0×** | 3,434 fewer viols | 🟢 SIGNIFICANT_IMPROVEMENT |
| `1p0_28a_cth_pc→1p0_32a_cth` | **0.0×** | -3,497 fewer viols | 🔴 NO_IMPROVEMENT |
| `1p0_32a_cth→1p0_35a_cth` | **1.1×** | 436 fewer viols | 🔴 NO_IMPROVEMENT |
| `1p0_35a_cth→1p0_35a_cth_pc` | **0.5×** | -2,964 fewer viols | 🔴 NO_IMPROVEMENT |
| `1p0_35a_cth_pc→1p0_39a_cth` | **2.0×** | 3,013 fewer viols | 🟡 INCREMENTAL_IMPROVEMENT |

**1p0_21a_cth→1p0_28a_cth:** No meaningful improvement 1p0_21a_cth→1p0_28a_cth; investigate regression

**1p0_28a_cth→1p0_28a_cth_new:** No meaningful improvement 1p0_28a_cth→1p0_28a_cth_new; investigate regression

**1p0_28a_cth_new→1p0_28a_cth_pc:** Backport 1p0_28a_cth_pc CTS recipe settings to 1p0_28a_cth_new; expected to reduce violations by ~3435×

  Investigation steps:
  - `diff 1p0_28a_cth_new/scripts/cts_options.tcl 1p0_28a_cth_pc/scripts/cts_options.tcl`
  - `Compare MBFF grouping policies (group_size, exclude lists)`
  - `Compare floorplan utilisation and blockage maps`
  - `Compare clock uncertainty / OCV margin settings`

**1p0_28a_cth_pc→1p0_32a_cth:** No meaningful improvement 1p0_28a_cth_pc→1p0_32a_cth; investigate regression

**1p0_32a_cth→1p0_35a_cth:** No meaningful improvement 1p0_32a_cth→1p0_35a_cth; investigate regression

**1p0_35a_cth→1p0_35a_cth_pc:** No meaningful improvement 1p0_35a_cth→1p0_35a_cth_pc; investigate regression

**1p0_35a_cth_pc→1p0_39a_cth:** Minor improvements from 1p0_35a_cth_pc→1p0_39a_cth; review skew targets


---

## Per-Run Detailed Reports



---

### `1p0_21a_cth/par_base_fuse`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_21a_cth/runs/par_base_fuse/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 2 |
| 🟡 Warnings | 18 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 30 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## 🟡 Warnings (Medium Priority)

- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`755` | pattern=`health_check`
  > check_pwr_integ = 755 at compile_final_opto
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`24` | pattern=`health_check`
  > check_pdn_pg_cuts = 24 at compile_final_opto
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`15` | pattern=`health_check`
  > check_io_placement = 15 at compile_final_opto
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`22` | pattern=`health_check`
  > check_pdfx_content = 22 at compile_final_opto
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`792` | pattern=`health_check`
  > check_pdn_polygons = 792 at compile_final_opto
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_netspec_lspec = 1 at compile_final_opto
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_halo_locations = 8 at compile_final_opto
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_port_net_names = 1 at compile_final_opto
- **[CHECK_LONG_FLAT_NAMES]** clock=`N/A` | value=`102` | pattern=`health_check`
  > check_long_flat_names = 102 at compile_final_opto
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`34` | pattern=`health_check`
  > check_placement_legality = 34 at compile_final_opto
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`343` | pattern=`health_check`
  > check_dangling_ports_pins = 343 at compile_final_opto
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`467` | pattern=`health_check`
  > check_signal_elevator_xor = 467 at compile_final_opto
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`23` | pattern=`health_check`
  > check_dangling_user_shapes = 23 at compile_final_opto
- **[CHECK_STD_CELL_POWER_HOOKUP]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_std_cell_power_hookup = 2 at compile_final_opto
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_ports_with_multi_terms = 5 at compile_final_opto
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_wire_objects_at_boundary = 2 at compile_final_opto
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`9` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 9 at compile_final_opto
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`9` | pattern=`health_check`
  > check_netspec_repeater_distance = 9 at compile_final_opto

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 16,238.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 0 | 0 | 2 | 🟡 B |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 30 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 755 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 24 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 15 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 22 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 792 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_long_flat_names = 102 at compile_final_opto
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
  - **Symptom:** check_signal_elevator_xor = 467 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 23 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_std_cell_power_hookup = 2 at compile_final_opto
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
  - **Symptom:** check_clock_cells_cbc_placement = 9 at compile_final_opto
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

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_21a_cth/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_21a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 2 |
| 🟡 Warnings | 21 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 4548 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## 🟡 Warnings (Medium Priority)

- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`322` | pattern=`health_check`
  > check_pwr_integ = 322 at compile_final_opto
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`106` | pattern=`health_check`
  > check_pdn_pg_cuts = 106 at compile_final_opto
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`138` | pattern=`health_check`
  > check_io_placement = 138 at compile_final_opto
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`164` | pattern=`health_check`
  > check_pdfx_content = 164 at compile_final_opto
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`790` | pattern=`health_check`
  > check_pdn_polygons = 790 at compile_final_opto
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`35` | pattern=`health_check`
  > check_netspec_lspec = 35 at compile_final_opto
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at compile_final_opto
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`74` | pattern=`health_check`
  > check_port_net_names = 74 at compile_final_opto
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_naming_convention = 1 at compile_final_opto
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`57` | pattern=`health_check`
  > check_placement_legality = 57 at compile_final_opto
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`5344` | pattern=`health_check`
  > check_dangling_ports_pins = 5344 at compile_final_opto
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`280` | pattern=`health_check`
  > check_signal_elevator_xor = 280 at compile_final_opto
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`488` | pattern=`health_check`
  > check_dangling_user_shapes = 488 at compile_final_opto
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`650` | pattern=`health_check`
  > check_netspec_missing_shield = 650 at compile_final_opto
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`16` | pattern=`health_check`
  > check_ports_with_multi_terms = 16 at compile_final_opto
- **[CHECK_TERMINALS_NOT_ON_TRACK]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_terminals_not_on_track = 3 at compile_final_opto
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`18` | pattern=`health_check`
  > check_wire_objects_at_boundary = 18 at compile_final_opto
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at compile_final_opto
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`53` | pattern=`health_check`
  > check_netspec_repeater_distance = 53 at compile_final_opto
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`158` | pattern=`health_check`
  > check_additional_td_route_objects = 158 at compile_final_opto
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 52,348.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 0 | 0 | 2 | 🟡 B |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 4548 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 322 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 106 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 138 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 164 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 790 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 35 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 74 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 57 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 5344 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 280 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 488 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 650 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 16 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_terminals_not_on_track = 3 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 18 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 53 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 158 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_28a_cth/par_base_fuse`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth/runs/par_base_fuse/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 3 |
| 🟡 Warnings | 22 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [CHECK_OPENS] clock=`N/A`
> check_opens = 49 at finish

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 21 at finish

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at finish — check run log


## 🟡 Warnings (Medium Priority)

- **[CTS_VIOLATION]** clock=`N/A` | value=`43` | pattern=`CTS-997`
  > 43 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`755` | pattern=`health_check`
  > check_pwr_integ = 755 at finish
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`33` | pattern=`health_check`
  > check_pdn_pg_cuts = 33 at finish
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`15` | pattern=`health_check`
  > check_io_placement = 15 at finish
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`803` | pattern=`health_check`
  > check_pdn_polygons = 803 at finish
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_netspec_lspec = 3 at finish
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_halo_locations = 8 at finish
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_port_net_names = 1 at finish
- **[CHECK_PDN_VIAS_ON_GRID]** clock=`N/A` | value=`250` | pattern=`health_check`
  > check_pdn_vias_on_grid = 250 at finish
- **[CHECK_SHIELD_TILO_CELLS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_shield_tilo_cells = 5 at finish
- **[CHECK_TIEOFF_CONNECTION]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_tieoff_connection = 3 at finish
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_placement_legality = 2 at finish
- **[CHECK_PDN_HIPS_CONNECTION]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_pdn_hips_connection = 1 at finish
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`205` | pattern=`health_check`
  > check_signal_elevator_xor = 205 at finish
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`26` | pattern=`health_check`
  > check_dangling_user_shapes = 26 at finish
- **[CHECK_STD_CELL_POWER_HOOKUP]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_std_cell_power_hookup = 2 at finish
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_netspec_missing_shield = 1 at finish
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_ports_with_multi_terms = 5 at finish
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_wire_objects_at_boundary = 2 at finish
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`11` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 11 at finish
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`4` | pattern=`health_check`
  > check_netspec_repeater_distance = 4 at finish
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`50` | pattern=`health_check`
  > check_additional_td_route_objects = 50 at finish

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 15,998.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 0 | 0 | 3 | 🟡 B |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `N/A`
  - **Symptom:** check_opens = 49 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 21 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at finish — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** 43 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 755 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 33 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 15 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 803 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 3 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 8 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 1 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_vias_on_grid = 250 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_shield_tilo_cells = 5 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_tieoff_connection = 3 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_hips_connection = 1 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 205 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 26 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_std_cell_power_hookup = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 1 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 5 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 11 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 4 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 50 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_28a_cth/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 2 |
| 🟡 Warnings | 23 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 3065 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## 🟡 Warnings (Medium Priority)

- **[CTS_VIOLATION]** clock=`N/A` | value=`73` | pattern=`CTS-997`
  > 73 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`312` | pattern=`health_check`
  > check_pwr_integ = 312 at compile_final_opto
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`106` | pattern=`health_check`
  > check_pdn_pg_cuts = 106 at compile_final_opto
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`138` | pattern=`health_check`
  > check_io_placement = 138 at compile_final_opto
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`164` | pattern=`health_check`
  > check_pdfx_content = 164 at compile_final_opto
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`790` | pattern=`health_check`
  > check_pdn_polygons = 790 at compile_final_opto
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`102` | pattern=`health_check`
  > check_netspec_lspec = 102 at compile_final_opto
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at compile_final_opto
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`74` | pattern=`health_check`
  > check_port_net_names = 74 at compile_final_opto
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_naming_convention = 1 at compile_final_opto
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`55` | pattern=`health_check`
  > check_placement_legality = 55 at compile_final_opto
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`5344` | pattern=`health_check`
  > check_dangling_ports_pins = 5344 at compile_final_opto
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`280` | pattern=`health_check`
  > check_signal_elevator_xor = 280 at compile_final_opto
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`89` | pattern=`health_check`
  > check_dangling_user_shapes = 89 at compile_final_opto
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`237` | pattern=`health_check`
  > check_netspec_missing_shield = 237 at compile_final_opto
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`16` | pattern=`health_check`
  > check_ports_with_multi_terms = 16 at compile_final_opto
- **[CHECK_TERMINALS_NOT_ON_TRACK]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_terminals_not_on_track = 3 at compile_final_opto
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`26` | pattern=`health_check`
  > check_wire_objects_at_boundary = 26 at compile_final_opto
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at compile_final_opto
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`45` | pattern=`health_check`
  > check_netspec_repeater_distance = 45 at compile_final_opto
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`208` | pattern=`health_check`
  > check_additional_td_route_objects = 208 at compile_final_opto
- **[CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_netspec_dont_touch_constraints = 5 at compile_final_opto
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 49,200.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 0 | 0 | 2 | 🟡 B |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 3065 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** 73 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 312 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 106 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 138 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 164 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 790 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 102 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 74 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 55 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 5344 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 280 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 89 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 237 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 16 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_terminals_not_on_track = 3 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 26 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 45 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 208 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_dont_touch_constraints = 5 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_28a_cth_new/par_base_fuse`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth_new/runs/par_base_fuse/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 3 |
| 🟡 Warnings | 19 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [CHECK_OPENS] clock=`N/A`
> check_opens = 65 at finish

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 1717 at finish

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at finish — check run log


## 🟡 Warnings (Medium Priority)

- **[CTS_VIOLATION]** clock=`N/A` | value=`45` | pattern=`CTS-997`
  > 45 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`754` | pattern=`health_check`
  > check_pwr_integ = 754 at finish
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_pdn_pg_cuts = 1 at finish
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`17` | pattern=`health_check`
  > check_io_placement = 17 at finish
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1004` | pattern=`health_check`
  > check_pdn_polygons = 1004 at finish
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`4` | pattern=`health_check`
  > check_netspec_lspec = 4 at finish
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_halo_locations = 8 at finish
- **[CHECK_PDN_VIAS_ON_GRID]** clock=`N/A` | value=`529` | pattern=`health_check`
  > check_pdn_vias_on_grid = 529 at finish
- **[CHECK_SHIELD_TILO_CELLS]** clock=`N/A` | value=`11` | pattern=`health_check`
  > check_shield_tilo_cells = 11 at finish
- **[CHECK_TIEOFF_CONNECTION]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_tieoff_connection = 3 at finish
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_placement_legality = 2 at finish
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`197` | pattern=`health_check`
  > check_signal_elevator_xor = 197 at finish
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`24` | pattern=`health_check`
  > check_dangling_user_shapes = 24 at finish
- **[CHECK_STD_CELL_POWER_HOOKUP]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_std_cell_power_hookup = 2 at finish
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_netspec_missing_shield = 1 at finish
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_ports_with_multi_terms = 5 at finish
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_wire_objects_at_boundary = 2 at finish
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 10 at finish
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`6` | pattern=`health_check`
  > check_netspec_repeater_distance = 6 at finish

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 16,410.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 0 | 0 | 3 | 🟡 B |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `N/A`
  - **Symptom:** check_opens = 65 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 1717 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at finish — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** 45 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 754 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 1 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 17 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1004 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 4 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 8 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_vias_on_grid = 529 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_shield_tilo_cells = 11 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_tieoff_connection = 3 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 197 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 24 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_std_cell_power_hookup = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 1 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 5 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 10 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 6 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_28a_cth_new/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth_new/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 51 |
| 🔴 Critical issues | 78 |
| 🟡 Warnings | 45 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,871 |
| Hold violations | 9,273 |
| Avg violations/clock | 134.7 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`tapclk`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`sbclk_left_temp_6`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left_temp_2`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_temp_2`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_4`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_9`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 3019 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log

### [SETUP_CLUSTERING] clock=`ALL`
> Avg 135 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Ranked Fixes:**

| # | Hypothesis | Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |


## 🟡 Warnings (Medium Priority)

- **[SKEW]** clock=`sbclk_right_temp_5` | value=`126.6098` | pattern=`global`
- **[SKEW]** clock=`sbclk_left_pm_temp_2` | value=`142.6697` | pattern=`global`
- **[SKEW]** clock=`oddccfclk_temp_8` | value=`106.0104` | pattern=`global`
- **[SKEW]** clock=`sbclk_right_pm_temp_9` | value=`140.2664` | pattern=`global`
- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1787.1019` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`visaclk` | value=`1066.6469` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk` | value=`3058.7981` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk_sys` | value=`3070.3252` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_div_200` | value=`3058.7981` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk` | value=`3272.1731` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`oddccfclk` | value=`2330.5398` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bscanclk` | value=`2229.3279` | pattern=`over_buffering`
  > high delay + low skew → likely over-buffering
- **[INSERTION_DELAY]** clock=`idv_osc_freqB_clk` | value=`1114.6165` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bclk` | value=`2153.5005` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`idv_osc_freqA_clk` | value=`1141.1667` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`idv_osc_freqC_clk` | value=`1091.7283` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`idv_osc_freqD_clk` | value=`1069.2214` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_200` | value=`3233.8354` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`dfx_secure_clk` | value=`2308.281` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`sbclk_left` | value=`1805.1783` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[CTS_VIOLATION]** clock=`N/A` | value=`290` | pattern=`CTS-997`
  > 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_TD_CELLS]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_td_cells = 1 at compile_final_opto
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`318` | pattern=`health_check`
  > check_pwr_integ = 318 at compile_final_opto
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`120` | pattern=`health_check`
  > check_pdn_pg_cuts = 120 at compile_final_opto
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`109` | pattern=`health_check`
  > check_io_placement = 109 at compile_final_opto
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`164` | pattern=`health_check`
  > check_pdfx_content = 164 at compile_final_opto
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1685` | pattern=`health_check`
  > check_pdn_polygons = 1685 at compile_final_opto
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`77` | pattern=`health_check`
  > check_netspec_lspec = 77 at compile_final_opto
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at compile_final_opto
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`83` | pattern=`health_check`
  > check_port_net_names = 83 at compile_final_opto
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_naming_convention = 1 at compile_final_opto
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`66` | pattern=`health_check`
  > check_placement_legality = 66 at compile_final_opto
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`5344` | pattern=`health_check`
  > check_dangling_ports_pins = 5344 at compile_final_opto
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`279` | pattern=`health_check`
  > check_signal_elevator_xor = 279 at compile_final_opto
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`506` | pattern=`health_check`
  > check_dangling_user_shapes = 506 at compile_final_opto
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`195` | pattern=`health_check`
  > check_netspec_missing_shield = 195 at compile_final_opto
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`14` | pattern=`health_check`
  > check_ports_with_multi_terms = 14 at compile_final_opto
- **[CHECK_TERMINALS_NOT_ON_TRACK]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_terminals_not_on_track = 3 at compile_final_opto
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`26` | pattern=`health_check`
  > check_wire_objects_at_boundary = 26 at compile_final_opto
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at compile_final_opto
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`124` | pattern=`health_check`
  > check_netspec_repeater_distance = 124 at compile_final_opto
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`207` | pattern=`health_check`
  > check_additional_td_route_objects = 207 at compile_final_opto
- **[CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_netspec_dont_touch_constraints = 2 at compile_final_opto
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto
- **[HOLD_VIOLATIONS]** clock=`multiple` | value=`9273` | pattern=`MODERATE_HOLD_ISSUES`
  > Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.
  ```tcl
  set_route_opt_strategy -hold_fixing true
  route_opt -incremental
  report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
  ```

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (474 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right, sbclk_left_temp_2, xtalclk. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 135 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 50,266.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 51 | 6,871 | 9,273 | 78 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth_new/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,273** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 16,691 |
| Estimated runtime | 83 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟡 Setup Violation Analysis


### 🔴 Setup Clustering — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth_new/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,871** across 51 clocks |
| Avg violations/clock | **134.7** |

**Root Cause:** Avg 135 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1265 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 269 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 228 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1941 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 208 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2038 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 225 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1457 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 235 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 249 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2144 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1455 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 418 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 1115 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 1014 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 1141 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 1092 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 1069 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 506 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 467 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6' max skew = 219 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2105 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 527 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1244 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_2`
  - **Symptom:** Clock 'sbclk_left_temp_2': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_4`
  - **Symptom:** Clock 'oddccfclk_temp_4': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_2`
  - **Symptom:** Clock 'oddccfclk_temp_2': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 3019 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 127 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 143 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8' max skew = 106 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9' max skew = 140 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1787 ps (1.787 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1067 ps (1.067 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 3059 ps (3.059 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3070 ps (3.070 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 3059 ps (3.059 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3272 ps (3.272 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2331 ps (2.331 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2229 ps (2.229 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' avg insertion delay = 1115 ps (1.115 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2154 ps (2.154 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' avg insertion delay = 1141 ps (1.141 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' avg insertion delay = 1092 ps (1.092 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' avg insertion delay = 1069 ps (1.069 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3234 ps (3.234 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2308 ps (2.308 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1805 ps (1.805 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_td_cells = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 318 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 120 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 109 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 164 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1685 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 77 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 83 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 66 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 5344 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 279 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 506 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 195 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 14 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_terminals_not_on_track = 3 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 26 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 124 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 207 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_dont_touch_constraints = 2 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_28a_cth_pc/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_28a_cth_pc/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 2 |
| 🟡 Warnings | 23 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 3065 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## 🟡 Warnings (Medium Priority)

- **[CTS_VIOLATION]** clock=`N/A` | value=`73` | pattern=`CTS-997`
  > 73 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`312` | pattern=`health_check`
  > check_pwr_integ = 312 at compile_final_opto
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`106` | pattern=`health_check`
  > check_pdn_pg_cuts = 106 at compile_final_opto
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`138` | pattern=`health_check`
  > check_io_placement = 138 at compile_final_opto
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`164` | pattern=`health_check`
  > check_pdfx_content = 164 at compile_final_opto
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`790` | pattern=`health_check`
  > check_pdn_polygons = 790 at compile_final_opto
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`102` | pattern=`health_check`
  > check_netspec_lspec = 102 at compile_final_opto
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at compile_final_opto
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`74` | pattern=`health_check`
  > check_port_net_names = 74 at compile_final_opto
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_naming_convention = 1 at compile_final_opto
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`55` | pattern=`health_check`
  > check_placement_legality = 55 at compile_final_opto
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`5344` | pattern=`health_check`
  > check_dangling_ports_pins = 5344 at compile_final_opto
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`280` | pattern=`health_check`
  > check_signal_elevator_xor = 280 at compile_final_opto
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`89` | pattern=`health_check`
  > check_dangling_user_shapes = 89 at compile_final_opto
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`237` | pattern=`health_check`
  > check_netspec_missing_shield = 237 at compile_final_opto
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`16` | pattern=`health_check`
  > check_ports_with_multi_terms = 16 at compile_final_opto
- **[CHECK_TERMINALS_NOT_ON_TRACK]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_terminals_not_on_track = 3 at compile_final_opto
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`26` | pattern=`health_check`
  > check_wire_objects_at_boundary = 26 at compile_final_opto
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at compile_final_opto
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`45` | pattern=`health_check`
  > check_netspec_repeater_distance = 45 at compile_final_opto
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`208` | pattern=`health_check`
  > check_additional_td_route_objects = 208 at compile_final_opto
- **[CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_netspec_dont_touch_constraints = 5 at compile_final_opto
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 49,200.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 0 | 0 | 2 | 🟡 B |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 3065 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** 73 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 312 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 106 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 138 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 164 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 790 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 102 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 74 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 1 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 55 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 5344 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_signal_elevator_xor = 280 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 89 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 237 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 16 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_terminals_not_on_track = 3 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 26 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 45 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 208 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_dont_touch_constraints = 5 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_32a_cth/par_base_fuse`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_32a_cth/runs/par_base_fuse/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 12 |
| 🔴 Critical issues | 22 |
| 🟡 Warnings | 20 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 105 |
| Hold violations | 403 |
| Avg violations/clock | 8.8 |
| Setup diagnosis | LOCALIZED_VIOLATIONS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`roclk`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`tapclk`
### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 1740 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## 🟡 Warnings (Medium Priority)

- **[SKEW]** clock=`oddccfclk` | value=`140.6492` | pattern=`global`
- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1130.0592` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[CTS_VIOLATION]** clock=`N/A` | value=`29` | pattern=`CTS-997`
  > 29 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`754` | pattern=`health_check`
  > check_pwr_integ = 754 at compile_final_opto
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_pg_cuts = 8 at compile_final_opto
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`17` | pattern=`health_check`
  > check_io_placement = 17 at compile_final_opto
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`22` | pattern=`health_check`
  > check_pdfx_content = 22 at compile_final_opto
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1004` | pattern=`health_check`
  > check_pdn_polygons = 1004 at compile_final_opto
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_netspec_lspec = 2 at compile_final_opto
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_halo_locations = 8 at compile_final_opto
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`34` | pattern=`health_check`
  > check_placement_legality = 34 at compile_final_opto
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`343` | pattern=`health_check`
  > check_dangling_ports_pins = 343 at compile_final_opto
- **[CHECK_SIGNAL_ELEVATOR_XOR]** clock=`N/A` | value=`461` | pattern=`health_check`
  > check_signal_elevator_xor = 461 at compile_final_opto
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`20` | pattern=`health_check`
  > check_dangling_user_shapes = 20 at compile_final_opto
- **[CHECK_STD_CELL_POWER_HOOKUP]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_std_cell_power_hookup = 2 at compile_final_opto
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`4` | pattern=`health_check`
  > check_netspec_missing_shield = 4 at compile_final_opto
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_ports_with_multi_terms = 5 at compile_final_opto
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_wire_objects_at_boundary = 2 at compile_final_opto
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`11` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 11 at compile_final_opto
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`9` | pattern=`health_check`
  > check_netspec_repeater_distance = 9 at compile_final_opto

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (408 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: oddccf_l2tclk, sbclk_right, ctfclk_200. May indicate post-CTS routing detours affecting both timing types.
- ℹ️  Total CTS buffer/inverter cells in design: 16,259.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 12 | 105 | 403 | 22 | 🔴 D |


## 🟢 Hold Violations

_No significant hold violations detected._


## 🟡 Setup Violation Analysis


### 🟢 Setup Clustering — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_32a_cth/runs/par_base_fuse/1278.6/apr_fc`

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

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 818 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 513 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

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

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 551 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 581 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 583 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 9 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 9 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
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

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_32a_cth/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_32a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | 2 |
| 🟡 Warnings | 17 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,892 |
| Hold violations | 112,722 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | MBFF_CLOCK_PUSH_EXPLOSION |

## 🔴 Critical Issues (High Priority)

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at floorplan — check run log

### [HOLD_EXPLOSION] clock=`ALL (MBFF)`
> 112,722 hold violations indicates clock path was pushed on replicated MBFFs. Pushing clock on MBFF affects all bits → massive skew delta → hold violations at all startpoints simultaneously.

**💰 ECO Cost Estimate:**

| Metric | Value |
|---|---|
| Estimated Hold Buffers | 281,805 |
| Area Um2 | 338,166 |
| Power Mw | 1409.0 |
| Runtime Hours | 1,409 |

**FC Commands:**
```tcl
undo                                              # Revert last clock ECO
set_multibit_options -exclude [get_cells {mbff_instances}]
compile_clock_tree -incremental
```


## 🟡 Warnings (Medium Priority)

- **[CHECK_TD_CELLS]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_td_cells = 1 at floorplan
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`318` | pattern=`health_check`
  > check_pwr_integ = 318 at floorplan
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`112` | pattern=`health_check`
  > check_pdn_pg_cuts = 112 at floorplan
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`109` | pattern=`health_check`
  > check_io_placement = 109 at floorplan
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`164` | pattern=`health_check`
  > check_pdfx_content = 164 at floorplan
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1783` | pattern=`health_check`
  > check_pdn_polygons = 1783 at floorplan
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at floorplan
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`83` | pattern=`health_check`
  > check_port_net_names = 83 at floorplan
- **[CHECK_UNPLACED_CELLS]** clock=`N/A` | value=`285864` | pattern=`health_check`
  > check_unplaced_cells = 285864 at floorplan
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`17` | pattern=`health_check`
  > check_naming_convention = 17 at floorplan
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`4106` | pattern=`health_check`
  > check_dangling_ports_pins = 4106 at floorplan
- **[CHECK_STD_CELL_POWER_HOOKUP]** clock=`N/A` | value=`7508` | pattern=`health_check`
  > check_std_cell_power_hookup = 7508 at floorplan
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`14` | pattern=`health_check`
  > check_ports_with_multi_terms = 14 at floorplan
- **[CHECK_TERMINALS_NOT_ON_TRACK]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_terminals_not_on_track = 3 at floorplan
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_wire_objects_at_boundary = 10 at floorplan
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at floorplan
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at floorplan

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- 🔴 MBFF CLOCK PUSH EXPLOSION detected (112,722 hold violations). Fixing with buffers would cost ~281,805 cells, ~338,166 µm² area, ~1409 hrs. STRONGLY RECOMMENDED: revert clock push + debank MBFFs.
- ℹ️  Total CTS buffer/inverter cells in design: 49,139.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 0 | 6,892 | 112,722 | 2 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🔴 Hold Analysis — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_32a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **MBFF_CLOCK_PUSH_EXPLOSION** |
| Confidence | HIGH |
| Hold violations | **112,722** |

**Root Cause:** 112,722 hold violations indicates clock path was pushed on replicated MBFFs. Pushing clock on MBFF affects all bits → massive skew delta → hold violations at all startpoints simultaneously.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 281,805 |
| Area overhead | 338,166 µm² |
| Power overhead | 1409.0 mW |
| Estimated runtime | 1409 hrs |

**Recommended Fix:** REVERT clock push + DEBANK affected MBFFs

**FC Commands:**
```tcl
undo                                              # Revert last clock ECO
set_multibit_options -exclude [get_cells {mbff_instances}]
compile_clock_tree -incremental
```

**Expected Outcome:** Add ~704 single-bit flops, avoid 281,805 hold buffers

**Net Savings (vs buffer fix):** ~336,406 µm² area saved, ~1409 hours runtime avoided


## 🟡 Setup Violation Analysis


### 🟢 Setup Clustering — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_32a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **NO_CLOCKS** |
| Confidence | LOW |
| Setup violations | **6,892** across 0 clocks |
| Avg violations/clock | **6892.0** |

**Root Cause:** 


## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at floorplan — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_td_cells = 1 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 318 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 112 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 109 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 164 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1783 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 83 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_unplaced_cells = 285864 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 17 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 4106 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_std_cell_power_hookup = 7508 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 14 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_terminals_not_on_track = 3 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 10 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at floorplan
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_35a_cth/par_base_fuse`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth/runs/par_base_fuse/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 12 |
| 🔴 Critical issues | 24 |
| 🟡 Warnings | 20 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 99 |
| Hold violations | 460 |
| Avg violations/clock | 8.2 |
| Setup diagnosis | LOCALIZED_VIOLATIONS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`roclk`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`tapclk`
### [CHECK_OPENS] clock=`N/A`
> check_opens = 66 at finish

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 1723 at finish

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at finish — check run log

### [CHECK_SIGNAL_ELEVATOR_XOR] clock=`N/A`
> TCL_ERROR in check_signal_elevator_xor at finish — check run log


## 🟡 Warnings (Medium Priority)

- **[SKEW]** clock=`oddccfclk` | value=`138.246` | pattern=`global`
- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1095.2065` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[CTS_VIOLATION]** clock=`N/A` | value=`44` | pattern=`CTS-997`
  > 44 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`752` | pattern=`health_check`
  > check_pwr_integ = 752 at finish
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_pg_cuts = 8 at finish
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`17` | pattern=`health_check`
  > check_io_placement = 17 at finish
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1004` | pattern=`health_check`
  > check_pdn_polygons = 1004 at finish
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`4` | pattern=`health_check`
  > check_netspec_lspec = 4 at finish
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_halo_locations = 8 at finish
- **[CHECK_ESD_CONNECTIVITY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_esd_connectivity = 2 at finish
- **[CHECK_PDN_VIAS_ON_GRID]** clock=`N/A` | value=`560` | pattern=`health_check`
  > check_pdn_vias_on_grid = 560 at finish
- **[CHECK_SHIELD_TILO_CELLS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_shield_tilo_cells = 10 at finish
- **[CHECK_TIEOFF_CONNECTION]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_tieoff_connection = 3 at finish
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_placement_legality = 2 at finish
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`23` | pattern=`health_check`
  > check_dangling_user_shapes = 23 at finish
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_netspec_missing_shield = 2 at finish
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`5` | pattern=`health_check`
  > check_ports_with_multi_terms = 5 at finish
- **[CHECK_WIRE_OBJECTS_AT_BOUNDARY]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_wire_objects_at_boundary = 2 at finish
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`11` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 11 at finish
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_netspec_repeater_distance = 3 at finish

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (371 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: oddccf_l2tclk, sbclk_right, ctfclk_200. May indicate post-CTS routing detours affecting both timing types.
- ℹ️  Total CTS buffer/inverter cells in design: 16,210.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 12 | 99 | 460 | 24 | 🔴 D |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 719 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 301 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 533 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk' max skew = 668 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk' max skew = 565 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 336 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 574 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 564 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 9 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 9 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 9 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 8 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_opens = 66 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_shorts = 1723 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at finish — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_signal_elevator_xor at finish — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 138 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1095 ps (1.095 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** 44 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 752 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 8 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 17 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1004 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 4 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 8 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_esd_connectivity = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_vias_on_grid = 560 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_shield_tilo_cells = 10 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_tieoff_connection = 3 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 23 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 5 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_wire_objects_at_boundary = 2 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 11 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 3 at finish
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_35a_cth/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 51 |
| 🔴 Critical issues | 78 |
| 🟡 Warnings | 40 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,026 |
| Hold violations | 9,642 |
| Avg violations/clock | 118.2 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`tapclk`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`sbclk_right_pm_temp_9`
### [SKEW] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left_temp_2`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_temp_2`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_4`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_9`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [CHECK_OPENS] clock=`N/A`
> check_opens = 439040 at route_opt

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at route_opt — check run log

### [SETUP_CLUSTERING] clock=`ALL`
> Avg 118 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Ranked Fixes:**

| # | Hypothesis | Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |


## 🟡 Warnings (Medium Priority)

- **[SKEW]** clock=`sbclk_right_temp_5` | value=`135.6316` | pattern=`global`
- **[SKEW]** clock=`oddccfclk_temp_3` | value=`139.6751` | pattern=`global`
- **[SKEW]** clock=`sbclk_right_temp_2` | value=`104.4655` | pattern=`global`
- **[SKEW]** clock=`sbclk_left_pm_temp_2` | value=`180.3207` | pattern=`global`
- **[SKEW]** clock=`oddccfclk_temp_8` | value=`159.0538` | pattern=`global`
- **[SKEW]** clock=`sbclk_right_pm_temp_4` | value=`103.7025` | pattern=`global`
- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1761.7588` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`visaclk` | value=`1081.8591` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk` | value=`2972.3325` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk_sys` | value=`3194.5547` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_div_200` | value=`2972.3325` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk` | value=`3495.5754` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`oddccfclk` | value=`2268.9033` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bscanclk` | value=`2130.1099` | pattern=`over_buffering`
  > high delay + low skew → likely over-buffering
- **[INSERTION_DELAY]** clock=`bclk` | value=`2096.4653` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_200` | value=`3458.2676` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`dfx_secure_clk` | value=`2217.7241` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`sbclk_left` | value=`1794.3535` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[CTS_VIOLATION]** clock=`N/A` | value=`290` | pattern=`CTS-997`
  > 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`318` | pattern=`health_check`
  > check_pwr_integ = 318 at route_opt
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`120` | pattern=`health_check`
  > check_pdn_pg_cuts = 120 at route_opt
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`109` | pattern=`health_check`
  > check_io_placement = 109 at route_opt
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_pdfx_content = 1 at route_opt
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1685` | pattern=`health_check`
  > check_pdn_polygons = 1685 at route_opt
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`139` | pattern=`health_check`
  > check_netspec_lspec = 139 at route_opt
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at route_opt
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`83` | pattern=`health_check`
  > check_port_net_names = 83 at route_opt
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`23` | pattern=`health_check`
  > check_naming_convention = 23 at route_opt
- **[CHECK_GNACPIN_CONNECTION]** clock=`N/A` | value=`7` | pattern=`health_check`
  > check_gnacpin_connection = 7 at route_opt
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`64` | pattern=`health_check`
  > check_placement_legality = 64 at route_opt
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_dangling_ports_pins = 3 at route_opt
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`948` | pattern=`health_check`
  > check_dangling_user_shapes = 948 at route_opt
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`204` | pattern=`health_check`
  > check_netspec_missing_shield = 204 at route_opt
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`14` | pattern=`health_check`
  > check_ports_with_multi_terms = 14 at route_opt
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at route_opt
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`177` | pattern=`health_check`
  > check_netspec_repeater_distance = 177 at route_opt
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`626` | pattern=`health_check`
  > check_additional_td_route_objects = 626 at route_opt
- **[CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_netspec_dont_touch_constraints = 2 at route_opt
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at route_opt
- **[HOLD_VIOLATIONS]** clock=`multiple` | value=`9642` | pattern=`MODERATE_HOLD_ISSUES`
  > Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.
  ```tcl
  set_route_opt_strategy -hold_fixing true
  route_opt -incremental
  report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
  ```

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (458 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right, sbclk_left_temp_2, xtalclk. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 118 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 50,610.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 51 | 6,026 | 9,642 | 78 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,642** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 17,355 |
| Estimated runtime | 86 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟡 Setup Violation Analysis


### 🔴 Setup Clustering — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,026** across 51 clocks |
| Avg violations/clock | **118.2** |

**Root Cause:** Avg 118 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1234 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 330 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 257 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1810 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 229 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2104 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 221 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1371 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 412 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 606 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2385 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1176 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 406 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 775 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 957 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 799 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 753 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 732 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 495 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 444 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2347 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 230 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9' max skew = 253 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1216 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_2`
  - **Symptom:** Clock 'sbclk_left_temp_2': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_4`
  - **Symptom:** Clock 'oddccfclk_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_2`
  - **Symptom:** Clock 'oddccfclk_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_opens = 439040 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at route_opt — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 136 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3' max skew = 140 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 180 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8' max skew = 159 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1762 ps (1.762 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1082 ps (1.082 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3195 ps (3.195 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3496 ps (3.496 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2269 ps (2.269 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2130 ps (2.130 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2096 ps (2.096 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3458 ps (3.458 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2218 ps (2.218 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1794 ps (1.794 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 318 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 120 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 109 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 1 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1685 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 139 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 83 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 23 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_gnacpin_connection = 7 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 64 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 3 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 948 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 204 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 14 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 177 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 626 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_dont_touch_constraints = 2 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_35a_cth_pc/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth_pc/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 51 |
| 🔴 Critical issues | 78 |
| 🟡 Warnings | 40 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,026 |
| Hold violations | 9,642 |
| Avg violations/clock | 118.2 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`tapclk`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`sbclk_right_pm_temp_9`
### [SKEW] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left_temp_2`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_temp_2`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_4`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_9`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [CHECK_OPENS] clock=`N/A`
> check_opens = 439040 at route_opt

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at route_opt — check run log

### [SETUP_CLUSTERING] clock=`ALL`
> Avg 118 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Ranked Fixes:**

| # | Hypothesis | Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |


## 🟡 Warnings (Medium Priority)

- **[SKEW]** clock=`sbclk_right_temp_5` | value=`135.6316` | pattern=`global`
- **[SKEW]** clock=`oddccfclk_temp_3` | value=`139.6751` | pattern=`global`
- **[SKEW]** clock=`sbclk_right_temp_2` | value=`104.4655` | pattern=`global`
- **[SKEW]** clock=`sbclk_left_pm_temp_2` | value=`180.3207` | pattern=`global`
- **[SKEW]** clock=`oddccfclk_temp_8` | value=`159.0538` | pattern=`global`
- **[SKEW]** clock=`sbclk_right_pm_temp_4` | value=`103.7025` | pattern=`global`
- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1761.7588` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`visaclk` | value=`1081.8591` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk` | value=`2972.3325` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk_sys` | value=`3194.5547` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_div_200` | value=`2972.3325` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk` | value=`3495.5754` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`oddccfclk` | value=`2268.9033` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bscanclk` | value=`2130.1099` | pattern=`over_buffering`
  > high delay + low skew → likely over-buffering
- **[INSERTION_DELAY]** clock=`bclk` | value=`2096.4653` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_200` | value=`3458.2676` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`dfx_secure_clk` | value=`2217.7241` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`sbclk_left` | value=`1794.3535` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[CTS_VIOLATION]** clock=`N/A` | value=`290` | pattern=`CTS-997`
  > 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
- **[CHECK_PWR_INTEG]** clock=`N/A` | value=`318` | pattern=`health_check`
  > check_pwr_integ = 318 at route_opt
- **[CHECK_PDN_PG_CUTS]** clock=`N/A` | value=`120` | pattern=`health_check`
  > check_pdn_pg_cuts = 120 at route_opt
- **[CHECK_IO_PLACEMENT]** clock=`N/A` | value=`109` | pattern=`health_check`
  > check_io_placement = 109 at route_opt
- **[CHECK_PDFX_CONTENT]** clock=`N/A` | value=`1` | pattern=`health_check`
  > check_pdfx_content = 1 at route_opt
- **[CHECK_PDN_POLYGONS]** clock=`N/A` | value=`1685` | pattern=`health_check`
  > check_pdn_polygons = 1685 at route_opt
- **[CHECK_NETSPEC_LSPEC]** clock=`N/A` | value=`139` | pattern=`health_check`
  > check_netspec_lspec = 139 at route_opt
- **[CHECK_HALO_LOCATIONS]** clock=`N/A` | value=`10` | pattern=`health_check`
  > check_halo_locations = 10 at route_opt
- **[CHECK_PORT_NET_NAMES]** clock=`N/A` | value=`83` | pattern=`health_check`
  > check_port_net_names = 83 at route_opt
- **[CHECK_NAMING_CONVENTION]** clock=`N/A` | value=`23` | pattern=`health_check`
  > check_naming_convention = 23 at route_opt
- **[CHECK_GNACPIN_CONNECTION]** clock=`N/A` | value=`7` | pattern=`health_check`
  > check_gnacpin_connection = 7 at route_opt
- **[CHECK_PLACEMENT_LEGALITY]** clock=`N/A` | value=`64` | pattern=`health_check`
  > check_placement_legality = 64 at route_opt
- **[CHECK_DANGLING_PORTS_PINS]** clock=`N/A` | value=`3` | pattern=`health_check`
  > check_dangling_ports_pins = 3 at route_opt
- **[CHECK_DANGLING_USER_SHAPES]** clock=`N/A` | value=`948` | pattern=`health_check`
  > check_dangling_user_shapes = 948 at route_opt
- **[CHECK_NETSPEC_MISSING_SHIELD]** clock=`N/A` | value=`204` | pattern=`health_check`
  > check_netspec_missing_shield = 204 at route_opt
- **[CHECK_PORTS_WITH_MULTI_TERMS]** clock=`N/A` | value=`14` | pattern=`health_check`
  > check_ports_with_multi_terms = 14 at route_opt
- **[CHECK_CLOCK_CELLS_CBC_PLACEMENT]** clock=`N/A` | value=`127` | pattern=`health_check`
  > check_clock_cells_cbc_placement = 127 at route_opt
- **[CHECK_NETSPEC_REPEATER_DISTANCE]** clock=`N/A` | value=`177` | pattern=`health_check`
  > check_netspec_repeater_distance = 177 at route_opt
- **[CHECK_ADDITIONAL_TD_ROUTE_OBJECTS]** clock=`N/A` | value=`626` | pattern=`health_check`
  > check_additional_td_route_objects = 626 at route_opt
- **[CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS]** clock=`N/A` | value=`2` | pattern=`health_check`
  > check_netspec_dont_touch_constraints = 2 at route_opt
- **[CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED]** clock=`N/A` | value=`8` | pattern=`health_check`
  > check_pdn_top_layer_hip_power_pins_exposed = 8 at route_opt
- **[HOLD_VIOLATIONS]** clock=`multiple` | value=`9642` | pattern=`MODERATE_HOLD_ISSUES`
  > Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.
  ```tcl
  set_route_opt_strategy -hold_fixing true
  route_opt -incremental
  report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
  ```

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (458 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right, sbclk_left_temp_2, xtalclk. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 118 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 50,610.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 51 | 6,026 | 9,642 | 78 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth_pc/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,642** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 17,355 |
| Estimated runtime | 86 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟡 Setup Violation Analysis


### 🔴 Setup Clustering — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_35a_cth_pc/runs/par_base_fabric_slice_1/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,026** across 51 clocks |
| Avg violations/clock | **118.2** |

**Root Cause:** Avg 118 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1234 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 330 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 257 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1810 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 229 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2104 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 221 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1371 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 412 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 606 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2385 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1176 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 406 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 775 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 957 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 799 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 753 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 732 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 495 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 444 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2347 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 230 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9' max skew = 253 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1216 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_2`
  - **Symptom:** Clock 'sbclk_left_temp_2': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_4`
  - **Symptom:** Clock 'oddccfclk_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_2`
  - **Symptom:** Clock 'oddccfclk_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_opens = 439040 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `N/A`
  - **Symptom:** TCL_ERROR in check_fcl_bu_pushdown at route_opt — check run log
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 136 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3' max skew = 140 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 180 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8' max skew = 159 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1762 ps (1.762 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1082 ps (1.082 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3195 ps (3.195 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3496 ps (3.496 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2269 ps (2.269 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2130 ps (2.130 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2096 ps (2.096 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3458 ps (3.458 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2218 ps (2.218 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1794 ps (1.794 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.
  - **Likely Cause:** CTS rule violation — pins may have excessive delay due to dont_touch nets or fanout limits.
  - **Suggested Fix:** Review `cts_high_delay_pins_*.rpt`; relax dont_touch if intentional; check CTS exception list.
  - **Confidence:** Medium

- **Clock:** `N/A`
  - **Symptom:** check_pwr_integ = 318 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_pg_cuts = 120 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_io_placement = 109 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdfx_content = 1 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_polygons = 1685 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_lspec = 139 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_halo_locations = 10 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_port_net_names = 83 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_naming_convention = 23 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_gnacpin_connection = 7 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_placement_legality = 64 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_ports_pins = 3 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_dangling_user_shapes = 948 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_missing_shield = 204 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_ports_with_multi_terms = 14 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_clock_cells_cbc_placement = 127 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_repeater_distance = 177 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_additional_td_route_objects = 626 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_netspec_dont_touch_constraints = 2 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

- **Clock:** `N/A`
  - **Symptom:** check_pdn_top_layer_hip_power_pins_exposed = 8 at route_opt
  - **Likely Cause:** Physical design integrity issue (opens/shorts/DRC) likely caused by routing congestion or ECO changes.
  - **Suggested Fix:** Run `check_routes` and `verify_drc`; review congestion hotspots; re-run detailed route if needed.
  - **Confidence:** High

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_39a_cth/par_base_fuse`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_39a_cth/runs/par_base_fuse/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 22 |
| 🔴 Critical issues | 40 |
| 🟡 Warnings | 12 |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,026 |
| Hold violations | 9,642 |
| Avg violations/clock | 273.9 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`tapclk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`roclk`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`sbclk_left`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`tapclk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`oddccfclk`
### [SETUP_CLUSTERING] clock=`ALL`
> Avg 274 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Ranked Fixes:**

| # | Hypothesis | Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |


## 🟡 Warnings (Medium Priority)

- **[SKEW]** clock=`oddccfclk` | value=`138.1697` | pattern=`global`
- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1067.9716` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_div_200` | value=`3049.9922` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bscanclk` | value=`2231.5203` | pattern=`over_buffering`
  > high delay + low skew → likely over-buffering
- **[INSERTION_DELAY]** clock=`idv_osc_freqB_clk` | value=`1119.0605` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bclk` | value=`2146.0027` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`idv_osc_freqA_clk` | value=`1145.3438` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`idv_osc_freqC_clk` | value=`1096.3821` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`idv_osc_freqD_clk` | value=`1073.9708` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`dfx_secure_clk` | value=`2323.5583` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`sbclk_left` | value=`1840.6405` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[HOLD_VIOLATIONS]** clock=`multiple` | value=`9642` | pattern=`MODERATE_HOLD_ISSUES`
  > Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.
  ```tcl
  set_route_opt_strategy -hold_fixing true
  route_opt -incremental
  report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
  ```

## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (619 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right, xtalclk, oddccf_t2lclk. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 274 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 22 | 6,026 | 9,642 | 40 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_39a_cth/runs/par_base_fuse/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **MODERATE_HOLD_ISSUES** |
| Confidence | MEDIUM |
| Hold violations | **9,642** |

**Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 17,355 |
| Estimated runtime | 86 hrs |

**Recommended Fix:** Targeted hold buffer insertion with `route_opt`

**FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟡 Setup Violation Analysis


### 🔴 Setup Clustering — `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_39a_cth/runs/par_base_fuse/1278.6/apr_fc`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **6,026** across 22 clocks |
| Avg violations/clock | **273.9** |

**Root Cause:** Avg 274 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Diagnostic Steps:**

1. Check max skew per clock (if >150 ps → relax skew target)
2. Check avg insertion delay (if >1.5 ns → over-buffering or congestion)
3. Check violation distribution per module (if clustered → floorplan issue)

**Ranked Fix Options:**

| # | Hypothesis | ECO Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |

**FC Commands (ranked):**

*Option 1 — Skew budget too tight:*
```tcl
set_clock_tree_options -target_skew 0.18; compile_clock_tree -incremental
```

*Option 2 — Over-buffering inflating latency:*
```tcl
set_clock_tree_options -buffer_relocation true; compile_clock_tree -incremental
```

*Option 3 — Floorplan congestion detour:*
```tcl
report_congestion; check_placement -verbose
```


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 692 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk' max skew = 681 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 565 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 545 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1447 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk' max skew = 577 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 336 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 1119 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 1004 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 1145 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 1096 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 1074 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 503 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 583 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 302 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 411 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1245 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 273 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 273 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

## 📋 Recommended Actions — Medium Priority

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 138 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1068 ps (1.068 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 3050 ps (3.050 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2232 ps (2.232 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' avg insertion delay = 1119 ps (1.119 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2146 ps (2.146 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' avg insertion delay = 1145 ps (1.145 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' avg insertion delay = 1096 ps (1.096 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' avg insertion delay = 1074 ps (1.074 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2324 ps (2.324 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1841 ps (1.841 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

---

### `1p0_39a_cth/par_base_fabric_slice_1`

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `/nfs/site/disks/zsc14.xne_rrfd.sd.053/ckumara/cbb/1p0_39a_cth/runs/par_base_fabric_slice_1/1278.6/apr_fc`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 20 |
| 🔴 Critical issues | 16 |
| 🟡 Warnings | 12 |
| 🟢 Healthy clocks | 3 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | 0.0 |
| Setup diagnosis | LOCALIZED_VIOLATIONS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`tapclk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`sbclk_left`
### [SKEW] clock=`oddccfclk`

## 🟡 Warnings (Medium Priority)

- **[INSERTION_DELAY]** clock=`sbclk_right` | value=`1762.0409` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`visaclk` | value=`1082.0498` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk` | value=`2974.0315` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`tapclk_sys` | value=`3205.5925` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_div_200` | value=`2974.0315` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk` | value=`3508.051` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`bscanclk` | value=`2131.3496` | pattern=`over_buffering`
  > high delay + low skew → likely over-buffering
- **[INSERTION_DELAY]** clock=`bclk` | value=`2096.717` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`ctfclk_200` | value=`3470.3044` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`dfx_secure_clk` | value=`2219.4468` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`sbclk_left` | value=`1794.5992` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue
- **[INSERTION_DELAY]** clock=`oddccfclk` | value=`2263.7153` | pattern=`routing_topology`
  > high delay + high skew → routing/topology issue

## 🟢 Healthy Clocks

- `xtalclk` — skew: 72 ps, ins_delay: 925 ps
- `oddccf_t2lclk` — skew: 1 ps, ins_delay: 3 ps
- `oddccf_l2tclk` — skew: 75 ps, ins_delay: 75 ps

## 🔍 Observations

- ⚠️  System-wide average skew (947 ps) exceeds target — potential global CTS topology or constraint issue.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `` | `apr_fc` | 20 | 0 | 0 | 16 | 🔴 D |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1233 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 272 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1811 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2114 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1372 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2397 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 781 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 956 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 806 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 760 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 739 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 495 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2359 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 239 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1216 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1176 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1762 ps (1.762 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1082 ps (1.082 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 2974 ps (2.974 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3206 ps (3.206 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 2974 ps (2.974 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3508 ps (3.508 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2131 ps (2.131 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2097 ps (2.097 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3470 ps (3.470 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2219 ps (2.219 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1795 ps (1.795 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2264 ps (2.264 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*
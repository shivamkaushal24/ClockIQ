# ClockIQ — Full CTS Analysis Report

> Enriched with CTS Warning & Error Reference | Warnings fully expanded with FC commands

---

<!-- ===== 1p0_21a_cth/par_base_fuse ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_21a_cth/par_base_fuse`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **2** |
| 🔴 Warnings | **18** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 18 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_LONG_FLAT_NAMES, CHECK_DANGLING_USER_SHAPES, CHECK_IO_PLACEMENT, CHECK_PDFX_CONTENT, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_STD_CELL_POWER_HOOKUP, CHECK_DANGLING_PORTS_PINS, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 30 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CHECK_PWR_INTEG** | `N/A` | `755 ps` | `0 ps` | health_check |
| 2 | **CHECK_PDN_PG_CUTS** | `N/A` | `24 ps` | `0 ps` | health_check |
| 3 | **CHECK_IO_PLACEMENT** | `N/A` | `15 ps` | `0 ps` | health_check |
| 4 | **CHECK_PDFX_CONTENT** | `N/A` | `22 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDN_POLYGONS** | `N/A` | `792 ps` | `0 ps` | health_check |
| 6 | **CHECK_NETSPEC_LSPEC** | `N/A` | `1 ps` | `0 ps` | health_check |
| 7 | **CHECK_HALO_LOCATIONS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 8 | **CHECK_PORT_NET_NAMES** | `N/A` | `1 ps` | `0 ps` | health_check |
| 9 | **CHECK_LONG_FLAT_NAMES** | `N/A` | `102 ps` | `0 ps` | health_check |
| 10 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `34 ps` | `0 ps` | health_check |
| 11 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `343 ps` | `0 ps` | health_check |
| 12 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `467 ps` | `0 ps` | health_check |
| 13 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `23 ps` | `0 ps` | health_check |
| 14 | **CHECK_STD_CELL_POWER_HOOKUP** | `N/A` | `2 ps` | `0 ps` | health_check |
| 15 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 16 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 17 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `9 ps` | `0 ps` | health_check |
| 18 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `9 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `755.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 755 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `24.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 24 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `15.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 15 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_PDFX_CONTENT] `N/A`

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

#### ⚠️ Warning 5 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `792.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 792 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_HALO_LOCATIONS] `N/A`

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

#### ⚠️ Warning 8 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_LONG_FLAT_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_LONG_FLAT_NAMES` |
| Clock | `N/A` |
| Measured value | `102.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_long_flat_names = 102 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_PLACEMENT_LEGALITY] `N/A`

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

#### ⚠️ Warning 11 — [CHECK_DANGLING_PORTS_PINS] `N/A`

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

#### ⚠️ Warning 12 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `467.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 467 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `23.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 23 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_STD_CELL_POWER_HOOKUP] `N/A`

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

#### ⚠️ Warning 15 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

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

#### ⚠️ Warning 16 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

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

#### ⚠️ Warning 17 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `9.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 9 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

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

- ℹ️  Total CTS buffer/inverter cells in design: 16,238.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_21a_cth` | `par_base_fuse` | 0 | 0 | 0 | 2 | 🟡 B |


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

<!-- ===== 1p0_21a_cth/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_21a_cth/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **2** |
| 🔴 Warnings | **21** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 21 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_TERMINALS_NOT_ON_TRACK, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS, CHECK_NAMING_CONVENTION, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 4548 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CHECK_PWR_INTEG** | `N/A` | `322 ps` | `0 ps` | health_check |
| 2 | **CHECK_PDN_PG_CUTS** | `N/A` | `106 ps` | `0 ps` | health_check |
| 3 | **CHECK_IO_PLACEMENT** | `N/A` | `138 ps` | `0 ps` | health_check |
| 4 | **CHECK_PDFX_CONTENT** | `N/A` | `164 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDN_POLYGONS** | `N/A` | `790 ps` | `0 ps` | health_check |
| 6 | **CHECK_NETSPEC_LSPEC** | `N/A` | `35 ps` | `0 ps` | health_check |
| 7 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 8 | **CHECK_PORT_NET_NAMES** | `N/A` | `74 ps` | `0 ps` | health_check |
| 9 | **CHECK_NAMING_CONVENTION** | `N/A` | `1 ps` | `0 ps` | health_check |
| 10 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `57 ps` | `0 ps` | health_check |
| 11 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `5344 ps` | `0 ps` | health_check |
| 12 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `280 ps` | `0 ps` | health_check |
| 13 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `488 ps` | `0 ps` | health_check |
| 14 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `650 ps` | `0 ps` | health_check |
| 15 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `16 ps` | `0 ps` | health_check |
| 16 | **CHECK_TERMINALS_NOT_ON_TRACK** | `N/A` | `3 ps` | `0 ps` | health_check |
| 17 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `18 ps` | `0 ps` | health_check |
| 18 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 19 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `53 ps` | `0 ps` | health_check |
| 20 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `158 ps` | `0 ps` | health_check |
| 21 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `322.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 322 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `106.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 106 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `138.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 138 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `164.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 164 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `790.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 790 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `35.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 35 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `74.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 74 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `57.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 57 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `5344.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 5344 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `280.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 280 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `488.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 488 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `650.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 650 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `16.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 16 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_TERMINALS_NOT_ON_TRACK] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TERMINALS_NOT_ON_TRACK` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_terminals_not_on_track = 3 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `18.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 18 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 19 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `53.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 53 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `158.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 158 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 21 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 52,348.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_21a_cth` | `par_base_fabric_slice_1` | 0 | 0 | 0 | 2 | 🟡 B |


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

<!-- ===== 1p0_28a_cth/par_base_fuse ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_28a_cth/par_base_fuse`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **3** |
| 🔴 Warnings | **22** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 22 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CHECK_STD_CELL_POWER_HOOKUP, CHECK_PDN_HIPS_CONNECTION, CHECK_SHIELD_TILO_CELLS, CTS_VIOLATION, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_PDN_VIAS_ON_GRID, CHECK_TIEOFF_CONNECTION, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [CHECK_OPENS] clock=`N/A`
> check_opens = 49 at finish

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 21 at finish

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at finish — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CTS_VIOLATION** | `N/A` | `43 ps` | `0 ps` | CTS-997 |
| 2 | **CHECK_PWR_INTEG** | `N/A` | `755 ps` | `0 ps` | health_check |
| 3 | **CHECK_PDN_PG_CUTS** | `N/A` | `33 ps` | `0 ps` | health_check |
| 4 | **CHECK_IO_PLACEMENT** | `N/A` | `15 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDN_POLYGONS** | `N/A` | `803 ps` | `0 ps` | health_check |
| 6 | **CHECK_NETSPEC_LSPEC** | `N/A` | `3 ps` | `0 ps` | health_check |
| 7 | **CHECK_HALO_LOCATIONS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 8 | **CHECK_PORT_NET_NAMES** | `N/A` | `1 ps` | `0 ps` | health_check |
| 9 | **CHECK_PDN_VIAS_ON_GRID** | `N/A` | `250 ps` | `0 ps` | health_check |
| 10 | **CHECK_SHIELD_TILO_CELLS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 11 | **CHECK_TIEOFF_CONNECTION** | `N/A` | `3 ps` | `0 ps` | health_check |
| 12 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 13 | **CHECK_PDN_HIPS_CONNECTION** | `N/A` | `1 ps` | `0 ps` | health_check |
| 14 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `205 ps` | `0 ps` | health_check |
| 15 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `26 ps` | `0 ps` | health_check |
| 16 | **CHECK_STD_CELL_POWER_HOOKUP** | `N/A` | `2 ps` | `0 ps` | health_check |
| 17 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `1 ps` | `0 ps` | health_check |
| 18 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 19 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 20 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `11 ps` | `0 ps` | health_check |
| 21 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `4 ps` | `0 ps` | health_check |
| 22 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `50 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `43.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 43 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `755.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 755 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `33.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 33 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `15.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 15 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `803.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 803 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 3 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 8 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 1 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_PDN_VIAS_ON_GRID] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_VIAS_ON_GRID` |
| Clock | `N/A` |
| Measured value | `250.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_vias_on_grid = 250 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_SHIELD_TILO_CELLS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SHIELD_TILO_CELLS` |
| Clock | `N/A` |
| Measured value | `5.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_shield_tilo_cells = 5 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_TIEOFF_CONNECTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TIEOFF_CONNECTION` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_tieoff_connection = 3 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_PDN_HIPS_CONNECTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_HIPS_CONNECTION` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_hips_connection = 1 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `205.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 205 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `26.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 26 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_STD_CELL_POWER_HOOKUP] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_STD_CELL_POWER_HOOKUP` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_std_cell_power_hookup = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 1 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `5.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 5 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 19 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `11.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 11 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 21 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `4.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 4 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 22 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `50.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 50 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 15,998.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_28a_cth` | `par_base_fuse` | 0 | 0 | 0 | 3 | 🟡 B |


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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 43  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_28a_cth/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_28a_cth/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **2** |
| 🔴 Warnings | **23** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 23 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CTS_VIOLATION, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_TERMINALS_NOT_ON_TRACK, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS, CHECK_NAMING_CONVENTION, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 3065 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CTS_VIOLATION** | `N/A` | `73 ps` | `0 ps` | CTS-997 |
| 2 | **CHECK_PWR_INTEG** | `N/A` | `312 ps` | `0 ps` | health_check |
| 3 | **CHECK_PDN_PG_CUTS** | `N/A` | `106 ps` | `0 ps` | health_check |
| 4 | **CHECK_IO_PLACEMENT** | `N/A` | `138 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDFX_CONTENT** | `N/A` | `164 ps` | `0 ps` | health_check |
| 6 | **CHECK_PDN_POLYGONS** | `N/A` | `790 ps` | `0 ps` | health_check |
| 7 | **CHECK_NETSPEC_LSPEC** | `N/A` | `102 ps` | `0 ps` | health_check |
| 8 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 9 | **CHECK_PORT_NET_NAMES** | `N/A` | `74 ps` | `0 ps` | health_check |
| 10 | **CHECK_NAMING_CONVENTION** | `N/A` | `1 ps` | `0 ps` | health_check |
| 11 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `55 ps` | `0 ps` | health_check |
| 12 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `5344 ps` | `0 ps` | health_check |
| 13 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `280 ps` | `0 ps` | health_check |
| 14 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `89 ps` | `0 ps` | health_check |
| 15 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `237 ps` | `0 ps` | health_check |
| 16 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `16 ps` | `0 ps` | health_check |
| 17 | **CHECK_TERMINALS_NOT_ON_TRACK** | `N/A` | `3 ps` | `0 ps` | health_check |
| 18 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `26 ps` | `0 ps` | health_check |
| 19 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 20 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `45 ps` | `0 ps` | health_check |
| 21 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `208 ps` | `0 ps` | health_check |
| 22 | **CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 23 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `73.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 73 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `312.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 312 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `106.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 106 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `138.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 138 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `164.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 164 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `790.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 790 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `102.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 102 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `74.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 74 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `55.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 55 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `5344.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 5344 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `280.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 280 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `89.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 89 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `237.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 237 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `16.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 16 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_TERMINALS_NOT_ON_TRACK] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TERMINALS_NOT_ON_TRACK` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_terminals_not_on_track = 3 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `26.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 26 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 19 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `45.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 45 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 21 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `208.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 208 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 22 — [CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS` |
| Clock | `N/A` |
| Measured value | `5.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_dont_touch_constraints = 5 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 23 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 49,200.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_28a_cth` | `par_base_fabric_slice_1` | 0 | 0 | 0 | 2 | 🟡 B |


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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 73  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_28a_cth_new/par_base_fuse ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_28a_cth_new/par_base_fuse`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **3** |
| 🔴 Warnings | **19** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 19 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CHECK_STD_CELL_POWER_HOOKUP, CHECK_SHIELD_TILO_CELLS, CTS_VIOLATION, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_PDN_VIAS_ON_GRID, CHECK_TIEOFF_CONNECTION, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [CHECK_OPENS] clock=`N/A`
> check_opens = 65 at finish

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 1717 at finish

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at finish — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CTS_VIOLATION** | `N/A` | `45 ps` | `0 ps` | CTS-997 |
| 2 | **CHECK_PWR_INTEG** | `N/A` | `754 ps` | `0 ps` | health_check |
| 3 | **CHECK_PDN_PG_CUTS** | `N/A` | `1 ps` | `0 ps` | health_check |
| 4 | **CHECK_IO_PLACEMENT** | `N/A` | `17 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDN_POLYGONS** | `N/A` | `1004 ps` | `0 ps` | health_check |
| 6 | **CHECK_NETSPEC_LSPEC** | `N/A` | `4 ps` | `0 ps` | health_check |
| 7 | **CHECK_HALO_LOCATIONS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 8 | **CHECK_PDN_VIAS_ON_GRID** | `N/A` | `529 ps` | `0 ps` | health_check |
| 9 | **CHECK_SHIELD_TILO_CELLS** | `N/A` | `11 ps` | `0 ps` | health_check |
| 10 | **CHECK_TIEOFF_CONNECTION** | `N/A` | `3 ps` | `0 ps` | health_check |
| 11 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 12 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `197 ps` | `0 ps` | health_check |
| 13 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `24 ps` | `0 ps` | health_check |
| 14 | **CHECK_STD_CELL_POWER_HOOKUP** | `N/A` | `2 ps` | `0 ps` | health_check |
| 15 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `1 ps` | `0 ps` | health_check |
| 16 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 17 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 18 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `10 ps` | `0 ps` | health_check |
| 19 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `6 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `45.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 45 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `754.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 754 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 1 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `17.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 17 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1004.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1004 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `4.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 4 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 8 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_PDN_VIAS_ON_GRID] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_VIAS_ON_GRID` |
| Clock | `N/A` |
| Measured value | `529.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_vias_on_grid = 529 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_SHIELD_TILO_CELLS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SHIELD_TILO_CELLS` |
| Clock | `N/A` |
| Measured value | `11.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_shield_tilo_cells = 11 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_TIEOFF_CONNECTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TIEOFF_CONNECTION` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_tieoff_connection = 3 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `197.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 197 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `24.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 24 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_STD_CELL_POWER_HOOKUP] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_STD_CELL_POWER_HOOKUP` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_std_cell_power_hookup = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 1 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `5.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 5 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 10 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 19 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `6.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 6 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 16,410.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_28a_cth_new` | `par_base_fuse` | 0 | 0 | 0 | 3 | 🟡 B |


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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 45  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_28a_cth_new/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_28a_cth_new/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 51 |
| 🔴 Critical issues | **78** |
| 🔴 Warnings | **45** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,871 |
| Hold violations | 9,273 |
| Avg violations/clock | 134.7 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

> ### ⚠️ 45 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `oddccfclk`, `oddccfclk_temp_8`, `idv_osc_freqD_clk`, `idv_osc_freqB_clk`, `idv_osc_freqA_clk`, `visaclk`, `bclk`, `sbclk_right`...
> **Metrics flagged:** CHECK_TD_CELLS, HOLD_VIOLATIONS, CTS_VIOLATION, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_TERMINALS_NOT_ON_TRACK, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, INSERTION_DELAY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS, CHECK_NAMING_CONVENTION, SKEW, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`sbclk_left_temp_6`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_4`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_2`
### [VIOLATIONS] clock=`sbclk_left_temp_2`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`tapclk`
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


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `oddccfclk_temp_8` | `106 ps` | `100 ps` | global |
| 2 | **SKEW** | `sbclk_left_pm_temp_2` | `143 ps` | `100 ps` | global |
| 3 | **SKEW** | `sbclk_right_temp_5` | `127 ps` | `100 ps` | global |
| 4 | **SKEW** | `sbclk_right_pm_temp_9` | `140 ps` | `100 ps` | global |
| 5 | **INSERTION_DELAY** | `oddccfclk` | `2331 ps` | `1000 ps` | routing_topology |
| 6 | **INSERTION_DELAY** | `idv_osc_freqD_clk` | `1069 ps` | `1000 ps` | routing_topology |
| 7 | **INSERTION_DELAY** | `idv_osc_freqB_clk` | `1115 ps` | `1000 ps` | routing_topology |
| 8 | **INSERTION_DELAY** | `idv_osc_freqA_clk` | `1141 ps` | `1000 ps` | routing_topology |
| 9 | **INSERTION_DELAY** | `visaclk` | `1067 ps` | `1000 ps` | routing_topology |
| 10 | **INSERTION_DELAY** | `bclk` | `2154 ps` | `1000 ps` | routing_topology |
| 11 | **INSERTION_DELAY** | `sbclk_right` | `1787 ps` | `1000 ps` | routing_topology |
| 12 | **INSERTION_DELAY** | `sbclk_left` | `1805 ps` | `1000 ps` | routing_topology |
| 13 | **INSERTION_DELAY** | `ctfclk_200` | `3234 ps` | `1000 ps` | routing_topology |
| 14 | **INSERTION_DELAY** | `bscanclk` | `2229 ps` | `1000 ps` | over_buffering |
| 15 | **INSERTION_DELAY** | `ctfclk` | `3272 ps` | `1000 ps` | routing_topology |
| 16 | **INSERTION_DELAY** | `tapclk_sys` | `3070 ps` | `1000 ps` | routing_topology |
| 17 | **INSERTION_DELAY** | `idv_osc_freqC_clk` | `1092 ps` | `1000 ps` | routing_topology |
| 18 | **INSERTION_DELAY** | `dfx_secure_clk` | `2308 ps` | `1000 ps` | routing_topology |
| 19 | **INSERTION_DELAY** | `ctfclk_div_200` | `3059 ps` | `1000 ps` | routing_topology |
| 20 | **INSERTION_DELAY** | `tapclk` | `3059 ps` | `1000 ps` | routing_topology |
| 21 | **CTS_VIOLATION** | `N/A` | `290 ps` | `0 ps` | CTS-997 |
| 22 | **CHECK_TD_CELLS** | `N/A` | `1 ps` | `0 ps` | health_check |
| 23 | **CHECK_PWR_INTEG** | `N/A` | `318 ps` | `0 ps` | health_check |
| 24 | **CHECK_PDN_PG_CUTS** | `N/A` | `120 ps` | `0 ps` | health_check |
| 25 | **CHECK_IO_PLACEMENT** | `N/A` | `109 ps` | `0 ps` | health_check |
| 26 | **CHECK_PDFX_CONTENT** | `N/A` | `164 ps` | `0 ps` | health_check |
| 27 | **CHECK_PDN_POLYGONS** | `N/A` | `1685 ps` | `0 ps` | health_check |
| 28 | **CHECK_NETSPEC_LSPEC** | `N/A` | `77 ps` | `0 ps` | health_check |
| 29 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 30 | **CHECK_PORT_NET_NAMES** | `N/A` | `83 ps` | `0 ps` | health_check |
| 31 | **CHECK_NAMING_CONVENTION** | `N/A` | `1 ps` | `0 ps` | health_check |
| 32 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `66 ps` | `0 ps` | health_check |
| 33 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `5344 ps` | `0 ps` | health_check |
| 34 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `279 ps` | `0 ps` | health_check |
| 35 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `506 ps` | `0 ps` | health_check |
| 36 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `195 ps` | `0 ps` | health_check |
| 37 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `14 ps` | `0 ps` | health_check |
| 38 | **CHECK_TERMINALS_NOT_ON_TRACK** | `N/A` | `3 ps` | `0 ps` | health_check |
| 39 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `26 ps` | `0 ps` | health_check |
| 40 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 41 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `124 ps` | `0 ps` | health_check |
| 42 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `207 ps` | `0 ps` | health_check |
| 43 | **CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS** | `N/A` | `2 ps` | `0 ps` | health_check |
| 44 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |
| 45 | **HOLD_VIOLATIONS** | `multiple` | `9273 ps` | `1000 ps` | MODERATE_HOLD_ISSUES |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `oddccfclk_temp_8`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk_temp_8` |
| Measured value | `106.0 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk_temp_8}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 2 — [SKEW] `sbclk_left_pm_temp_2`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_left_pm_temp_2` |
| Measured value | `142.7 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_left_pm_temp_2}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 3 — [SKEW] `sbclk_right_temp_5`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_5` |
| Measured value | `126.6 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_5}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 4 — [SKEW] `sbclk_right_pm_temp_9`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_pm_temp_9` |
| Measured value | `140.3 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_pm_temp_9}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 5 — [INSERTION_DELAY] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `oddccfclk` |
| Measured value | `2330.5 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {oddccfclk}
```

#### ⚠️ Warning 6 — [INSERTION_DELAY] `idv_osc_freqD_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqD_clk` |
| Measured value | `1069.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqD_clk}
```

#### ⚠️ Warning 7 — [INSERTION_DELAY] `idv_osc_freqB_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqB_clk` |
| Measured value | `1114.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqB_clk}
```

#### ⚠️ Warning 8 — [INSERTION_DELAY] `idv_osc_freqA_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqA_clk` |
| Measured value | `1141.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqA_clk}
```

#### ⚠️ Warning 9 — [INSERTION_DELAY] `visaclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `visaclk` |
| Measured value | `1066.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {visaclk}
```

#### ⚠️ Warning 10 — [INSERTION_DELAY] `bclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bclk` |
| Measured value | `2153.5 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bclk}
```

#### ⚠️ Warning 11 — [INSERTION_DELAY] `sbclk_right`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_right` |
| Measured value | `1787.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_right}
```

#### ⚠️ Warning 12 — [INSERTION_DELAY] `sbclk_left`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_left` |
| Measured value | `1805.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_left}
```

#### ⚠️ Warning 13 — [INSERTION_DELAY] `ctfclk_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_200` |
| Measured value | `3233.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_200}
```

#### ⚠️ Warning 14 — [INSERTION_DELAY] `bscanclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bscanclk` |
| Measured value | `2229.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bscanclk}
```

#### ⚠️ Warning 15 — [INSERTION_DELAY] `ctfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk` |
| Measured value | `3272.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk}
```

#### ⚠️ Warning 16 — [INSERTION_DELAY] `tapclk_sys`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk_sys` |
| Measured value | `3070.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk_sys}
```

#### ⚠️ Warning 17 — [INSERTION_DELAY] `idv_osc_freqC_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqC_clk` |
| Measured value | `1091.7 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqC_clk}
```

#### ⚠️ Warning 18 — [INSERTION_DELAY] `dfx_secure_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `dfx_secure_clk` |
| Measured value | `2308.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {dfx_secure_clk}
```

#### ⚠️ Warning 19 — [INSERTION_DELAY] `ctfclk_div_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_div_200` |
| Measured value | `3058.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_div_200}
```

#### ⚠️ Warning 20 — [INSERTION_DELAY] `tapclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk` |
| Measured value | `3058.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk}
```

#### ⚠️ Warning 21 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `290.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 22 — [CHECK_TD_CELLS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TD_CELLS` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_td_cells = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 23 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `318.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 318 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 24 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `120.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 120 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 25 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `109.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 109 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 26 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `164.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 164 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 27 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1685.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1685 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 28 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `77.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 77 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 29 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 30 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `83.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 83 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 31 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 32 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `66.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 66 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 33 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `5344.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 5344 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 34 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `279.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 279 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 35 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `506.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 506 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 36 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `195.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 195 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 37 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `14.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 14 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 38 — [CHECK_TERMINALS_NOT_ON_TRACK] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TERMINALS_NOT_ON_TRACK` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_terminals_not_on_track = 3 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 39 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `26.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 26 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 40 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 41 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `124.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 124 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 42 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `207.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 207 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 43 — [CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_dont_touch_constraints = 2 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 44 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 45 — [HOLD_VIOLATIONS] `multiple`

| Field | Value |
|-------|-------|
| Metric | `HOLD_VIOLATIONS` |
| Clock | `multiple` |
| Measured value | `9273.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `MODERATE_HOLD_ISSUES` |

> 💡 **Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

**🔧 Suggested FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (474 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right_pm_temp_4, oddccfclk, sbclk_left_temp_5. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 135 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 50,266.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_28a_cth_new` | `par_base_fabric_slice_1` | 51 | 6,871 | 9,273 | 78 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `1p0_28a_cth_new/par_base_fabric_slice_1`

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


### 🔴 Setup Clustering — `1p0_28a_cth_new/par_base_fabric_slice_1`

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

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1455 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 1069 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 1115 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 1141 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 228 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 1014 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1265 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1244 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 249 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2105 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 235 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2144 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 506 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2038 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 269 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 418 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6' max skew = 219 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 1092 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 527 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1457 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 225 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 467 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 208 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1941 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_4`
  - **Symptom:** Clock 'oddccfclk_temp_4': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 135 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_2`
  - **Symptom:** Clock 'sbclk_left_temp_2': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 134 setup + 182 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 134 setup + 181 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8' max skew = 106 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 143 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 127 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9' max skew = 140 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2331 ps (2.331 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' avg insertion delay = 1069 ps (1.069 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' avg insertion delay = 1115 ps (1.115 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' avg insertion delay = 1141 ps (1.141 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1067 ps (1.067 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2154 ps (2.154 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1787 ps (1.787 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1805 ps (1.805 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3234 ps (3.234 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2229 ps (2.229 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3272 ps (3.272 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3070 ps (3.070 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' avg insertion delay = 1092 ps (1.092 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2308 ps (2.308 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 3059 ps (3.059 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 3059 ps (3.059 ns). high delay + high skew → routing/topology issue
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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 290  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_28a_cth_pc/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_28a_cth_pc/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **2** |
| 🔴 Warnings | **23** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 23 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CTS_VIOLATION, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_TERMINALS_NOT_ON_TRACK, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS, CHECK_NAMING_CONVENTION, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 3065 at compile_final_opto

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at compile_final_opto — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CTS_VIOLATION** | `N/A` | `73 ps` | `0 ps` | CTS-997 |
| 2 | **CHECK_PWR_INTEG** | `N/A` | `312 ps` | `0 ps` | health_check |
| 3 | **CHECK_PDN_PG_CUTS** | `N/A` | `106 ps` | `0 ps` | health_check |
| 4 | **CHECK_IO_PLACEMENT** | `N/A` | `138 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDFX_CONTENT** | `N/A` | `164 ps` | `0 ps` | health_check |
| 6 | **CHECK_PDN_POLYGONS** | `N/A` | `790 ps` | `0 ps` | health_check |
| 7 | **CHECK_NETSPEC_LSPEC** | `N/A` | `102 ps` | `0 ps` | health_check |
| 8 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 9 | **CHECK_PORT_NET_NAMES** | `N/A` | `74 ps` | `0 ps` | health_check |
| 10 | **CHECK_NAMING_CONVENTION** | `N/A` | `1 ps` | `0 ps` | health_check |
| 11 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `55 ps` | `0 ps` | health_check |
| 12 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `5344 ps` | `0 ps` | health_check |
| 13 | **CHECK_SIGNAL_ELEVATOR_XOR** | `N/A` | `280 ps` | `0 ps` | health_check |
| 14 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `89 ps` | `0 ps` | health_check |
| 15 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `237 ps` | `0 ps` | health_check |
| 16 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `16 ps` | `0 ps` | health_check |
| 17 | **CHECK_TERMINALS_NOT_ON_TRACK** | `N/A` | `3 ps` | `0 ps` | health_check |
| 18 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `26 ps` | `0 ps` | health_check |
| 19 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 20 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `45 ps` | `0 ps` | health_check |
| 21 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `208 ps` | `0 ps` | health_check |
| 22 | **CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 23 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `73.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 73 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `312.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 312 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `106.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 106 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `138.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 138 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `164.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 164 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `790.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 790 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `102.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 102 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `74.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 74 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 1 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `55.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 55 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `5344.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 5344 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_SIGNAL_ELEVATOR_XOR] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SIGNAL_ELEVATOR_XOR` |
| Clock | `N/A` |
| Measured value | `280.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_signal_elevator_xor = 280 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `89.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 89 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `237.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 237 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `16.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 16 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_TERMINALS_NOT_ON_TRACK] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TERMINALS_NOT_ON_TRACK` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_terminals_not_on_track = 3 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 18 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `26.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 26 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 19 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `45.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 45 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 21 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `208.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 208 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 22 — [CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS` |
| Clock | `N/A` |
| Measured value | `5.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_dont_touch_constraints = 5 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 23 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at compile_final_opto

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ℹ️  Total CTS buffer/inverter cells in design: 49,200.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_28a_cth_pc` | `par_base_fabric_slice_1` | 0 | 0 | 0 | 2 | 🟡 B |


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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 73  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_32a_cth/par_base_fuse ===== -->

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
> **Affected clocks:** `sbclk_right`, `N/A`, `oddccfclk`
> **Metrics flagged:** CHECK_STD_CELL_POWER_HOOKUP, CTS_VIOLATION, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_SIGNAL_ELEVATOR_XOR, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, INSERTION_DELAY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, SKEW, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`roclk`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`tapclk`
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
- 🔍 Mixed hold+setup violations on: tapclk_sys, roclk, fuse_roclk. May indicate post-CTS routing detours affecting both timing types.
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

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 581 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk' max skew = 566 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 513 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk' max skew = 637 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 818 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 551 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 583 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 9 setup + 34 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 9 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 9 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 8 setup + 33 hold violations (CLUSTERED). Type: mixed.
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

<!-- ===== 1p0_32a_cth/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_32a_cth/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 0 |
| 🔴 Critical issues | **2** |
| 🔴 Warnings | **17** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,892 |
| Hold violations | 112,722 |
| Avg violations/clock | — |
| Setup diagnosis | NO_CLOCKS |
| Hold diagnosis | MBFF_CLOCK_PUSH_EXPLOSION |

> ### ⚠️ 17 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `N/A`
> **Metrics flagged:** CHECK_TD_CELLS, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_IO_PLACEMENT, CHECK_PDFX_CONTENT, CHECK_STD_CELL_POWER_HOOKUP, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_NAMING_CONVENTION, CHECK_DANGLING_PORTS_PINS, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_UNPLACED_CELLS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_TERMINALS_NOT_ON_TRACK, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

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


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **CHECK_TD_CELLS** | `N/A` | `1 ps` | `0 ps` | health_check |
| 2 | **CHECK_PWR_INTEG** | `N/A` | `318 ps` | `0 ps` | health_check |
| 3 | **CHECK_PDN_PG_CUTS** | `N/A` | `112 ps` | `0 ps` | health_check |
| 4 | **CHECK_IO_PLACEMENT** | `N/A` | `109 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDFX_CONTENT** | `N/A` | `164 ps` | `0 ps` | health_check |
| 6 | **CHECK_PDN_POLYGONS** | `N/A` | `1783 ps` | `0 ps` | health_check |
| 7 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 8 | **CHECK_PORT_NET_NAMES** | `N/A` | `83 ps` | `0 ps` | health_check |
| 9 | **CHECK_UNPLACED_CELLS** | `N/A` | `285864 ps` | `0 ps` | health_check |
| 10 | **CHECK_NAMING_CONVENTION** | `N/A` | `17 ps` | `0 ps` | health_check |
| 11 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `4106 ps` | `0 ps` | health_check |
| 12 | **CHECK_STD_CELL_POWER_HOOKUP** | `N/A` | `7508 ps` | `0 ps` | health_check |
| 13 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `14 ps` | `0 ps` | health_check |
| 14 | **CHECK_TERMINALS_NOT_ON_TRACK** | `N/A` | `3 ps` | `0 ps` | health_check |
| 15 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `10 ps` | `0 ps` | health_check |
| 16 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 17 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [CHECK_TD_CELLS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TD_CELLS` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_td_cells = 1 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 2 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `318.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 318 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 3 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `112.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 112 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `109.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 109 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 5 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `164.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 164 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 6 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1783.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1783 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `83.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 83 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_UNPLACED_CELLS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_UNPLACED_CELLS` |
| Clock | `N/A` |
| Measured value | `285864.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_unplaced_cells = 285864 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `17.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 17 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `4106.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 4106 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_STD_CELL_POWER_HOOKUP] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_STD_CELL_POWER_HOOKUP` |
| Clock | `N/A` |
| Measured value | `7508.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_std_cell_power_hookup = 7508 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `14.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 14 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_TERMINALS_NOT_ON_TRACK] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TERMINALS_NOT_ON_TRACK` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_terminals_not_on_track = 3 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_WIRE_OBJECTS_AT_BOUNDARY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_WIRE_OBJECTS_AT_BOUNDARY` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_wire_objects_at_boundary = 10 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 17 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at floorplan

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- 🔴 MBFF CLOCK PUSH EXPLOSION detected (112,722 hold violations). Fixing with buffers would cost ~281,805 cells, ~338,166 µm² area, ~1409 hrs. STRONGLY RECOMMENDED: revert clock push + debank MBFFs.
- ℹ️  Total CTS buffer/inverter cells in design: 49,139.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_32a_cth` | `par_base_fabric_slice_1` | 0 | 6,892 | 112,722 | 2 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🔴 Hold Analysis — `1p0_32a_cth/par_base_fabric_slice_1`

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


### 🟢 Setup Clustering — `1p0_32a_cth/par_base_fabric_slice_1`

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

<!-- ===== 1p0_35a_cth/par_base_fuse ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_35a_cth/par_base_fuse`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 12 |
| 🔴 Critical issues | **24** |
| 🔴 Warnings | **20** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 99 |
| Hold violations | 460 |
| Avg violations/clock | 8.2 |
| Setup diagnosis | LOCALIZED_VIOLATIONS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 20 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `sbclk_right`, `N/A`, `oddccfclk`
> **Metrics flagged:** CHECK_ESD_CONNECTIVITY, CHECK_SHIELD_TILO_CELLS, CTS_VIOLATION, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_PDN_VIAS_ON_GRID, CHECK_TIEOFF_CONNECTION, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_WIRE_OBJECTS_AT_BOUNDARY, CHECK_PLACEMENT_LEGALITY, INSERTION_DELAY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, SKEW
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`roclk`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`tapclk`
### [CHECK_OPENS] clock=`N/A`
> check_opens = 66 at finish

### [CHECK_SHORTS] clock=`N/A`
> check_shorts = 1723 at finish

### [CHECK_FCL_BU_PUSHDOWN] clock=`N/A`
> TCL_ERROR in check_fcl_bu_pushdown at finish — check run log

### [CHECK_SIGNAL_ELEVATOR_XOR] clock=`N/A`
> TCL_ERROR in check_signal_elevator_xor at finish — check run log


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `oddccfclk` | `138 ps` | `100 ps` | global |
| 2 | **INSERTION_DELAY** | `sbclk_right` | `1095 ps` | `1000 ps` | routing_topology |
| 3 | **CTS_VIOLATION** | `N/A` | `44 ps` | `0 ps` | CTS-997 |
| 4 | **CHECK_PWR_INTEG** | `N/A` | `752 ps` | `0 ps` | health_check |
| 5 | **CHECK_PDN_PG_CUTS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 6 | **CHECK_IO_PLACEMENT** | `N/A` | `17 ps` | `0 ps` | health_check |
| 7 | **CHECK_PDN_POLYGONS** | `N/A` | `1004 ps` | `0 ps` | health_check |
| 8 | **CHECK_NETSPEC_LSPEC** | `N/A` | `4 ps` | `0 ps` | health_check |
| 9 | **CHECK_HALO_LOCATIONS** | `N/A` | `8 ps` | `0 ps` | health_check |
| 10 | **CHECK_ESD_CONNECTIVITY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 11 | **CHECK_PDN_VIAS_ON_GRID** | `N/A` | `560 ps` | `0 ps` | health_check |
| 12 | **CHECK_SHIELD_TILO_CELLS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 13 | **CHECK_TIEOFF_CONNECTION** | `N/A` | `3 ps` | `0 ps` | health_check |
| 14 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 15 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `23 ps` | `0 ps` | health_check |
| 16 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `2 ps` | `0 ps` | health_check |
| 17 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `5 ps` | `0 ps` | health_check |
| 18 | **CHECK_WIRE_OBJECTS_AT_BOUNDARY** | `N/A` | `2 ps` | `0 ps` | health_check |
| 19 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `11 ps` | `0 ps` | health_check |
| 20 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `3 ps` | `0 ps` | health_check |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk` |
| Measured value | `138.2 ps` |
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
| Measured value | `1095.2 ps` |
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
| Measured value | `44.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 44 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 4 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `752.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 752 at finish

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

> 💡 **Root Cause:** check_pdn_pg_cuts = 8 at finish

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

> 💡 **Root Cause:** check_io_placement = 17 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 7 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1004.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1004 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 8 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `4.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 4 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 9 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 8 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 10 — [CHECK_ESD_CONNECTIVITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ESD_CONNECTIVITY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_esd_connectivity = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 11 — [CHECK_PDN_VIAS_ON_GRID] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_VIAS_ON_GRID` |
| Clock | `N/A` |
| Measured value | `560.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_vias_on_grid = 560 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 12 — [CHECK_SHIELD_TILO_CELLS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_SHIELD_TILO_CELLS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_shield_tilo_cells = 10 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 13 — [CHECK_TIEOFF_CONNECTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_TIEOFF_CONNECTION` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_tieoff_connection = 3 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 14 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 2 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 15 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `23.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 23 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 16 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 2 at finish

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

> 💡 **Root Cause:** check_ports_with_multi_terms = 5 at finish

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

> 💡 **Root Cause:** check_wire_objects_at_boundary = 2 at finish

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

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 11 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 3 at finish

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (371 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: tapclk_sys, roclk, fuse_roclk. May indicate post-CTS routing detours affecting both timing types.
- ℹ️  Total CTS buffer/inverter cells in design: 16,210.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_35a_cth` | `par_base_fuse` | 12 | 99 | 460 | 24 | 🔴 D |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 533 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 574 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk' max skew = 565 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 301 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk' max skew = 668 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 719 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 336 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 564 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 9 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 9 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 9 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 8 setup + 39 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 8 setup + 38 hold violations (CLUSTERED). Type: mixed.
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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 44  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_35a_cth/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_35a_cth/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 51 |
| 🔴 Critical issues | **78** |
| 🔴 Warnings | **40** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,026 |
| Hold violations | 9,642 |
| Avg violations/clock | 118.2 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

> ### ⚠️ 40 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `sbclk_right_pm_temp_4`, `oddccfclk`, `oddccfclk_temp_8`, `visaclk`, `bclk`, `oddccfclk_temp_3`, `sbclk_right`, `sbclk_left`...
> **Metrics flagged:** HOLD_VIOLATIONS, CTS_VIOLATION, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_GNACPIN_CONNECTION, CHECK_PLACEMENT_LEGALITY, INSERTION_DELAY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS, CHECK_NAMING_CONVENTION, SKEW, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`sbclk_right_pm_temp_9`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_4`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_2`
### [VIOLATIONS] clock=`sbclk_left_temp_2`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`tapclk`
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


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `sbclk_right_pm_temp_4` | `104 ps` | `100 ps` | global |
| 2 | **SKEW** | `oddccfclk_temp_8` | `159 ps` | `100 ps` | global |
| 3 | **SKEW** | `oddccfclk_temp_3` | `140 ps` | `100 ps` | global |
| 4 | **SKEW** | `sbclk_left_pm_temp_2` | `180 ps` | `100 ps` | global |
| 5 | **SKEW** | `sbclk_right_temp_5` | `136 ps` | `100 ps` | global |
| 6 | **SKEW** | `sbclk_right_temp_2` | `104 ps` | `100 ps` | global |
| 7 | **INSERTION_DELAY** | `oddccfclk` | `2269 ps` | `1000 ps` | routing_topology |
| 8 | **INSERTION_DELAY** | `visaclk` | `1082 ps` | `1000 ps` | routing_topology |
| 9 | **INSERTION_DELAY** | `bclk` | `2096 ps` | `1000 ps` | routing_topology |
| 10 | **INSERTION_DELAY** | `sbclk_right` | `1762 ps` | `1000 ps` | routing_topology |
| 11 | **INSERTION_DELAY** | `sbclk_left` | `1794 ps` | `1000 ps` | routing_topology |
| 12 | **INSERTION_DELAY** | `ctfclk_200` | `3458 ps` | `1000 ps` | routing_topology |
| 13 | **INSERTION_DELAY** | `bscanclk` | `2130 ps` | `1000 ps` | over_buffering |
| 14 | **INSERTION_DELAY** | `ctfclk` | `3496 ps` | `1000 ps` | routing_topology |
| 15 | **INSERTION_DELAY** | `tapclk_sys` | `3195 ps` | `1000 ps` | routing_topology |
| 16 | **INSERTION_DELAY** | `dfx_secure_clk` | `2218 ps` | `1000 ps` | routing_topology |
| 17 | **INSERTION_DELAY** | `ctfclk_div_200` | `2972 ps` | `1000 ps` | routing_topology |
| 18 | **INSERTION_DELAY** | `tapclk` | `2972 ps` | `1000 ps` | routing_topology |
| 19 | **CTS_VIOLATION** | `N/A` | `290 ps` | `0 ps` | CTS-997 |
| 20 | **CHECK_PWR_INTEG** | `N/A` | `318 ps` | `0 ps` | health_check |
| 21 | **CHECK_PDN_PG_CUTS** | `N/A` | `120 ps` | `0 ps` | health_check |
| 22 | **CHECK_IO_PLACEMENT** | `N/A` | `109 ps` | `0 ps` | health_check |
| 23 | **CHECK_PDFX_CONTENT** | `N/A` | `1 ps` | `0 ps` | health_check |
| 24 | **CHECK_PDN_POLYGONS** | `N/A` | `1685 ps` | `0 ps` | health_check |
| 25 | **CHECK_NETSPEC_LSPEC** | `N/A` | `139 ps` | `0 ps` | health_check |
| 26 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 27 | **CHECK_PORT_NET_NAMES** | `N/A` | `83 ps` | `0 ps` | health_check |
| 28 | **CHECK_NAMING_CONVENTION** | `N/A` | `23 ps` | `0 ps` | health_check |
| 29 | **CHECK_GNACPIN_CONNECTION** | `N/A` | `7 ps` | `0 ps` | health_check |
| 30 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `64 ps` | `0 ps` | health_check |
| 31 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `3 ps` | `0 ps` | health_check |
| 32 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `948 ps` | `0 ps` | health_check |
| 33 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `204 ps` | `0 ps` | health_check |
| 34 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `14 ps` | `0 ps` | health_check |
| 35 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 36 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `177 ps` | `0 ps` | health_check |
| 37 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `626 ps` | `0 ps` | health_check |
| 38 | **CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS** | `N/A` | `2 ps` | `0 ps` | health_check |
| 39 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |
| 40 | **HOLD_VIOLATIONS** | `multiple` | `9642 ps` | `1000 ps` | MODERATE_HOLD_ISSUES |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `sbclk_right_pm_temp_4`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_pm_temp_4` |
| Measured value | `103.7 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_pm_temp_4}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 2 — [SKEW] `oddccfclk_temp_8`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk_temp_8` |
| Measured value | `159.1 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk_temp_8}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 3 — [SKEW] `oddccfclk_temp_3`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk_temp_3` |
| Measured value | `139.7 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk_temp_3}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 4 — [SKEW] `sbclk_left_pm_temp_2`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_left_pm_temp_2` |
| Measured value | `180.3 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_left_pm_temp_2}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 5 — [SKEW] `sbclk_right_temp_5`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_5` |
| Measured value | `135.6 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_5}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 6 — [SKEW] `sbclk_right_temp_2`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_2` |
| Measured value | `104.5 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_2}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 7 — [INSERTION_DELAY] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `oddccfclk` |
| Measured value | `2268.9 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {oddccfclk}
```

#### ⚠️ Warning 8 — [INSERTION_DELAY] `visaclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `visaclk` |
| Measured value | `1081.9 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {visaclk}
```

#### ⚠️ Warning 9 — [INSERTION_DELAY] `bclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bclk` |
| Measured value | `2096.5 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bclk}
```

#### ⚠️ Warning 10 — [INSERTION_DELAY] `sbclk_right`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_right` |
| Measured value | `1761.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_right}
```

#### ⚠️ Warning 11 — [INSERTION_DELAY] `sbclk_left`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_left` |
| Measured value | `1794.4 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_left}
```

#### ⚠️ Warning 12 — [INSERTION_DELAY] `ctfclk_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_200` |
| Measured value | `3458.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_200}
```

#### ⚠️ Warning 13 — [INSERTION_DELAY] `bscanclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bscanclk` |
| Measured value | `2130.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bscanclk}
```

#### ⚠️ Warning 14 — [INSERTION_DELAY] `ctfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk` |
| Measured value | `3495.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk}
```

#### ⚠️ Warning 15 — [INSERTION_DELAY] `tapclk_sys`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk_sys` |
| Measured value | `3194.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk_sys}
```

#### ⚠️ Warning 16 — [INSERTION_DELAY] `dfx_secure_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `dfx_secure_clk` |
| Measured value | `2217.7 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {dfx_secure_clk}
```

#### ⚠️ Warning 17 — [INSERTION_DELAY] `ctfclk_div_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_div_200` |
| Measured value | `2972.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_div_200}
```

#### ⚠️ Warning 18 — [INSERTION_DELAY] `tapclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk` |
| Measured value | `2972.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk}
```

#### ⚠️ Warning 19 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `290.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `318.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 318 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 21 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `120.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 120 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 22 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `109.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 109 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 23 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 1 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 24 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1685.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1685 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 25 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `139.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 139 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 26 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 27 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `83.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 83 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 28 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `23.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 23 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 29 — [CHECK_GNACPIN_CONNECTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_GNACPIN_CONNECTION` |
| Clock | `N/A` |
| Measured value | `7.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_gnacpin_connection = 7 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 30 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `64.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 64 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 31 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 3 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 32 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `948.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 948 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 33 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `204.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 204 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 34 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `14.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 14 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 35 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 36 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `177.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 177 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 37 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `626.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 626 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 38 — [CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_dont_touch_constraints = 2 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 39 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 40 — [HOLD_VIOLATIONS] `multiple`

| Field | Value |
|-------|-------|
| Metric | `HOLD_VIOLATIONS` |
| Clock | `multiple` |
| Measured value | `9642.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `MODERATE_HOLD_ISSUES` |

> 💡 **Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

**🔧 Suggested FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (458 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right_pm_temp_4, oddccfclk, sbclk_left_temp_5. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 118 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 50,610.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_35a_cth` | `par_base_fabric_slice_1` | 51 | 6,026 | 9,642 | 78 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `1p0_35a_cth/par_base_fabric_slice_1`

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


### 🔴 Setup Clustering — `1p0_35a_cth/par_base_fabric_slice_1`

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

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1176 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 732 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 775 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 799 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 257 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 957 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1234 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1216 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 606 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2347 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 412 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2385 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 495 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2104 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 330 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 406 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9' max skew = 253 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 753 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 230 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1371 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 221 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 444 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 229 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1810 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_4`
  - **Symptom:** Clock 'oddccfclk_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_2`
  - **Symptom:** Clock 'sbclk_left_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8' max skew = 159 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3' max skew = 140 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 180 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 136 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2269 ps (2.269 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1082 ps (1.082 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2096 ps (2.096 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1762 ps (1.762 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1794 ps (1.794 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3458 ps (3.458 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2130 ps (2.130 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3496 ps (3.496 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3195 ps (3.195 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2218 ps (2.218 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 290  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_35a_cth_pc/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_35a_cth_pc/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 51 |
| 🔴 Critical issues | **78** |
| 🔴 Warnings | **40** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,026 |
| Hold violations | 9,642 |
| Avg violations/clock | 118.2 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

> ### ⚠️ 40 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `sbclk_right_pm_temp_4`, `oddccfclk`, `oddccfclk_temp_8`, `visaclk`, `bclk`, `oddccfclk_temp_3`, `sbclk_right`, `sbclk_left`...
> **Metrics flagged:** HOLD_VIOLATIONS, CTS_VIOLATION, CHECK_PORT_NET_NAMES, CHECK_PDN_PG_CUTS, CHECK_NETSPEC_LSPEC, CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS, CHECK_NETSPEC_REPEATER_DISTANCE, CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED, CHECK_PWR_INTEG, CHECK_PDN_POLYGONS, CHECK_DANGLING_USER_SHAPES, CHECK_DANGLING_PORTS_PINS, CHECK_PORTS_WITH_MULTI_TERMS, CHECK_HALO_LOCATIONS, CHECK_CLOCK_CELLS_CBC_PLACEMENT, CHECK_GNACPIN_CONNECTION, CHECK_PLACEMENT_LEGALITY, INSERTION_DELAY, CHECK_NETSPEC_MISSING_SHIELD, CHECK_IO_PLACEMENT, CHECK_ADDITIONAL_TD_ROUTE_OBJECTS, CHECK_NAMING_CONVENTION, SKEW, CHECK_PDFX_CONTENT
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`sbclk_right_pm_temp_9`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_4`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_2`
### [VIOLATIONS] clock=`sbclk_left_temp_2`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`tapclk`
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


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `sbclk_right_pm_temp_4` | `104 ps` | `100 ps` | global |
| 2 | **SKEW** | `oddccfclk_temp_8` | `159 ps` | `100 ps` | global |
| 3 | **SKEW** | `oddccfclk_temp_3` | `140 ps` | `100 ps` | global |
| 4 | **SKEW** | `sbclk_left_pm_temp_2` | `180 ps` | `100 ps` | global |
| 5 | **SKEW** | `sbclk_right_temp_5` | `136 ps` | `100 ps` | global |
| 6 | **SKEW** | `sbclk_right_temp_2` | `104 ps` | `100 ps` | global |
| 7 | **INSERTION_DELAY** | `oddccfclk` | `2269 ps` | `1000 ps` | routing_topology |
| 8 | **INSERTION_DELAY** | `visaclk` | `1082 ps` | `1000 ps` | routing_topology |
| 9 | **INSERTION_DELAY** | `bclk` | `2096 ps` | `1000 ps` | routing_topology |
| 10 | **INSERTION_DELAY** | `sbclk_right` | `1762 ps` | `1000 ps` | routing_topology |
| 11 | **INSERTION_DELAY** | `sbclk_left` | `1794 ps` | `1000 ps` | routing_topology |
| 12 | **INSERTION_DELAY** | `ctfclk_200` | `3458 ps` | `1000 ps` | routing_topology |
| 13 | **INSERTION_DELAY** | `bscanclk` | `2130 ps` | `1000 ps` | over_buffering |
| 14 | **INSERTION_DELAY** | `ctfclk` | `3496 ps` | `1000 ps` | routing_topology |
| 15 | **INSERTION_DELAY** | `tapclk_sys` | `3195 ps` | `1000 ps` | routing_topology |
| 16 | **INSERTION_DELAY** | `dfx_secure_clk` | `2218 ps` | `1000 ps` | routing_topology |
| 17 | **INSERTION_DELAY** | `ctfclk_div_200` | `2972 ps` | `1000 ps` | routing_topology |
| 18 | **INSERTION_DELAY** | `tapclk` | `2972 ps` | `1000 ps` | routing_topology |
| 19 | **CTS_VIOLATION** | `N/A` | `290 ps` | `0 ps` | CTS-997 |
| 20 | **CHECK_PWR_INTEG** | `N/A` | `318 ps` | `0 ps` | health_check |
| 21 | **CHECK_PDN_PG_CUTS** | `N/A` | `120 ps` | `0 ps` | health_check |
| 22 | **CHECK_IO_PLACEMENT** | `N/A` | `109 ps` | `0 ps` | health_check |
| 23 | **CHECK_PDFX_CONTENT** | `N/A` | `1 ps` | `0 ps` | health_check |
| 24 | **CHECK_PDN_POLYGONS** | `N/A` | `1685 ps` | `0 ps` | health_check |
| 25 | **CHECK_NETSPEC_LSPEC** | `N/A` | `139 ps` | `0 ps` | health_check |
| 26 | **CHECK_HALO_LOCATIONS** | `N/A` | `10 ps` | `0 ps` | health_check |
| 27 | **CHECK_PORT_NET_NAMES** | `N/A` | `83 ps` | `0 ps` | health_check |
| 28 | **CHECK_NAMING_CONVENTION** | `N/A` | `23 ps` | `0 ps` | health_check |
| 29 | **CHECK_GNACPIN_CONNECTION** | `N/A` | `7 ps` | `0 ps` | health_check |
| 30 | **CHECK_PLACEMENT_LEGALITY** | `N/A` | `64 ps` | `0 ps` | health_check |
| 31 | **CHECK_DANGLING_PORTS_PINS** | `N/A` | `3 ps` | `0 ps` | health_check |
| 32 | **CHECK_DANGLING_USER_SHAPES** | `N/A` | `948 ps` | `0 ps` | health_check |
| 33 | **CHECK_NETSPEC_MISSING_SHIELD** | `N/A` | `204 ps` | `0 ps` | health_check |
| 34 | **CHECK_PORTS_WITH_MULTI_TERMS** | `N/A` | `14 ps` | `0 ps` | health_check |
| 35 | **CHECK_CLOCK_CELLS_CBC_PLACEMENT** | `N/A` | `127 ps` | `0 ps` | health_check |
| 36 | **CHECK_NETSPEC_REPEATER_DISTANCE** | `N/A` | `177 ps` | `0 ps` | health_check |
| 37 | **CHECK_ADDITIONAL_TD_ROUTE_OBJECTS** | `N/A` | `626 ps` | `0 ps` | health_check |
| 38 | **CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS** | `N/A` | `2 ps` | `0 ps` | health_check |
| 39 | **CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED** | `N/A` | `8 ps` | `0 ps` | health_check |
| 40 | **HOLD_VIOLATIONS** | `multiple` | `9642 ps` | `1000 ps` | MODERATE_HOLD_ISSUES |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `sbclk_right_pm_temp_4`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_pm_temp_4` |
| Measured value | `103.7 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_pm_temp_4}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 2 — [SKEW] `oddccfclk_temp_8`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk_temp_8` |
| Measured value | `159.1 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk_temp_8}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 3 — [SKEW] `oddccfclk_temp_3`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk_temp_3` |
| Measured value | `139.7 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk_temp_3}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 4 — [SKEW] `sbclk_left_pm_temp_2`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_left_pm_temp_2` |
| Measured value | `180.3 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_left_pm_temp_2}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 5 — [SKEW] `sbclk_right_temp_5`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_5` |
| Measured value | `135.6 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_5}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 6 — [SKEW] `sbclk_right_temp_2`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_2` |
| Measured value | `104.5 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_2}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 7 — [INSERTION_DELAY] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `oddccfclk` |
| Measured value | `2268.9 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {oddccfclk}
```

#### ⚠️ Warning 8 — [INSERTION_DELAY] `visaclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `visaclk` |
| Measured value | `1081.9 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {visaclk}
```

#### ⚠️ Warning 9 — [INSERTION_DELAY] `bclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bclk` |
| Measured value | `2096.5 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bclk}
```

#### ⚠️ Warning 10 — [INSERTION_DELAY] `sbclk_right`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_right` |
| Measured value | `1761.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_right}
```

#### ⚠️ Warning 11 — [INSERTION_DELAY] `sbclk_left`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_left` |
| Measured value | `1794.4 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_left}
```

#### ⚠️ Warning 12 — [INSERTION_DELAY] `ctfclk_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_200` |
| Measured value | `3458.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_200}
```

#### ⚠️ Warning 13 — [INSERTION_DELAY] `bscanclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bscanclk` |
| Measured value | `2130.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bscanclk}
```

#### ⚠️ Warning 14 — [INSERTION_DELAY] `ctfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk` |
| Measured value | `3495.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk}
```

#### ⚠️ Warning 15 — [INSERTION_DELAY] `tapclk_sys`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk_sys` |
| Measured value | `3194.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk_sys}
```

#### ⚠️ Warning 16 — [INSERTION_DELAY] `dfx_secure_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `dfx_secure_clk` |
| Measured value | `2217.7 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {dfx_secure_clk}
```

#### ⚠️ Warning 17 — [INSERTION_DELAY] `ctfclk_div_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_div_200` |
| Measured value | `2972.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_div_200}
```

#### ⚠️ Warning 18 — [INSERTION_DELAY] `tapclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk` |
| Measured value | `2972.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk}
```

#### ⚠️ Warning 19 — [CTS_VIOLATION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CTS_VIOLATION` |
| Clock | `N/A` |
| Measured value | `290.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `CTS-997` |

> 💡 **Root Cause:** 290 CTS-997 pins in cts_high_delay_pins_CTS-997.rpt.

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 20 — [CHECK_PWR_INTEG] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PWR_INTEG` |
| Clock | `N/A` |
| Measured value | `318.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pwr_integ = 318 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 21 — [CHECK_PDN_PG_CUTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_PG_CUTS` |
| Clock | `N/A` |
| Measured value | `120.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_pg_cuts = 120 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 22 — [CHECK_IO_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_IO_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `109.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_io_placement = 109 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 23 — [CHECK_PDFX_CONTENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDFX_CONTENT` |
| Clock | `N/A` |
| Measured value | `1.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdfx_content = 1 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 24 — [CHECK_PDN_POLYGONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_POLYGONS` |
| Clock | `N/A` |
| Measured value | `1685.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_polygons = 1685 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 25 — [CHECK_NETSPEC_LSPEC] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_LSPEC` |
| Clock | `N/A` |
| Measured value | `139.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_lspec = 139 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 26 — [CHECK_HALO_LOCATIONS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_HALO_LOCATIONS` |
| Clock | `N/A` |
| Measured value | `10.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_halo_locations = 10 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 27 — [CHECK_PORT_NET_NAMES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORT_NET_NAMES` |
| Clock | `N/A` |
| Measured value | `83.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_port_net_names = 83 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 28 — [CHECK_NAMING_CONVENTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NAMING_CONVENTION` |
| Clock | `N/A` |
| Measured value | `23.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_naming_convention = 23 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 29 — [CHECK_GNACPIN_CONNECTION] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_GNACPIN_CONNECTION` |
| Clock | `N/A` |
| Measured value | `7.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_gnacpin_connection = 7 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 30 — [CHECK_PLACEMENT_LEGALITY] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PLACEMENT_LEGALITY` |
| Clock | `N/A` |
| Measured value | `64.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_placement_legality = 64 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 31 — [CHECK_DANGLING_PORTS_PINS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_PORTS_PINS` |
| Clock | `N/A` |
| Measured value | `3.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_ports_pins = 3 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 32 — [CHECK_DANGLING_USER_SHAPES] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_DANGLING_USER_SHAPES` |
| Clock | `N/A` |
| Measured value | `948.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_dangling_user_shapes = 948 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 33 — [CHECK_NETSPEC_MISSING_SHIELD] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_MISSING_SHIELD` |
| Clock | `N/A` |
| Measured value | `204.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_missing_shield = 204 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 34 — [CHECK_PORTS_WITH_MULTI_TERMS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PORTS_WITH_MULTI_TERMS` |
| Clock | `N/A` |
| Measured value | `14.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_ports_with_multi_terms = 14 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 35 — [CHECK_CLOCK_CELLS_CBC_PLACEMENT] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_CLOCK_CELLS_CBC_PLACEMENT` |
| Clock | `N/A` |
| Measured value | `127.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_clock_cells_cbc_placement = 127 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 36 — [CHECK_NETSPEC_REPEATER_DISTANCE] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_REPEATER_DISTANCE` |
| Clock | `N/A` |
| Measured value | `177.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_repeater_distance = 177 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 37 — [CHECK_ADDITIONAL_TD_ROUTE_OBJECTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_ADDITIONAL_TD_ROUTE_OBJECTS` |
| Clock | `N/A` |
| Measured value | `626.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_additional_td_route_objects = 626 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 38 — [CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_NETSPEC_DONT_TOUCH_CONSTRAINTS` |
| Clock | `N/A` |
| Measured value | `2.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_netspec_dont_touch_constraints = 2 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 39 — [CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED] `N/A`

| Field | Value |
|-------|-------|
| Metric | `CHECK_PDN_TOP_LAYER_HIP_POWER_PINS_EXPOSED` |
| Clock | `N/A` |
| Measured value | `8.0 ps` |
| Threshold | `0.0 ps` |
| Pattern | `health_check` |

> 💡 **Root Cause:** check_pdn_top_layer_hip_power_pins_exposed = 8 at route_opt

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {N/A}
```

#### ⚠️ Warning 40 — [HOLD_VIOLATIONS] `multiple`

| Field | Value |
|-------|-------|
| Metric | `HOLD_VIOLATIONS` |
| Clock | `multiple` |
| Measured value | `9642.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `MODERATE_HOLD_ISSUES` |

> 💡 **Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

**🔧 Suggested FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (458 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right_pm_temp_4, oddccfclk, sbclk_left_temp_5. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 118 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 50,610.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_35a_cth_pc` | `par_base_fabric_slice_1` | 51 | 6,026 | 9,642 | 78 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `1p0_35a_cth_pc/par_base_fabric_slice_1`

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


### 🔴 Setup Clustering — `1p0_35a_cth_pc/par_base_fabric_slice_1`

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

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1176 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 732 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 775 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 799 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 257 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 957 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1234 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1216 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 606 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2347 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 412 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2385 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 495 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2104 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 330 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 406 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9' max skew = 253 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 753 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 230 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1371 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 221 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 444 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 229 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1810 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 119 setup + 190 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 119 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_9`
  - **Symptom:** Clock 'sbclk_right_pm_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_4`
  - **Symptom:** Clock 'oddccfclk_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_2`
  - **Symptom:** Clock 'sbclk_left_temp_2': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 118 setup + 189 hold violations (CLUSTERED). Type: mixed.
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

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8' max skew = 159 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3' max skew = 140 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 180 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 136 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_2`
  - **Symptom:** Clock 'sbclk_right_temp_2' max skew = 104 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2269 ps (2.269 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1082 ps (1.082 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2096 ps (2.096 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1762 ps (1.762 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1794 ps (1.794 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3458 ps (3.458 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2130 ps (2.130 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3496 ps (3.496 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3195 ps (3.195 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2218 ps (2.218 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 2972 ps (2.972 ns). high delay + high skew → routing/topology issue
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

## 📖 CTS Warning & Error Reference

> Each CTS DRC code below is explained with root cause, impact, and Fusion Compiler fix commands.

### 🟡 `CTS-997` — Pre-Existing Cell Resizing Failure
**File:** `cts_high_delay_pins_CTS-997.rpt`  |  **Count:** 290  |  **Priority:** MEDIUM

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

<!-- ===== 1p0_39a_cth/par_base_fuse ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_39a_cth/par_base_fuse`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 22 |
| 🔴 Critical issues | **40** |
| 🔴 Warnings | **12** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 6,026 |
| Hold violations | 9,642 |
| Avg violations/clock | 273.9 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MODERATE_HOLD_ISSUES |

> ### ⚠️ 12 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `ctfclk_div_200`, `oddccfclk`, `bscanclk`, `multiple`, `idv_osc_freqD_clk`, `idv_osc_freqB_clk`, `idv_osc_freqA_clk`, `idv_osc_freqC_clk`...
> **Metrics flagged:** INSERTION_DELAY, HOLD_VIOLATIONS, SKEW
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`fuse_roclk`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`roclk`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`xtalclk`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`oddccfclk`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`sbclk_right`
### [VIOLATIONS] clock=`sbclk_left`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`fuse_roclk`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`roclk`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`tapclk`
### [SETUP_CLUSTERING] clock=`ALL`
> Avg 274 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Ranked Fixes:**

| # | Hypothesis | Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `oddccfclk` | `138 ps` | `100 ps` | global |
| 2 | **INSERTION_DELAY** | `idv_osc_freqD_clk` | `1074 ps` | `1000 ps` | routing_topology |
| 3 | **INSERTION_DELAY** | `idv_osc_freqB_clk` | `1119 ps` | `1000 ps` | routing_topology |
| 4 | **INSERTION_DELAY** | `idv_osc_freqA_clk` | `1145 ps` | `1000 ps` | routing_topology |
| 5 | **INSERTION_DELAY** | `bclk` | `2146 ps` | `1000 ps` | routing_topology |
| 6 | **INSERTION_DELAY** | `sbclk_right` | `1068 ps` | `1000 ps` | routing_topology |
| 7 | **INSERTION_DELAY** | `sbclk_left` | `1841 ps` | `1000 ps` | routing_topology |
| 8 | **INSERTION_DELAY** | `bscanclk` | `2232 ps` | `1000 ps` | over_buffering |
| 9 | **INSERTION_DELAY** | `idv_osc_freqC_clk` | `1096 ps` | `1000 ps` | routing_topology |
| 10 | **INSERTION_DELAY** | `dfx_secure_clk` | `2324 ps` | `1000 ps` | routing_topology |
| 11 | **INSERTION_DELAY** | `ctfclk_div_200` | `3050 ps` | `1000 ps` | routing_topology |
| 12 | **HOLD_VIOLATIONS** | `multiple` | `9642 ps` | `1000 ps` | MODERATE_HOLD_ISSUES |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `oddccfclk` |
| Measured value | `138.2 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {oddccfclk}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 2 — [INSERTION_DELAY] `idv_osc_freqD_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqD_clk` |
| Measured value | `1074.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqD_clk}
```

#### ⚠️ Warning 3 — [INSERTION_DELAY] `idv_osc_freqB_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqB_clk` |
| Measured value | `1119.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqB_clk}
```

#### ⚠️ Warning 4 — [INSERTION_DELAY] `idv_osc_freqA_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqA_clk` |
| Measured value | `1145.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqA_clk}
```

#### ⚠️ Warning 5 — [INSERTION_DELAY] `bclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bclk` |
| Measured value | `2146.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bclk}
```

#### ⚠️ Warning 6 — [INSERTION_DELAY] `sbclk_right`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_right` |
| Measured value | `1068.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_right}
```

#### ⚠️ Warning 7 — [INSERTION_DELAY] `sbclk_left`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_left` |
| Measured value | `1840.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_left}
```

#### ⚠️ Warning 8 — [INSERTION_DELAY] `bscanclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bscanclk` |
| Measured value | `2231.5 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bscanclk}
```

#### ⚠️ Warning 9 — [INSERTION_DELAY] `idv_osc_freqC_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqC_clk` |
| Measured value | `1096.4 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqC_clk}
```

#### ⚠️ Warning 10 — [INSERTION_DELAY] `dfx_secure_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `dfx_secure_clk` |
| Measured value | `2323.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {dfx_secure_clk}
```

#### ⚠️ Warning 11 — [INSERTION_DELAY] `ctfclk_div_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_div_200` |
| Measured value | `3050.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_div_200}
```

#### ⚠️ Warning 12 — [HOLD_VIOLATIONS] `multiple`

| Field | Value |
|-------|-------|
| Metric | `HOLD_VIOLATIONS` |
| Clock | `multiple` |
| Measured value | `9642.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `MODERATE_HOLD_ISSUES` |

> 💡 **Root Cause:** Likely due to localised clock skew or over-aggressive setup fixing pushing data paths too hard, creating hold exposure.

**🔧 Suggested FC Commands:**
```tcl
set_route_opt_strategy -hold_fixing true
route_opt -incremental
report_timing -path_type full_clock_expanded -slack_lesser_than 0 -max_paths 50
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (619 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: oddccfclk, idv_osc_freqD_clk, idv_osc_freqB_clk. May indicate post-CTS routing detours affecting both timing types.
- 🔴 SYSTEMIC CTS ISSUE: avg 274 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_39a_cth` | `par_base_fuse` | 22 | 6,026 | 9,642 | 40 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🟡 Hold Analysis — `1p0_39a_cth/par_base_fuse`

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


### 🔴 Setup Clustering — `1p0_39a_cth/par_base_fuse`

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

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 1074 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 1119 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 1145 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 1004 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 692 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1245 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 302 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk' max skew = 577 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 503 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 545 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk' max skew = 583 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 1096 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk' max skew = 681 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 411 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1447 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 336 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 565 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 274 setup + 439 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `fuse_roclk`
  - **Symptom:** Clock 'fuse_roclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `roclk`
  - **Symptom:** Clock 'roclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 274 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 273 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 273 setup + 438 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

## 📋 Recommended Actions — Medium Priority

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 138 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' avg insertion delay = 1074 ps (1.074 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' avg insertion delay = 1119 ps (1.119 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' avg insertion delay = 1145 ps (1.145 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2146 ps (2.146 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1068 ps (1.068 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1841 ps (1.841 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2232 ps (2.232 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' avg insertion delay = 1096 ps (1.096 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2324 ps (2.324 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 3050 ps (3.050 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

<!-- ===== 1p0_39a_cth/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_39a_cth/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 20 |
| 🔴 Critical issues | **16** |
| 🔴 Warnings | **12** |
| 🟢 Healthy clocks | 3 |
| Setup violations | 0 |
| Hold violations | 0 |
| Avg violations/clock | 0.0 |
| Setup diagnosis | LOCALIZED_VIOLATIONS |
| Hold diagnosis | NORMAL_HOLD_FIXING |

> ### ⚠️ 12 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `ctfclk_div_200`, `tapclk_sys`, `oddccfclk`, `ctfclk_200`, `bscanclk`, `ctfclk`, `visaclk`, `bclk`...
> **Metrics flagged:** INSERTION_DELAY
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`oddccfclk`
### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`visaclk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`sbclk_right`
### [SKEW] clock=`sbclk_left`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`dfx_secure_clk`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`tapclk`

## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **INSERTION_DELAY** | `oddccfclk` | `2264 ps` | `1000 ps` | routing_topology |
| 2 | **INSERTION_DELAY** | `visaclk` | `1082 ps` | `1000 ps` | routing_topology |
| 3 | **INSERTION_DELAY** | `bclk` | `2097 ps` | `1000 ps` | routing_topology |
| 4 | **INSERTION_DELAY** | `sbclk_right` | `1762 ps` | `1000 ps` | routing_topology |
| 5 | **INSERTION_DELAY** | `sbclk_left` | `1795 ps` | `1000 ps` | routing_topology |
| 6 | **INSERTION_DELAY** | `ctfclk_200` | `3470 ps` | `1000 ps` | routing_topology |
| 7 | **INSERTION_DELAY** | `bscanclk` | `2131 ps` | `1000 ps` | over_buffering |
| 8 | **INSERTION_DELAY** | `tapclk_sys` | `3206 ps` | `1000 ps` | routing_topology |
| 9 | **INSERTION_DELAY** | `dfx_secure_clk` | `2219 ps` | `1000 ps` | routing_topology |
| 10 | **INSERTION_DELAY** | `ctfclk_div_200` | `2974 ps` | `1000 ps` | routing_topology |
| 11 | **INSERTION_DELAY** | `ctfclk` | `3508 ps` | `1000 ps` | routing_topology |
| 12 | **INSERTION_DELAY** | `tapclk` | `2974 ps` | `1000 ps` | routing_topology |

---

### Warning Details

#### ⚠️ Warning 1 — [INSERTION_DELAY] `oddccfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `oddccfclk` |
| Measured value | `2263.7 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {oddccfclk}
```

#### ⚠️ Warning 2 — [INSERTION_DELAY] `visaclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `visaclk` |
| Measured value | `1082.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {visaclk}
```

#### ⚠️ Warning 3 — [INSERTION_DELAY] `bclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bclk` |
| Measured value | `2096.7 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bclk}
```

#### ⚠️ Warning 4 — [INSERTION_DELAY] `sbclk_right`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_right` |
| Measured value | `1762.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_right}
```

#### ⚠️ Warning 5 — [INSERTION_DELAY] `sbclk_left`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `sbclk_left` |
| Measured value | `1794.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {sbclk_left}
```

#### ⚠️ Warning 6 — [INSERTION_DELAY] `ctfclk_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_200` |
| Measured value | `3470.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_200}
```

#### ⚠️ Warning 7 — [INSERTION_DELAY] `bscanclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bscanclk` |
| Measured value | `2131.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bscanclk}
```

#### ⚠️ Warning 8 — [INSERTION_DELAY] `tapclk_sys`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk_sys` |
| Measured value | `3205.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk_sys}
```

#### ⚠️ Warning 9 — [INSERTION_DELAY] `dfx_secure_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `dfx_secure_clk` |
| Measured value | `2219.4 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {dfx_secure_clk}
```

#### ⚠️ Warning 10 — [INSERTION_DELAY] `ctfclk_div_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_div_200` |
| Measured value | `2974.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_div_200}
```

#### ⚠️ Warning 11 — [INSERTION_DELAY] `ctfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk` |
| Measured value | `3508.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk}
```

#### ⚠️ Warning 12 — [INSERTION_DELAY] `tapclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk` |
| Measured value | `2974.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk}
```


## 🟢 Healthy Clocks

- `oddccf_l2tclk` — skew: 75 ps, ins_delay: 75 ps
- `oddccf_t2lclk` — skew: 1 ps, ins_delay: 3 ps
- `xtalclk` — skew: 72 ps, ins_delay: 925 ps

## 🔍 Observations

- ⚠️  System-wide average skew (947 ps) exceeds target — potential global CTS topology or constraint issue.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_39a_cth` | `par_base_fabric_slice_1` | 20 | 0 | 0 | 16 | 🔴 D |


## 🟢 Hold Violations

_No significant hold violations detected._


## 📋 Recommended Actions — High Priority (Critical)

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' max skew = 1176 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 739 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 781 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 806 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 272 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 956 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' max skew = 1233 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' max skew = 1216 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2359 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 495 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2114 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 760 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' max skew = 239 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
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

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1811 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

## 📋 Recommended Actions — Medium Priority

- **Clock:** `oddccfclk`
  - **Symptom:** Clock 'oddccfclk' avg insertion delay = 2264 ps (2.264 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1082 ps (1.082 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2097 ps (2.097 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_right`
  - **Symptom:** Clock 'sbclk_right' avg insertion delay = 1762 ps (1.762 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `sbclk_left`
  - **Symptom:** Clock 'sbclk_left' avg insertion delay = 1795 ps (1.795 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3470 ps (3.470 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 2131 ps (2.131 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3206 ps (3.206 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 2219 ps (2.219 ns). high delay + high skew → routing/topology issue
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

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 2974 ps (2.974 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*

<!-- ===== 1p0_Func_ECO_ww06/par_base_fabric_slice_1 ===== -->

# 🕐 ClockIQ — Clock Tree Diagnostics Report

**Source:** `1p0_Func_ECO_ww06/par_base_fabric_slice_1`

## Summary

| Metric | Value |
|---|---|
| Clocks analyzed | 48 |
| 🔴 Critical issues | **69** |
| 🔴 Warnings | **18** |
| 🟢 Healthy clocks | 0 |
| Setup violations | 8,816 |
| Hold violations | 113,957 |
| Avg violations/clock | 183.7 |
| Setup diagnosis | SYSTEMIC_CTS_ISSUE |
| Hold diagnosis | MBFF_CLOCK_PUSH_EXPLOSION |

> ### ⚠️ 18 WARNINGS REQUIRE ATTENTION
> **Affected clocks:** `ctfclk_div_200`, `tapclk_sys`, `sbclk_right_temp_4`, `sbclk_right_temp_3`, `ctfclk_200`, `bscanclk`, `sbclk_left_temp_6`, `idv_osc_freqB_clk`...
> **Metrics flagged:** INSERTION_DELAY, SKEW
> These warnings indicate sub-optimal CTS quality. Left unresolved they can become critical after route_opt or ECO.

## 🔴 Critical Issues (High Priority)

### [SKEW] clock=`idv_osc_freqD_clk`
### [SKEW] clock=`idv_osc_freqB_clk`
### [SKEW] clock=`idv_osc_freqA_clk`
### [SKEW] clock=`bclk`
### [SKEW] clock=`sbclk_right_temp_8`
### [SKEW] clock=`ctfclk_200`
### [SKEW] clock=`sbclk_right_temp_7`
### [SKEW] clock=`ctfclk`
### [SKEW] clock=`sbclk_left_pm_temp_2`
### [SKEW] clock=`apm_osc_clk`
### [SKEW] clock=`tapclk_sys`
### [SKEW] clock=`sbclk_left_pm_temp_7`
### [SKEW] clock=`sbclk_left_temp_7`
### [SKEW] clock=`idv_osc_freqC_clk`
### [SKEW] clock=`ctfclk_div_200`
### [SKEW] clock=`sbclk_right_pm_temp_3`
### [SKEW] clock=`sbclk_right_temp_9`
### [SKEW] clock=`sbclk_right_pm_temp_7`
### [SKEW] clock=`tapclk`
### [VIOLATIONS] clock=`sbclk_right_temp_3`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_4`
### [VIOLATIONS] clock=`sbclk_left_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_8`
### [VIOLATIONS] clock=`idv_osc_freqD_clk`
### [VIOLATIONS] clock=`idv_osc_freqB_clk`
### [VIOLATIONS] clock=`idv_osc_freqA_clk`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_8`
### [VIOLATIONS] clock=`visaclk`
### [VIOLATIONS] clock=`bclk`
### [VIOLATIONS] clock=`oddccfclk_temp_3`
### [VIOLATIONS] clock=`oddccfclk_temp_0`
### [VIOLATIONS] clock=`sbclk_right_temp_8`
### [VIOLATIONS] clock=`sbclk_right_temp_4`
### [VIOLATIONS] clock=`ctfclk_200`
### [VIOLATIONS] clock=`bscanclk`
### [VIOLATIONS] clock=`oddccfclk_temp_5`
### [VIOLATIONS] clock=`sbclk_right_temp_7`
### [VIOLATIONS] clock=`ctfclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_2`
### [VIOLATIONS] clock=`oddccf_l2tclk`
### [VIOLATIONS] clock=`oddccfclk_temp_2`
### [VIOLATIONS] clock=`sbclk_right_temp_5`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_4`
### [VIOLATIONS] clock=`sbclk_left_temp_3`
### [VIOLATIONS] clock=`apm_osc_clk`
### [VIOLATIONS] clock=`tapclk_sys`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_7`
### [VIOLATIONS] clock=`sbclk_left_temp_6`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_5`
### [VIOLATIONS] clock=`oddccf_t2lclk`
### [VIOLATIONS] clock=`idv_osc_freqC_clk`
### [VIOLATIONS] clock=`xtalclk`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_5`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_6`
### [VIOLATIONS] clock=`dfx_secure_clk`
### [VIOLATIONS] clock=`oddccfclk_temp_1`
### [VIOLATIONS] clock=`ctfclk_div_200`
### [VIOLATIONS] clock=`oddccfclk_temp_7`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_3`
### [VIOLATIONS] clock=`sbclk_left_pm_temp_6`
### [VIOLATIONS] clock=`oddccfclk_temp_6`
### [VIOLATIONS] clock=`sbclk_right_temp_9`
### [VIOLATIONS] clock=`sbclk_left_temp_4`
### [VIOLATIONS] clock=`sbclk_right_pm_temp_7`
### [VIOLATIONS] clock=`tapclk`
### [HOLD_EXPLOSION] clock=`ALL (MBFF)`
> 113,957 hold violations indicates clock path was pushed on replicated MBFFs. Pushing clock on MBFF affects all bits → massive skew delta → hold violations at all startpoints simultaneously.

**💰 ECO Cost Estimate:**

| Metric | Value |
|---|---|
| Estimated Hold Buffers | 284,892 |
| Area Um2 | 341,870 |
| Power Mw | 1424.5 |
| Runtime Hours | 1,424 |

**FC Commands:**
```tcl
undo                                              # Revert last clock ECO
set_multibit_options -exclude [get_cells {mbff_instances}]
compile_clock_tree -incremental
```

### [SETUP_CLUSTERING] clock=`ALL`
> Avg 184 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

**Ranked Fixes:**

| # | Hypothesis | Cost | Expected Improvement |
|---|---|---|---|
| 1 | Skew budget too tight | LOW (re-synthesis only) | 30–50% violation reduction |
| 2 | Over-buffering inflating latency | MEDIUM (~200 buffers removed) | 20–40% violation reduction |
| 3 | Floorplan congestion detour | HIGH (floorplan change) | Up to 60% if hotspot resolved |


## ⚠️ Warnings (Action Required)

### Warning Overview

| # | Metric | Clock | Value | Threshold | Pattern |
|---|--------|-------|-------|-----------|---------|
| 1 | **SKEW** | `sbclk_right_temp_3` | `134 ps` | `100 ps` | global |
| 2 | **SKEW** | `sbclk_right_pm_temp_8` | `108 ps` | `100 ps` | global |
| 3 | **SKEW** | `visaclk` | `164 ps` | `100 ps` | global |
| 4 | **SKEW** | `sbclk_right_temp_4` | `119 ps` | `100 ps` | global |
| 5 | **SKEW** | `sbclk_right_temp_5` | `164 ps` | `100 ps` | global |
| 6 | **SKEW** | `sbclk_left_temp_3` | `108 ps` | `100 ps` | global |
| 7 | **SKEW** | `sbclk_left_temp_6` | `174 ps` | `100 ps` | global |
| 8 | **INSERTION_DELAY** | `idv_osc_freqB_clk` | `1015 ps` | `1000 ps` | routing_topology |
| 9 | **INSERTION_DELAY** | `idv_osc_freqA_clk` | `1037 ps` | `1000 ps` | routing_topology |
| 10 | **INSERTION_DELAY** | `visaclk` | `1005 ps` | `1000 ps` | routing_topology |
| 11 | **INSERTION_DELAY** | `bclk` | `2081 ps` | `1000 ps` | routing_topology |
| 12 | **INSERTION_DELAY** | `ctfclk_200` | `3224 ps` | `1000 ps` | routing_topology |
| 13 | **INSERTION_DELAY** | `bscanclk` | `3001 ps` | `1000 ps` | over_buffering |
| 14 | **INSERTION_DELAY** | `ctfclk` | `3265 ps` | `1000 ps` | routing_topology |
| 15 | **INSERTION_DELAY** | `tapclk_sys` | `3373 ps` | `1000 ps` | routing_topology |
| 16 | **INSERTION_DELAY** | `dfx_secure_clk` | `3162 ps` | `1000 ps` | over_buffering |
| 17 | **INSERTION_DELAY** | `ctfclk_div_200` | `3115 ps` | `1000 ps` | routing_topology |
| 18 | **INSERTION_DELAY** | `tapclk` | `3160 ps` | `1000 ps` | routing_topology |

---

### Warning Details

#### ⚠️ Warning 1 — [SKEW] `sbclk_right_temp_3`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_3` |
| Measured value | `134.4 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_3}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 2 — [SKEW] `sbclk_right_pm_temp_8`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_pm_temp_8` |
| Measured value | `108.1 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_pm_temp_8}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 3 — [SKEW] `visaclk`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `visaclk` |
| Measured value | `163.7 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {visaclk}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 4 — [SKEW] `sbclk_right_temp_4`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_4` |
| Measured value | `119.4 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_4}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 5 — [SKEW] `sbclk_right_temp_5`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_right_temp_5` |
| Measured value | `164.2 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_right_temp_5}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 6 — [SKEW] `sbclk_left_temp_3`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_left_temp_3` |
| Measured value | `108.2 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_left_temp_3}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 7 — [SKEW] `sbclk_left_temp_6`

| Field | Value |
|-------|-------|
| Metric | `SKEW` |
| Clock | `sbclk_left_temp_6` |
| Measured value | `173.6 ps` |
| Threshold | `100.0 ps` |
| Pattern | `global` |

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -type local_skew -clocks {sbclk_left_temp_6}
set_clock_tree_options -target_skew 0.18
compile_clock_tree -incremental
```

#### ⚠️ Warning 8 — [INSERTION_DELAY] `idv_osc_freqB_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqB_clk` |
| Measured value | `1014.6 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqB_clk}
```

#### ⚠️ Warning 9 — [INSERTION_DELAY] `idv_osc_freqA_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `idv_osc_freqA_clk` |
| Measured value | `1036.7 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {idv_osc_freqA_clk}
```

#### ⚠️ Warning 10 — [INSERTION_DELAY] `visaclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `visaclk` |
| Measured value | `1004.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {visaclk}
```

#### ⚠️ Warning 11 — [INSERTION_DELAY] `bclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bclk` |
| Measured value | `2081.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bclk}
```

#### ⚠️ Warning 12 — [INSERTION_DELAY] `ctfclk_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_200` |
| Measured value | `3223.8 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_200}
```

#### ⚠️ Warning 13 — [INSERTION_DELAY] `bscanclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `bscanclk` |
| Measured value | `3001.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {bscanclk}
```

#### ⚠️ Warning 14 — [INSERTION_DELAY] `ctfclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk` |
| Measured value | `3265.0 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk}
```

#### ⚠️ Warning 15 — [INSERTION_DELAY] `tapclk_sys`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk_sys` |
| Measured value | `3373.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk_sys}
```

#### ⚠️ Warning 16 — [INSERTION_DELAY] `dfx_secure_clk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `dfx_secure_clk` |
| Measured value | `3162.1 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `over_buffering` |

> 💡 **Root Cause:** high delay + low skew → likely over-buffering

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {dfx_secure_clk}
```

#### ⚠️ Warning 17 — [INSERTION_DELAY] `ctfclk_div_200`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `ctfclk_div_200` |
| Measured value | `3115.3 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {ctfclk_div_200}
```

#### ⚠️ Warning 18 — [INSERTION_DELAY] `tapclk`

| Field | Value |
|-------|-------|
| Metric | `INSERTION_DELAY` |
| Clock | `tapclk` |
| Measured value | `3160.2 ps` |
| Threshold | `1000.0 ps` |
| Pattern | `routing_topology` |

> 💡 **Root Cause:** high delay + high skew → routing/topology issue

**🔧 Suggested FC Commands:**
```tcl
report_clock_qor -clocks {tapclk}
```


## 🟢 Healthy Clocks

_No fully healthy clocks identified._

## 🔍 Observations

- ⚠️  System-wide average skew (440 ps) exceeds target — potential global CTS topology or constraint issue.
- 🔍 Mixed hold+setup violations on: sbclk_right_temp_3, sbclk_right_pm_temp_4, sbclk_left_temp_5. May indicate post-CTS routing detours affecting both timing types.
- 🔴 MBFF CLOCK PUSH EXPLOSION detected (113,957 hold violations). Fixing with buffers would cost ~284,892 cells, ~341,870 µm² area, ~1424 hrs. STRONGLY RECOMMENDED: revert clock push + debank MBFFs.
- 🔴 SYSTEMIC CTS ISSUE: avg 184 violations/clock — global skew, over-buffering, or floorplan problem. Targeted ECO will not be sufficient — CTS re-synthesis required.
- ℹ️  Total CTS buffer/inverter cells in design: 52,987.

## 🎓 Fellow-Level Deep-Dive

## 📋 Master Scorecard

| Flow | Block | Clocks | Setup Viols | Hold Viols | 🔴 Critical | Grade |
|---|---|---|---|---|---|---|
| `1p0_Func_ECO_ww06` | `par_base_fabric_slice_1` | 48 | 8,816 | 113,957 | 69 | 🔴 D |


## 🔴 Hold Violation Deep-Dive


### 🔴 Hold Analysis — `1p0_Func_ECO_ww06/par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **MBFF_CLOCK_PUSH_EXPLOSION** |
| Confidence | HIGH |
| Hold violations | **113,957** |

**Root Cause:** 113,957 hold violations indicates clock path was pushed on replicated MBFFs. Pushing clock on MBFF affects all bits → massive skew delta → hold violations at all startpoints simultaneously.

#### 💰 ECO Cost Estimate (if fixed with buffers)

| Metric | Estimate |
|---|---|
| Hold buffers needed | 284,892 |
| Area overhead | 341,870 µm² |
| Power overhead | 1424.5 mW |
| Estimated runtime | 1424 hrs |

**Recommended Fix:** REVERT clock push + DEBANK affected MBFFs

**FC Commands:**
```tcl
undo                                              # Revert last clock ECO
set_multibit_options -exclude [get_cells {mbff_instances}]
compile_clock_tree -incremental
```

**Expected Outcome:** Add ~712 single-bit flops, avoid 284,892 hold buffers

**Net Savings (vs buffer fix):** ~340,090 µm² area saved, ~1424 hours runtime avoided


## 🟡 Setup Violation Analysis


### 🔴 Setup Clustering — `1p0_Func_ECO_ww06/par_base_fabric_slice_1`

| Field | Detail |
|---|---|
| Diagnosis | **SYSTEMIC_CTS_ISSUE** |
| Confidence | HIGH |
| Setup violations | **8,816** across 48 clocks |
| Avg violations/clock | **183.7** |

**Root Cause:** Avg 184 violations/clock → global problem: likely skew budget, insertion delay, or floorplan.

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

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk' max skew = 981 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' max skew = 1014 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' max skew = 1037 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' max skew = 969 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8' max skew = 634 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' max skew = 2153 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7' max skew = 354 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' max skew = 2195 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2' max skew = 305 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk' max skew = 780 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' max skew = 2145 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7' max skew = 367 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7' max skew = 538 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk' max skew = 996 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' max skew = 1797 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3' max skew = 348 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9' max skew = 445 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7' max skew = 403 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** High

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' max skew = 1695 ps (threshold 100 ps).
  - **Likely Cause:** Localised routing detour or physical placement cluster far from clock trunk causing asymmetric delay on affected sinks.
  - **Suggested Fix:** Identify outlier sinks via `report_clock_tree -skew`; adjust cell placement or insert local balance buffers near affected region.
  - **Confidence:** High

- **Clock:** `sbclk_right_temp_3`
  - **Symptom:** Clock 'sbclk_right_temp_3': 184 setup + 2375 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_4`
  - **Symptom:** Clock 'sbclk_right_pm_temp_4': 184 setup + 2375 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_5`
  - **Symptom:** Clock 'sbclk_left_temp_5': 184 setup + 2375 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_6`
  - **Symptom:** Clock 'sbclk_right_temp_6': 184 setup + 2375 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_8`
  - **Symptom:** Clock 'oddccfclk_temp_8': 184 setup + 2375 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqD_clk`
  - **Symptom:** Clock 'idv_osc_freqD_clk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_8`
  - **Symptom:** Clock 'sbclk_right_pm_temp_8': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_3`
  - **Symptom:** Clock 'oddccfclk_temp_3': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_0`
  - **Symptom:** Clock 'oddccfclk_temp_0': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_8`
  - **Symptom:** Clock 'sbclk_right_temp_8': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_4`
  - **Symptom:** Clock 'sbclk_right_temp_4': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_5`
  - **Symptom:** Clock 'oddccfclk_temp_5': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_7`
  - **Symptom:** Clock 'sbclk_right_temp_7': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_2`
  - **Symptom:** Clock 'sbclk_left_pm_temp_2': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_l2tclk`
  - **Symptom:** Clock 'oddccf_l2tclk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_2`
  - **Symptom:** Clock 'oddccfclk_temp_2': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_4`
  - **Symptom:** Clock 'sbclk_left_pm_temp_4': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_3`
  - **Symptom:** Clock 'sbclk_left_temp_3': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `apm_osc_clk`
  - **Symptom:** Clock 'apm_osc_clk': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_7`
  - **Symptom:** Clock 'sbclk_left_pm_temp_7': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_7`
  - **Symptom:** Clock 'sbclk_left_temp_7': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_5`
  - **Symptom:** Clock 'sbclk_right_pm_temp_5': 184 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccf_t2lclk`
  - **Symptom:** Clock 'oddccf_t2lclk': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqC_clk`
  - **Symptom:** Clock 'idv_osc_freqC_clk': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `xtalclk`
  - **Symptom:** Clock 'xtalclk': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_5`
  - **Symptom:** Clock 'sbclk_left_pm_temp_5': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_6`
  - **Symptom:** Clock 'sbclk_right_pm_temp_6': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_1`
  - **Symptom:** Clock 'oddccfclk_temp_1': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_7`
  - **Symptom:** Clock 'oddccfclk_temp_7': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_3`
  - **Symptom:** Clock 'sbclk_right_pm_temp_3': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_pm_temp_6`
  - **Symptom:** Clock 'sbclk_left_pm_temp_6': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `oddccfclk_temp_6`
  - **Symptom:** Clock 'oddccfclk_temp_6': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_9`
  - **Symptom:** Clock 'sbclk_right_temp_9': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_4`
  - **Symptom:** Clock 'sbclk_left_temp_4': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_7`
  - **Symptom:** Clock 'sbclk_right_pm_temp_7': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk': 183 setup + 2374 hold violations (CLUSTERED). Type: mixed.
  - **Likely Cause:** Mixed hold + setup violations suggest clock skew imbalance or post-CTS routing detours affecting multiple path types.
  - **Suggested Fix:** Rebalance CTS; run incremental `clock_opt`; check post-route timing with updated parasitics.
  - **Confidence:** Medium

## 📋 Recommended Actions — Medium Priority

- **Clock:** `sbclk_right_temp_3`
  - **Symptom:** Clock 'sbclk_right_temp_3' max skew = 134 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_pm_temp_8`
  - **Symptom:** Clock 'sbclk_right_pm_temp_8' max skew = 108 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' max skew = 164 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_4`
  - **Symptom:** Clock 'sbclk_right_temp_4' max skew = 119 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_right_temp_5`
  - **Symptom:** Clock 'sbclk_right_temp_5' max skew = 164 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_3`
  - **Symptom:** Clock 'sbclk_left_temp_3' max skew = 108 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `sbclk_left_temp_6`
  - **Symptom:** Clock 'sbclk_left_temp_6' max skew = 174 ps (threshold 100 ps).
  - **Likely Cause:** Global CTS topology imbalance or incorrect target latency constraints causing unequal path lengths across the design.
  - **Suggested Fix:** Re-run CTS with tighter skew targets; review `set_clock_tree_options` skew constraints; verify clock tree reference cells.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqB_clk`
  - **Symptom:** Clock 'idv_osc_freqB_clk' avg insertion delay = 1015 ps (1.015 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `idv_osc_freqA_clk`
  - **Symptom:** Clock 'idv_osc_freqA_clk' avg insertion delay = 1037 ps (1.037 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `visaclk`
  - **Symptom:** Clock 'visaclk' avg insertion delay = 1005 ps (1.005 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bclk`
  - **Symptom:** Clock 'bclk' avg insertion delay = 2081 ps (2.081 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `ctfclk_200`
  - **Symptom:** Clock 'ctfclk_200' avg insertion delay = 3224 ps (3.224 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `bscanclk`
  - **Symptom:** Clock 'bscanclk' avg insertion delay = 3001 ps (3.001 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `ctfclk`
  - **Symptom:** Clock 'ctfclk' avg insertion delay = 3265 ps (3.265 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk_sys`
  - **Symptom:** Clock 'tapclk_sys' avg insertion delay = 3373 ps (3.373 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `dfx_secure_clk`
  - **Symptom:** Clock 'dfx_secure_clk' avg insertion delay = 3162 ps (3.162 ns). high delay + low skew → likely over-buffering
  - **Likely Cause:** Excessive buffer insertion due to over-aggressive CTS target latency or too many reference cells in library.
  - **Suggested Fix:** Reduce `set_clock_tree_options -target_skew`; filter CTS reference cell list to faster drive-strength cells; check max_transition constraints.
  - **Confidence:** High

- **Clock:** `ctfclk_div_200`
  - **Symptom:** Clock 'ctfclk_div_200' avg insertion delay = 3115 ps (3.115 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

- **Clock:** `tapclk`
  - **Symptom:** Clock 'tapclk' avg insertion delay = 3160 ps (3.160 ns). high delay + high skew → routing/topology issue
  - **Likely Cause:** Routing congestion or sub-optimal clock trunk placement forcing long wire detours increasing both delay and skew.
  - **Suggested Fix:** Improve floorplan to bring clock source closer to load clusters; add clock guide constraints; review NDR rules.
  - **Confidence:** Medium

## ⚠️ Parse Warnings

- No clock data detected. Ensure input is a Fusion Compiler CTS report.

---
*ClockIQ — Clock Tree Diagnostics & Optimization Assistant*


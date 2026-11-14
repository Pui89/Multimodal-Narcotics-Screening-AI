# PUI89 Sentinel — Validation and Evidence Matrix

**Product:** All-Terrain Inspection Robot Dog  
**Revision:** 0.1  
**Status:** Initial evidence plan; no physical robot validation is claimed.

## Evidence status vocabulary

- **Verified:** the named test completed and evidence is retained for the stated configuration and scope.
- **Failed:** a test ran and did not meet its acceptance criterion.
- **Not measured:** suitable evidence is not yet available.
- **Not applicable:** the requirement does not apply to the declared configuration.

A design statement, simulation result, supplier claim or illustrative image is not proof of physical performance.

## Requirements and evidence gates

| ID | Requirement | Evidence / test method | Acceptance basis | Current status | Next action |
|---|---|---|---|---|---|
| SYS-01 | Mission and operating envelope are explicit | Approved mission profile, hazard analysis and site constraints | Every intended mission has measurable limits and no-go conditions | Not measured | Define first inspection mission |
| MOB-01 | Four-leg locomotion is stable within declared terrain limits | Instrumented gait tests across named surfaces, slopes and transitions | No unsafe instability; repeatable metrics and documented limits | Not measured | Define mobility test fixture and metrics |
| MOB-02 | Threshold and step traversal are bounded | Controlled tests with measured geometry, payload and approach conditions | Successful traversal only within published tested envelope | Not measured | Define step/threshold classes |
| MOB-03 | Stop, hold and retreat behaviours work under faults | Fault injection for localisation, footing, power and communications | Safe response occurs within measured limits | Not measured | Specify fault scenarios |
| PER-01 | RGB perception reports supported observations | Labelled, permissioned dataset; held-out evaluation | Per-class precision/recall and known limitations reported | Not measured | Define first visual inspection task |
| PER-02 | Depth / LiDAR geometry is calibrated and time-aligned | Calibration records, target measurements and timestamp tests | Error and drift remain within declared task tolerances | Not measured | Select candidate sensors only after requirements |
| PER-03 | Uncertainty and abstention are explicit | Missing, stale, contradictory and out-of-distribution tests | Unknown conditions do not produce unsupported positive claims | Not measured | Define uncertainty test set |
| NAV-01 | Localisation and mapping are repeatable | Repeat-route trials with ground-truth reference | Error, drift and recovery measured across scenarios | Not measured | Establish simulation baseline |
| SAFE-01 | Emergency stop is independent of AI software | Hardware design review and controlled stop-time tests | Independent stop path verified for final hardware | Not measured | Specify safety circuit |
| SAFE-02 | Critical faults fail closed | Unit, integration and fault-injection tests | Missing/invalid critical signals produce SAFE_HOLD | Not measured | Implement and test safety gate |
| SAFE-03 | Human approval gates are enforced | Permission and workflow tests | Unapproved consequential actions cannot proceed | Not measured | Define action allowlist |
| DATA-01 | Evidence is traceable and privacy-aware | Provenance, timestamp, retention and access-control audit | Each record has source, configuration, reviewer and handling basis | Not measured | Define evidence schema |
| REL-01 | Endurance and thermal limits are known | Loaded duty-cycle tests with power and temperature logging | Published limits supported by repeated measurements | Not measured | Define target duty cycle |
| INT-01 | Hardware/software interfaces are versioned | Interface contract tests and compatibility matrix | Breaking changes detected and documented | Not measured | Freeze initial interface contracts |
| SUP-01 | Components have verified origin and sourcing records | Manufacturer documentation and supplier quotation review | Exact model, origin evidence, price date and lead time recorded | Not measured | Build candidate sourcing shortlist |

## Required test record

Every test record should include:

- Test ID, date, location/lab and responsible operator.
- Robot configuration, payload, firmware/software/model versions.
- Sensor manufacturer/model, calibration state and timestamp status.
- Environment, terrain, weather and scenario conditions.
- Procedure, expected result, measured result and acceptance criterion.
- Raw logs, images/video, plots and evidence hashes.
- Faults, deviations, corrective actions and reviewer sign-off.

## Validation sequence

1. Requirements review and hazard analysis.
2. Simulation and repeatable scenario testing.
3. Bench tests for compute, sensors, power and communications.
4. Controlled locomotion and fault-injection tests.
5. Supervised site trial after documented safety and permission reviews.

Passing simulation does not establish real-world performance. No capability may be advertised as implemented or validated until the corresponding evidence is reviewed and approved.

## Current evidence boundary

This matrix is an initial plan. The physical robot has not been validated; no performance metric, terrain rating, endurance figure or operational readiness claim is established by this document.

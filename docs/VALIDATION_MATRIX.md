# PUI89 Sentinel — Quadruped Exploration & Inspection Validation Matrix

**Baseline:** Stage 1 — concept and requirements reset.  
**Important:** No physical robot, selected sensor suite, integrated locomotion controller or field performance is currently claimed. All numerical acceptance thresholds remain TBD until the engineering baseline is approved.

| ID | Requirement | Test approach | Required evidence | Current status |
|---|---|---|---|---|
| REQ-01 | Mission and operating envelope | Define site, terrain classes, no-go zones, operator and abort conditions | Approved mission profile and hazard analysis | Not yet established |
| PER-01 | RGB image quality and scene perception | Controlled image set; lighting, blur, occlusion and motion cases | Dataset provenance, annotations, per-class metrics | Not measured |
| SPA-01 | Depth/spatial estimation | Calibrated targets and geometry scenarios | Sensor calibration, error distribution, valid range | No sensor selected |
| TER-01 | Terrain and obstacle assessment | Paved, gravel, grass, soil, slope, step and roughness scenarios | Ground truth, traversability confusion matrix, false-safe analysis | Simulation/physical tests pending |
| LOC-01 | Localisation and mapping | Repeatable routes, drift, occlusion and degraded sensor cases | Pose/map error, relocalisation and failure logs | Not measured |
| QDR-01 | Quadruped state awareness | Joint, IMU and foot-contact fault injection | State estimation error, slip/stumble detection evidence | No hardware selected |
| MOB-01 | Locomotion, balance and recovery | Controlled gait/terrain trials with safety supervision | Stability, fall, slip, step and recovery results | Not implemented/validated |
| INS-01 | Inspection and change detection | Repeated asset/area observations | Change precision/recall, evidence traceability | Not measured |
| SAF-01 | Stop, safe-hold and emergency stop | Sensor, communications, localisation and power fault tests | Stop latency, independent interlock and fault records | Requirements only |
| HUM-01 | Human mission authority | Workflow and usability tests | Operator permissions, abort/override evidence | Requirements only |
| PRI-01 | Privacy and evidence governance | Data-flow and retention review | Data minimisation, access and deletion policy | Requirements only |
| ENV-01 | Environmental limits | Temperature, rain/dust, ingress and atmosphere-risk assessment | Qualified tests and calibrated instruments | Not measured |
| REL-01 | Endurance and reliability | Repeated mission cycles and component stress tests | Runtime, failure rate, maintenance and recovery logs | Not measured |

## Evidence classes

- **Software:** schemas, unit tests and deterministic logic.
- **Simulation:** simulator version, model/asset provenance, scenario, seed and logs.
- **Bench:** actual sensor/compute/power components and calibration records.
- **Physical:** controlled robot tests with safety controls and independent observations.
- **Field:** authorised, risk-assessed missions with environmental conditions and operator records.

Passing one class does not imply passing a later class. Simulation does not prove physical performance.

## Prohibited evidence transfer

Former narcotics-screening workflow tests, synthetic classification metrics, chemical/X-ray documents and the old 45% readiness score are not evidence for the quadruped exploration product. Establish new baselines only from evidence relevant to Sentinel's current requirements.

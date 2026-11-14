# PUI89 Sentinel — Complete System Blueprint

**Product:** All-Terrain Inspection Robot Dog  
**Revision:** 0.1  
**Status:** Concept and engineering architecture; not a built, integrated or validated robot.  
**Procurement / build approval:** Not authorised by this document.

## 1. Product definition

PUI89 Sentinel is a four-legged mobile inspection platform intended to support authorised operators in industrial, infrastructure, logistics, port and selected outdoor environments. It observes accessible surroundings and assets, records traceable evidence, reports conditions and proposes bounded inspection actions for human review.

Sentinel is a quadruped with four articulated legs. It is distinct from PUI89 NOMAD, which is a four-wheel mobile assistant.

## 2. System architecture

```text
Mission request + site permissions + operating envelope
                  |
                  v
       Mission / Task Supervisor
                  |
                  v
 Sensors -> Perception & Task Intelligence -> World State
                  |                              |
                  v                              v
       Evidence & Provenance             Risk / Safety Monitor
                  |                              |
                  v                              v
        Operator Review <--- Action Proposal / Safe Hold
                  |
                  v
      Approved motion request (bounded interface)
                  |
                  v
     Independent motion & hardware safety controls
                  |
                  v
        Locomotion / actuators (future hardware)
```

The diagram describes a target architecture. It does not imply that sensors, compute, actuators or interfaces are currently integrated.

## 3. Intelligence capabilities

### Perception
- RGB image quality, object detection and classification, tracking and segmentation.
- Depth and spatial estimation where supported by calibrated sensors.
- Scene understanding, obstacle and traversability cues, change and anomaly detection.
- Sensor health, timestamp freshness, calibration state and modality availability.
- Confidence, uncertainty, disagreement and explicit abstention.

### Task intelligence
- Convert an authorised mission into a bounded checklist and inspection route proposal.
- Prioritise observations and assets according to the approved task.
- Maintain task state, completion evidence and unresolved findings.
- Request human clarification when goals, permissions or observations conflict.

### Robotics intelligence
- State estimation from IMU, joint state and foot-contact signals.
- Mapping, localisation, route planning and terrain-aware gait proposals.
- Obstacle awareness, foothold assessment, slip/stumble/fall-risk cues.
- Safe stop, hold, retreat and supervised recovery proposals.

All items above are design capabilities or requirements until individually implemented and verified.

## 4. Candidate sensing and compute

| Element | Intended role | Status |
|---|---|---|
| RGB cameras | Scene context, visible asset inspection and evidence | Candidate |
| Depth camera | Near-field geometry and clearance | Candidate |
| 360-degree LiDAR | Mapping, localisation and obstacle awareness | Candidate |
| IMU | Body motion and orientation | Required design function |
| Joint and foot-contact sensors | Leg state, contact and gait estimation | Required design function |
| Thermal camera | Temperature-pattern observation for justified missions | Optional candidate |
| Microphones / speaker | Acoustic event cues and operator communication | Optional candidate |
| Edge AI computer | Local perception, task support and evidence handling | Candidate |
| Calibrated atmosphere instruments | Mission-specific environmental safety measurements | Optional; risk-assessment driven |

Exact manufacturer, model, origin, compatibility, supplier, price, lead time and warranty must be verified before procurement. No component is selected or purchased by this blueprint.

## 5. Mission lifecycle

1. Receive an authorised mission, site rules, task boundaries and operator identity/role.
2. Confirm robot health, sensor availability, calibration and communications.
3. Build a local world state with timestamps, provenance and uncertainty.
4. Assess route, terrain, obstacles, people, asset access and exit/retreat options.
5. Propose the next bounded inspection action.
6. Apply deterministic safety checks independently of AI confidence.
7. Request operator approval where required; otherwise remain in the permitted supervised mode.
8. Capture observations and evidence with source, timestamp, model/version and uncertainty.
9. Report findings for human review; do not convert uncertain observations into definitive claims.
10. Stop, hold, retreat or request assistance when safety conditions are unknown or violated.

## 6. Safety architecture

- Independent emergency-stop path and hardware safety controller are required for physical operation.
- AI models may provide observations and proposals; they cannot override safety interlocks.
- Missing, stale, contradictory or invalid critical signals must fail closed to SAFE_HOLD.
- Motion requests must be allowlisted, bounded by speed/force/joint/workspace limits and checked before execution.
- People, vehicles, edges, unstable surfaces, overhead hazards and restricted zones must be represented in the risk assessment.
- Loss of localisation, unsafe footing, sensor disagreement, watchdog timeout or communications failure must trigger a defined safe response.
- No unsupervised entry into hazardous, inaccessible or unassessed environments.
- Privacy, data minimisation, access control, retention limits and auditability apply to captured data.

A software STOP/HOLD decision does not physically stop a robot unless an independently validated hardware safety path is present.

## 7. Operating envelope

“All-terrain” is an engineering ambition, not a guarantee. Each terrain class, slope, step, threshold, payload, speed, weather condition and environmental exposure requires measurable limits and controlled validation. Deep water, unstable structures, hazardous environments, unassessed confined spaces and conditions outside the verified envelope are no-go conditions.

## 8. Evidence and validation workflow

Use the progression:

**Specify -> Simulate -> Bench-test -> Controlled prototype test -> Supervised site trial**

Record scenario, environment, robot configuration, payload, sensor calibration, software/model versions, operator, test procedure, raw evidence, expected result, measured result, failures and corrective actions.

Simulation results establish simulation behaviour only. They do not establish physical mobility, perception accuracy, endurance, safety or field readiness.

## 9. Development gates

- **Gate A — Requirements:** mission definition, hazard analysis, measurable acceptance criteria and operating envelope.
- **Gate B — Simulation:** repeatable gait, terrain, obstacle, localisation and fault scenarios.
- **Gate C — Component selection:** verified non-Chinese-origin sourcing evidence, compatibility and written quotations.
- **Gate D — Bench integration:** power, compute, sensor timing, thermal and communications checks.
- **Gate E — Controlled mobility:** stability, payload, gait, stopping and emergency-stop validation.
- **Gate F — Supervised mission trial:** site permission, safety review, operator training and documented acceptance.

No later gate is assumed passed by completion of an earlier one.

## 10. Current status

Sentinel remains at concept and requirements definition. No physical prototype, integrated sensor stack, validated gait, terrain performance, inspection accuracy or operational deployment is claimed.

## Related engineering records

- [Sentinel engineering requirements](SENTINEL_ALL_TERRAIN_INSPECTION_ROBOT_DOG_REQUIREMENTS_V0.2.md)
- [Validation and evidence matrix](VALIDATION_MATRIX.md)
- [PUI89 AI Core contract](PUI89_AI_CORE_CONTRACT.md)
- [Safety requirements](SAFETY.md)

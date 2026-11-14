# PUI89 Sentinel — All-Terrain Inspection Robot Dog Engineering Requirements

**Revision:** 0.2  
**Status:** Concept and requirements definition only  
**Product form:** Four-legged quadruped robot dog; no wheels  
**Mission:** General industrial, infrastructure, logistics, port and selected outdoor inspection  
**Procurement / build approval:** Not authorised by this document

## 1. Product identity and boundary

Sentinel is a general-purpose mobile inspection robot dog. It is not a narcotics-screening product and this baseline does not include an X-ray payload or dedicated narcotics-detection subsystem. PUI89 NOMAD is a separate four-wheel mobile assistant. Sentinel's four articulated legs are intended for selected terrain and access challenges that may be unsuitable for wheeled platforms.

This is an engineering target, not a built or validated robot.

## 2. Mission requirements

- Inspect authorised industrial facilities, infrastructure, warehouses, logistics yards and port areas.
- Patrol approved routes, observe assets and environmental conditions, capture timestamped evidence and report anomalies for human review.
- Approach assigned container entrances and assess geometry and hazards before any entry.
- Enter only where doorway, threshold, floor, overhead clearance, atmosphere controls, localisation and exit route have been assessed and approved.
- Support safe retreat, stop and operator escalation when conditions become uncertain.

## 3. Quadruped mobility requirements

- Four articulated legs with mechanically rated joints, actuators and structural members.
- Controlled forward/reverse walking, turning, sidestepping and speed transitions.
- Adaptive gait and foot placement for validated surface classes.
- IMU, joint-state and foot-contact estimation; slip/stumble detection.
- Managed centre of mass and payload envelope.
- Fall-risk mitigation, controlled stop and supervised recovery research.
- Speed must adapt to terrain, slope, payload, traction, visibility, temperature and battery state.
- Candidate algorithms: gait planning, state estimation, MPC and whole-body control; selection requires simulation and comparative testing.

No claim of running speed, guaranteed balance, impact resistance, self-righting or unrestricted all-terrain operation is permitted without test evidence.

## 4. Target environment and no-go conditions

Target surfaces for staged evaluation: indoor floors, corridors, paved paths, gravel, grass, firm soil, moderate slopes, steps and selected uneven/rubble-like surfaces. Each surface class requires documented traction, stability, payload, endurance, weather and obstacle tests.

No-go unless separately engineered, risk-assessed and authorised: deep water, cliffs, unstable structures, extreme slopes, inaccessible gaps, hazardous atmospheres, fire zones and conditions outside the validated operating envelope.

## 5. Container and confined-area requirements

| Challenge | Required behaviour / evidence |
|---|---|
| Narrow entrance | Measure and verify body/leg clearance; accurate approach and alignment |
| Raised threshold | Controlled step-over only after geometry and footing assessment |
| Dark interior | Low-light imaging and onboard illumination where safe |
| Crowded cargo | Narrow-space navigation, overhead awareness and safe retreat |
| Uneven floor | Adaptive foot placement, slip detection and stable stopping |
| Long container | Local mapping, localisation confidence and return-route planning |
| Lost communication | Safe hold, local safety behaviour and recovery procedure |
| Unknown atmosphere | No entry until site-approved assessment and suitable calibrated instruments establish safe conditions |

Cameras, depth sensors and LiDAR cannot certify breathable air or detect all hazardous gases. Site risk assessment, operator authorisation and calibrated atmosphere instruments are separate requirements where relevant. If clearance, footing, localisation, atmosphere status or exit route is unknown, Sentinel must not proceed.

## 6. Candidate sensing and compute

RGB, depth, 360° LiDAR, IMU, joint/foot state, audio and edge compute are candidate core elements. Thermal imaging and calibrated gas/atmosphere instruments are mission-specific options. Each candidate requires exact manufacturer/model, part number, country of manufacture and origin evidence, technical datasheet, interface compatibility, power/thermal analysis, supplier, dated quotation, lead time and warranty review.

No component is selected, purchased or integrated by this document.

## 7. Six intelligence groups

Vision; Audio; Multimodal; Robotics; Action & Reaction; Safety & Control. Their roles and limitations are defined in the project README. All model outputs remain bounded proposals. Safety policy must be independent of model confidence and must enforce operating envelopes, safe hold, human approval and emergency-stop boundaries.

## 8. Safety and privacy

- Authorised operation only; comply with site traffic and exclusion zones.
- Treat people, forklifts, trucks and moving cargo as dynamic hazards.
- No biometric identity inference, voice identity recognition, profiling or autonomous enforcement.
- No automatic accusation, detention, search or coercive action.
- Human approval for consequential actions.
- Preserve timestamp, sensor identity, calibration status, provenance, uncertainty and audit record.
- Safe hold and operator escalation on loss of localisation, unsafe footing, sensor conflict, communications failure or unknown hazard.
- Do not use visual sensing as a substitute for gas detection, structural assessment or site safety procedures.

## 9. Verification plan

1. Requirements review and simulation of gait, stability, obstacle clearance and safe-stop behaviours.
2. Bench verification of power, thermal, compute, sensing and emergency-stop interfaces.
3. Controlled indoor locomotion tests with unloaded and representative payload configurations.
4. Incremental terrain tests with measurable traction, stability, speed, endurance and recovery criteria.
5. Container mock-up tests for entrance, threshold, narrow-space movement, mapping and retreat.
6. Supervised site trial only after independent safety review and operator/site approval.

Simulation results are not physical validation. A successful test on one surface or configuration does not establish all-terrain capability.

## 10. Preliminary prototype cost

**Planning estimate: ฿1,225,000–฿2,990,000 for one engineering prototype.** This is a high-uncertainty estimate, not a supplier quote, verified BOM, fixed budget or purchase approval. It assumes a custom quadruped platform, actuators, mobility control, battery/power, core perception sensors, edge compute and integration/testing. It excludes salaries, facilities, VAT, duty, freight, certification, tooling, mass production and maintenance. Specialist thermal or atmosphere instruments may add cost. Final cost requires a defined mass/payload envelope, supplier-verified BOM and written quotations.

## 11. Approval gates

No procurement, fabrication or field deployment is authorised. Proceed only after mission definition, safety review, supplier/origin verification, BOM and budget approval, controlled test plan and explicit owner approval.

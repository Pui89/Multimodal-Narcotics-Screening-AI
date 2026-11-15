# PUI89 Sentinel — All-Terrain Exploration & Inspection Quadruped Requirements

**Revision:** 0.3  
**Product form:** Four-legged AI quadruped; no wheels  
**Tagline:** Explore Anywhere — design ambition, not validated capability  
**Status:** Stage 1 concept and requirements only  
**Procurement/build approval:** Not authorised

## 1. Product identity

Sentinel is a general-purpose quadruped for supervised exploration, environmental awareness and inspection. It is distinct from PUI89 AI NOMAD, a four-wheel mobile assistant, and PUI89 AI HOME, a four-wheel indoor assistant. Sentinel is not a narcotics-screening, X-ray, chemical-identification or enforcement product.

## 2. Mission requirements

- Explore and inspect authorised industrial facilities, infrastructure, warehouses, logistics yards, ports and selected outdoor environments.
- Observe terrain, access routes, obstacles, visible assets and environmental changes.
- Capture timestamped, provenance-aware evidence and report uncertainty for human review.
- Support repeatable operator-defined inspection missions and checklists.
- Stop, safe-hold, retreat or request operator assistance when the environment or robot state is uncertain.
- Support supervised reconnaissance from safe, authorised locations; do not claim unvalidated emergency entry or rescue capability.

## 3. Quadruped mobility requirements

Four articulated legs with mechanically rated joints, actuators and structural members. Future engineering must evaluate controlled forward/reverse walking, turning, sidestepping, adaptive gait, foot placement, IMU/joint/foot-contact estimation, slip/stumble/fall-risk detection, centre of mass, payload, power, thermal limits, safe stop and supervised recovery.

Joint count, dimensions, mass, payload, actuator models, gait algorithms and operating thresholds remain TBD. No claim of running speed, guaranteed balance, self-righting, fall recovery or unrestricted all-terrain operation is permitted without reproducible evidence.

## 4. Candidate environment classes

Initial research candidates: indoor hard floors, corridors, paved paths, compacted gravel, grass, firm soil, moderate slopes, low steps and selected uneven terrain. Each class needs measurable traction, stability, obstacle, payload, endurance, weather and safety acceptance criteria.

No-go unless separately engineered, risk-assessed and authorised: deep water, cliffs, unstable structures, extreme slopes, inaccessible gaps, fire zones, explosive/hazardous atmospheres, unknown confined spaces and any condition outside the validated operating envelope.

## 5. Perception and sensing

Candidate sensors include RGB cameras, depth/stereo, optional 360° LiDAR, IMU, joint encoders and foot/contact sensors. Thermal, audio and calibrated environmental sensors are mission-specific options. Each sensor requires documented manufacturer/model, origin, operating principle, range, interface, calibration, power/thermal impact, data rights and validation method. No sensor is selected, purchased or integrated by this document.

## 6. AI capability requirements

- Vision: image quality, detection, classification, tracking, segmentation and scene understanding.
- Spatial: depth geometry, obstacle/free-space estimation, mapping and localisation confidence.
- Terrain: slope, step, roughness, traversability and uncertainty.
- Quadruped state: body attitude, joint/gait state, foot contact, slip/stumble/fall-risk observations.
- Mission: task decomposition, inspection checklists, event/change detection and evidence reporting.
- Safety: independent constraints, permission checks, safe-hold, fault response and human escalation.

AI outputs are observations and bounded proposals only. No language model or perception model may directly authorise actuator commands.

## 7. Confined and hazardous environments

Container or confined-area entry is not an assumed capability. Any future mission requires site authorisation, doorway/body/leg clearance, footing, overhead hazards, localisation, communications, atmosphere assessment and a viable exit route. RGB, depth and LiDAR cannot certify breathable air or structural integrity. If any critical condition is unknown, the robot must not enter or must stop and request human assistance.

## 8. Validation gates

1. Requirements and hazard analysis.
2. Software contracts, mock sensors, uncertainty and negative tests.
3. Simulation of terrain, gait, obstacles, localisation and faults.
4. Bench integration of selected sensors and compute.
5. Controlled physical locomotion tests with independent safety controls.
6. Supervised field trials, one environment class at a time.
7. Independent safety, reliability, privacy and release review.

Simulation is not physical validation. A concept illustration is not a prototype. No performance metric is claimed until measured with a defined protocol and traceable evidence.

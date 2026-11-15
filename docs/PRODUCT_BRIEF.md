# Product Brief — PUI89 Sentinel

**Official working name:** PUI89 Sentinel — All-Terrain Exploration & Inspection Robot  
**Product class:** AI quadruped / four-legged mobile robot  
**Tagline:** Explore Anywhere  
**Mission:** Supervised exploration, situational awareness, inspection and evidence capture across selected environments.  
**Portfolio distinction:** Sentinel is four-legged; AI NOMAD and AI HOME are separate four-wheel products.  
**Status:** Stage 1 — concept and requirements definition. No physical robot, integrated sensors, validated locomotion or field performance is claimed.

## 1. Product intent

PUI89 Sentinel is a general-purpose quadruped platform intended to help an authorised operator explore and inspect places that are difficult, repetitive or inconvenient to access. It combines environmental perception, spatial and terrain awareness, robot-state monitoring, inspection workflows and evidence reporting. The robot should understand conditions around itself and communicate uncertainty before any movement or task proposal.

“Explore Anywhere” is an ambition to develop broad environmental adaptability. It is not a promise that the robot can safely traverse every terrain, enter every structure or operate in hazardous conditions.

## 2. Target users and use cases

- Facility and infrastructure inspection teams.
- Industrial, warehouse, logistics and port operators.
- Research and engineering teams studying quadruped mobility and embodied AI.
- Emergency-response teams needing supervised reconnaissance from safe, authorised locations.
- Operators performing repeatable outdoor condition monitoring.

Target missions include visible asset inspection, route/terrain observation, obstacle awareness, environmental change detection, site documentation and evidence collection. All require site permission, risk assessment and mission-specific operating limits.

## 3. Product capability groups

1. **Perception:** RGB image quality, detection, classification, tracking, segmentation, scene understanding and visible anomaly/change cues.
2. **Spatial awareness:** depth/point-cloud processing, geometry, free-space, obstacle clearance, slope/step/roughness estimation and traversability uncertainty.
3. **Quadruped state awareness:** IMU, joint state, gait phase, foot contact, slip, stumble, body attitude and fall-risk observations.
4. **Mapping and localisation:** local map, pose estimate, localisation confidence, route context and recovery/retreat proposals.
5. **Multimodal environment awareness:** optional thermal, audio and mission-specific calibrated environment sensors; no sensor is assumed present until selected and tested.
6. **Inspection intelligence:** mission checklist, asset/area observations, change detection, event timeline, evidence bundle and structured report.
7. **Task intelligence:** bounded mission planning, waypoint/inspection proposals, risk-aware task sequencing and human escalation.
8. **Safety supervision:** independent limits, permissions, fault monitoring, stop/safe-hold, emergency stop and human-approved recovery.

These are target capabilities. Each must be classified as proposed, implemented, tested, simulated, measured or validated with supporting evidence.

## 4. Operating envelope and exclusions

Initial research should focus on controlled, low-speed, supervised operation on defined surfaces. Candidate terrain categories include paved floors, compacted paths, gravel, grass, soil, moderate slopes, low steps and selected uneven ground. Acceptance limits for grade, step height, roughness, water exposure, payload, speed, endurance and temperature must be measured before use.

No-go until separately engineered and validated: deep water, cliffs, unstable structures, fire, explosive atmospheres, hazardous gases, extreme slopes, inaccessible gaps, unknown confined spaces and any site outside the approved envelope. RGB/depth/LiDAR cannot certify air quality or structural integrity.

Out of scope: narcotics/substance screening, X-ray or chemical identification, autonomous enforcement, weaponisation, pursuit, restraint, forced entry, biometric identification and unrestricted covert surveillance. Historical screening artifacts are not product features.

## 5. User experience

The operator defines the mission, permitted area, route constraints, observation checklist and abort conditions. Sentinel provides a live status view, map/terrain context when supported, obstacle and robot-state indicators, event notifications, uncertainty, evidence capture and a post-mission report. The operator remains responsible for authorising consequential actions.

## 6. Technical architecture

Sensor inputs → validation/provenance → perception and spatial intelligence → terrain and robot WorldState → mission/inspection reasoning → independent safety supervisor → human review and bounded action proposal → evidence, logs and reports.

Reuse PUI89 Shared AI Core contracts: Observation, WorldState, ActionProposal and FailureReport. Include source/time/quality/calibration metadata, uncertainty, explicit unknown/conflict states and fail-safe behaviour.

## 7. Development gates

- **G1 Requirements:** mission profiles, hazards, operating envelope, sensor requirements and acceptance criteria.
- **G2 Software foundation:** schemas, perception adapters, world state, evidence and deterministic negative tests.
- **G3 Simulation:** repeatable terrain, gait, obstacle, localisation and fault scenarios; report simulation separately.
- **G4 Bench:** selected sensors, compute, power, communications and safety interfaces tested without physical locomotion.
- **G5 Prototype:** controlled locomotion, stability, foot contact, payload, endurance and emergency-stop tests.
- **G6 Field validation:** supervised, permitted and risk-assessed site trials with reproducible evidence.
- **G7 Release review:** independent safety, reliability, privacy, maintenance, regulatory and procurement assessment.

## 8. Evidence and maturity

Do not inherit the former screening workflow's 45% readiness score, datasets, precision/recall or tests as evidence for this quadruped. Create a new evidence ledger and baseline. Passing software tests does not validate physical mobility; simulation does not validate real terrain; a sensor listed in a document is not proof of purchase, integration or calibration.

## 9. Procurement boundary

Candidate hardware must be evaluated for exact manufacturer, model/part number, country of manufacture and origin evidence, technical compatibility, supplier, dated indicative price, lead time, warranty and serviceability. Prefer verifiable non-Chinese-origin options where suitable. This brief authorises no purchase, installation or paid service.

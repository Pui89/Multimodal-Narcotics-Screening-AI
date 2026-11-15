# PUI89 Sentinel — All-Terrain Exploration & Inspection Quadruped Concept

**Product direction:** AI quadruped / four-legged robot  
**Tagline:** Explore Anywhere  
**Status:** Proposed concept and requirements only. No built robot, integrated sensor suite, validated gait, autonomous navigation or field performance is claimed.

![PUI89 Sentinel quadruped concept](images/pui89-sentinel-quadruped-inspection-v3.svg)

## 1. Mission

A human-supervised mobile platform for exploring and inspecting selected industrial, infrastructure, logistics, outdoor and difficult-to-access environments. Sentinel should perceive its surroundings, assess terrain and obstacles, monitor its own body state, observe visible assets and environmental changes, capture traceable evidence and communicate uncertainty to an operator.

Explore Anywhere is the long-term design ambition—not unrestricted access or a validated capability claim.

## 2. Quadruped form

- Four articulated legs with independently controlled joints; exact joint count and mechanical layout remain engineering decisions.
- Protected central body for compute, power and mission-appropriate sensors.
- Forward RGB/depth perception and optional elevated 360-degree awareness sensor, subject to design review.
- IMU, joint-state and foot-contact sensing for body and locomotion awareness.
- Modular payload interfaces only after mass, centre-of-gravity, power, thermal and safety budgets are defined.
- Physical emergency stop and independent safety controller required before any powered prototype.
- No wheels, drone/aircraft, weapon, manipulator or forced-entry device is part of the current concept.

## 3. Mission workflow

1. **Authorise:** operator defines mission purpose, area, permissions, route limits, data policy and abort conditions.
2. **Observe:** collect only configured and authorised sensor inputs with source, timestamp and quality metadata.
3. **Understand:** perform image quality checks, object/scene perception, spatial estimation, terrain assessment and robot-state estimation.
4. **Assess:** estimate traversability, obstacle clearance, localisation confidence, sensor health, risk and uncertainty.
5. **Propose:** prepare bounded inspection steps, route/waypoint suggestions, evidence capture and safe-stop/retreat recommendations.
6. **Supervise:** independent safety controls and operator approval govern any physical movement or consequential action.
7. **Report:** preserve event timeline, evidence references, software/model versions, uncertainty, faults and operator decisions.

## 4. Intelligence architecture

- **Vision:** object/asset detection, classification, tracking, segmentation, scene understanding and visible change/anomaly cues.
- **Spatial:** depth, geometry, free-space, obstacle clearance, slope/step/roughness and terrain traversability.
- **Locomotion awareness:** body attitude, joint state, gait phase, foot contact, slip, stumble, fall-risk and safe-hold state.
- **Mapping:** local map, pose/localisation confidence, route context and mapping quality.
- **Multimodal:** optional thermal, audio and mission-specific environment sensors with independent provenance and calibration.
- **Mission intelligence:** task decomposition, inspection checklists, waypoint proposals, event interpretation and human escalation.
- **Safety:** independent constraints, fault handling, safe hold, emergency stop and supervised recovery.

## 5. Operating envelope

Candidate environments include suitable indoor industrial floors, paved paths, compacted gravel, grass, soil, moderate slopes, low steps and selected uneven terrain. Every terrain class requires defined test conditions and acceptance thresholds before physical use.

No-go conditions until specifically engineered and independently validated include deep water, cliffs, unstable structures, fire, explosive/hazardous atmospheres, extreme slopes, inaccessible gaps, unknown confined spaces and any environment outside the approved envelope. Cameras, depth sensors and LiDAR cannot certify breathable air, toxic gas absence or structural integrity.

## 6. Product boundaries

Sentinel is not the former Multimodal Narcotics Screening AI. Narcotics screening, substance identification, chemical analysis, X-ray/baggage screening and enforcement workflows are excluded. Historical screening code, documents, test data and artwork are legacy artifacts only and are not product capabilities.

No autonomous enforcement, pursuit, restraint, forced access, person scoring, facial recognition or biometric identification. No drone or aerial flight capability is included.

## 7. Development stages

Requirements and mission profiles → software-first perception, world-state, evidence and safety contracts → simulation of terrain, obstacles, quadruped state and fault cases → controlled sensor/compute bench integration after approval → physical locomotion prototype and safety testing → supervised field validation with measurable acceptance criteria.

## 8. Evidence rules

Label every capability PROPOSED, IMPLEMENTED, TESTED, SIMULATED, MEASURED or VALIDATED with the supporting artifact. Software tests do not prove locomotion; simulation does not prove real-world terrain performance; a concept image does not prove a prototype. No physical Sentinel capability is currently claimed.

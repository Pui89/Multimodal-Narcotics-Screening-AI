# Complete System Blueprint — PUI89 Sentinel Quadruped Inspection Robot

**Product identity:** Four-legged quadruped inspection robot.  
**Mission:** Supervised inspection, situational awareness and traceable evidence capture in authorised industrial, infrastructure, logistics and selected outdoor environments.  
**Status:** Concept and engineering requirements. This document is an architecture proposal, not evidence of a built or validated robot.

## 1. System boundary

Sentinel is a mobile inspection platform with four articulated legs. It is not a wheeled assistant, narcotics-screening product, chemical analyser or X-ray system. PUI89 NOMAD is a separate four-wheel mobile assistant.

The robot may collect observations and propose bounded actions. It must not independently authorise hazardous entry, enforcement, search, detention or other consequential actions.

## 2. Proposed system architecture

```text
Operator mission / site permissions / operating envelope
  -> Mission manager and task constraints
  -> Independent safety supervisor and emergency-stop chain
  -> Locomotion controller <-> actuators / joint encoders / foot contacts
  -> State estimation <-> IMU / joint state / odometry
  -> Perception & Task Intelligence
       RGB / depth / LiDAR / audio / optional mission sensors
       quality checks / detection / segmentation / tracking
       mapping / obstacle and terrain assessment / uncertainty
  -> Shared AI Core contracts
       Observation / WorldState / ActionProposal / FailureReport
  -> Bounded route and inspection proposals
  -> Human approval where required
  -> Evidence package / event log / inspection report
```

This is a logical architecture only. Sensor selection, interfaces, compute allocation, control rates and mechanical design remain to be engineered and verified.

## 3. Functional subsystems

1. **Mechanical platform:** four articulated legs, joints, transmissions, feet, protective structure and defined payload envelope.
2. **Actuation and locomotion:** joint drives, real-time low-level control, gait generation, state feedback and controlled stop.
3. **Power and thermal:** battery, BMS, contactors, fusing, DC/DC conversion, power monitoring and thermal limits.
4. **State estimation:** IMU, joint feedback and suitable odometry/contact observations; report localisation confidence and degraded modes.
5. **Perception:** RGB, depth and/or LiDAR candidates for scene understanding, obstacles, terrain, assets and visible condition changes.
6. **Mission intelligence:** supervised route planning, inspection task sequencing, evidence capture, anomaly reporting and safe retreat proposals.
7. **Communications and operator interface:** status, teleoperation/supervision, alerts, loss-of-link behavior and audit trail.
8. **Safety system:** independent E-stop, bounded speed/force/operating envelope, watchdogs, fault handling, safe hold and human authorisation.

## 4. Shared AI Core contracts

All cross-module messages should carry a schema version, source, timestamp, frame/reference where applicable, quality, confidence/uncertainty and provenance.

- **Observation:** sensor-derived evidence with modality, calibration/version and quality metadata.
- **WorldState:** estimated robot/site state with uncertainty and freshness.
- **ActionProposal:** bounded candidate action with preconditions, limits, expected outcome and abort conditions. It is not an actuator command or safety override.
- **FailureReport:** fault code, severity, evidence, affected subsystem, safe-state recommendation and recovery constraints.

The safety supervisor remains independent of model confidence and may reject or stop any proposal.

## 5. Operating and safety principles

- Operate only with site permission and a documented task-specific operating envelope.
- Treat people, vehicles, edges, stairs, drop-offs and moving equipment as hazards requiring conservative handling.
- Stop or request operator intervention on uncertain footing, localisation loss, sensor disagreement, overheating, power faults, communication loss or unknown hazards.
- Do not enter hazardous atmospheres based on RGB, depth or LiDAR. Use suitable calibrated instruments and site-authorised procedures when required.
- Do not claim container entry, stair climbing, fall recovery, water resistance or all-terrain capability without dedicated verification.
- Preserve privacy, minimise collection and apply access controls and retention rules to inspection evidence.

## 6. Simulation and verification workflow

Use an evidence-gated sequence: requirements → software-in-the-loop → simulation → component bench tests → controlled indoor locomotion → incremental terrain tests → supervised site trial. Simulation is not physical validation.

Each test record should include requirement ID, test procedure, configuration, software/model version, hardware/firmware identity, date, operator, raw evidence, measured result, acceptance criterion, deviations and reviewer.

## 7. Candidate sensing and compute

RGB, depth, 360° LiDAR, IMU, joint/foot sensing, microphones and edge compute are candidates or design functions, not selected hardware. Thermal and atmosphere instruments are mission-specific options. No manufacturer, part number, country of manufacture, supplier or price is approved by this architecture.

## 8. Evidence and release gates

- [ ] Mission, operator, site and prohibited-use boundaries approved.
- [ ] Mechanical, mass, payload, actuator and power requirements baselined.
- [ ] Safety architecture and independent emergency-stop path reviewed.
- [ ] Candidate parts checked for specifications, compatibility and origin evidence.
- [ ] Simulation scenarios and acceptance criteria documented.
- [ ] Bench and locomotion tests completed with traceable evidence.
- [ ] Terrain and mission-specific tests completed within a defined envelope.
- [ ] Privacy, cybersecurity, maintainability and operator procedures reviewed.
- [ ] Release claims match demonstrated evidence; unresolved risks are disclosed.

## 9. Current boundary

No physical Sentinel prototype, selected or purchased sensor suite, integrated locomotion system, validated gait, measured terrain envelope, container-entry capability, fall recovery, industrial deployment or certification is claimed. Budget is **not yet established** pending engineering definition, verified BOM and written supplier quotations.

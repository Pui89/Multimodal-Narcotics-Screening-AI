# PUI89 Sentinel — Complete Quadruped Exploration & Inspection System Blueprint

**Status:** Proposed system architecture; not a deployed robot or validated autonomy stack.

## System flow

Authorised mission → RGB/depth/optional LiDAR/IMU/joint and foot sensors/optional mission sensors → input validation, calibration and provenance → vision, spatial and terrain perception → robot-state estimation and local WorldState → inspection and mission reasoning → independent safety supervisor → human-supervised bounded action proposal → evidence bundle, event log and report.

## Main subsystems

1. **Sensor ingestion:** validate source, timestamp, frame, quality, calibration, freshness and mission permission.
2. **Perception:** image quality, detection, classification, tracking, segmentation, scene understanding and visible change/anomaly cues.
3. **Spatial intelligence:** depth/point-cloud geometry, free-space, obstacle clearance, slope/step/roughness and terrain uncertainty.
4. **Quadruped state:** IMU, joint state, gait phase, foot contact, body attitude, slip/stumble/fall-risk observations.
5. **Mapping/localisation:** local map, pose estimate, confidence, map consistency and safe-retreat context.
6. **Inspection intelligence:** mission checklist, visible asset observations, change comparison, event timeline and evidence capture.
7. **Safety supervisor:** independent operating limits, permissions, watchdog, emergency stop, safe hold and fault response.
8. **Operator interface:** mission status, map/terrain context, uncertainty, alerts, evidence and abort/override controls.

## Shared AI Core contracts

- **Observation:** source, time, quality, calibration, provenance and uncertainty.
- **WorldState:** spatial and mission state with freshness and conflict handling.
- **ActionProposal:** bounded advisory proposal; never direct actuator permission.
- **FailureReport:** fault, severity, safe state, evidence and recovery request.

## Engineering rules

Local-first and open-source-first where suitable; CPU-capable software baseline. Keep AI perception and mission reasoning separate from deterministic low-level motor control. No model or language model can bypass safety interlocks or operator authority. Fail safe on uncertain footing, localisation, sensor health, communications or operating-envelope status. Use optional sensors only when a defined mission justifies them and calibration/validation are feasible. Protect privacy, minimise retention and preserve evidence provenance.

## Current boundaries

No physical robot, quadruped gait, obstacle avoidance, sensor calibration, autonomous navigation, thermal/gas detection, all-terrain performance or field deployment is established. The former screening pipeline is legacy material and is not the current product system.

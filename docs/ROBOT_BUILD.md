# PUI89 Sentinel — Quadruped Build & Validation Roadmap

This document defines a staged engineering path. It does not authorise purchases, installations or physical operation.

## Stage 1 — Software and requirements

1. Define mission profiles, terrain classes, no-go conditions and operating envelope.
2. Define Observation, WorldState, ActionProposal and FailureReport contracts.
3. Build mock sensor adapters for RGB, depth, IMU, joint state and foot contact.
4. Implement image/spatial quality, uncertainty, event and evidence handling.
5. Add deterministic negative tests for missing, stale, invalid and conflicting inputs.

## Stage 2 — Simulation

1. Select a lightweight, open-source quadruped simulation path after licence, provenance, resource and hardware review.
2. Model the robot only from a documented geometry/joint baseline.
3. Add terrain, slope, step, loose-ground, obstacle, lighting and sensor-fault scenarios.
4. Evaluate stability, gait state, contact, slip, localisation, stop and recovery proposals.
5. Report simulator results as simulation only; do not present them as physical validation.

## Stage 3 — Bench integration

Only after separate approval: connect selected cameras, depth, IMU, joint/foot sensors and edge compute on a controlled bench. Verify calibration, timing, power, thermal, communication, emergency-stop and watchdog interfaces. Do not enable locomotion by default.

## Stage 4 — Controlled quadruped prototype

After mechanical and safety review, test low-speed locomotion in a bounded test area with physical emergency stop, independent safety controller, trained operator and documented exclusion zone. Measure stability, slip, stumble, falls, payload, endurance, thermal and recovery behaviour.

## Stage 5 — Supervised field validation

Test one terrain/environment class at a time under written permission and risk assessment. Record conditions, ground truth, failures, interventions, stop events and limitations. Expand the operating envelope only after evidence review.

## Non-negotiable boundaries

No unrestricted “go anywhere” autonomy. No entry into deep water, unstable structures or hazardous atmospheres without specific engineering and independent validation. No direct actuator control from an LLM or perception model. No autonomous enforcement, pursuit, restraint, forced access or biometric identification. No drone or aerial flight capability. No claim of a built prototype, sensor integration or field performance without evidence.

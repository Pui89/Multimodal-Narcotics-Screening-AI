# PUI89 Shared AI Core — Sentinel Quadruped Exploration & Inspection Profile

**Status:** Proposed integration profile; documentation only. No runtime integration or sensor connection is claimed.  
**Product:** PUI89 Sentinel — All-Terrain Exploration & Inspection Robot.

## Purpose

Reuse PUI89 Shared AI Core contracts for environmental perception, spatial/terrain awareness, quadruped state observations, supervised inspection tasks, uncertainty, evidence and safety proposals.

## Observation requirements

Each observation should carry source/device identifier and authorised mission context; timestamp and freshness; modality, data quality and calibration state; coordinate frame and transform provenance where spatial data is used; confidence/uncertainty and explicit missing, invalid or conflicting status; software/model/configuration version and evidence reference.

Candidate modalities: RGB, depth/stereo, optional LiDAR, IMU, joint encoders, foot-contact sensors, and mission-specific thermal/audio/environmental sensors only when selected and validated.

## WorldState requirements

Represent scene objects and visible assets; local geometry, obstacles, free-space and terrain estimates; robot pose, body attitude, joint/gait state and foot-contact observations; localisation/map confidence and sensor health; mission progress, operator-defined constraints and no-go zones; uncertainty, stale data, conflicts and unknown regions.

Do not infer safe traversability from a single image or model score. Missing or conflicting evidence must remain UNKNOWN/CONFLICT.

## ActionProposal boundary

Permitted proposal classes may include observe, capture evidence, inspect asset, request operator review, suggest waypoint, slow/stop, safe-hold or request supervised recovery. A proposal is not actuator authority. Physical motion requires an independently engineered controller, interlocks, emergency stop, operating-envelope checks and human-authorised mission control.

## FailureReport requirements

Record sensor dropout, localisation loss, map inconsistency, obstacle uncertainty, slip/stumble/fall-risk cues, communications loss, battery/thermal faults, emergency stop and operator abort. Include timestamp, source, severity, safe state, evidence references and recovery request.

## Validation

Test stale/missing sensors, invalid transforms, conflicting geometry, low light, dynamic obstacles, map drift, localisation loss, foot-contact dropout, slip/stumble scenarios, communication loss, emergency-stop and recovery proposals. Keep synthetic, simulation, bench and field evidence separate.

No narcotics screening, chemical-identification or X-ray task belongs in the current Sentinel integration profile.

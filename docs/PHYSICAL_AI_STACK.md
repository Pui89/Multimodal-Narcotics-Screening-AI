# PUI89 Sentinel — Physical AI & Embodied Intelligence Stack

## Proposed architecture

1. **Perception models:** object/asset detection, classification, segmentation, tracking, image quality and scene understanding.
2. **Spatial models:** depth/point-cloud processing, free-space, obstacle geometry, terrain features and traversability estimates.
3. **State estimation:** sensor time alignment, IMU, joint-state and foot-contact fusion, body attitude and localisation confidence.
4. **World model:** timestamped local representation of observed objects, terrain, obstacles, robot state, mission constraints and uncertainty.
5. **Mission reasoning:** convert an operator-approved inspection objective into a checklist and bounded route/observation proposals.
6. **Safety supervisor:** deterministic operating-envelope checks, watchdog, emergency stop, safe hold and fault handling independent of AI models.
7. **Evidence layer:** preserve source, timestamp, calibration, quality, model/software version, uncertainty and operator review.

## Candidate software direction

Prefer a CPU-first, open-source, local workflow. ROS 2 and Gazebo may be considered for robotics middleware and simulation only after checking exact versions, licence, origin/provenance, installation size, hardware needs and compatibility. Do not install or download large stacks/models automatically.

## Safe proposal vocabulary

Examples: observe area, capture evidence, inspect asset, suggest waypoint, request operator review, slow/stop, safe hold, request supervised recovery.

These are proposal labels, not commands to actuators. An independent low-level controller and physical safety system must authorise movement.

## Evaluation requirements

Measure perception metrics on permission-cleared, annotated data; spatial error against calibrated references; terrain false-safe/false-stop rates; localisation drift; contact/slip detection; task completion; stop latency; resource use; and failure recovery. Report sample counts, conditions and confidence intervals where appropriate. No metrics are currently claimed.

## Current implementation boundary

The repository's legacy screening workflow and tests are not Sentinel's active embodied-AI baseline. This document describes target architecture only; no VLM/VLA, locomotion policy, sensor driver or physical robot integration is claimed.

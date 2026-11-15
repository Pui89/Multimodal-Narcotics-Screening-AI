# PUI89 Sentinel — Spatial & Terrain Intelligence

## Purpose

Provide geometry and spatial context for supervised quadruped exploration, terrain assessment and inspection. This profile is a proposed integration direction; no runtime sensor integration is claimed.

## Planned functions

- RGB-D/depth geometry and point-cloud quality assessment.
- Obstacle and free-space estimation.
- Slope, step, roughness and terrain-shape cues.
- Traversability confidence and explicit unknown regions.
- Local map, coordinate-frame and localisation confidence.
- Dynamic obstacle observation and change detection.
- Quadruped body-state context: attitude, joint state and foot-contact observations.
- Evidence references and uncertainty for operator review.

## Safety boundaries

- A map or traversability score is not permission to move.
- A camera, depth sensor or LiDAR cannot certify structural integrity, air quality or absence of hazardous gas.
- Missing, stale, misaligned or conflicting geometry must remain UNKNOWN/CONFLICT.
- Physical movement requires independent low-level control, interlocks, emergency stop and human-authorised mission control.
- No chemical/substance classification, X-ray screening or enforcement task is part of Sentinel.

The Shared AI Core integration is a proposed profile only. Sensor drivers, calibration, coordinate transforms, mapping quality and field performance remain unvalidated.

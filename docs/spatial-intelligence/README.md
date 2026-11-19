# PUI89 Sentinel — All-Terrain Exploration & Inspection Robot: Spatial Intelligence integration profile

## Intended use
Optional geometry context for inspection positioning and scene documentation only.

## Planned tasks
- Scene layout and inspection-position context
- Terrain, obstacle and traversability evidence for supervised inspection
- Geometry evidence kept separate from non-spatial sensor and mission evidence
- Human-review workflow references

## Safety boundaries
- Geometry and spatial perception cannot determine chemical composition or certify atmospheric safety.
- Do not enter confined or potentially hazardous areas based on RGB, depth or LiDAR alone; follow site-authorised procedures and use calibrated instruments when required by the risk assessment.
- Inspection observations remain advisory and require human review.

The Spatial Intelligence Engine v0.1 was merged into the private Shared AI Core on 10 November 2026 ([PR #26](https://github.com/Pui89/PUI89-Shared-AI-Core/pull/26)). This profile documents intended integration only; no runtime import, live sensor integration or product validation is claimed. The Shared AI Core is private and requires maintainer access.

**Status:** profile documentation added; runtime adapter, real sensor integration, accuracy and field validation pending. No paid services or hardware purchase required.

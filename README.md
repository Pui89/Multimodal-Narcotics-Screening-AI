# PUI89 Sentinel — All-Terrain Exploration & Inspection Robot

**Product identity:** Four-legged AI quadruped robot for supervised exploration, environmental awareness and inspection.  
**Tagline:** Explore Anywhere.  
**Mission:** Help authorised operators explore and inspect selected indoor, industrial, infrastructure, logistics, outdoor and difficult-to-access environments; understand terrain and surroundings; observe assets and environmental conditions; and return traceable evidence for human review.  
**Portfolio distinction:** Sentinel is a four-legged quadruped. PUI89 AI NOMAD is a separate four-wheel mobile assistant. PUI89 AI HOME is a separate four-wheel indoor assistant.  
**Development status:** Stage 1 — concept and requirements reset. No physical Sentinel prototype, integrated sensors, validated locomotion, all-terrain capability or field performance is claimed.

![PUI89 Sentinel quadruped robot concept](docs/images/pui89-sentinel-quadruped-inspection-v3.svg)

*Concept illustration only; not evidence of a built or tested robot.*

## Product purpose

PUI89 Sentinel is a general-purpose, human-supervised quadruped exploration and inspection platform. It is intended to help an operator observe places and conditions that are difficult, repetitive or inconvenient to inspect on foot. The robot's AI should perceive the environment, estimate terrain and obstacles, monitor its own state, identify visible changes or anomalies, capture evidence and propose bounded next steps.

**Sentinel is not a narcotics-screening product.** Substance detection, chemical identification, X-ray screening, baggage screening and enforcement workflows are outside the current product scope. Historical material from the former project direction is explicitly separated in [the legacy migration register](docs/SENTINEL_SCOPE_MIGRATION.md).

## Target mission environments

- Industrial facilities, plant rooms, utilities and infrastructure.
- Warehouses, logistics yards, ports and authorised inspection areas.
- Outdoor paths, gravel, grass, soil, moderate slopes, steps and selected uneven terrain.
- Remote observation and supervised reconnaissance from safe, permitted locations.
- Emergency-site situational awareness from approved safe stand-off locations.
- Routine inspection patrols, condition snapshots and change detection.

These are target use cases, not validated deployments. “Explore Anywhere” is an engineering ambition, not a guarantee of unrestricted access. Deep water, cliffs, unstable structures, hazardous atmospheres, extreme slopes, fire, explosive zones and unknown environments are no-go until specifically engineered and validated.

## Core AI capabilities — proposed

1. **Vision intelligence:** image quality, object/asset detection and classification, tracking, segmentation, scene understanding and visible change/anomaly cues.
2. **Spatial intelligence:** RGB-D/depth and optional LiDAR geometry, obstacle/free-space estimation, terrain shape, slope/step/roughness cues and traversability confidence.
3. **Terrain and locomotion awareness:** quadruped body state, IMU, joint state, foot contact, gait phase, slip/stumble/fall-risk cues and safe-hold status.
4. **Mapping and localisation:** local mapping, localisation confidence, route context and recovery/retreat proposals; no claim of validated autonomous navigation.
5. **Multimodal awareness:** optional thermal, audio and mission-specific environmental sensor inputs, each with independent provenance, quality and uncertainty.
6. **Inspection intelligence:** operator-defined mission checklist, visible asset observations, change/anomaly comparison, event timeline and evidence capture.
7. **Task intelligence:** bounded mission decomposition, waypoint and inspection-step proposals, risk assessment and human escalation.
8. **Safety intelligence:** independent operating envelope, permission checks, fault monitoring, stop/safe-hold, emergency-stop interface and supervised recovery proposals.

All capabilities are proposed requirements until implemented and supported by appropriate software, simulation, bench or real-world evidence. AI models do not directly authorise actuator commands.

## Proposed system architecture

Sensors → input validation and provenance → perception → spatial/terrain world state → mission and inspection reasoning → independent safety supervisor → human-approved bounded action proposal → evidence and event report.

Reuse PUI89 Shared AI Core contracts: Observation, WorldState, ActionProposal and FailureReport, with timestamps, source provenance, quality, uncertainty, explicit UNKNOWN/CONFLICT states and safe-hold outcomes. Safety must remain independent of model confidence and language-model reasoning.

## Candidate hardware direction

| Area | Candidate | Status |
|---|---|---|
| Vision | RGB cameras; optional stereo/depth | Candidate |
| Spatial sensing | Depth camera; optional 360° LiDAR | Candidate |
| Body state | IMU, joint encoders, foot/contact sensing | Required design functions; hardware TBD |
| Environment | Optional thermal, audio or calibrated mission-specific sensors | Mission-specific; not selected |
| Compute | Local CPU-first edge compute; optional GPU/NPU | Candidate |
| Robotics | Quadruped state, gait, localisation, mapping and safety interfaces | Requirements only |

No manufacturer, part number, country of origin, supplier, price or component is confirmed. Hardware selection requires compatibility, provenance, non-Chinese-origin and cost review. No purchase is authorised.

## Safety and privacy

- Human defines the mission, area, permissions, operating limits and abort conditions.
- Stop or safe-hold on uncertain footing, obstacle clearance, localisation, sensor health, battery/thermal state, communications or safety-system status.
- Never enter a hazardous atmosphere or structure based only on RGB, depth or LiDAR.
- No weapon, pursuit, restraint, forced access, autonomous enforcement or person scoring.
- No facial recognition, biometric identification or covert/unrestricted surveillance.
- Preserve source, time, quality, calibration, uncertainty, software/model version and operator review.
- A model proposal cannot bypass independent safety controls or human approval.

## Development sequence

1. **Stage 1 — Requirements and software contracts:** mission profiles, operating envelope, hazards, sensor interfaces, evidence records and acceptance criteria.
2. **Stage 2 — Simulation:** reproducible quadruped/terrain scenarios; simulation is not physical validation.
3. **Stage 3 — Bench integration:** selected sensors and compute only after separate approval.
4. **Stage 4 — Controlled prototype:** locomotion, stability, foot contact, payload, endurance, thermal behaviour and emergency-stop tests.
5. **Stage 5 — Supervised field validation:** risk-assessed trials with defined terrain and environmental limits.
6. **Stage 6 — Release consideration:** independent safety, reliability, privacy, maintenance, procurement and regulatory review.

## Current evidence boundary

The current physical product is at **concept / requirements definition**. Existing repository code or historical screening workflow tests do not prove quadruped locomotion, perception accuracy, mapping, obstacle avoidance, sensor integration or field performance. Do not transfer former screening maturity scores or metrics to the new Sentinel mission. Establish a new evidence baseline.

## Key documents

- [Product brief](docs/PRODUCT_BRIEF.md)
- [Exploration and inspection system specification v0.1](docs/PUI89_SENTINEL_EXPLORATION_INSPECTION_SYSTEM_SPEC_V0.1.md)
- [Quadruped robot concept](docs/PUI89_SENTINEL_ROBOT_CONCEPT.md)
- [Validation matrix](docs/VALIDATION_MATRIX.md)
- [Legacy scope migration register](docs/SENTINEL_SCOPE_MIGRATION.md)
- [Security policy](SECURITY.md)

## Project links

- [English website](https://pui89.github.io/sentinel.html)
- [เว็บไซต์ภาษาไทย](https://pui89.github.io/sentinel-th.html)
- [PUI89 portfolio](https://pui89.github.io/)
- [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core)

**PUI89 | Intelligent Systems. Verifiable Decisions. Safer Outcomes.**

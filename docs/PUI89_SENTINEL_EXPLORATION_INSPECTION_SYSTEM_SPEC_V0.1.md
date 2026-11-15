# PUI89 Sentinel — Exploration & Inspection System Specification v0.1

**Product:** PUI89 Sentinel — All-Terrain Exploration & Inspection Robot  
**Form factor:** Four-legged AI quadruped  
**Design ambition:** Explore Anywhere  
**Stage:** 1 — concept and requirements definition  
**Status:** Requirements proposal only; no physical robot or validated capability is claimed.

## 1. Product objective

Develop a human-supervised quadruped platform that can perceive, understand and document selected environments and terrain. Sentinel is intended to extend an operator's reach for exploration and inspection while preserving human authority, evidence provenance, uncertainty and independent physical safety controls.

“Explore Anywhere” means designing for broad adaptability over time. It does not mean unrestricted operation or guaranteed traversal of every environment.

## 2. Mission profiles

- Industrial and infrastructure condition inspection.
- Warehouse, logistics-yard and port-area observation where authorised.
- Outdoor exploration on selected paths and terrain classes.
- Environmental observation and visible change detection.
- Supervised reconnaissance from safe, permitted locations.
- Repeatable patrol/checklist execution and evidence reporting.

Each mission must define area, purpose, operator, route limits, permitted sensors, privacy rules, environmental envelope, abort conditions and return/retreat plan.

## 3. Core intelligence

### 3.1 Vision Perception
Image quality, object/asset detection, classification, tracking, segmentation, scene understanding and visible change/anomaly cues.

### 3.2 Spatial Perception
Depth and point-cloud quality, geometry, free-space, obstacle clearance, terrain shape, slope/step/roughness cues and traversability confidence.

### 3.3 Quadruped State Intelligence
IMU, joint-state, gait-phase and foot-contact observations; body attitude; slip, stumble and fall-risk cues; safe-hold state. These require future sensors and controller interfaces.

### 3.4 Mapping and Localisation
Local map, pose estimate, coordinate frames, localisation confidence, map consistency and safe retreat context. GNSS-denied capability is a research objective, not a current claim.

### 3.5 Multimodal Environment Awareness
Optional thermal, audio and mission-specific environmental measurements. Every modality requires documented sensor principle, range, calibration, provenance and independent validation. RGB/depth/LiDAR cannot establish chemical composition, air quality or structural integrity.

### 3.6 Mission and Inspection Intelligence
Mission checklist, task decomposition, inspection-point proposals, visible asset observations, event detection, change comparison, evidence capture and post-mission report.

### 3.7 Safety and Recovery Intelligence
Independent operating limits, permissions, fault monitoring, stop/safe-hold, emergency-stop interface, human escalation and supervised recovery proposals.

## 4. Proposed system architecture

Sensor inputs → input validation and provenance → perception → spatial and terrain WorldState → quadruped state estimation → mission/inspection reasoning → independent safety supervisor → human-authorised bounded proposal → evidence and reporting.

Reuse Shared AI Core contracts:
- Observation
- WorldState
- ActionProposal
- FailureReport

Every observation should carry source, timestamp, quality, calibration where applicable, coordinate frame where relevant, uncertainty and explicit missing/invalid/conflict state.

## 5. Hardware interfaces — not selected

| Subsystem | Candidate interface | Key unknowns |
|---|---|---|
| Vision | RGB camera(s) | FOV, low-light, shutter, weather protection |
| Spatial | Depth/stereo camera; optional LiDAR | Range, accuracy, reflectivity, sunlight, calibration |
| Body state | IMU, joint encoders, foot/contact sensors | Joint topology, update rate, precision, durability |
| Compute | CPU-first edge computer; optional accelerator | RAM, power, thermal, latency, support lifecycle |
| Power | Battery, BMS, contactors, DC/DC | Runtime, peak current, charging and thermal limits |
| Environment | Optional thermal/audio/calibrated sensors | Mission need, operating range, calibration and safety |
| Operator interface | Local dashboard and emergency stop | Human factors, connectivity and override path |

No manufacturer, model, part number, country of manufacture, supplier, price or purchase is approved by this specification.

## 6. Operating envelope

Candidate terrain classes for future evaluation: indoor hard floors, paved paths, compacted gravel, grass, soil, moderate slopes, low steps and selected uneven ground.

Before use, define measurable limits for:
- slope and cross-slope;
- step height and gap width;
- terrain roughness and loose-surface depth;
- obstacle height and clearance;
- speed, payload and centre of gravity;
- water/dust ingress and ambient temperature;
- endurance, battery reserve and thermal state;
- localisation confidence and communications quality.

No-go until separately engineered and validated: deep water, cliffs, unstable structures, fire, explosive or hazardous atmospheres, extreme slopes, inaccessible gaps and unknown confined spaces.

## 7. Safety invariants

1. Human authorises mission, area, purpose and limits.
2. No physical movement until independent low-level control, emergency stop and safety interlocks are tested.
3. AI models and language models cannot directly command actuators or bypass the safety supervisor.
4. Uncertain footing, localisation, sensor health, communications or power state leads to stop/safe-hold.
5. Unknown and conflicting observations are preserved; the system must not force a confident answer.
6. No autonomous enforcement, pursuit, restraint, forced access or biometric identification.
7. Evidence includes source, time, quality, calibration, uncertainty and software/model version.
8. No claim of all-terrain performance without a defined and independently tested operating envelope.

## 8. Verification strategy

- Software: schemas, adapters, deterministic logic, negative tests and evidence integrity.
- Simulation: terrain, gait, contact, obstacles, localisation, sensor dropout and communication loss.
- Bench: actual sensors, calibration, compute, power, thermal, communications and E-stop.
- Physical prototype: bounded low-speed mobility, stability, slip, stumble, falls, endurance and recovery.
- Field: authorised, risk-assessed, supervised trials, one terrain/environment class at a time.

Simulation and software tests do not prove physical performance. Publish metrics only with test conditions, sample counts, ground truth and limitations.

## 9. Explicit exclusions

The former narcotics-screening mission is discontinued and is not part of Sentinel. No narcotics/substance screening, X-ray/baggage screening, chemical identification, enforcement, weapons, drone or aerial flight function is included.

## 10. Stage 1 exit criteria

- Approved mission profiles and no-go envelope.
- Hazard analysis and human authority model.
- Versioned sensor/robot-state interface requirements.
- Shared AI Core contract mapping.
- Testable software acceptance criteria and simulation scenario plan.
- Evidence ledger reset for the new quadruped mission.

No Stage 1 exit is claimed until each item has a review record.

# PUI89 Sentinel — All-Terrain Exploration & Inspection Robot

**A supervised four-legged quadruped for exploration, situational awareness and inspection evidence capture.**

[English project page](https://pui89.github.io/sentinel.html) · [ภาษาไทย](https://pui89.github.io/sentinel-th.html) · [PUI89 portfolio](https://pui89.github.io/)

![PUI89 Sentinel quadruped inspection robot concept](docs/images/pui89-sentinel-quadruped-inspection-v3.svg)

*Concept illustration only. It is not evidence of a built, integrated, tested or validated robot.*

## What this product is

PUI89 Sentinel is a **four-legged ground robot** intended for human-supervised inspection in authorised industrial, infrastructure, logistics and selected outdoor environments. Its mission is to help operators observe difficult-to-access areas and collect traceable evidence while the human operator retains authority.

**ผู้ใช้งาน:** เจ้าหน้าที่ตรวจสอบโรงงาน โครงสร้างพื้นฐาน คลังสินค้า และพื้นที่ที่ได้รับอนุญาต  
**ประโยชน์หลัก:** ช่วยสำรวจ สังเกตสภาพแวดล้อม และรวบรวมหลักฐานเพื่อให้เจ้าหน้าที่ตรวจสอบ โดยมีมนุษย์กำกับภารกิจ

## Product-specific functions

- Quadruped mobility and terrain perception are engineering priorities, not validated capabilities.
- Intended inspection evidence may combine authorised camera, audio, map, spatial and other sensor observations.
- Support operator-reviewed inspection notes, anomaly cues and evidence records.
- Treat uncertain, missing, stale or conflicting observations as unknown and request human review.
- Select payloads and sensors only after the first mission, site hazards and operating envelope are defined.

## What is not established or in scope

- No physical prototype, integrated sensor suite, validated gait, terrain traversal, field deployment or all-terrain performance is established.
- “All-terrain” is the product direction, not a guarantee of access to every surface or hazardous area.
- **Narcotics detection, X-ray screening, chemical identification and enforcement are outside current Sentinel scope.** Historical screening material is legacy work, not current product capability.
- RGB, depth or LiDAR observations alone cannot authorise entry into a hazardous atmosphere.

## Current development status

**Specified — quadruped product requirements are documented.** No physical robot or field validation is claimed.

**Next evidence gate:** select one supervised inspection mission; define its site, users, operating envelope, hazards, sensor requirements and measurable acceptance criteria before selecting hardware.

## Product documentation

- [Sentinel quadruped concept and scope](docs/PUI89_SENTINEL_ROBOT_CONCEPT.md)
- [All-terrain quadruped requirements](docs/SENTINEL_ALL_TERRAIN_INSPECTION_ROBOT_DOG_REQUIREMENTS_V0.2.md)
- [Historical scope migration register](docs/SENTINEL_SCOPE_MIGRATION.md)

## Shared PUI89 engineering

Cross-product architecture, evidence contracts, safety, privacy, security, recovery, device interaction and localization requirements are maintained in the [PUI89 Shared AI Core](https://github.com/Pui89/PUI89-Shared-AI-Core). Sentinel-specific mobility, inspection payloads and mission risks remain defined and validated separately.

Current maturity labels follow the [PUI89 Portfolio Alignment Register](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_PORTFOLIO_ALIGNMENT_REGISTER_2026-11-18.md) and [Evidence-Based Development Maturity Standard](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_DEVELOPMENT_STAGE_STANDARD.md).

## AI Model & Intelligence profile

**Candidate capability profile:** Object Detection, Image Segmentation, Object Tracking, SLAM, Sensor Fusion and Anomaly Detection for supervised quadruped inspection; Predictive Models for condition/risk trends; VLM/LLM for evidence-linked, human-reviewed inspection summaries. No autonomous gait or actuator authority is implied.

All nine shared capability families and their definitions, evaluation requirements, provenance/uncertainty rules and safety boundaries are maintained in the [PUI89 Shared AI Core Model Intelligence Framework](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/architecture/PUI89_MODEL_INTELLIGENCE_FRAMEWORK_V1.0.md). This product profile is a **candidate engineering allocation**, not evidence of model installation, runtime integration, benchmark results, field validation or certified performance. Select and enable each capability only after product-specific requirements, approved data, compute/energy budgets and verification gates are satisfied.

## Robot Capabilities & Functional Capacity

**Scope boundary:** PUI89 Sentinel is currently defined as a human-supervised, four-legged quadruped for exploration, situational awareness and inspection evidence capture in authorised environments. It is not the historical narcotics/X-ray screening concept; narcotics detection, X-ray screening, chemical identification and enforcement are explicitly outside the current product scope.

### 1. Physical capacity
- Four-legged quadruped ground robot; physical prototype and integrated hardware are not established.
- Define dimensions, complete mass, payload, leg reach, foot geometry, centre of gravity, structural limits and recovery/handling points after the first inspection mission is selected.
- Payload and sensor mounting capacity: **TBD**; no carrying rating is claimed.

### 2. Mobility capacity
- Quadruped locomotion and traversal of selected terrain are engineering objectives, not validated capabilities.
- Define gait modes, speed, slope, step/obstacle height, ground clearance, surface friction, stability margins, endurance and recovery behaviour for the chosen mission.
- Do not interpret “all-terrain” as access to every surface or hazardous area.
- **Validated terrain envelope and mobility performance:** not established.

### 3. Perception capacity
- Candidate perception includes authorised camera, audio, spatial/depth, mapping and selected environmental observations appropriate to the inspection mission.
- Support scene understanding, obstacle/terrain cues, anomaly observations, spatial context and traceable inspection evidence.
- Fuse observations with timestamps, source provenance, sensor-health status, confidence and uncertainty.
- Treat missing, stale, conflicting or out-of-distribution observations as unknown and request operator review.
- RGB, depth or LiDAR observations alone cannot establish that a hazardous atmosphere is safe to enter.
- Detection ranges, coverage, localisation accuracy and environmental limits remain TBD.

### 4. Computing capacity
- Define onboard compute, memory, storage, latency and thermal budgets after mission and sensor selection.
- Prefer local processing for inspection data; document model provenance, version, resource use and failure behaviour.
- **Processor, RAM, storage and measured inference performance:** TBD.

### 5. Power capacity
- Define battery chemistry, usable energy, peak leg-actuator power, mission runtime, charging, thermal limits and safe low-battery recovery.
- **Battery capacity, runtime and charging time:** TBD.

### 6. Communication capacity
- Define operator control/telemetry link, range, latency, local data storage, approved remote access and loss-of-link behaviour for the selected site.
- The robot must enter a mission-appropriate safe state on communication loss; no unapproved cloud or remote access is assumed.
- **Protocols, range and link reliability:** TBD.

### 7. Safety capacity
- Require supervised missions, pre-mission site/hazard review, emergency stop, safe gait/actuator state, fall detection/recovery strategy and manual recovery procedures before field trials.
- Do not enter a hazardous atmosphere based solely on robot perception; require appropriate certified instruments and site procedures.
- No autonomous enforcement, pursuit, confrontation or unsupervised entry into dangerous areas is claimed.

### 8. Maintenance capacity
- Plan inspection and replacement for legs, joints, actuators, feet, fasteners, batteries, connectors and sensor mounts.
- Include actuator diagnostics, joint/IMU calibration, sensor cleaning, mechanical wear checks and traceable maintenance history.
- **Service intervals and validated repair procedures:** TBD.

### 9. Operating limits
- Current status is requirements/specification; no physical prototype, integrated sensor suite, validated gait, terrain traversal or field deployment is established.
- Actual payload, terrain, slope, speed, endurance, weather resistance and sensor performance remain TBD.
- Narcotics detection, X-ray screening, chemical identification and enforcement are outside the current Sentinel scope.

**Capacity evidence status:** Quadruped design direction documented; all physical and operational capacities remain TBD / not validated until supported by test evidence.


## Physical & Multimodal Sensor Privacy

PUI89 adopts the [Physical & Multimodal Sensor Privacy Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/privacy/PUI89_PHYSICAL_MULTIMODAL_SENSOR_PRIVACY_STANDARD_V1.0.md) as a shared engineering requirement. Every installed inspection camera requires a manual physical cover; every microphone requires a hardware disconnect. Spatial scans, maps and inspection evidence are local by default. Disabling required perception restricts or stops the supervised mission.

**Evidence status:** requirements/specification only. No product-level hardware implementation or verification is claimed by this README section.


## Long-Life Battery & Energy Intelligence

PUI89 adopts the [Long-Life Battery & Energy Intelligence Standard v1.0](https://github.com/Pui89/PUI89-Shared-AI-Core/blob/main/docs/energy/PUI89_LONG_LIFE_BATTERY_ENERGY_INTELLIGENCE_STANDARD_V1.0.md) as a shared engineering requirement. Prioritise locomotion, perception, mapping, communication and inspection-payload efficiency. Validate mission runtime across terrain and payload, including a safe stop/return reserve.

Battery runtime, chemistry, capacity, cycle life, charging performance and safety compliance remain **TBD until designed and evidenced**. No unverified runtime or battery-life claim is made. The design must include an energy budget, independent BMS protections, thermal/electrical safety, service strategy and representative runtime validation.

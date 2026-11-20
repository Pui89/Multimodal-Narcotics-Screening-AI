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

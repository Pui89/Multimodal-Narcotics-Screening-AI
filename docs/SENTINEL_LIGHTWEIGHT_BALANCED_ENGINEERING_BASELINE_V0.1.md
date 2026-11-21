# PUI89 Sentinel — Lightweight-to-Balanced Engineering Baseline v0.1

**Status:** Preliminary engineering direction approved; requirements and analysis only  
**Date:** 2026-11-21  
**Product:** Human-supervised four-legged quadruped for exploration and inspection  
**Procurement / fabrication / deployment:** Not authorised

## 1. Approved design direction

Develop Sentinel as a **lightweight-to-balanced all-terrain inspection and exploration quadruped**. Prioritise strong, agile and controlled walking, stability, fall-risk mitigation, useful operating endurance, maintainability and cost discipline. Do not pursue minimum mass at the expense of structural integrity, stability, thermal margin or service life.

The phrase *all-terrain* remains a development direction. The eventual operating envelope must identify specific tested surface classes, slopes, obstacles, weather limits and no-go conditions.

## 2. Preliminary mass target

| Parameter | Preliminary baseline | Status |
|---|---:|---|
| Complete robot target mass | **18–22 kg** | Approved direction for engineering study; not measured or validated |
| Payload capacity | TBD | Must be derived from mission and stability/actuator analysis |
| External mission payload | Excluded from target mass unless explicitly defined in the future mass budget | Definition to be confirmed at detailed design |
| Battery, baseline sensors, onboard compute and protective covers | Include in complete-robot mass accounting | Engineering accounting rule |
| Dimensions, height, footprint and leg reach | TBD | Do not freeze before mission definition and CAD/layout study |

The 18–22 kg range is a target for the complete baseline robot, including its battery, baseline sensors, onboard computing and protective covers. Any mission payload must be separately declared in the mass budget. The final mass may change if calculations show that safety, durability, stability or useful endurance cannot be met within this range. No physical prototype mass is claimed.

## 3. Design priorities

1. Stable, controlled quadruped locomotion with managed centre of mass.
2. Agile movement and speed appropriate to terrain, payload and risk.
3. Fall-risk mitigation, safe stop and a supervised recovery strategy.
4. Structural strength and fatigue life with a practical mass budget.
5. Efficient actuators and transmissions sized from joint-load calculations.
6. Battery and power system sized from representative mission duty cycles, peak loads and safe reserve.
7. Thermal management for actuators, motor drivers, battery and compute.
8. Replaceable leg modules, feet, actuators, battery, sensors and serviceable connectors.
9. Repairability and modular interfaces; avoid unnecessary custom parts.
10. Traceable component provenance and supply-chain integrity under PUI89 policy.

## 4. Engineering work required before dimensions or hardware are frozen

- Select one supervised inspection mission and define its environment, duration, speed, obstacle and slope requirements.
- Build a mass budget by subsystem: frame, four legs, actuators/transmissions, feet, battery/BMS, compute, sensors, wiring, covers and payload.
- Calculate joint torque, speed, peak and continuous duty cycle, impact loads and thermal dissipation.
- Assess frame strength, fatigue, fasteners, joint bearings, foot contact and repair access.
- Establish centre-of-gravity and stability margins for unloaded and representative payload configurations.
- Size battery usable energy, peak power, thermal limits and safe return/stop reserve against a measured or modelled duty cycle.
- Define dimensions from access width, obstacle geometry, stance, leg reach, stability and transport/maintenance constraints.
- Compare costed design alternatives using traceable BOMs and written supplier quotations. No budget is established by this document.

## 5. Verification gates

| Gate | Required evidence |
|---|---|
| G1 — Mission & operating envelope | Named use case, site assumptions, hazards, surfaces, slopes, obstacles, duty cycle and measurable acceptance criteria |
| G2 — Mass & packaging | Subsystem mass budget, CAD/layout, centre-of-gravity estimate, access and serviceability review |
| G3 — Mechanical & actuator design | Load cases, torque/speed/duty calculations, structural and fatigue analysis, joint/foot design |
| G4 — Power & thermal | Battery energy/power budget, BMS protections, thermal analysis and safe reserve |
| G5 — Simulation & bench | Gait/stability simulation; actuator, power, thermal, sensing and emergency-stop bench evidence |
| G6 — Controlled physical testing | Incremental indoor and selected-terrain tests with measured stability, speed, payload, endurance, recovery and failures |
| G7 — Supervised field trial | Independent safety review, site/operator approval and evidence against the declared operating envelope |

Passing one gate does not imply passing later gates. Simulation is not physical validation; one tested surface or payload does not establish unrestricted all-terrain capability.

## 6. Non-negotiable design boundaries

- No claim of validated speed, payload, runtime, slope, obstacle height, fall resistance, ingress protection or service life without test evidence.
- No autonomous enforcement, pursuit or unsupervised entry into hazardous areas.
- Loss of localisation, unsafe footing, critical sensor conflict, communication failure or unknown hazard must trigger a mission-appropriate safe response and operator escalation.
- RGB, depth and LiDAR do not certify safe air or replace calibrated atmosphere instruments and site procedures.
- No component purchase, fabrication or field deployment is authorised by this baseline.
- Verify manufacturer, model/part number, country of manufacture, origin evidence, supplier ownership/control, firmware/software provenance and replaceability before approval. Unknown or unverifiable provenance is a blocker under PUI89 supply-chain policy.

## 7. Decision record

The user approved the lightweight-to-balanced inspection and exploration direction and the **18–22 kg preliminary complete-robot target** on 2026-11-21. This is a design-study baseline only. Detailed dimensions, payload, actuator architecture, battery, runtime, cost and operating envelope remain open engineering decisions.

## 8. Relationship to existing requirements

This document supplements, and does not replace, the [All-Terrain Inspection Robot Engineering Requirements v0.2](SENTINEL_ALL_TERRAIN_INSPECTION_ROBOT_DOG_REQUIREMENTS_V0.2.md), [Complete System Blueprint](COMPLETE_SYSTEM_BLUEPRINT.md) and [Validation Matrix](VALIDATION_MATRIX.md). Product identity remains a four-legged quadruped, distinct from the four-wheel PUI89 AI NOMAD.

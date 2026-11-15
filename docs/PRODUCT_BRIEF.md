# Product brief — PUI89 Sentinel All-Terrain Inspection Robot Dog

**Product identity:** Four-legged quadruped inspection robot dog.  
**Mission:** Supervised inspection, situational awareness and evidence capture in authorised industrial, infrastructure, logistics and selected outdoor environments.  
**Relationship to NOMAD:** Sentinel uses articulated legs; PUI89 AI NOMAD is a separate four-wheel mobile assistant.  
**Development status:** Concept and engineering requirements. No physical Sentinel prototype, sensor integration, terrain capability or field performance is claimed.

## Product problem

Operators need a safer, more repeatable way to observe assets and environmental conditions in locations where a supervised mobile inspection platform may be useful. Sentinel is intended to collect traceable visual and spatial observations, assess traversability, document visible changes and provide evidence for a human operator. It is not an enforcement system or a substitute for certified safety instruments.

## Intended operating contexts

- Industrial facilities, plant rooms and infrastructure inspection.
- Warehouses, logistics yards, ports and authorised cargo areas.
- Selected outdoor routes and uneven terrain, only within a validated operating envelope.
- Disaster-site reconnaissance from safe, authorised locations.
- Routine inspection patrols and documented condition monitoring.

These are target use cases, not validated deployments. Each site requires permission, risk assessment, environmental limits and task-specific verification.

## Core product capabilities — proposed

1. **Perception:** image quality checks, object/asset observation, detection, classification, tracking, segmentation, depth/spatial estimation and visible change/anomaly cues.
2. **Terrain intelligence:** obstacle and free-space estimation, slope/step/roughness cues, traversability confidence and no-go-zone recognition.
3. **Robot state:** localisation confidence, motion state, joint/foot-contact observations, slip/stumble/fall-risk cues and sensor-health status.
4. **Inspection workflow:** operator-defined checklist, waypoint/route proposals, evidence capture, timestamps, provenance and structured reports.
5. **Action and response:** bounded task planning, operator notification, safe stop/hold, retreat or recovery proposals.
6. **Safety and control:** independent operating limits, permission checks, emergency-stop provisions, fault handling and human approval gates.

All capabilities are proposed until implemented and validated. Model outputs are observations or bounded proposals, not direct authority to actuate hardware.

## Mobility requirements — proposed

Sentinel is a quadruped with four articulated legs, not a wheeled base. Candidate engineering work includes gait planning, foot placement, state estimation, balance control, slip detection, payload and power budgeting, safe hold and supervised recovery. “All-terrain” is an engineering ambition, not a guarantee of unrestricted movement.

Cliffs, deep water, unstable structures, hazardous atmospheres, inaccessible gaps, extreme slopes and any environment outside the validated operating envelope are no-go conditions. RGB, depth and LiDAR do not certify breathable air or detect every hazardous gas. Entry into a confined or potentially hazardous area requires site-authorised procedures and suitable calibrated instruments where the risk assessment requires them.

## Sensor and compute direction

Candidate components may include RGB cameras, depth sensing, IMU, joint encoders, foot-contact sensing, optional LiDAR, edge AI compute, battery management and environmental protection. Final selection depends on a documented mission, verified compatibility, origin/licence evidence, power and thermal budgets, safety assessment and supplier validation. No component purchase is authorised by this brief.

## Evidence and validation gates

- **Gate 1 — requirements:** define mission, operating envelope, hazards, operator workflow and measurable acceptance criteria.
- **Gate 2 — software:** implement schemas, perception interfaces, uncertainty, provenance, reports and deterministic tests.
- **Gate 3 — simulation:** evaluate locomotion and inspection scenarios in a reproducible simulator; simulation is not physical validation.
- **Gate 4 — bench prototype:** validate sensors, compute, power, communications and emergency-stop interfaces on a controlled bench.
- **Gate 5 — supervised physical trials:** conduct risk-assessed trials in bounded environments with human oversight and recorded failure cases.
- **Gate 6 — release readiness:** independent safety, reliability, privacy, maintainability and procurement review.

Report software tests, simulated results, bench tests and physical trials separately. Do not publish performance metrics without reproducible evidence, dataset/scenario definitions and limitations.

## Legacy scope boundary

Older repository files may still contain the former “Multimodal Narcotics Screening AI” name, screening workflows, chemical-sensor references, or screening-specific code and artwork. These are historical software artifacts from an earlier project direction; they are not the current Sentinel product definition, do not establish chemical-identification capability, and must not be presented as Sentinel features. See [Sentinel scope migration and legacy artifact register](SENTINEL_SCOPE_MIGRATION.md). Existing history is retained; this scope correction does not authorise bulk deletion.

## Cost and procurement

Any prototype cost range is a preliminary, high-uncertainty planning allowance, not a verified bill of materials or supplier quote. Commercial/custom quadruped platform, actuators, locomotion control, battery/power, perception sensors, edge compute and controlled integration must be separately scoped. Thermal or calibrated atmosphere instruments are mission-specific options. No purchase or supplier commitment is authorised.

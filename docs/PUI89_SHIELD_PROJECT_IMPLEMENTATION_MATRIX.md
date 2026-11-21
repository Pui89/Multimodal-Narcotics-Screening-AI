# PUI89 SHIELD Project Implementation Matrix

**Status legend:** `POLICY_DEFINED` means requirements are documented; `SOFTWARE_REFERENCE` means dependency-free reference logic and tests exist on this development branch; `NOT_CREATED` means the project repository is not present in the connected Pui89 account. None of these statuses establishes physical validation.

## Shared requirements for all projects

- Reuse `WorldState`, `Observation`, `ActionProposal`, and `FailureReport` from the PUI89 Shared AI Core where already available.
- Preserve evidence provenance, timestamps, uncertainty, conflicting/missing input and calibration status.
- Use SHIELD warning states: `NORMAL`, `ADVISORY`, `WARNING`, `CRITICAL`, `EMERGENCY`, `UNKNOWN_DEGRADED`.
- Require safety gates and human review for consequential physical-action proposals.
- Keep AI outputs as proposals; no direct actuator command is introduced by the reference policy.
- Define project-specific safe states, operating envelopes, hazard thresholds and emergency procedures.
- Run unit, regression, security, simulation and benchmark checks; retain test configuration and evidence.
- Physical water/fire/battery/impact/functional safety and cybersecurity claims require suitable independent evidence.

## Project-by-project hazard and response matrix

| Project | Principal hazard focus | Safe-state design questions (must be answered and tested per project) | Current repository status |
|---|---|---|---|
| 01 Coconut Harvest AI | Worker/animal proximity, falling fruit, cutter and arm pinch/jam, dropped loads, tree/terrain stability, rain/moisture, battery and motor heat | Inhibit cutting when the safety envelope is uncertain; prevent uncontrolled arm/load motion; require local emergency stop and human recovery | Existing repository; SHIELD scope defined |
| 02 PUI89 Sentinel | Quadruped stability, foot-contact/slip/stumble, terrain traversability, falls, sensor calibration, environmental exposure, communications loss | Define terrain limits, safe hold, supervised recovery and independent emergency-stop behaviour; do not infer mobility from simulation alone | Existing repository; SHIELD scope defined |
| 03 PUI89 AI HOME | Smoke/heat/fire, water leaks, electrical anomalies, falls, pinch points, privacy, network loss and safe charging | Keep certified alarms primary; notify authorised users; use a tested stationary/parked safe state and preserve privacy | Existing repository; SHIELD scope defined |
| 04 PUI89 AI NOMAD | Wheeled stability, obstacle/curb clearance, wet-ground traction, payload limits, weather exposure, privacy and human interaction | Define terrain and payload limits, safe stop, manual handling and human override before mobility tests | Existing repository; SHIELD scope defined |
| 05 PUI89 AI Global SUV | Pedestrians/cyclists, collision, braking/steering faults, tire and stability faults, road/weather conditions, battery thermal events, sensor/GPS spoofing and driver override | Keep AI advisory; maintain driver control and independent vehicle safeguards; no autonomous road operation before formal validation | Existing repository; SHIELD scope defined |
| 06 PUI89 AI Step-Through Scooter | Rider falls, lean/balance dynamics, traction, braking, road users, blind spots, battery/thermal events, sensor faults and rider override | Prioritise rider stability; no unvalidated steering/braking/torque commands; define rider override and emergency behaviour | Existing repository; SHIELD scope defined |

## Minimum validation layers

1. **Contract/unit tests:** schemas, missing/stale/conflicting inputs, warning-state precedence, evidence references and human-approval flags.
2. **Software integration tests:** sensor adapters, stale-message rejection, logging, privacy and permission boundaries.
3. **Simulation:** project-specific hazard scenarios with fixed seeds, model/version capture, expected outcomes and repeatable metrics.
4. **Component bench tests:** only when suitable equipment and safe facilities exist; document calibration and test limits.
5. **Assembled-system / field validation:** separate approval, hazard analysis, competent supervision and appropriate independent assessment.

## Shared benchmark record

For every scenario, record: scenario ID, project, hazard, initial state, injected fault, expected warning, expected safe-state proposal, actual result, false alarm/missed hazard, latency, evidence references, software/configuration version, random seed (if simulated), limitations and reviewer.

Do not combine simulation success with physical validation. Do not invent thresholds. Thresholds must come from the project hazard analysis, component specifications and appropriate standards.

## Next implementation actions

- Keep the common warning policy and contract tests in sync across the existing repositories until a separately governed shared-core package is established.
- Add project-specific scenario tests before enabling any physical response.
- Review existing repository workflows and security checks; avoid duplicate paid scans or new services.
- Create the Car and Motorcycle repositories only when repository creation is explicitly available/authorized; apply this standard from their first commit.

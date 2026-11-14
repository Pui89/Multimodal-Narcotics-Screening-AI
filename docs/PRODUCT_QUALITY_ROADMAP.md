# PUI89 Sentinel — Product Quality Roadmap

**Product stage:** Concept and requirements definition.  
**Evidence boundary:** No physical prototype, integrated sensor stack or validated field capability is claimed.

## Release gates

1. **Mission and operating envelope:** define intended inspection tasks, permitted environments, payload, terrain classes, no-go conditions and operator responsibilities.
2. **Requirements and hazards:** document measurable system requirements, hazard analysis, emergency-stop architecture, human exclusion zones and safe recovery behaviour.
3. **Simulation and scenarios:** build repeatable gait, terrain, obstacle, localisation, sensor-fault and communications-loss scenarios. Label all simulation results as simulation.
4. **Hardware and sourcing:** compare candidate components by exact manufacturer, model/part number, country of manufacture/origin evidence, compatibility, supplier, dated price, lead time and warranty. No procurement without approval.
5. **Perception evaluation:** use permissioned, representative data with traceable labels. Report per-class precision/recall, false positives/negatives, calibration, uncertainty and abstention.
6. **Mobility validation:** measure stability, payload, gait, step/threshold capability, stopping, recovery, endurance and thermal behaviour within a declared operating envelope.
7. **Safety and human oversight:** verify independent emergency stop, fail-closed controls, operator approval, privacy, access control and audit trail.
8. **Release evidence:** publish only reproducible results for the exact hardware/software configuration, including sample counts, test conditions, limitations and unresolved risks.

## Current priorities

- Complete the system blueprint and validation matrix.
- Define the first narrow inspection mission and its measurable acceptance criteria.
- Establish simulation-only baselines before hardware procurement.
- Keep concept, implementation, simulation, bench-test and field-validation evidence separate.

## Quality rule

A passing software test or simulation is not proof of real-world safety or performance. Every public capability statement must point to evidence appropriate to the claim.

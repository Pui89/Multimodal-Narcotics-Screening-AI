# Engineering Requirements and Evidence Matrix — PUI89 Sentinel Quadruped Inspection Robot

**Last reviewed:** 2026-11-16  
**Scope:** Requirements and evidence tracking for the proposed four-legged inspection robot. This matrix does not establish physical implementation or test completion.

## Evidence and status rules

- **Verified** means a named test completed successfully for the exact configuration and scope stated, with traceable evidence.
- **Failed** means a test ran and did not meet its predeclared acceptance criterion.
- **Not run** means no test evidence is available.
- **Not measured** means the requirement has not yet been quantified or measured.
- Simulation, synthetic fixtures, design review and software tests do not establish physical robot performance.
- Do not use PASS without a dated test record, configuration, method, measured result and reviewer.

## Requirements and evidence matrix

| ID | Requirement | Verification method / evidence required | Acceptance basis | Current evidence | Status | Next action |
|---|---|---|---|---|---|---|
| SYS-01 | Product identity is a four-legged quadruped inspection robot | Review approved product definition and repository/site identity | All project materials consistently distinguish Sentinel from wheeled NOMAD and narcotics-screening work | README and requirements define quadruped identity; conflicting legacy documents are being corrected | In review | Verify all linked project and portfolio references |
| MIS-01 | Mission and operating envelope are defined | Approved mission scenarios, site constraints, prohibited-use list and measurable limits | Owner and safety reviewer approve a bounded intended-use definition | Target use cases are documented; quantitative envelope not baselined | Not measured | Define first customer task, environment and measurable limits |
| MEC-01 | Mass, dimensions, payload and centre-of-mass limits are defined | CAD, mass properties and measured prototype configuration | Values meet approved mission and stability requirements | No physical platform or verified mass properties documented | Not measured | Establish target dimensions, mass and payload |
| ACT-01 | Actuators meet joint torque, speed, duty and thermal requirements | Datasheets, calculations, bench tests under representative loads | Each joint remains within approved limits with margin | No actuator selected or tested | Not run | Derive joint loads and shortlist verifiable parts |
| LOC-01 | Controlled locomotion is stable within a defined envelope | Instrumented indoor tests across declared speeds, turns, payloads and surfaces | Predeclared stability, tracking, stop-distance and fault criteria | No integrated locomotion platform or measured gait | Not run | Define simulation and bench acceptance criteria |
| PWR-01 | Power system supports peak load, runtime and safe shutdown | Power budget, BMS evidence, load/thermal tests and fault injection | Voltage/current/temperature remain within component limits; safe shutdown works | No battery or power architecture selected | Not run | Build a measured subsystem power budget |
| PER-01 | Perception detects relevant obstacles and inspection targets | Licensed representative dataset and controlled sensor tests; per-class metrics and failure review | Task-specific thresholds established before testing | Sensors and models are candidates only; no representative robot sensor evaluation | Not run | Define first inspection task and lawful data plan |
| NAV-01 | Localisation, mapping and retreat behavior meet mission needs | Repeatable route tests, localisation error and failure injection | Predeclared accuracy, availability and safe-stop criteria | No integrated robot navigation test | Not run | Specify environment and localisation requirements |
| SAF-01 | Independent emergency stop and safe-state behavior work | Hardware-in-loop and physical E-stop tests, watchdog and power/communications fault injection | Stop path independent of AI; measured stop behavior meets risk-based limits | Safety principles documented; no hardware implementation verified | Not run | Design and review safety architecture before procurement |
| ENV-01 | Environmental limits are defined and verified | Ingress, temperature, vibration and surface-specific tests as applicable | Test limits match declared operating envelope | No environmental test evidence | Not run | Define only mission-relevant environmental requirements |
| CNT-01 | Container/confined-area operation is safe where included | Mock-up tests for clearance, threshold, localisation, atmosphere procedure and retreat | Site-specific risk assessment and measurable entry/exit criteria | Candidate use case only; no physical test | Not run | Keep excluded until geometry and risk controls are specified |
| DAT-01 | Evidence has provenance, timestamp, quality and privacy controls | Schema tests, audit-log inspection and data-handling review | Traceable records; minimised and access-controlled data | Architecture requirement documented; implementation not verified | Not run | Define evidence schema and retention policy |
| SRC-01 | Hardware origin and compatibility are verified | Manufacturer datasheet, exact part number, country-of-manufacture evidence, supplier and dated quote | Each selected component has traceable source and compatibility review | No hardware selected or purchased | Not run | Prepare non-Chinese-origin sourcing shortlist with evidence |
| COST-01 | Prototype budget is defensible | Engineering baseline, verified BOM and current written supplier quotations | Reconciled total with taxes, freight, lead time, warranty and exclusions | No verified BOM or supplier quotation; public estimates withdrawn | Not established | Define mass/payload and subsystem requirements before costing |
| REL-01 | Maintenance and reliability targets are measurable | FMEA, service plan, endurance and fault-recovery tests | Risk-based acceptance criteria and traceable service intervals | No prototype or endurance evidence | Not run | Conduct preliminary hazard/FMEA review |

## Current release decision

**Physical prototype procurement: NOT AUTHORISED by this matrix.**

The project remains at concept and engineering-requirements definition. The next gate is a bounded mission definition and quantified mechanical, actuator, power, sensing and safety requirements. Do not publish cost ranges or capability claims until supporting evidence is reviewed.

## Evidence record template

For each test, record: requirement ID; test ID; date; operator/reviewer; hardware and firmware configuration; software/model version; procedure; environment; sample count or repetitions; raw evidence location; measured result; acceptance criterion; pass/fail/not-run status; deviations; corrective action; and approval.

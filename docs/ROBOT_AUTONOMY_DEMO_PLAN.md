# Multimodal Narcotics Screening AI — Robot Demonstration Plan

> **Status:** Proposed simulation/prototype plan. This document is not evidence of a physically built or field-validated robot. It does not claim chemical identification or autonomous law-enforcement decisions.

## Mission: assist screening staff, not replace their authority

The robot's purpose is to reduce repetitive handling and help staff inspect more consistently. It can autonomously collect permitted observations, check sensor quality, flag unusual items for review, and create an auditable report. A trained, authorized officer remains responsible for searches, escalation, and consequential decisions.

## Concept platform

- Mobile base with obstacle sensors and emergency stop.
- RGB/depth camera for visible object geometry and scene context.
- Optional LiDAR for navigation and mapping.
- Docking/inspection station with access to authorized X-ray/CT images where such equipment and data are legally available.
- On-device computer running the local screening application.
- Operator console showing observations, uncertainty, sensor status, and review history.

These are proposed components, not a claim that they are currently connected or operational.

## Demonstration workflow

1. **Receive task:** operator authorizes an inspection zone and defines boundaries.
2. **Navigate safely:** robot moves only in a controlled test area; stop if localization, obstacle sensing, or communications become unreliable.
3. **Observe:** capture a permitted image/scan and attach timestamps and sensor-health metadata.
4. **Check quality:** reject blurry, missing, stale, or mismatched inputs.
5. **Analyze supported evidence:** run only models that have actually been installed and evaluated. RGB imagery alone cannot see through closed luggage or establish chemical identity.
6. **Triage:** return REVIEW_REQUIRED, NO_FLAG_IN_TEST, or UNKNOWN; do not treat a low score as proof of safety.
7. **Human decision:** authorized staff inspect the evidence and decide what action is lawful and appropriate.
8. **Log:** save the input identifier, model/version, output, uncertainty, and reviewer outcome without exposing sensitive personal data unnecessarily.

## What it can do instead of a person — in a bounded task

| Repetitive task | Robot contribution | Human remains responsible for |
|---|---|---|
| Moving between inspection points | Controlled navigation in a mapped, safe area | Defining authorized area and responding to incidents |
| Capturing repeated observations | Timestamped camera/depth capture | Ensuring lawful, appropriate inspection |
| Flagging unusual visual patterns | Prioritizing cases for review | Interpreting evidence and deciding next steps |
| Recording inspection metadata | Automatic structured logs | Confirming outcomes and handling exceptions |
| Rechecking sensor/input quality | Automated quality gates | Resolving ambiguous or failed checks |

## Free, local-first prototype milestones

- **M0 — Offline replay:** process prerecorded, lawfully usable sample data; no robot hardware required.
- **M1 — Mock robot loop:** use a simulated pose and obstacle map to demonstrate observe → analyze → stop/continue → report.
- **M2 — Evaluation:** measure processing time, false-positive rate, missed-case rate, UNKNOWN rate, and sensor-failure handling on a documented test set.
- **M3 — Hardware bench test:** only after simulation passes, test a mobile base in a controlled area with an emergency stop.
- **M4 — Authorized pilot:** only with relevant permissions, validated equipment, privacy review, and independent safety testing.

## Demo acceptance criteria

- Unsafe or invalid sensor input produces a safe stop or UNKNOWN.
- Missing modalities are reported, not silently fabricated.
- A model's score is labelled as a model output, not a probability of guilt or proof of substance identity.
- The operator can stop the robot immediately.
- Every test result records software/model version and whether data is synthetic, recorded, or live.
- Performance numbers are published only after reproducible tests have been run.

## Current vs proposed

**Current:** this repository documents an AI screening application/prototype and local evaluation workflow. Check the code and test outputs to determine which components are executable in the current checkout.

**Proposed:** physical mobile navigation, live sensor integration, authorized X-ray/CT integration, and field deployment are future engineering tasks unless separately demonstrated and documented with test evidence.

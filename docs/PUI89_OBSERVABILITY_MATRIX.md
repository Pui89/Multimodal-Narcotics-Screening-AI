# PUI89 Observability Matrix — software to hardware

**Purpose:** define a consistent, evidence-led way to observe the screening project from code to model and (only when connected) physical hardware. This document is a monitoring plan, not evidence that the system or robot has been validated.

## Observation layers

| Layer | What to record | Example signals | Current evidence boundary |
|---|---|---|---|
| Software | Build, imports, unit tests, exceptions, dependency versions | commit SHA, Python version, test counts, error IDs, duration | CI can measure code paths it actually runs; syntax checks are not full validation |
| Hardware and sensors | Device connection, sensor health, calibration, timestamps, temperature/power where available, emergency-stop state | connected/disconnected, stale frames, calibration ID, sensor fault | **NOT_CONNECTED / NOT_RUN** until real devices and an approved test rig provide evidence; never infer hardware health from software tests |
| System | CPU/RAM/disk, process health, queue depth, network status if applicable | resource snapshots, timeouts, restart count | Measure only on the environment where the system runs; hosted CI is not the user's laptop or a deployed robot |
| AI model | Model identifier/version/hash, licence approval, runtime, input quality, uncertainty, out-of-distribution and abstention behavior | model loaded/not loaded, latency, missing modality, confidence/uncertainty, UNKNOWN | Model not loaded or benchmark not run must remain **NOT_RUN**; synthetic tests do not establish detection accuracy |
| Workflow step | Ordered stages, input/output IDs, duration, outcome, failure reason, human-review handoff | validate → observe → assess → propose → review → close | Each stage needs a timestamp and result; no enforcement action is automated |
| Safety and review | Safe-hold decision, operator takeover, review reference, audit completeness | stop reason, reviewer reference, review timestamp | Software policy tests are not a certified physical safety controller |

## Status vocabulary

- `PASS` / `FAIL`: a named check actually ran and has an evidence reference and observation timestamp.
- `NOT_RUN`: a check is defined but has not been run.
- `NOT_CONNECTED`: required hardware or external component is not connected.
- `UNKNOWN`: the state cannot be determined reliably. Unknown must not be silently converted to pass.
- `BLOCKED`: prerequisites, lawful data access, licence review, calibration or authorised review are missing.

## Evidence record minimum

Each observed event should include: UTC timestamp, project and commit, layer, component/check ID, status, duration if measured, a concise failure code, evidence/artifact reference, and environment/model/sensor version where applicable. Avoid recording names, faces, case details, raw video or other sensitive data in ordinary CI logs. Store sensitive evidence only in an authorised, access-controlled system with a retention policy.

## Recommended end-to-end sequence

1. **Software gate:** syntax, unit tests, dependency and configuration checks.
2. **System gate:** resource/timeout checks in the actual target environment.
3. **Model gate:** explicit model/license/hash preflight; inference tests only when a model is intentionally installed; record uncertainty and abstention.
4. **Sensor gate:** verify connection, timestamp freshness, calibration and fault injection on approved test equipment.
5. **Simulation gate:** replay repeatable scenarios; inject missing, stale, conflicting and malformed observations.
6. **Hardware gate:** only after simulation and an independent safety review; use a controlled test area, physical emergency stop and human supervisor.
7. **Operational gate:** independent evaluation, privacy/security review, authorised pilot and documented acceptance criteria.

## Free-first implementation boundary

The starter report generator uses Python's standard library and performs no network calls, package installs, model downloads, sensor reads or actuator commands. It produces an honest baseline with unrun/unconnected statuses. Populate future evidence only from checks that really ran. Do not add a scheduled workflow by default; run on code changes or manually to limit resource use.

## Project-specific safeguards

For screening, an AI alert is not proof of chemical identity or wrongdoing. Ordinary RGB imagery cannot confirm a substance. Missing, stale or conflicting modalities must lead to uncertainty/abstention and authorised human review, not an automatic enforcement action. No face recognition, identity profiling, detention or autonomous search is part of this observability layer.

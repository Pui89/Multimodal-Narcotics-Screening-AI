# PUI89 AI Core Contract

**Status:** shared engineering contract for software and simulation tests; not a certification or claim of field readiness.

This contract defines reusable interfaces across the seven PUI89 products. Each product retains domain-specific perception, task logic, hardware boundaries and validation requirements. Shared AI Core is a foundation, not an eighth product.

## 1. Core records

The shared interface uses four versioned records:

- **Observation:** source modality, payload reference, timestamp, provenance, quality, calibration state and uncertainty.
- **WorldState:** current estimated environment/asset/robot state, freshness, confidence, missing information and known hazards.
- **ActionProposal:** bounded task or next-step proposal, preconditions, expected outcome, risk, expiry and required approval level.
- **FailureReport:** fault or unexpected outcome, affected subsystem, evidence, severity, safe-state recommendation and recovery status.

Records must be schema-validated, versioned and traceable. Unknown or missing critical information must remain explicit; it must not be silently converted into a confident positive result.

## 2. Required world-state safety signals

Where a product uses an action supervisor, every action proposal must receive explicit Boolean values for applicable safety signals. Missing, malformed or unknown critical values must fail closed to SAFE_HOLD.

| Field | Safe-to-proceed value | Fail-safe condition |
|---|---|---|
| emergency_stop | false | true, missing, or not Boolean |
| sensors_ok | true | false, missing, or not Boolean |
| sensor_data_fresh | true | false, missing, or not Boolean |
| comms_ok | true | false, missing, or not Boolean |

Do not silently coerce strings such as "false", integers such as 1, or null values into Booleans. Product-specific hardware interlocks remain independent of AI confidence.

## 3. Perception uncertainty and provenance

- Confidence must be a finite numeric value in the interval [0, 1]; Boolean values are not numeric confidence.
- Missing, malformed, out-of-range or non-finite confidence must result in abstention (for example, UNKNOWN) rather than an affirmative detection.
- Conflicting modalities or missing required modalities must be represented explicitly and must not be hidden by a single confidence score.
- Preserve source, timestamp, calibration, licence/permission context and transformation history where applicable.
- Project-specific thresholds must be documented and evaluated against appropriate labelled test data before any performance claim.

## 4. Human review and action boundary

- Shared interfaces generate observations and bounded proposals; they do not independently authorise hardware actuation.
- High-impact, safety-critical or uncertain actions require the appropriate human approval and independent hardware safeguards.
- A simulation scenario passing is not evidence of real-world safety, accuracy, rescue capability, harvest capability, terrain mobility or vehicle performance.
- AI must not make enforcement decisions, accuse individuals or bypass a product's operator and safety procedures.

## 5. Reproducible scenario reports

Automated scenarios should record the scenario identifier, seed where applicable, engine/version, input state, proposed action, decision trace, expected action, pass/fail outcome and whether hardware actuation occurred. Reports should be deterministic for identical inputs where the implementation supports it.

At minimum, regression tests should cover:
- each required safety field missing or malformed;
- emergency stop, sensor failure, stale data and communication loss;
- recovery after a fault clears;
- invalid confidence and conflicting/missing modalities;
- human-review gates for high-impact actions;
- stable report identifiers and an explicit no-hardware-actuation assertion.

## 6. Product-specific extensions

- **Coconut Harvest AI:** maturity-stage uncertainty, cutting/capture hazards, drop zone, and worker/animal separation.
- **Extreme Flood Rescue AI:** water/environment uncertainty, victim-location confidence, communication degradation, and simulation-only depth scenarios.
- **PUI89 Sentinel quadruped:** obstacle/free-space observations, terrain traversability, localisation/motion-state confidence, foot-contact and slip/stumble cues, inspection evidence, safe hold and supervised recovery.
- **PUI89 AI HOME / AI NOMAD:** indoor/outdoor wheeled navigation, obstacle clearance, payload limits, human interaction and environment-specific safe-stop behaviour.
- **PUI89 AI Global SUV:** medium-size passenger-vehicle road context, obstacle and hazard warnings, vehicle/battery/thermal state and human-driver advisory interaction. This is a separate four-wheel product project.
- **PUI89 AI Step-Through Scooter:** two-wheel rider/road context, obstacle and hazard warnings, scooter/battery/thermal state and rider advisory interaction. This is a separate product project with its own requirements and validation. No autonomous steering, throttle or braking is authorised for either product by this contract.

## 7. Release gate

Before merging a change that affects the shared interface:
1. run the relevant product regression tests and shared-interface smoke checks;
2. review failure reports rather than relying only on a green summary;
3. document untested assumptions and limitations;
4. keep model downloads, package installs, cloud services and hardware actuation disabled unless separately approved and assessed.

**No measured results should be advertised unless they are reproducible and the dataset/scenario, split strategy, metric definition and test conditions are recorded.**

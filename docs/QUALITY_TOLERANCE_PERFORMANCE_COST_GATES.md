# Quality, tolerance, performance, safety and cost gates

**Status:** proposed engineering acceptance plan for an AI screening concept. An alert is not proof of a substance, intent, identity or wrongdoing.

## 1. Tolerance, sensor quality and uncertainty

For each modality, record source/provenance, timestamp, calibration, valid range, quality score, uncertainty and known failure modes. Detect missing, stale, saturated, obstructed, corrupted or conflicting readings. Do not fuse data as if all sensors were equally reliable. If a modality is unavailable or outside calibration, mark it unavailable and lower system confidence or abstain; never silently substitute a fabricated value.

## 2. Worker, passenger and animal safety

- Keep robot motion limits and collision/stop behavior in a deterministic safety layer independent of AI classification.
- Use risk-assessed speed and separation limits near people, workers, mobility aids and animals. Pause when people are too close or the route is blocked; avoid sudden movements and unannounced approach.
- Do not chase, corner, touch, frighten or injure animals, including monkeys. If an animal enters the path, stop and wait for a safe route.
- AI outputs must not autonomously trigger arrest, search, detention, denial of service or other enforcement. A qualified human reviews alerts and supporting sensor evidence.
- Do not identify people, infer intent or assign guilt from appearance or proximity. Minimize personal data, restrict access, set retention limits and log who reviewed each alert.
- Physical or chemical screening claims require suitable validated sensors, calibration, lawful protocols and independent evaluation. Image/video alone does not establish chemical identity.

## 3. Performance metrics

Evaluate:
- each sensor/modality separately and the fused model;
- per-class precision, recall, false-positive and false-negative rates with confidence intervals;
- calibration quality, uncertainty/abstention rate and performance when modalities are missing or disagree;
- results by relevant lawful test conditions and environmental strata to identify uneven error rates;
- latency, throughput, CPU/RAM/VRAM, energy use and operator-review burden;
- human factors: alert comprehensibility, override, disagreement and escalation rate.

Use a lawful, expert-reviewed, source-separated dataset with documented provenance, licence, consent/legal basis and contamination controls. Synthetic fixtures can test software logic but cannot establish real-world chemical detection performance.

## 4. Tolerance and fault injection

Test low-quality input, camera obstruction, sensor drift, stale timestamp, calibration expiry, missing modality, contradictory modalities, out-of-distribution inputs, network loss, repeated alert and attempted unauthorized access. Expected response: flag degraded state, abstain or route to human review, preserve an audit record and avoid automatic enforcement. A detector that produces a confident answer on invalid inputs fails the acceptance test.

## 5. Cost and maintainability

- Default to existing local Python tooling and synthetic test fixtures.
- No paid API, cloud GPU, automatic model download, recurring scheduled workflow or new package unless explicitly cost/licence reviewed.
- Record hardware/sensor costs, calibration consumables, maintenance, storage, operator time and any software charges.
- Check licence, model size, RAM/VRAM, privacy terms and offline operation before considering optional models.
- Prefer modular sensor interfaces, local-first logs, minimal data collection and documented manual override.

## 6. Release gates

1. Unit and negative tests pass; evidence reports match underlying data.
2. Sensor-fault and abstention tests pass.
3. Dataset legality, provenance, calibration and evaluation design are reviewed.
4. Independent privacy, security, human-factors and risk reviews are complete.
5. Controlled tests with suitable reference instruments measure bounded performance.
6. Human-in-the-loop pilot validates workflow and error handling before deployment claims.

Passing a software test does not certify a sensor, prove chemical identity, establish fairness or authorize enforcement.

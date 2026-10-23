# Product Quality Roadmap — Multimodal Narcotics Screening AI

**Priority:** Equal top priority across all PUI89 projects.  
**Current evidence level:** screening workflow and evaluation prototype; no validated narcotics detector or chemical-identification system.

## Release gates

1. **Define a narrow authorised task:** specify intended use, target classes, decision boundary, authorised operators, and what the system must never conclude.
2. **Data and ground truth:** document lawful source, consent/authority where applicable, provenance, modality, calibration, labels, reviewer qualifications, and limitations. Keep synthetic examples separate from real samples.
3. **Leakage-safe evaluation:** split by source, subject/item, device, site, and session where relevant. Freeze the held-out set before model selection.
4. **Fair baseline comparison:** measure each modality separately before fusion; compare against fusion on the same split. Report per-class precision/recall, confusion matrix, false-positive/false-negative rates, calibration, uncertainty, abstention coverage/risk, and missing/conflicting-modality behavior.
5. **Human review and privacy:** incomplete, conflicting, out-of-distribution, or low-confidence input must be escalated or abstained from. Minimize sensitive data, restrict access, protect audit logs, and document retention/deletion.
6. **No automated enforcement:** model output is a screening signal, not proof of substance identity, illegality, intent, or wrongdoing.

## Milestones

- [ ] Document intended use and prohibited uses.
- [ ] Inventory input modalities, data provenance, licenses, and ground truth.
- [ ] Add tests for missing, corrupted, conflicting, stale, and misleading inputs.
- [ ] Establish unimodal baselines and a comparable fusion evaluation.
- [ ] Publish metrics, uncertainty/abstention results, false-positive examples, and limitations.
- [ ] Review privacy, security, dependencies/licenses, human-review flow, and rollback.

## Resource policy

Prefer dependency-light local evaluation. Do not automatically download large models, send sensitive data to external services, or incur paid compute/API charges. Review model and dataset licenses before use.

## Honest status rule

A populated dashboard, synthetic test, passing unit test, trained model, validated sensor, and real-sample laboratory evaluation are different evidence levels. Do not claim reliable chemical identification without appropriate controlled ground-truth validation and independent testing.

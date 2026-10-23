# PUI89 Product Engineering Standard — Multimodal Screening AI

**Product direction:** auditable multimodal screening and evidence triage for trained human reviewers.  
**Status rule:** a model score is not proof of a substance identity, illegality, intent, or wrongdoing.

## Product promise

Combine available input modalities into a transparent decision-support workflow that exposes missing evidence, conflicting signals, uncertainty, and reasons for escalation. The system must be allowed to abstain.

## Architecture boundaries

1. **Input quality:** validate file types, sensor metadata, timestamps, calibration status, and input completeness before inference.
2. **Single-modality baselines:** evaluate each modality independently to establish what it contributes.
3. **Fusion:** compare a fusion method against single-modality baselines using the same leakage-safe split.
4. **Evidence trace:** link every output to input identifiers, model versions, processing steps, confidence/uncertainty, and reviewer action.
5. **Abstention:** escalate when inputs are missing, conflicting, out of distribution, or below a pre-registered quality threshold.
6. **Human review:** no automated output alone should determine arrest, punishment, denial of rights, or a definitive claim about an unknown substance.
7. **Privacy and security:** minimize retained sensitive data, control access, protect audit logs, and document retention/deletion behavior.

## Required evaluation gates

- Clearly distinguish real, synthetic, simulated, and unverified data.
- Use source-aware and subject/device/session-aware splits where relevant; prevent near-duplicate and provenance leakage.
- Report per-class precision/recall, confusion matrices, calibration, false-positive/false-negative costs, abstention coverage/risk, missing-modality performance, and robustness under corrupted or conflicting inputs.
- Compare unimodal baselines against fusion; fusion is only an improvement if held-out evidence supports it.
- Test malformed inputs, adversarially misleading metadata, sensor drift, missing channels, distribution shift, and safe failure behavior.
- Include subgroup analysis only when lawful, ethically appropriate, adequately powered, and supported by valid labels.

## Release blockers

Do not claim reliable real-substance identification unless validated with suitable ground-truth samples, controlled procedures, and independent testing. Synthetic-only metrics must never be presented as real-world accuracy. Do not present model outputs as legal findings.

## Model and license policy

Keep large weights out of Git history. Record model source/revision, checksum, license and commercial-use implications, training data provenance, compute needs, and known limitations. Avoid automatic large downloads and training in CI.

## Product-grade release evidence

Each release should include an auditable evaluation report, data and model cards, privacy/security review, dependency/license inventory, reviewer workflow, uncertainty/abstention tests, and rollback instructions.

## Current truthfulness rule

A dashboard, rule-based workflow, synthetic evaluation, trained classifier, validated sensor pipeline, and real-world screening deployment are distinct maturity levels. State the actual level and evidence for every release.

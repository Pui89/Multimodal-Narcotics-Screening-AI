# Complete System Blueprint — Multimodal Narcotics Screening AI

**Scope:** evidence-management and human-supervised screening prototype. This is not a validated narcotics detector, chemical analyser or autonomous enforcement system.

## System architecture

```text
Authorised RGB / depth / thermal / X-ray or CT / metadata inputs
  -> consent, provenance, access-control and quality checks
  -> modality-specific model adapters (only for available, validated sensors)
  -> calibration / out-of-distribution / missing-modality checks
  -> evidence aggregation with explicit uncertainty
  -> triage state: NO INDICATION / REVIEW / UNKNOWN
  -> authorised human review and confirmatory procedure
  -> access-controlled audit record and evaluation report
```

## Component contracts

1. **Authorised input only:** retain source, collection context, licence/permission, timestamp and data handling basis. Minimise personal data and avoid unnecessary retention.
2. **Modality boundaries:** ordinary RGB imagery cannot establish the chemical identity of a substance or see through closed luggage. X-ray/CT requires the relevant authorised sensor and suitable labelled data. Do not present an unimplemented modality as active.
3. **Model adapter:** record model/checkpoint hash, input modality, training-data scope, confidence and known exclusions. Never treat confidence as a probability unless calibration was measured.
4. **Fusion:** combine only evidence that has been validated for the intended task. Missing or conflicting modalities must lead to UNKNOWN/REVIEW, not an automatic positive decision.
5. **Human review:** an AI flag is a screening hypothesis, not proof of narcotics. Consequential action must not be triggered solely by the model.
6. **Audit/privacy:** log reviewer decisions and versioned evidence references with role-based access; avoid copying sensitive imagery into logs or public repositories.
7. **Evaluation:** report per-class precision/recall, confusion matrix, false-positive and false-negative rates, calibration, abstention rate, subgroup/condition analysis and independent expert review.

## Free-first development profile

- Run the software pipeline locally; no paid inference endpoint or cloud GPU is required.
- C3PI is a prescription-pill image resource, not a dataset proving illicit-narcotics identification. It may be used only for a clearly scoped pill-image workflow after its licence/terms and label meaning are reviewed.
- A seized-ecstasy image collection must not be used until redistribution/use rights, provenance and ground-truth basis are verified. Image appearance alone is not chemical confirmation.
- Keep sensitive datasets, personal information and model weights out of Git unless authorised and licensed for publication.

## Acceptance gates

- [ ] Intended use, operator role, prohibited use and data governance are documented.
- [ ] Every data source has a verified licence/permission and traceable ground-truth basis.
- [ ] Labels are reviewed by an appropriate qualified source; uncertain cases remain UNKNOWN.
- [ ] Independent splits prevent the same item, subject, scene or near-duplicate from leaking across train and test.
- [ ] Evaluation includes false positives/negatives, calibration, abstention, out-of-distribution inputs and failure cases.
- [ ] Missing modality, low-quality input, tampered metadata and model failure all produce safe review/unknown states.
- [ ] A qualified human and, where relevant, an authorised confirmatory test determine actual substance identity.

## Current boundary

The repository contains a screening workflow and evaluation tooling, including synthetic pipeline checks. This blueprint does not establish a trained model validated on real narcotics, chemical identification, X-ray/CT capability or a deployed screening robot. Mark each gate **PASS**, **FAIL**, or **NOT RUN** and link evidence.
# PUI89 Shared AI Core — Sentinel Screening Adapter

**Status:** Integration plan; documentation only.  
**Platform contract:** [PUI89 Evidence-to-Action Intelligence Platform](https://github.com/Pui89/Pui89.github.io/blob/main/docs/PUI89_EVIDENCE_TO_ACTION_PLATFORM.md)

## Purpose

Apply shared evidence, provenance, multimodal quality, uncertainty, abstention and human-review contracts to the Sentinel screening workflow. This project is decision support; it is not an autonomous enforcement system.

## Modality observations

Each modality is an independent evidence item with source, timestamp, device/system identifier, quality status, calibration status when documented, provenance, licence/permission context, and missing/failed status. RGB, X-ray and chemical-sensor observations must not be represented as available unless corresponding lawful data and actual equipment exist.

## World-state requirements

Track modality availability, image/sensor quality, conflicts between modalities, model/version provenance, evidence age, and human-review status. Do not merge incompatible scores or treat an absent modality as a negative result.

## Proposal and safety rules

- Outputs are screening indicators for authorised human review only.
- HOLD when modalities are missing, degraded, uncalibrated, stale, out of distribution or materially conflicting.
- Abstain rather than force a classification when evidence is inadequate.
- Never infer guilt, intent or legal status from model output.
- No search, detention, seizure, denial of service or other enforcement action may be triggered by the AI core.
- Consequential decisions remain with authorised personnel under applicable law and procedure.

## Evaluation gates

1. Validate shared schemas and modality-specific metadata.
2. Test missing, degraded, corrupted, conflicting and out-of-distribution inputs.
3. Report per-modality and fused results separately.
4. Measure false-positive and false-negative rates on a lawful, representative, permission-verified evaluation set.
5. Report class balance, uncertainty, abstention/coverage and subgroup limitations where lawful and statistically meaningful.
6. Test human-review escalation and ensure no automatic enforcement path exists.
7. Keep synthetic data results separate from real-world validation.

## Required report

Include dataset provenance/permissions, modality availability, model/version, test split, confusion matrix, class counts, false-positive/negative analysis, abstention rate, calibration method, limitations and reviewer. If lawful representative data or actual sensor integrations are unavailable, report the corresponding metrics as NOT MEASURED.

## Implementation boundary

This document is an adoption plan. It does not establish a validated substance detector, X-ray/chemical integration, field accuracy or deployed robotic screening capability.

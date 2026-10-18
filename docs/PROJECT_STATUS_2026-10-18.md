# Project status and verification log — 18 October 2026

## Current state

**Stage:** screening workflow prototype and evaluation-pipeline tests. It is not a validated narcotics-identification system and must not be used to make law-enforcement decisions.

### Completed and evidenced
- [Latest local-first regression run passed](https://github.com/Pui89/Multimodal-Narcotics-Screening-AI/actions/runs/39092345879).
- The regression workflow checks application/evaluation behaviour; it does not validate real-world drug identification.
- Dataset acquisition and labelling plan, manifest template, and local manifest audit tool are present.
- Documentation distinguishes pharmaceutical pill recognition from illicit-narcotics identification.

### In progress
- Verify dataset provenance, licensing, permitted use, class labels and annotation quality.
- C3PI/RxIMAGE is a pharmaceutical-pill image resource, not evidence of illicit-substance classification. Its stated licence and terms must be checked before reuse.
- A seized-ecstasy image set is not approved for use unless lawful access and redistribution/research terms are independently verified.
- Expand tests for missing modalities, malformed records, uncertain predictions, calibration and abstention.

### Not yet demonstrated
- A legally cleared, representative dataset for the exact intended screening task.
- Held-out accuracy, calibration, false-positive/false-negative rates, cross-device generalization, or validated multimodal benefit.
- Reliable identification of a substance from images alone or suitability for operational decisions.

## Next actions
1. Freeze a precise and lawful intended-use definition; avoid treating prescription-pill images as narcotics evidence.
2. Audit source/licence/consent, provenance, duplicate leakage, class balance and label confidence.
3. Test fail-closed handling: missing or conflicting modalities, low confidence, out-of-distribution inputs and malformed evidence must route to human review/abstention.
4. Evaluate on a held-out, source-separated dataset; report per-class precision/recall, confusion matrix, calibration and error analysis.
5. Keep a human expert in the loop and state that model output is a screening cue, not a determination of legality or substance identity.

## Future
- Compare image-only and multimodal baselines only when lawful, aligned, representative data are available.
- Assess domain shift, packaging variation, lighting, image capture devices and deliberate ambiguity.
- Document privacy, retention, access controls, audit trail and independent validation before any real-world pilot.

## Cost and safety
Free/local-first and no paid cloud inference requirement. Do not collect or publish sensitive case data without authorization. No model output should be treated as proof of illicit substance or used as the sole basis for detention, search, or other consequential action.
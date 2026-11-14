# Physical AI stack — Multimodal Narcotics Screening AI

## Planned architecture

1. **Vision-language model (VLM):** summarize inspection images and identify visible features that may warrant review. A VLM description is not proof of substance identity.
2. **Task/action LLM:** convert an approved inspection request into a structured checklist and propose the next non-invasive inspection step.
3. **Multimodal evidence fusion:** combine only validated and legally sourced modalities, preserving each modality's separate result and limitations.
4. **Provenance and audit trail:** record sample/reference ID, modality, timestamp, model/version, transformations, confidence and reviewer decisions.
5. **Uncertainty and disagreement handling:** return “inconclusive” for missing, conflicting or out-of-distribution evidence; route cases to qualified reviewers.
6. **Autonomy supervisor:** retain the existing supervisor as an independent gate. The LLM cannot bypass it.
7. **Evaluation:** measure per-class precision/recall, false positives/negatives, calibration, subgroup limitations and performance with missing modalities.

## Safe starter action vocabulary

Use high-level allowlisted actions such as `review_sample_metadata`, `request_additional_measurement`, `compare_validated_modalities`, `mark_inconclusive`, and `request_human_review`. The planner must not declare guilt, identify a substance conclusively without validated evidence, or trigger enforcement actions.

## Current implementation status

- `pui89_autonomy/llm_interfaces.py` provides dependency-free data contracts and validators for vision findings and action plans.
- It does **not** load or run a VLM/LLM, connect to an API, identify narcotics, or control a robot.
- Model output is an aid to inspection only; it must not be treated as proof of substance identity or guilt.
- Only use datasets and sensor inputs with appropriate permissions and documented provenance.

## Next steps

1. Define the legally and scientifically valid input modalities before choosing a model.
2. Establish a transparent baseline and an independent evaluation protocol.
3. Test conflicting inputs, missing modalities, adversarial examples and out-of-distribution cases.
4. Add a local model adapter only after checking model license, hardware fit, download size and reproducible evaluation.

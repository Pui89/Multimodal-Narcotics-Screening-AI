# Multimodal Narcotics Screening AI — Low-Cost Screening Station Concept

## Design goal

Create a human-supervised screening workstation that organizes authorized image or sensor evidence and highlights cases requiring further review. The safest low-cost first version is a **stationary software prototype**, not an autonomous enforcement robot.

## Concept architecture

1. **Input:** use lawful, authorized sample images or synthetic data. Do not collect personal data or real evidence without authorization.
2. **Local workstation:** run a local Python application on an existing computer.
3. **Image handling:** use OpenCV for image quality checks, cropping, and basic visual inspection. Use PyTorch or another locally run model only for tasks supported by validated data.
4. **Screening output:** use neutral labels such as POSSIBLE MATCH, NO MATCH IN THIS MODEL'S SCOPE, or UNKNOWN / INSUFFICIENT EVIDENCE.
5. **Operator interface:** show source, timestamp, uncertainty, and review notes. Preserve an audit log without exposing sensitive details.
6. **Voice output:** read neutral status messages only when appropriate. Avoid speaking confidential case details in public.
7. **Physical automation:** no robotic arm, physical handling, chemical testing, or enforcement action is needed for the initial prototype. Any future sensor or scanner must be lawfully acquired, validated, and operated by qualified personnel.

## Important scientific limitation

Ordinary RGB photographs cannot reliably establish a substance's chemical identity. A visual resemblance is not confirmation that an item contains methamphetamine, heroin, cannabis, or another substance. Chemical identification requires appropriate validated analytical methods and qualified review. The AI should not identify a person, infer guilt, or make an enforcement decision.

## Free-first software

- Python, OpenCV, and PyTorch for local experimentation.
- Jupyter or local scripts for evaluation.
- Kokoro-82M for English voice experiments; SakThai TTS for experimental Thai voice output.
- GitHub for code and documentation.

Free software does not mean scanners, laboratory instruments, calibration materials, or qualified testing are free. Do not add paid hosted inference APIs; use synthetic or properly authorized sample data in the first stage.

## Staged prototype plan

- [ ] Stage 1: build a local image-review UI using synthetic or authorized data.
- [ ] Stage 2: test image-quality checks and UNKNOWN handling.
- [ ] Stage 3: evaluate any supported model on a documented, representative held-out dataset.
- [ ] Stage 4: report false positives, false negatives, and limits; avoid claims of chemical confirmation from photographs.
- [ ] Stage 5: request independent scientific, privacy, legal, and operational review before any real deployment.

## Safety, privacy, and governance checks

- Human review is required before consequential action.
- Do not use image-only outputs as proof of chemical identity or wrongdoing.
- Do not identify or track people unless a lawful, necessary, specifically reviewed use case exists.
- Limit access, minimize retention, and protect sensitive evidence.
- Log model version, input source, uncertainty, and reviewer decision where lawful.

**Status:** stationary screening-software concept only. No validated narcotics detector or autonomous enforcement capability is claimed.

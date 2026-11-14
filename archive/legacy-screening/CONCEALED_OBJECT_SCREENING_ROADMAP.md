# Concealed-object screening: staged technical roadmap

## Objective

Explore whether a screening system can flag an unusual concealed object for a trained, authorised human reviewer. **Chemical identification is a later phase**, not part of the first prototype.

## Key technical boundary

An ordinary RGB camera and a general-purpose image model cannot see through underwear or reliably determine what is hidden beneath clothing. A visual anomaly score from a photograph only measures a difference in visible image features; it is not evidence that a concealed object exists.

A future concealed-object experiment must use data from an appropriate, legally approved screening sensor. Depending on the intended setting, candidate modalities may include a certified millimetre-wave security scanner or other approved imaging equipment. Access to raw scanner data, vendor restrictions, image format, safety rules, and licensing must be confirmed before choosing a model. Do not try to imitate scanner output using ordinary photos.

## Staged implementation

1. **Stage A — software plumbing now:** keep the current DINOv2 embedding-distance script as a generic image-anomaly baseline. Verify that it runs locally on non-sensitive test images. It is not the concealed-object detector.
2. **Stage B — sensor/data feasibility:** identify an approved sensor modality and obtain lawfully sourced, consented, de-identified example data with clear rights for research. Record the sensor, acquisition conditions, permitted use, and label provenance.
3. **Stage C — anomaly benchmark:** build a separate adapter for that sensor's image/data format. Establish a normal-only reference baseline, then evaluate on a held-out set with reviewed labels. Measure false-positive rate, false-negative rate, sensitivity at a stated false-alarm rate, and performance across relevant acquisition conditions. Split by person/session/source to prevent leakage where applicable.
4. **Stage D — human-reviewed prototype:** show only a sensor-region alert and uncertainty to an authorised operator. The system must not infer guilt, identify a substance, or autonomously trigger a search or detention.
5. **Stage E — chemical testing later:** only after an independently validated sensor alert, an authorised procedure may use a suitable chemical trace test or laboratory confirmation. A visual anomaly model cannot replace that step.

## Privacy and safety requirements

- Use only lawful, consented or otherwise properly authorised datasets; avoid collecting intimate images or identifiable personal data for this software baseline.
- Do not build a covert camera workflow or use this model to score people.
- Minimise retention, restrict access, document purpose and legal basis, and require human review.
- Treat every alert as an uncertain prompt for further approved checking, never a positive narcotics finding.

## Current evidence status

- Software baseline: code added in the associated pull request; local execution and metrics still unverified.
- Concealed-object detection: **not implemented**; requires approved sensor data and a separate model/adapter.
- Chemical detection: **deferred** as requested; no chemical sensor integration is implemented.
- Real-world screening capability: not validated.

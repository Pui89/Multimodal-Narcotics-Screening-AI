# Real Screening Dataset Plan

**Status: source discovery and licensing review only. No dataset has been approved for training yet.**

This project must use real, provenance-tracked images and labels for evaluation. Do not treat concept art, generated images, unverified web images, or ordinary RGB photographs as evidence that a concealed substance is narcotics.

## Dataset sources to review

| Source | What it provides | Intended use in this project | Important limitation |
|---|---|---|---|
| [SIXray dataset repository](https://github.com/MeioJane/SIXray) | Real baggage X-ray screening images for prohibited-item research | Candidate source for generic X-ray screening research after checking the repository's access and licence terms | Its commonly described classes are prohibited objects, not confirmed narcotics. Do not label an image as a drug-positive case without a trustworthy ground-truth record. |
| [CargoX dataset and paper](https://osf.io/7hd3v/), [open-access paper](https://doi.org/10.1371/journal.pone.0272961) | Cargo-domain X-ray data described in a peer-reviewed study | Candidate for cargo-X-ray domain research after checking the dataset page's actual licence, access conditions, and data card | The paper's open-access licence does not automatically establish the dataset files' reuse licence. The dataset description includes synthetic cargo scans, so record whether each image is real or synthetic. |
| [Xray-PI dataset](https://github.com/LPAIS/Xray-PI) | X-ray images with masks/annotations for seven prohibited-item classes and normal images | Academic-only exploratory benchmark if its access conditions are met | The repository states that images and annotations are for academic use only and disallows commercial use. **Do not use for a commercial product unless the rights holder grants written permission.** Its listed classes are not narcotics classes. |
| [UNODC Individual Drug Seizure data](https://dmpone.unodc.org/downloadIDS) | Structured records about reported drug-seizure events, not a labelled image dataset | Background statistics and terminology only; cite UNODC where reused | This is not an image source and must not be converted into image labels. Public data can be reused with attribution under the stated terms, but coverage is incomplete. |

## Dataset acceptance checklist

Before any image enters training, validation, or test:

- [ ] Record the source URL, download date, dataset version, original filename or stable ID, and file hash.
- [ ] Record the exact licence or written permission, including commercial-use and redistribution terms. If unclear, quarantine the data.
- [ ] Record modality: RGB photo, baggage X-ray, cargo X-ray, chemical-sensor measurement, or other. Never mix these as if they were interchangeable.
- [ ] Record whether the image is real, simulated, or synthetic.
- [ ] Record the label's evidence source and annotation method. Distinguish *visible object*, *suspected prohibited item*, and *chemically confirmed substance*.
- [ ] Keep personal data and identifiable people out unless collection and use are lawful, necessary, and authorised. Prefer de-identified item-only scans.
- [ ] Detect duplicate and near-duplicate images before splitting.
- [ ] Split by original scan/session/source/subject as appropriate, not by random near-identical image crops, to reduce leakage.
- [ ] Keep the final test set untouched until model selection is finished.
- [ ] Publish dataset counts, class balance, exclusions, and licence notes without redistributing source files unless permitted.

## Initial train / validation / test protocol

Use **70% train / 15% validation / 15% test only after** provenance, labels, duplicates, and grouping have been checked. The split must be group-aware; if a source provides an official split, preserve it and document any changes. Do not force a split when a dataset is too small or lacks reliable labels.

Track separate evaluations for each modality and task:
- Generic visible-object detection: precision, recall, mAP (when bounding-box labels exist), and false-positive review.
- X-ray prohibited-item detection: class-specific precision/recall and performance on cluttered/occluded scans.
- Chemical or trace sensing: evaluate calibrated sensor measurements against documented reference standards and an approved protocol; images alone cannot establish chemical identity.
- Human workflow: report uncertainty and operator review outcomes. A model alert is not proof of narcotics or grounds for an accusation.

## Current project boundary

At present, the repository has no verified narcotics-labelled image dataset approved for model training. Generic X-ray data can support a separate prohibited-object baseline only where the terms permit it. It cannot validate narcotics identification, concealed-drug detection, or a real-world screening robot. Do not claim model accuracy until a reproducible evaluation has been run on an appropriate, held-out dataset.

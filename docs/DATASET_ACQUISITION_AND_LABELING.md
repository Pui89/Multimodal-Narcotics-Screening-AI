# Free dataset sourcing, annotation and training plan

Last reviewed: 18 October 2026

## Cost and rights rules

- Use local downloads and local training only. No paid APIs, hosted inference, paid notebooks, cloud GPUs or subscriptions are required by this plan.
- Do not commit downloaded images, large archives, trained weights, credentials or sensitive operational data to Git.
- “Public” or “open record” is not enough by itself: verify the dataset's explicit licence and any conditions for redistribution, derivative annotations, and commercial use before training.
- This project is a screening-support research prototype. Image appearance alone must not be represented as proof of chemical identity. Keep human review and uncertainty handling.

## Candidate sources and limits

| Source | Useful for | Labels and limits | Licence / decision |
|---|---|---|---|
| [NIH/NLM C3PI / RxIMAGE pill images](https://catalog.data.gov/dataset/computational-photography-project-for-pill-identification-c3pi) | A free, labelled **prescription-pill** image benchmark; useful for testing local image ingestion, pill localization or visual retrieval tooling | Data.gov describes 133,000 consumer-grade pill images and 4,000 reference images. It concerns prescription medication images, not illicit narcotics, and is not evidence that a model can identify controlled substances. | Data.gov lists ODbL for the dataset record. Read the linked source's own terms and attribution requirements before use; do not assume every image or metadata field has identical rights. Candidate only for a separate pill-image pipeline/proxy task. |
| [Seized ecstasy pills image dataset (Zenodo, DOI 10.5281/zenodo.4124562)](https://zenodo.org/records/4124562) | Potential forensic-research image source | Record describes 602 high-resolution JPG images of seized ecstasy pills. This is a small, narrow forensic collection, not a representative screening benchmark; image appearance does not establish chemical composition. | The licence was not reliably verified in this review. **Do not download for training or redistribute until the Zenodo record's explicit licence and terms are confirmed.** |
| [ePillID benchmark](https://github.com/usuyama/ePillID-benchmark) | Fine-grained prescription-pill image retrieval research | Prescription-pill identity, not illicit-substance detection. | Review the repository and underlying NIH Pillbox data terms before use; do not infer a licence from code availability alone. |

### Verified public download entry points

- [C3PI sample archive (493 MB)](https://data.lhncbc.nlm.nih.gov/public/Pills/sampleData.zip) — start here rather than downloading the full archive. The Data.gov record lists ODbL metadata and describes the collection as prescription-pill images for research and development. Check the source terms/attribution before using or redistributing images.
- [C3PI training images index](https://data.lhncbc.nlm.nih.gov/public/Pills/index.html) — described by NLM as 133,000 consumer-grade prescription-pill images.
- [C3PI reference images (6.8 GB)](https://data.lhncbc.nlm.nih.gov/public/Pills/rximage.zip) — larger controlled-light reference set; do not download until the sample and licence review are complete.

These are **prescription-pill** data, not illicit-narcotics ground truth. The seized-ecstasy Zenodo record remains excluded until its explicit dataset licence is verified. No narcotics training dataset is approved by this documentation update.

## Recommended local workflow

1. Begin with a small sample or source metadata, not a multi-gigabyte download. Confirm the dataset's own licence, citation, intended-use conditions and whether redistribution/derivative labels are permitted.
2. Store source URLs, record DOI/version, licence text/URL, retrieval date, checksums and any restrictions in a local manifest.
3. Keep tasks distinct: (A) generic pill localization/retrieval using prescription-pill images; (B) controlled-substance screening using independently verified, lawfully accessible forensic data. Results from A must never be reported as results for B.
4. If the intended research is real narcotics screening, request data access through an authorized forensic laboratory, regulator or research partner. Do not scrape social media, marketplace listings, police images or private records without rights and authorization.
5. Use a free local annotation tool such as [CVAT Community](https://github.com/cvat-ai/cvat) or [Label Studio Community](https://github.com/HumanSignal/label-studio) after checking the current self-hosted setup/licence. Annotations must be reviewed by a qualified person and supported by an authoritative ground-truth source; visual guesses are not chemical labels.
6. Split by physical item/seizure/case/source batch, not near-duplicate views of the same pill across train and test. Freeze the test split before model selection.
7. Train locally only with a compatible open-source framework and a licence-cleared checkpoint. If the hardware cannot train the model, pause instead of enabling paid cloud services.
8. Report per-class precision/recall, confusion matrix, false-positive/false-negative rates, abstention, calibration, image/source conditions, independent ground-truth method and failure cases. A visual model must not issue a definitive chemical identification without validated analytical evidence and authorized human review.

## Label policy

- `unreviewed`: downloaded/imported; label correctness unknown.
- `review_needed`: proposed labels exist but independent review is incomplete.
- `human_verified`: a reviewer checked labels against documented ground truth.
- `excluded`: rights unclear, duplicate, corrupt, out of scope or unsuitable.

Do not label an image “narcotics” merely because a person or website says so. For controlled-substance research, record the provenance and ground-truth basis (for example, an authorized laboratory result) without publishing sensitive case details.

## Status

No images have been downloaded, labelled, or used for training by this documentation change. The free NIH/NLM source is a **prescription-pill proxy dataset**, not a narcotics dataset. The Zenodo seized-ecstasy source remains blocked pending licence verification. No model metrics are claimed.

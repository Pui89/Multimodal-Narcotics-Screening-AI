# Free and Open-Licence Screening Image Plan

**Status: source review only. No image set is approved or downloaded for training yet.**

PUI89 requires **zero-cost data** and, for future commercial flexibility, sources whose actual image-level terms permit commercial reuse. A page being publicly accessible or a dataset card saying “free” is not enough. Do not pay for data, subscribe, or start a gated download without approval.

## Sources and decision

| Source | What it contains | Decision for this project |
|---|---|---|
| [Open Images V7](https://storage.googleapis.com/openimages/web/factsfigures_v7.html) | General photographs and annotations; image licences are listed per image, commonly CC BY 2.0, while annotations are CC BY 4.0 | **Conditional use for visible-object experiments only.** Select only images with verified image-level licence and preserve attribution, source URL and ID. It is not a narcotics or concealed-object dataset. |
| [STCray on Hugging Face](https://huggingface.co/datasets/Naoufel555/STCray-Dataset) | 46,642 baggage X-ray image-caption pairs for security-threat categories | **Not approved yet.** Files are gated and require accepting access conditions; do not download until the actual terms and any commercial-use restrictions are reviewed. The listed categories do not establish narcotics labels. |
| [SIXray](https://github.com/MeioJane/SIXray) | Real baggage X-ray images with labels for guns, knives, wrenches, pliers, scissors and hammers | **Exclude from commercial-use data.** The source explicitly restricts use to academic purposes and prohibits commercial use unless permission is separately granted. |
| [Xray-PI](https://github.com/LPAIS/Xray-PI) | Baggage X-ray images labelled for prohibited objects | **Exclude from commercial-use data.** The source states academic use only and no commercial use. |
| [CargoX paper and data page](https://osf.io/7hd3v/) | Research data described for cargo X-ray experiments | **Not approved yet.** Verify the data files' own licence and real-versus-synthetic status; the paper's open-access licence does not automatically license dataset images. |

## Rules before an image can be used

- [ ] Zero cost to access and download; no paid account, subscription, or API.
- [ ] Verify the **actual image-level or dataset-level licence** and confirm commercial reuse is allowed if the data may support a product.
- [ ] Keep a manifest: source, image ID, original URL, author/attribution, licence, download date, file hash, and any restrictions.
- [ ] Separate RGB photos, baggage X-rays, cargo X-rays, and chemical-sensor readings. Never treat them as equivalent.
- [ ] Record whether each image is real-world, staged, or synthetic.
- [ ] Use only reliable labels. A photo of a package or a suspicious-looking object is not a confirmed narcotics-positive sample.
- [ ] Remove duplicates before making group-aware train/validation/test splits. Preserve official splits where appropriate.
- [ ] Keep personal or identifiable data out unless lawful, necessary and authorised.
- [ ] Do not redistribute downloaded image files unless the licence permits redistribution.

## Training and testing plan

Use a 70% / 15% / 15% train/validation/test split only after a sufficiently sized, correctly labelled dataset is approved. Group by source, scan session, or original item to reduce leakage; preserve an untouched test set.

Report metrics separately for each valid task: precision, recall, mAP where suitable annotations exist, false-positive rates, and uncertainty. Generic image and X-ray datasets can support **visible-object or prohibited-item research only**. They do not validate narcotics identification.

## Narcotics-specific evidence gap

No openly licensed, commercially reusable, real image dataset with verified narcotics-specific ground truth has been approved in this project yet. Do not relabel generic X-ray images as narcotics, infer chemical identity from ordinary photographs, or claim drug-detection performance without an appropriate validated source. A future chemical-identification track needs lawful, properly labelled sensor/reference data and a validated measurement protocol.

**Free-first rule:** do not download large datasets or model weights automatically. Check licence, access terms, dataset size, available disk space, and the user's local hardware before starting.

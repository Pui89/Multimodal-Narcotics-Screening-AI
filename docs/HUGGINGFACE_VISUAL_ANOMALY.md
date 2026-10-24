# Local visual anomaly baseline (Hugging Face)

## What this adds

`tools/huggingface_visual_anomaly_baseline.py` is a free-first, local-only research baseline. It uses a pretrained Hugging Face DINOv2 image encoder (`facebook/dinov2-small`) to embed a query image and a set of reference images, then reports the cosine distance between the query embedding and the mean reference embedding.

This is a simple **image-level outlier score**, not a specialised or validated anomaly-detection model. It does not generate a heatmap or bounding box. It is included as an initial baseline that can be compared with dedicated visual-anomaly frameworks after checking their model cards, licences, code, and dependencies.

## Safe scope and important limitations

- Test with consented, non-sensitive images of ordinary objects or scenes and a clearly defined reference set.
- This is not a narcotics detector, chemical-identification system, body scanner, concealed-item detector, or method for seeing through clothing.
- Visual difference does not establish that an item is suspicious, illegal, or dangerous.
- Do not score people or use outputs for search, detention, employment, or enforcement decisions.
- The score is not a calibrated probability. Do not choose a threshold on the same images used to evaluate the system.
- Report false-positive rate, false-negative rate, and results on held-out images before describing any performance. A single image is not a benchmark.

## Free, local-first setup

Install compatible versions of PyTorch, Transformers, and Pillow in a project virtual environment. The script does not install packages automatically and does not call a hosted inference API. The first run may download the DINOv2 model weights from Hugging Face; this uses internet bandwidth and local disk space. Check the model card and licence before use or redistribution.

## Windows example

Put several representative, rights-cleared reference images in a local folder such as `data/anomaly_reference/`. These should depict the expected baseline for the specific object/scene task; do not mix unrelated image categories and expect a meaningful score.

```powershell
python tools/huggingface_visual_anomaly_baseline.py "data/test/query.jpg" --normal-dir "data/anomaly_reference"
```

Optionally record a provisional flag threshold and JSON report:

```powershell
python tools/huggingface_visual_anomaly_baseline.py "data/test/query.jpg" --normal-dir "data/anomaly_reference" --threshold 0.18 --json-out "outputs/anomaly-baseline.json"
```

The example threshold is only a placeholder; it is not a recommended operational threshold. Calibrate on a separate validation set and report uncertainty and false alarms.

## Current status

- Implemented in this branch: embedding-distance baseline, local image input, reference-directory input, JSON output, and explicit limitations.
- Not yet verified: dependency installation, model download, inference on this project's machine, threshold calibration, benchmark performance, or compatibility with dedicated anomaly models.
- Not a validated physical screening capability.

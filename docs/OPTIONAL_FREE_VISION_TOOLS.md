# Optional Free Vision and Screening Resources

These resources are optional support tools. They do not establish that a package contains a controlled substance, and they do not replace the project's uncertainty, provenance and mandatory human-review controls.

## Recommended order

1. **OpenCV** — local image decoding/quality checks, normalization and visual review overlays. It is not chemical identification.
2. **CVAT Community** — optional self-hosted annotation and double-review workflow for lawful, well-documented training/evaluation imagery.
3. **Tesseract OCR** — optional local extraction of visible printed text only. OCR output is untrusted metadata; it must never by itself trigger a positive narcotics finding or enforcement.
4. **OpenVINO** — a later, optional CPU-inference benchmark if the selected model and hardware support it.
5. **Open3D** — low priority unless the project later works with genuine depth/point-cloud sensors.

## Free-resource register

| Resource | Local check | Licence note | Official source |
|---|---|---|---|
| OpenCV Python (cv2) | Python module | OpenCV 4.5.0+ is Apache-2.0; older releases have different terms and bundled dependencies may differ. | [Licence](https://opencv.org/license/) · [Project](https://github.com/opencv/opencv) |
| CVAT Community | Manual/self-hosted service check | Community core is MIT; review FFmpeg and third-party asset/dependency licences too. | [Community repository](https://github.com/cvat-ai/cvat) · [Licence overview](https://docs.cvat.ai/docs/getting_started/overview/) |
| Tesseract OCR engine | tesseract executable | Apache-2.0; language data and distribution packages have their own details. | [Official documentation](https://tesseract-ocr.github.io/tessdoc/) |
| OpenVINO | Python module (openvino) | Apache-2.0 toolkit; model weights retain their own licences. | [Official repository](https://github.com/openvinotoolkit/openvino) |
| Open3D | Python module (open3d) | MIT. Check the exact release and bundled dependencies. | [Project and licence](https://www.open3d.org/) |

## Check what is already available

Run from the repository root:

    python tools/check_optional_resources.py

The command emits JSON to the terminal and checks only local module metadata/PATH entries. It makes no network requests, installs no packages and downloads no model weights. A resource marked **manual_check** (such as CVAT Community) is deliberately not treated as installed or running.

## Safety, evidence and lawful use

Treat OCR strings and visual anomaly scores as noisy evidence, never as proof of chemical identity. Keep the model, sensor, preprocessing and OCR versions in each experiment record; document data source permissions, chain of custody where relevant, and the human-review result. Evaluate false positives, false negatives, uncertainty/abstention, calibration, latency and memory on representative held-out data. Never connect these optional tools directly to enforcement or physical actuation.

No dependency is added to the core install. No install, model inference or benchmark is performed by the probe.
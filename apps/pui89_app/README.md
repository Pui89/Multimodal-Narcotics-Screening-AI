# PUI89 World-Model Multimodal Screening AI Application

A conservative evidence-review service for authorized screening workflows. It fuses supplied sensor-quality and anomaly evidence into **screening hypotheses for human review**. It does not identify a chemical from images, prove narcotics are present, or trigger enforcement actions.

## Interactive web demo

The Streamlit dashboard lets you explore an example screening review: toggle sensor availability, change timestamp alignment and illustrative spatial/temporal/anomaly scores, submit the values to the API, inspect uncertainty and missing-modality flags, and download a JSON report.

### Run locally

From the repository root, install dependencies:

```bash
python -m pip install -r apps/pui89_app/requirements.txt
```

**Terminal 1 — start the API:**

```bash
uvicorn apps.pui89_app.main:app --reload
```

**Terminal 2 — start the dashboard:**

```bash
streamlit run apps/pui89_app/web_demo.py
```

Open the local URL printed by Streamlit. API documentation is available at `http://127.0.0.1:8000/docs`.

An optional uploaded image is **preview-only**. The dashboard does not run computer vision on the image or identify substances. Scores are manually selected demonstration inputs sent to the existing API.

## API

- `GET /health` — service status.
- `POST /screen` — modality-quality checks, consistency evidence and anomaly review.
- `GET /metrics` — request counters, not model benchmark results.

Example:
```json
{
  "observation_id": "inspection-001",
  "rgb_valid": true,
  "depth_valid": true,
  "thermal_valid": false,
  "lidar_valid": true,
  "timestamp_skew_ms": 15,
  "visual_anomaly_score": 0.72,
  "depth_consistency_score": 0.92,
  "temporal_consistency_score": 0.81,
  "ood_score": 0.18
}
```

## World-model semantics and responsible use

The API uses supplied temporal and spatial consistency values as evidence fields. It does not reconstruct a 3D/4D scene or run a trained anomaly model; validated perception/world-model adapters would need separate integration. Missing modalities are marked missing, never silently treated as negative evidence. High OOD, contradictions or insufficient inputs produce `UNKNOWN` / `HUMAN_REVIEW`.

Screening outputs are hypotheses only, not proof of chemical identity or grounds for an enforcement decision. Require validated, lawful sensing, calibration, evidence provenance and authorized human review. The service has no actuator authority.

## Evaluation

Use a legally authorized, representative and independently labeled dataset. Report per-class precision/recall, false-positive and false-negative rates, calibration error, abstention coverage, OOD detection, missing-modality robustness, end-to-end latency, memory and subgroup/error analysis where lawful and appropriate. Separate synthetic, lab and field results.

## Tests
```bash
python -m unittest discover -s apps/pui89_app -p 'test_*.py' -v
```

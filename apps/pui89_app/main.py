"""PUI89 multimodal screening evidence-review API; not a chemical identifier."""
from __future__ import annotations

from collections import Counter
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="PUI89 World-Model Screening AI", version="1.0.0",
              description="Evidence-aware screening hypotheses with abstention and human review; no enforcement or actuator authority.")
COUNTERS: Counter[str] = Counter()


class ScreenRequest(BaseModel):
    observation_id: str = Field(min_length=1, max_length=100)
    rgb_valid: bool
    depth_valid: bool
    thermal_valid: bool = False
    lidar_valid: bool = False
    timestamp_skew_ms: float = Field(ge=0)
    visual_anomaly_score: float = Field(ge=0, le=1)
    depth_consistency_score: float | None = Field(default=None, ge=0, le=1)
    temporal_consistency_score: float = Field(ge=0, le=1)
    ood_score: float = Field(ge=0, le=1)


@app.get("/health")
def health():
    return {"status": "ok", "service": "world-model-screening-ai",
            "chemical_identification_authority": False, "actuator_authority": False}


@app.get("/metrics")
def metrics():
    return {"screen_requests_total": COUNTERS["screen"],
            "metric_type": "service counters, not model-performance benchmarks"}


@app.post("/screen")
def screen(req: ScreenRequest):
    COUNTERS["screen"] += 1
    available = sum((req.rgb_valid, req.depth_valid, req.thermal_valid, req.lidar_valid))
    missing = [name for name, valid in (
        ("rgb", req.rgb_valid), ("depth", req.depth_valid),
        ("thermal", req.thermal_valid), ("lidar", req.lidar_valid)) if not valid]
    reasons = []
    if not req.rgb_valid:
        reasons.append("RGB_REQUIRED_INPUT_MISSING")
    if available < 2:
        reasons.append("INSUFFICIENT_MODALITIES")
    if req.timestamp_skew_ms > 50:
        reasons.append("TIMESTAMP_SKEW_EXCEEDED")
    if req.ood_score >= 0.70:
        reasons.append("OUT_OF_DISTRIBUTION")
    if req.depth_consistency_score is not None and req.depth_consistency_score < 0.40:
        reasons.append("SPATIAL_EVIDENCE_CONTRADICTION")
    if req.temporal_consistency_score < 0.40:
        reasons.append("TEMPORAL_EVIDENCE_INCONSISTENT")

    # This is an evidence triage rule, not a chemical classifier.
    evidence_score = round(
        0.40 * req.visual_anomaly_score
        + 0.25 * (1 - (req.depth_consistency_score if req.depth_consistency_score is not None else 0.5))
        + 0.20 * (1 - req.temporal_consistency_score)
        + 0.15 * req.ood_score, 4)
    if reasons or available < 2:
        decision = "UNKNOWN"
        review = "HUMAN_REVIEW"
    elif req.ood_score >= 0.40 or evidence_score >= 0.55:
        decision = "SCREENING_ANOMALY_HYPOTHESIS"
        review = "HUMAN_REVIEW"
    else:
        decision = "NO_SCREENING_ANOMALY_SIGNAL_IN_SUPPLIED_FEATURES"
        review = "HUMAN_REVIEW_REQUIRED_FOR_CONSEQUENTIAL_USE"

    return {"observation_id": req.observation_id, "decision": decision,
            "review_status": review, "evidence_score": evidence_score,
            "missing_modalities": missing, "reasons": reasons,
            "chemical_identity_established": False,
            "enforcement_action_authorized": False, "actuator_commands_sent": False,
            "limitations": ["Scores are heuristic evidence triage, not calibrated probabilities.",
                            "No trained detector or 3D/4D reconstruction runs in this API.",
                            "This output is not proof of substance identity."]}

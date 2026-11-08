"""Map synthetic multimodal screening context to Shared AI Core v0.1.

This adapter preserves modality descriptions for human review only. It does not
identify substances, infer guilt, score suspects, or recommend enforcement.
"""
from __future__ import annotations
from datetime import datetime

SCHEMA_VERSION = "0.1.0"

def _timestamp(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("timestamp must be a non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("timestamp must be valid ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return value

def build_screening_v01_records(envelope):
    """Translate only the existing synthetic review envelope into v0.1 records."""
    if not isinstance(envelope, dict):
        raise ValueError("envelope must be an object")
    evidence = envelope.get("evidence")
    observations = envelope.get("observations")
    if not isinstance(evidence, dict) or not isinstance(observations, list) or not observations:
        raise ValueError("envelope must contain evidence and observations")
    source_id = evidence.get("source_id")
    if not isinstance(source_id, str) or not source_id.strip():
        raise ValueError("evidence.source_id must be a non-empty string")
    observed_at = _timestamp(evidence.get("timestamp"))
    created_at = _timestamp(envelope.get("agent_message", {}).get("timestamp"))
    if evidence.get("evidence_kind") != "synthetic":
        raise ValueError("Screening v0.1 mapping accepts synthetic evidence only")

    observation = {
        "schema_version": SCHEMA_VERSION,
        "observation_id": source_id,
        "observed_at": observed_at,
        "source": {
            "source_id": source_id,
            "source_type": "simulation",
            "device_or_system": "PUI89 Sentinel synthetic multimodal context adapter",
        },
        "modality": "other",
        "payload": {
            "domain": "multimodal_narcotics_screening",
            "modality_observations": observations[0].get("modality_observations", []),
            "interpretation": "non_diagnostic_context_for_human_review",
            "limitations": envelope.get("limitations", []),
        },
        "quality": {
            "status": "unknown",
            "notes": "Synthetic modality descriptions; no physical sensor or diagnostic result is represented.",
        },
        "uncertainty": {
            "description": "No validated substance identification, diagnostic inference, suspicion score, or enforcement finding is produced.",
        },
        "provenance": {"recorded_at": observed_at, "dataset_or_file": evidence.get("source_ref", "")},
    }
    proposal = {
        "schema_version": SCHEMA_VERSION,
        "proposal_id": f"screening-human-review:{envelope.get('request_id', source_id)}",
        "created_at": created_at,
        "objective": "Request independent human review of synthetic multimodal context.",
        "actions": [{
            "action_id": f"review:{source_id}",
            "description": "Have an authorised reviewer inspect the supplied context and record evidence gaps.",
            "risk_level": "unknown",
            "preconditions": [
                "Treat all supplied modality descriptions as synthetic and unverified.",
                "Use separately validated evidence and applicable procedures for any real-world assessment.",
            ],
            "expected_effect": "A human reviewer records context limitations or requests additional evidence.",
            "hazards": [
                "False interpretation may cause unjustified suspicion or harm.",
                "No chemical identity, guilt, intent, or legal status may be inferred from this record.",
                "No detention, arrest, seizure, or other enforcement action is proposed.",
            ],
            "evidence_refs": [source_id],
        }],
        "authority": {
            "mode": "advisory_only",
            "human_approval_required": True,
            "execution_authorized": False,
        },
        "uncertainties": [
            "Synthetic modality descriptions only; no model inference or sensor validation.",
            "No chemical identification, suspect scoring, or enforcement decision is supported.",
        ],
    }
    return {"observation": observation, "action_proposal": proposal}

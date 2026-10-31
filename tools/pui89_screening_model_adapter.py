"""Multimodal screening adapter: modality context for human review only."""
from __future__ import annotations
from typing import Any
from pui89_project_adapter_common import build_review_envelope, reject_command_fields

ALLOWED_MODALITIES = {"rgb", "thermal", "acoustic", "depth", "lidar"}
FORBIDDEN_INFERENCE_KEYS = {
    "chemical_identity", "substance_name", "drug_name", "guilt", "suspect_score",
    "enforcement_action", "detention", "arrest", "seizure", "prosecution",
}

def _reject_identity_or_enforcement(value: Any) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_INFERENCE_KEYS:
                raise ValueError(f"chemical-identity or enforcement inference is prohibited: {key}")
            _reject_identity_or_enforcement(child)
    elif isinstance(value, list):
        for child in value:
            _reject_identity_or_enforcement(child)

def adapt_screening_mock(request: Any) -> dict[str, Any]:
    if not isinstance(request, dict):
        raise ValueError("request must be an object")
    reject_command_fields(request)
    sample = request.get("mock_observation")
    if not isinstance(sample, dict):
        raise ValueError("mock_observation must be an object")
    _reject_identity_or_enforcement(sample)
    channels = sample.get("modality_observations")
    if not isinstance(channels, list) or not channels:
        raise ValueError("modality_observations must be a non-empty list")
    cleaned = []
    for index, channel in enumerate(channels):
        if not isinstance(channel, dict):
            raise ValueError(f"modality_observations[{index}] must be an object")
        modality = channel.get("modality")
        description = channel.get("context")
        if modality not in ALLOWED_MODALITIES:
            raise ValueError(f"modality_observations[{index}] has unsupported modality")
        if not isinstance(description, str) or not description.strip():
            raise ValueError(f"modality_observations[{index}].context must be non-empty")
        cleaned.append({"modality": modality, "context": description})
    observation = {
        "domain": "multimodal_narcotics_screening",
        "observation_type": "multimodal_context_for_human_review",
        "modality_observations": cleaned,
        "interpretation": "non_diagnostic_context_only",
    }
    return build_review_envelope(
        project_id="multimodal_narcotics_screening", request=request,
        observation=observation, modality="multimodal_mock_fixture",
        limitations=[
            "This adapter organises synthetic modality descriptions only.",
            "It does not identify chemicals, drugs or substances.",
            "It does not infer guilt, suspicion, intent or legal status.",
            "It cannot recommend detention, arrest, seizure or enforcement action.",
            "A qualified human reviewer must assess any separately validated evidence.",
        ],
    )

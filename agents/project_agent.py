"""Human-review triage agent for Multimodal Narcotics Screening AI.

This is not a narcotics classifier or chemical-identification tool. It never
infers chemical identity, criminality, or guilt from appearance. No external
services or model downloads are used.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class AgentDecision:
    project: str
    status: str
    recommendation: str
    reasons: tuple[str, ...]
    requires_human_approval: bool = True
    actuator_command: None = None

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["reasons"] = list(self.reasons)
        return result


def run_agent(observation: dict[str, Any]) -> AgentDecision:
    """Triage a manually supplied screening record for expert review.

    Optional keys: authorised_context, modalities (list), conflicting_inputs,
    sensor_ok, human_reviewed. No substances are identified or classified.
    """
    if not isinstance(observation, dict):
        raise TypeError("observation must be a dictionary")
    if observation.get("sensor_ok") is False:
        return AgentDecision("multimodal-screening", "STOP", "CHECK_SENSOR_AND_CHAIN_OF_CUSTODY",
                             ("A sensor or input-integrity check failed.",))
    if observation.get("authorised_context") is not True:
        return AgentDecision("multimodal-screening", "HOLD", "VERIFY_AUTHORITY_AND_PROCEDURE",
                             ("Authorised screening context has not been confirmed.",))
    modalities = observation.get("modalities", [])
    if not isinstance(modalities, list) or any(not isinstance(item, str) for item in modalities):
        return AgentDecision("multimodal-screening", "NEED_DATA", "CHECK_MODALITY_RECORD",
                             ("modalities must be a list of modality names.",))
    if not modalities:
        return AgentDecision("multimodal-screening", "NEED_DATA", "REQUEST_SENSOR_DATA",
                             ("No modality inputs were supplied.",))
    if observation.get("conflicting_inputs") is True:
        return AgentDecision("multimodal-screening", "REVIEW_REQUIRED", "REFER_TO_QUALIFIED_HUMAN",
                             ("Inputs conflict; do not resolve this automatically.",))
    if observation.get("human_reviewed") is not True:
        return AgentDecision("multimodal-screening", "REVIEW_REQUIRED", "REFER_TO_QUALIFIED_HUMAN",
                             ("All records remain unverified; expert review is required.",
                              "No chemical identity, contraband status, or personal culpability is inferred."))
    return AgentDecision("multimodal-screening", "REVIEW_RECORDED", "STORE_REVIEW_OUTCOME",
                         ("Human review was recorded; this agent makes no chemical-identification claim.",))

"""PUI89 SHIELD warning classification reference logic.

This module is a software policy reference only. It does not read hardware sensors,
control actuators, stop vehicles, isolate batteries, or certify safety.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class WarningState(str, Enum):
    NORMAL = "NORMAL"
    ADVISORY = "ADVISORY"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
    EMERGENCY = "EMERGENCY"
    UNKNOWN_DEGRADED = "UNKNOWN_DEGRADED"


@dataclass(frozen=True)
class HazardAssessment:
    """Evidence-bounded input to the SHIELD policy classifier."""
    observation_valid: bool
    sensor_conflict: bool = False
    advisory: bool = False
    severity: str = "unknown"
    imminent_hazard_confirmed: bool = False
    evidence_refs: Tuple[str, ...] = ()


def classify_warning(assessment: HazardAssessment) -> WarningState:
    """Return a warning state; never issue a physical command.

    Independently confirmed imminent hazards take precedence. Invalid, missing,
    conflicting or unsupported observations fail to UNKNOWN_DEGRADED. Remaining
    severity thresholds must be defined and validated separately per project.
    """
    if assessment.imminent_hazard_confirmed:
        if not assessment.evidence_refs:
            return WarningState.UNKNOWN_DEGRADED
        return WarningState.EMERGENCY

    if not assessment.observation_valid or assessment.sensor_conflict:
        return WarningState.UNKNOWN_DEGRADED

    severity = assessment.severity.lower()
    if severity in {"critical", "high", "medium", "low"} and not assessment.evidence_refs:
        return WarningState.UNKNOWN_DEGRADED
    if severity == "critical":
        return WarningState.CRITICAL
    if severity == "high":
        return WarningState.WARNING
    if assessment.advisory or severity == "medium":
        return WarningState.ADVISORY
    if severity in {"low", "none"}:
        return WarningState.NORMAL
    return WarningState.UNKNOWN_DEGRADED


def proposal_requires_human_review(*, physical_action: bool = True) -> bool:
    """Physical-action proposals require human review; this never authorizes execution."""
    return bool(physical_action)


# PUI89 Shared AI Core adapter — pinned to contract schema v0.1.0.
# These functions create advisory records only; they do not access sensors or actuators.
SHARED_CORE_SCHEMA_VERSION = "0.1.0"


def build_core_observation(*, observation_id, observed_at, source_id,
                           source_type, modality, payload, quality_status,
                           provenance, uncertainty=None, device_or_system=None):
    """Map one already-collected Sentinel input to Shared Core Observation v0.1.0."""
    if quality_status not in {"usable", "degraded", "invalid", "unknown"}:
        raise ValueError("unsupported quality_status")
    if source_type not in {"sensor", "human", "dataset", "simulation", "software", "external"}:
        raise ValueError("unsupported source_type")
    if modality not in {"rgb", "depth", "thermal", "audio", "lidar", "radar",
                        "imu", "gps", "xray", "chemical", "text", "other"}:
        raise ValueError("unsupported modality")
    if not isinstance(provenance, dict) or not provenance.get("recorded_at"):
        raise ValueError("provenance.recorded_at is required")
    if not observation_id or not observed_at or not source_id:
        raise ValueError("observation identifiers and timestamp are required")
    quality_notes = ""
    if quality_status != "usable":
        quality_notes = "Input is not eligible for a positive screening conclusion."
    record = {
        "schema_version": SHARED_CORE_SCHEMA_VERSION,
        "observation_id": observation_id,
        "observed_at": observed_at,
        "source": {"source_id": source_id, "source_type": source_type},
        "modality": modality,
        "payload": payload,
        "quality": {"status": quality_status, "notes": quality_notes},
        "provenance": dict(provenance),
    }
    if device_or_system:
        record["source"]["device_or_system"] = device_or_system
    if uncertainty is not None:
        record["uncertainty"] = dict(uncertainty)
    return record


def build_core_world_state(*, state_id, updated_at, evidence_refs,
                           entities=None, unknowns=(), conflicts=(), valid_until=None,
                           notes=""):
    """Create a time-bounded state while preserving unknowns and conflicts."""
    if not state_id or not updated_at:
        raise ValueError("state_id and updated_at are required")
    record = {
        "schema_version": SHARED_CORE_SCHEMA_VERSION,
        "state_id": state_id,
        "updated_at": updated_at,
        "evidence_refs": sorted(set(evidence_refs)),
        "entities": list(entities or []),
        "unknowns": list(unknowns),
    }
    if conflicts:
        record["conflicts"] = list(conflicts)
    if valid_until:
        record["valid_until"] = valid_until
    if notes:
        record["notes"] = notes
    return record


def build_human_review_proposal(*, proposal_id, created_at, objective,
                                action_id, description, risk_level,
                                preconditions, expected_effect, evidence_refs=(),
                                hazards=(), uncertainties=(), world_state_ref=None,
                                expires_at=None):
    """Create an advisory-only proposal. Execution is always explicitly disabled."""
    if risk_level not in {"low", "moderate", "high", "critical", "unknown"}:
        raise ValueError("unsupported risk_level")
    if not proposal_id or not created_at or not objective or not action_id or not description:
        raise ValueError("proposal identifiers, timestamp, objective and description are required")
    record = {
        "schema_version": SHARED_CORE_SCHEMA_VERSION,
        "proposal_id": proposal_id,
        "created_at": created_at,
        "objective": objective,
        "actions": [{
            "action_id": action_id,
            "description": description,
            "risk_level": risk_level,
            "preconditions": list(preconditions),
            "expected_effect": expected_effect,
            "hazards": list(hazards),
            "evidence_refs": sorted(set(evidence_refs)),
        }],
        "authority": {
            "mode": "advisory_only",
            "human_approval_required": True,
            "execution_authorized": False,
        },
        "uncertainties": list(uncertainties),
    }
    if world_state_ref:
        record["world_state_ref"] = world_state_ref
    if expires_at:
        record["expires_at"] = expires_at
    return record


def build_core_failure_report(*, failure_id, occurred_at, component, severity,
                              summary, observed_result, evidence_refs=(),
                              expected_result="", suspected_causes=(),
                              response_status="open", corrective_actions=()):
    """Record a fault/degraded condition using Shared Core FailureReport v0.1.0."""
    if severity not in {"informational", "low", "moderate", "high", "critical", "unknown"}:
        raise ValueError("unsupported severity")
    if response_status not in {"open", "contained", "investigating", "resolved", "unknown"}:
        raise ValueError("unsupported response_status")
    if not failure_id or not occurred_at or not component or not summary:
        raise ValueError("failure identifiers, timestamp, component and summary are required")
    record = {
        "schema_version": SHARED_CORE_SCHEMA_VERSION,
        "failure_id": failure_id,
        "occurred_at": occurred_at,
        "system_or_component": component,
        "severity": severity,
        "summary": summary,
        "observed_result": observed_result,
        "evidence_refs": sorted(set(evidence_refs)),
        "response_status": response_status,
    }
    if expected_result:
        record["expected_result"] = expected_result
    if suspected_causes:
        record["suspected_causes"] = list(suspected_causes)
    if corrective_actions:
        record["corrective_actions"] = list(corrective_actions)
    return record

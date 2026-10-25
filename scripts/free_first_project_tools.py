"""Free-first, offline, standard-library project validation tools.

No network, model download, paid API, telemetry, or hardware control.
"""
from __future__ import annotations
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable, Mapping


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json_report(path: str | Path, payload: Mapping[str, Any]) -> None:
    """Write deterministic, human-readable JSON locally; never uploads the report."""
    Path(path).write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def finite_unit_interval(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(value)
        and 0.0 <= value <= 1.0
    )


def required_nonempty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


ALLOWED_REVIEW_STATUSES = {"review_required", "inconclusive", "measurement_needed", "reviewed"}


def validate_evidence_record(record: Mapping[str, Any]) -> list[str]:
    """Check provenance and review fields; does not identify a substance or infer guilt."""
    errors = []
    for key in ("evidence_id", "source_reference", "modality", "captured_at", "model_version"):
        if not required_nonempty_text(record.get(key)):
            errors.append(f"{key} must be supplied and non-empty")
    status = record.get("review_status")
    if status not in ALLOWED_REVIEW_STATUSES:
        errors.append("review_status is not an allowed workflow status")
    confidence = record.get("confidence")
    if confidence is not None and not finite_unit_interval(confidence):
        errors.append("confidence must be finite and within [0, 1]")
    if record.get("modality_missing") is True or record.get("modalities_conflict") is True:
        if status not in {"review_required", "inconclusive", "measurement_needed"}:
            errors.append("missing or conflicting modalities require review/inconclusive status")
    if record.get("automated_enforcement") is True:
        errors.append("automated enforcement decisions are prohibited by this scaffold")
    return errors


def route_evidence(record: Mapping[str, Any]) -> str:
    """Conservative workflow routing, never a substance-identity decision."""
    issues = validate_evidence_record(record)
    if issues:
        return "review_required"
    if record.get("modality_missing") or record.get("modalities_conflict"):
        return "inconclusive"
    if record.get("review_status") != "reviewed":
        return "review_required"
    return "reviewed"


def binary_classification_metrics(y_true: Iterable[int | bool], y_pred: Iterable[int | bool]) -> dict[str, float | int]:
    """Compute reproducible binary metrics without third-party dependencies.

    Inputs must be equal-length, non-empty sequences containing only 0/1 or bool.
    This reports metrics; it does not certify a model or set a deployment threshold.
    """
    truth, predicted = list(y_true), list(y_pred)
    if not truth or len(truth) != len(predicted):
        raise ValueError("y_true and y_pred must be non-empty and have equal lengths")
    if any(v not in (0, 1, False, True) for v in truth + predicted):
        raise ValueError("labels must contain only binary 0/1 values")
    truth = [int(v) for v in truth]
    predicted = [int(v) for v in predicted]
    tp = sum(t == 1 and p == 1 for t, p in zip(truth, predicted))
    tn = sum(t == 0 and p == 0 for t, p in zip(truth, predicted))
    fp = sum(t == 0 and p == 1 for t, p in zip(truth, predicted))
    fn = sum(t == 1 and p == 0 for t, p in zip(truth, predicted))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "sample_count": len(truth), "tp": tp, "tn": tn, "fp": fp, "fn": fn,
        "accuracy": (tp + tn) / len(truth), "precision": precision,
        "recall": recall, "f1": f1,
    }

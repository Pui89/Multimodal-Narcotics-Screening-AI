"""Build deterministic experiment metadata and optional latency summaries.

This utility reports measurements supplied by callers. It does not validate model
accuracy or establish suitability for safety-critical decisions.
"""
from __future__ import annotations

import math
import re
import statistics
from typing import Any, Mapping, Sequence


_DIGEST_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def build_experiment_report(
    *,
    project: str,
    run_id: str,
    code_version: str,
    dataset_sha256: str,
    metrics: Mapping[str, int | float],
    latency_ms: Sequence[int | float] | None = None,
) -> dict[str, Any]:
    """Return stable JSON-compatible run metadata with sorted, finite metrics."""
    for label, value in (("project", project), ("run_id", run_id), ("code_version", code_version)):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{label} must be a non-empty string")
    if not isinstance(dataset_sha256, str) or not _DIGEST_RE.fullmatch(dataset_sha256):
        raise ValueError("dataset_sha256 must be a 64-character hexadecimal SHA-256 digest")
    if not isinstance(metrics, Mapping):
        raise ValueError("metrics must be a mapping")
    normalised_metrics: dict[str, int | float] = {}
    for key in sorted(metrics):
        if not isinstance(key, str) or not key.strip():
            raise ValueError("metric names must be non-empty strings")
        value = metrics[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"metric {key!r} must be a finite number")
        if not math.isfinite(float(value)):
            raise ValueError(f"metric {key!r} must be a finite number")
        normalised_metrics[key] = value

    latency_summary = None
    if latency_ms is not None:
        values: list[float] = []
        for value in latency_ms:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError("latency values must be finite non-negative numbers")
            numeric = float(value)
            if not math.isfinite(numeric) or numeric < 0:
                raise ValueError("latency values must be finite non-negative numbers")
            values.append(numeric)
        if values:
            ordered = sorted(values)
            nearest_rank_index = max(0, math.ceil(0.95 * len(ordered)) - 1)
            latency_summary = {
                "sample_count": len(values),
                "mean_ms": statistics.fmean(values),
                "median_ms": statistics.median(values),
                "p95_ms_nearest_rank": ordered[nearest_rank_index],
                "min_ms": ordered[0],
                "max_ms": ordered[-1],
            }
        else:
            latency_summary = {
                "sample_count": 0,
                "mean_ms": None,
                "median_ms": None,
                "p95_ms_nearest_rank": None,
                "min_ms": None,
                "max_ms": None,
            }
    return {
        "schema_version": 1,
        "project": project,
        "run_id": run_id,
        "code_version": code_version,
        "dataset_sha256": dataset_sha256.lower(),
        "metrics": normalised_metrics,
        "latency": latency_summary,
        "interpretation_limit": (
            "Caller-supplied metrics only. This report records values and provenance; "
            "it does not certify dataset validity, model accuracy, or physical safety."
        ),
    }

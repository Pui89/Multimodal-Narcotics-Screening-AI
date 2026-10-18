"""Small, dependency-free metrics for documented classification evaluations."""
from dataclasses import dataclass
import math
from typing import Sequence


@dataclass(frozen=True)
class ClassificationMetrics:
    accuracy: float
    precision: float
    recall: float
    f1: float


def classification_metrics(
    y_true: Sequence[str],
    y_pred: Sequence[str],
    positive_label: str | None = None,
) -> ClassificationMetrics:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("inputs must be non-empty and equal length")
    if any(not isinstance(label, str) or not label.strip() for label in (*y_true, *y_pred)):
        raise ValueError("labels must be non-empty strings")
    accuracy = sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true)
    if positive_label is None:
        positive_label = sorted(set(y_true) | set(y_pred))[0]
    if not isinstance(positive_label, str) or not positive_label.strip():
        raise ValueError("positive_label must be a non-empty string")
    tp = sum(a == positive_label and b == positive_label for a, b in zip(y_true, y_pred))
    fp = sum(a != positive_label and b == positive_label for a, b in zip(y_true, y_pred))
    fn = sum(a == positive_label and b != positive_label for a, b in zip(y_true, y_pred))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return ClassificationMetrics(accuracy, precision, recall, f1)


def expected_calibration_error(
    confidences: Sequence[float],
    correct: Sequence[bool],
    bins: int = 10,
) -> float:
    if len(confidences) != len(correct) or not confidences:
        raise ValueError("inputs must be non-empty and equal length")
    if not isinstance(bins, int) or isinstance(bins, bool) or bins < 1:
        raise ValueError("bins must be a positive integer")
    normalized = []
    for confidence in confidences:
        if isinstance(confidence, bool):
            raise ValueError("confidences must be finite numbers between 0 and 1")
        try:
            score = float(confidence)
        except (TypeError, ValueError) as exc:
            raise ValueError("confidences must be finite numbers between 0 and 1") from exc
        if not math.isfinite(score) or not 0.0 <= score <= 1.0:
            raise ValueError("confidences must be finite numbers between 0 and 1")
        normalized.append(score)
    if any(not isinstance(value, bool) for value in correct):
        raise ValueError("correct values must be booleans")
    total, error = len(normalized), 0.0
    for i in range(bins):
        lo, hi = i / bins, (i + 1) / bins
        members = [
            j for j, score in enumerate(normalized)
            if lo <= score < hi or (i == bins - 1 and score == hi)
        ]
        if members:
            avg_conf = sum(normalized[j] for j in members) / len(members)
            avg_acc = sum(correct[j] for j in members) / len(members)
            error += len(members) / total * abs(avg_conf - avg_acc)
    return error

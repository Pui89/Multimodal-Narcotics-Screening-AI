"""Reproducible JSONL evaluation runner.

Input records require y_true, y_pred and confidence. The reported correctness
used for calibration is derived from y_true/y_pred to prevent contradictory
hand-entered correctness flags from silently changing calibration metrics.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

try:
    from .metrics import classification_metrics, expected_calibration_error
except ImportError:  # Support direct execution: python evaluation/run_evaluation.py
    from metrics import classification_metrics, expected_calibration_error


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSON on line {line_number}: {exc.msg}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"line {line_number} must contain a JSON object")
        rows.append(row)
    if not rows:
        raise ValueError("input contains no prediction records")
    return rows


def evaluate(rows: list[dict], positive_label: str | None = None) -> dict:
    if not rows:
        raise ValueError("at least one prediction record is required")

    y_true = []
    y_pred = []
    confidence = []
    correct = []
    for index, row in enumerate(rows, start=1):
        missing = {"y_true", "y_pred", "confidence"} - row.keys()
        if missing:
            raise ValueError(f"record {index} missing required fields: {', '.join(sorted(missing))}")
        if not isinstance(row["y_true"], str) or not row["y_true"].strip():
            raise ValueError(f"record {index} y_true must be a non-empty string")
        if not isinstance(row["y_pred"], str) or not row["y_pred"].strip():
            raise ValueError(f"record {index} y_pred must be a non-empty string")
        score = float(row["confidence"])
        if not math.isfinite(score) or not 0.0 <= score <= 1.0:
            raise ValueError(f"record {index} confidence must be finite and between 0 and 1")
        if "correct" in row and not isinstance(row["correct"], bool):
            raise ValueError(f"record {index} optional correct field must be a boolean")
        actual_correct = row["y_true"] == row["y_pred"]
        if "correct" in row and row["correct"] != actual_correct:
            raise ValueError(f"record {index} correct flag contradicts y_true/y_pred")
        y_true.append(str(row["y_true"]))
        y_pred.append(str(row["y_pred"]))
        confidence.append(score)
        correct.append(actual_correct)

    if positive_label is None:
        positive_label = "review" if "review" in set(y_true) | set(y_pred) else sorted(set(y_true) | set(y_pred))[0]
    if positive_label not in set(y_true) | set(y_pred):
        raise ValueError(f"positive label {positive_label!r} does not occur in labels")
    metrics = classification_metrics(y_true, y_pred, positive_label=positive_label)
    return {
        "positive_label": positive_label,
        "n": len(rows),
        "accuracy": metrics.accuracy,
        "precision": metrics.precision,
        "recall": metrics.recall,
        "f1": metrics.f1,
        "ece": expected_calibration_error(confidence, correct),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("reports/evaluation.json"))
    parser.add_argument("--positive-label", help="Label treated as positive; defaults to review when present, otherwise the alphabetically first label.")
    args = parser.parse_args()
    result = evaluate(load_jsonl(args.input), positive_label=args.positive_label)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

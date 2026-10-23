import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from evaluation.run_evaluation import evaluate, load_jsonl


class EvaluationRunnerTests(unittest.TestCase):
    def test_computes_metrics_from_prediction_labels(self):
        result = evaluate([
            {"y_true": "review", "y_pred": "review", "confidence": 0.9},
            {"y_true": "clear", "y_pred": "review", "confidence": 0.8},
        ])
        self.assertEqual(result["n"], 2)
        self.assertAlmostEqual(result["accuracy"], 0.5)
        self.assertAlmostEqual(result["precision"], 0.5)
        self.assertAlmostEqual(result["recall"], 1.0)
        self.assertEqual(result["positive_label"], "review")

    def test_rejects_correct_flag_that_contradicts_labels(self):
        with self.assertRaisesRegex(ValueError, "contradicts"):
            evaluate([{
                "y_true": "review", "y_pred": "review",
                "confidence": 0.9, "correct": False,
            }])

    def test_rejects_non_finite_or_out_of_range_confidence(self):
        for confidence in (-0.1, 1.1, float("nan"), float("inf")):
            with self.subTest(confidence=confidence), self.assertRaisesRegex(ValueError, "confidence"):
                evaluate([{"y_true": "a", "y_pred": "a", "confidence": confidence}])

    def test_rejects_non_numeric_or_boolean_confidence(self):
        for confidence in (True, False, "0.9", None, [], {}):
            with self.subTest(confidence=confidence), self.assertRaisesRegex(ValueError, "confidence"):
                evaluate([{"y_true": "a", "y_pred": "a", "confidence": confidence}])

    def test_rejects_empty_or_non_string_labels(self):
        for row in (
            {"y_true": "", "y_pred": "review", "confidence": 0.5},
            {"y_true": "review", "y_pred": 2, "confidence": 0.5},
        ):
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, "y_true|y_pred"):
                evaluate([row])

    def test_rejects_missing_fields_and_empty_input(self):
        with self.assertRaisesRegex(ValueError, "required fields"):
            evaluate([{"y_true": "a", "confidence": 0.5}])
        with self.assertRaisesRegex(ValueError, "at least one"):
            evaluate([])

    def test_load_jsonl_rejects_duplicate_keys_with_line_number(self):
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "predictions.jsonl"
            path.write_text(
                '{"y_true":"review","y_pred":"clear","confidence":0.1,"confidence":0.99}\n',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate JSON key on line 1"):
                load_jsonl(path)

    def test_load_jsonl_rejects_duplicate_nested_keys(self):
        with TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "predictions.jsonl"
            path.write_text(
                '{"y_true":"review","y_pred":"clear","confidence":0.8,"metadata":{"source":"A","source":"B"}}\n',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate JSON key on line 1"):
                load_jsonl(path)


if __name__ == "__main__":
    unittest.main()

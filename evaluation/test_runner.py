import unittest

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

    def test_rejects_missing_fields_and_empty_input(self):
        with self.assertRaisesRegex(ValueError, "required fields"):
            evaluate([{"y_true": "a", "confidence": 0.5}])
        with self.assertRaisesRegex(ValueError, "at least one"):
            evaluate([])


if __name__ == "__main__":
    unittest.main()

"""Edge cases for dependency-free classification metrics.

Metrics are meaningful only for an explicitly defined evaluation dataset and
label policy; these tests do not claim screening accuracy on real-world data.
"""
import unittest

from evaluation.metrics import classification_metrics


class ClassificationMetricsEdgeCaseTests(unittest.TestCase):
    def test_all_predictions_wrong_produce_zero_f1_for_positive_class(self):
        result = classification_metrics(
            ["review", "review"],
            ["clear", "clear"],
            positive_label="review",
        )
        self.assertEqual(result.accuracy, 0.0)
        self.assertEqual(result.precision, 0.0)
        self.assertEqual(result.recall, 0.0)
        self.assertEqual(result.f1, 0.0)

    def test_positive_class_absent_from_both_sequences_is_zero_not_division_error(self):
        result = classification_metrics(
            ["clear", "clear"],
            ["clear", "clear"],
            positive_label="review",
        )
        self.assertEqual(result.accuracy, 1.0)
        self.assertEqual(result.precision, 0.0)
        self.assertEqual(result.recall, 0.0)
        self.assertEqual(result.f1, 0.0)

    def test_calibration_rejects_integer_too_large_to_convert_to_float(self):
        from evaluation.metrics import expected_calibration_error

        with self.assertRaisesRegex(ValueError, "finite numbers between 0 and 1"):
            expected_calibration_error([10**10000], [True])

    def test_default_positive_label_is_deterministic(self):
        result = classification_metrics(["z", "a"], ["z", "a"])
        self.assertEqual(result.accuracy, 1.0)
        self.assertEqual(result.precision, 1.0)
        self.assertEqual(result.recall, 1.0)
        self.assertEqual(result.f1, 1.0)


if __name__ == "__main__":
    unittest.main()

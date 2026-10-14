import unittest

from evaluation.metrics import classification_metrics, expected_calibration_error


class MetricsTests(unittest.TestCase):
    def test_binary_metrics_with_explicit_positive_label(self):
        result = classification_metrics(
            ["review", "clear", "review", "clear"],
            ["review", "review", "clear", "clear"],
            positive_label="review",
        )
        self.assertAlmostEqual(result.accuracy, 0.5)
        self.assertAlmostEqual(result.precision, 0.5)
        self.assertAlmostEqual(result.recall, 0.5)
        self.assertAlmostEqual(result.f1, 0.5)

    def test_empty_or_mismatched_classification_inputs_rejected(self):
        with self.assertRaises(ValueError):
            classification_metrics([], [])
        with self.assertRaises(ValueError):
            classification_metrics(["a"], ["a", "b"])

    def test_perfect_calibration_has_zero_error(self):
        self.assertAlmostEqual(expected_calibration_error([1.0, 0.0], [True, False]), 0.0)

    def test_confidence_bounds_validated(self):
        for value in (-0.01, 1.01):
            with self.subTest(value=value), self.assertRaises(ValueError):
                expected_calibration_error([value], [True])

    def test_bins_must_be_positive(self):
        with self.assertRaises(ValueError):
            expected_calibration_error([0.5], [True], bins=0)

    def test_calibration_error_is_bounded(self):
        score = expected_calibration_error([0.9, 0.9, 0.1, 0.1], [False, False, True, True])
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)


if __name__ == "__main__":
    unittest.main()

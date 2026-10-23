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

    def test_empty_labels_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "non-empty strings"):
            classification_metrics([""], ["clear"])

    def test_perfect_calibration_has_zero_error(self):
        self.assertAlmostEqual(expected_calibration_error([1.0, 0.0], [True, False]), 0.0)

    def test_confidence_bounds_and_finiteness_validated(self):
        for value in (-0.01, 1.01, float("nan"), float("inf"), float("-inf"), True, None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                expected_calibration_error([value], [True])

    def test_bins_must_be_positive_integer(self):
        for bins in (0, -1, 1.5, True):
            with self.subTest(bins=bins), self.assertRaises(ValueError):
                expected_calibration_error([0.5], [True], bins=bins)

    def test_correctness_values_must_be_boolean(self):
        with self.assertRaisesRegex(ValueError, "booleans"):
            expected_calibration_error([0.5], [1])

    def test_positive_label_must_be_non_empty_string(self):
        for positive_label in ("", "   ", None, 1):
            with self.subTest(positive_label=positive_label), self.assertRaises(ValueError):
                classification_metrics(["clear"], ["clear"], positive_label=positive_label)

    def test_ece_assigns_confidence_one_to_final_bin(self):
        # A confidence of exactly 1.0 belongs in the last bin and is not dropped.
        self.assertAlmostEqual(expected_calibration_error([1.0], [True], bins=10), 0.0)
        self.assertAlmostEqual(expected_calibration_error([1.0], [False], bins=10), 1.0)

    def test_calibration_error_is_bounded(self):
        score = expected_calibration_error([0.9, 0.9, 0.1, 0.1], [False, False, True, True])
        self.assertGreaterEqual(score, 0.0)
        self.assertLessEqual(score, 1.0)


if __name__ == "__main__":
    unittest.main()

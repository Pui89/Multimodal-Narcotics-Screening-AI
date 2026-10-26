import unittest
from scripts.free_first_project_tools import validate_evidence_record, route_evidence, binary_classification_metrics

BASE={"evidence_id":"E-001","source_reference":"case-ref-001","modality":"image",
      "captured_at":"2026-10-25T10:00:00Z","model_version":"not-run",
      "confidence":None,"review_status":"review_required"}

class FreeFirstTests(unittest.TestCase):
    def test_missing_modality_routes_to_inconclusive(self):
        record={**BASE,"modality_missing":True,"review_status":"inconclusive"}
        self.assertEqual(route_evidence(record),"inconclusive")
        self.assertEqual(validate_evidence_record(record),[])

    def test_conflicting_modalities_cannot_be_auto_reviewed(self):
        record={**BASE,"modalities_conflict":True,"review_status":"reviewed"}
        self.assertTrue(any("require review" in e for e in validate_evidence_record(record)))

    def test_missing_provenance_requires_review(self):
        record={**BASE,"source_reference":""}
        self.assertEqual(route_evidence(record),"review_required")

    def test_automated_enforcement_is_rejected(self):
        self.assertTrue(any("prohibited" in e for e in validate_evidence_record({**BASE,"automated_enforcement":True})))

    def test_malformed_review_status_does_not_crash(self):
        record={**BASE,"review_status":[]}
        self.assertTrue(validate_evidence_record(record))
        self.assertEqual(route_evidence(record),"review_required")

    def test_reviewed_record_requires_review_provenance(self):
        missing_reviewer={**BASE,"review_status":"reviewed"}
        self.assertTrue(any("reviewer_reference" in e for e in validate_evidence_record(missing_reviewer)))
        self.assertEqual(route_evidence(missing_reviewer),"review_required")

        record={**BASE,"review_status":"reviewed","reviewer_reference":"reviewer-role-01",
                "reviewed_at":"2026-10-26T10:00:00Z"}
        self.assertEqual(validate_evidence_record(record),[])
        self.assertEqual(route_evidence(record),"reviewed")


    def test_binary_metrics_match_hand_calculation(self):
        result = binary_classification_metrics([1, 1, 0, 0], [1, 0, 1, 0])
        self.assertEqual((result["tp"], result["tn"], result["fp"], result["fn"]), (1, 1, 1, 1))
        self.assertEqual(result["accuracy"], 0.5)
        self.assertEqual(result["precision"], 0.5)
        self.assertEqual(result["recall"], 0.5)
        self.assertEqual(result["f1"], 0.5)

    def test_binary_metrics_reject_empty_or_mismatched_inputs(self):
        with self.assertRaises(ValueError):
            binary_classification_metrics([], [])
        with self.assertRaises(ValueError):
            binary_classification_metrics([1], [1, 0])

    def test_binary_metrics_handle_zero_division(self):
        result = binary_classification_metrics([0, 0], [0, 0])
        self.assertEqual(result["precision"], 0.0)
        self.assertEqual(result["recall"], 0.0)
        self.assertEqual(result["f1"], 0.0)

if __name__ == "__main__": unittest.main()

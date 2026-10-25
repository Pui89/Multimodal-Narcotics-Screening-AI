import unittest
from scripts.free_first_project_tools import validate_evidence_record, route_evidence

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

    def test_reviewed_record_can_pass_workflow_validation(self):
        record={**BASE,"review_status":"reviewed"}
        self.assertEqual(validate_evidence_record(record),[])
        self.assertEqual(route_evidence(record),"reviewed")

if __name__ == "__main__": unittest.main()

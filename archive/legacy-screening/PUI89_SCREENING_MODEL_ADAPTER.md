# Multimodal Screening — PUI89 Project Model Adapter

**Status:** mock-only; model inference is disabled.

The adapter is `tools/pui89_screening_model_adapter.py`. It accepts synthetic modality-context fixtures (RGB, thermal, acoustic, depth or LiDAR) and emits non-diagnostic context for qualified human review.

It rejects chemical identity, substance name, drug name, guilt, suspect score and enforcement fields at any level of the request. It also rejects physical command fields. Accepted outputs always request human review and contain no proposed actions.

Evidence must be explicitly marked `synthetic`, use a `synthetic://` source reference, include timestamp and lineage, and not be future-dated relative to the request. This is not a chemical identification, contraband detection, suspicion scoring or enforcement system.

Run tests: `PYTHONPATH=tools python -m unittest discover -s tests -p "test_pui89_screening_model_adapter.py" -v`.

No model weights, third-party packages, network calls, paid APIs, cloud GPUs or hardware are used. This tests the software boundary only.
"""Interactive front end for the multimodal screening evidence-review API.

Uploaded images are preview-only. No substance is identified from pixels and no
trained detector is run by this dashboard.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

import requests
import streamlit as st

st.set_page_config(page_title="Multimodal Screening AI", page_icon="🔎", layout="wide")
st.title("🔎 Multimodal Narcotics Screening AI")
st.caption("Research prototype · Multimodal evidence review · Human-supervised screening")
st.warning(
    "This is a research demonstration, not a validated narcotics detector. It cannot identify a substance "
    "from a photo, prove chemical identity, accuse a person, authorize a search or seizure, or control a robot. "
    "Use only lawfully obtained data and authorized procedures."
)

with st.sidebar:
    st.header("API connection")
    api_url = st.text_input("API base URL", value="http://127.0.0.1:8000").rstrip("/")
    st.markdown("[Interactive API docs](http://127.0.0.1:8000/docs)")
    st.caption("Start the FastAPI service in one terminal and this dashboard in another.")

left, right = st.columns([1, 1], gap="large")
with left:
    st.subheader("1 · Observation context")
    observation_id = st.text_input("Observation ID", value="screening-demo-001", max_chars=100)
    uploaded = st.file_uploader("Optional reference image (preview only)", type=["png", "jpg", "jpeg", "webp"])
    if uploaded is not None:
        st.image(uploaded, caption="Reference image only — not analyzed by this demo", use_container_width=True)
    st.markdown("**Sensor quality**")
    rgb_valid = st.checkbox("RGB camera data valid", value=True)
    depth_valid = st.checkbox("Depth data valid", value=True)
    thermal_valid = st.checkbox("Thermal data available and valid", value=False)
    lidar_valid = st.checkbox("LiDAR data available and valid", value=False)
    timestamp_skew_ms = st.slider("Timestamp difference (ms)", min_value=0, max_value=250, value=12)

with right:
    st.subheader("2 · Example evidence features")
    st.caption("Adjustable synthetic/manual values. They are not measurements extracted from your uploaded image.")
    visual_anomaly_score = st.slider("Visual anomaly feature score", 0.0, 1.0, 0.62, 0.01)
    depth_enabled = st.checkbox("Include depth-consistency score", value=True)
    depth_consistency_score = st.slider("Depth consistency", 0.0, 1.0, 0.82, 0.01) if depth_enabled else None
    temporal_consistency_score = st.slider("Temporal consistency", 0.0, 1.0, 0.85, 0.01)
    ood_score = st.slider("Out-of-distribution (unfamiliar input) score", 0.0, 1.0, 0.12, 0.01)
    st.caption("High anomaly or unfamiliarity scores are not evidence that narcotics are present.")

payload = {
    "observation_id": observation_id.strip() or "screening-demo",
    "rgb_valid": rgb_valid,
    "depth_valid": depth_valid,
    "thermal_valid": thermal_valid,
    "lidar_valid": lidar_valid,
    "timestamp_skew_ms": timestamp_skew_ms,
    "visual_anomaly_score": visual_anomaly_score,
    "depth_consistency_score": depth_consistency_score,
    "temporal_consistency_score": temporal_consistency_score,
    "ood_score": ood_score,
}

with st.expander("View request payload"):
    st.json(payload)

if st.button("Review example evidence", type="primary", use_container_width=True):
    try:
        response = requests.post(f"{api_url}/screen", json=payload, timeout=10)
        response.raise_for_status()
        st.session_state["screening_result"] = response.json()
        st.session_state["screening_payload"] = payload
        st.session_state["screening_timestamp"] = datetime.now(timezone.utc).isoformat()
    except requests.RequestException as exc:
        st.error(f"Could not reach API at {api_url}. Start the API first. Details: {exc}")

result = st.session_state.get("screening_result")
if result:
    st.divider()
    st.subheader("3 · Evidence-review output")
    a, b, c = st.columns(3)
    a.metric("Screening status", result.get("decision", "UNKNOWN"))
    b.metric("Review status", result.get("review_status", "HUMAN_REVIEW"))
    c.metric("Chemical identity established", "No")
    reasons = result.get("reasons", [])
    if reasons:
        st.error("Quality / uncertainty flags: " + ", ".join(reasons))
    else:
        st.info("No configured quality flag was triggered. This is not proof that an item is safe or contains any particular substance.")
    st.write("**Missing modalities:**", ", ".join(result.get("missing_modalities", [])) or "None flagged by these inputs")
    st.write("**Evidence triage score:**", result.get("evidence_score", "Not available"))
    st.caption("The score is a heuristic for demonstration, not a calibrated probability or chemical identification.")
    st.json(result)
    report = {
        "created_at_utc": st.session_state.get("screening_timestamp"),
        "demo_only": True,
        "image_inference_performed": False,
        "request": st.session_state.get("screening_payload"),
        "response": result,
    }
    st.download_button(
        "Download review report (JSON)",
        data=json.dumps(report, indent=2),
        file_name="multimodal_screening_demo_report.json",
        mime="application/json",
    )

st.divider()
st.caption(
    "No enforcement decisions, chemical conclusions or robot commands are made. A screening anomaly is only a "
    "hypothesis for authorized human review; use validated analytical procedures for chemical identification."
)

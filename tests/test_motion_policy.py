import math

import pytest

from narcotics_platform.motion_policy import MotionObservation, decide_motion


def observe(**overrides):
    values = dict(
        requested_speed_mps=1.0,
        speed_cap_mps=1.2,
        obstacle_distance_m=3.0,
        pedestrian_distance_m=4.0,
        localization_confidence=0.95,
        obstacle_sensor_healthy=True,
        communications_healthy=True,
        emergency_stop=False,
    )
    values.update(overrides)
    return MotionObservation(**values)


def test_clear_path_respects_requested_speed_and_cap():
    assert decide_motion(observe()).commanded_speed_mps == 1.0
    assert decide_motion(observe(requested_speed_mps=2.0)).commanded_speed_mps == 1.2


@pytest.mark.parametrize(
    "overrides",
    [
        {"emergency_stop": True},
        {"obstacle_sensor_healthy": False},
        {"communications_healthy": False},
        {"localization_confidence": 0.69},
        {"obstacle_distance_m": 0.49},
        {"pedestrian_distance_m": 0.79},
    ],
)
def test_critical_condition_fails_closed(overrides):
    decision = decide_motion(observe(**overrides))
    assert decision.commanded_speed_mps == 0.0
    assert decision.state == "SAFE_STOP"
    assert decision.reasons


def test_near_obstacle_reduces_speed():
    decision = decide_motion(observe(obstacle_distance_m=1.0))
    assert decision.commanded_speed_mps <= 0.20
    assert "near_obstacle_slowdown" in decision.reasons


def test_near_pedestrian_yields_at_reduced_speed():
    decision = decide_motion(observe(pedestrian_distance_m=1.5))
    assert decision.commanded_speed_mps <= 0.15
    assert "pedestrian_yield_speed" in decision.reasons


def test_moderate_localization_confidence_reduces_speed():
    decision = decide_motion(observe(localization_confidence=0.80))
    assert decision.commanded_speed_mps <= 0.20
    assert "reduced_localization_confidence" in decision.reasons


@pytest.mark.parametrize(
    "field,value",
    [
        ("requested_speed_mps", math.nan),
        ("requested_speed_mps", math.inf),
        ("speed_cap_mps", -0.1),
        ("obstacle_distance_m", math.nan),
        ("pedestrian_distance_m", -1.0),
        ("localization_confidence", math.inf),
        ("localization_confidence", 1.1),
        ("emergency_stop", "false"),
        ("obstacle_sensor_healthy", 1),
    ],
)
def test_malformed_or_unsafe_inputs_fail_closed(field, value):
    decision = decide_motion(observe(**{field: value}))
    assert decision.commanded_speed_mps == 0.0
    assert decision.state == "SAFE_STOP"


def test_non_observation_fails_closed():
    assert decide_motion(None).commanded_speed_mps == 0.0

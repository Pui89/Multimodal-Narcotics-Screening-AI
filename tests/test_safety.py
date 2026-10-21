from __future__ import annotations

import math

import pytest

from narcotics_platform.safety import NavigationState, SafetyGate


def test_safe_motion():
    assert SafetyGate().allow_motion(NavigationState(0.95, 2.0))


def test_low_localization_blocks():
    assert not SafetyGate().allow_motion(NavigationState(0.50, 2.0))


def test_human_and_estop_block():
    gate = SafetyGate()
    assert not gate.allow_motion(NavigationState(0.95, 2.0, human_in_exclusion_zone=True))
    assert not gate.allow_motion(NavigationState(0.95, 2.0, emergency_stop=True))


@pytest.mark.parametrize("value", [math.nan, math.inf, -math.inf, -0.1, 1.1, True, "0.8", None])
def test_invalid_localization_confidence_fails_closed(value):
    assert not SafetyGate().allow_motion(NavigationState(value, 2.0))


@pytest.mark.parametrize("value", [math.nan, math.inf, -math.inf, -0.1, True, "2.0", None])
def test_invalid_obstacle_distance_fails_closed(value):
    assert not SafetyGate().allow_motion(NavigationState(0.95, value))


@pytest.mark.parametrize("value", [1, 0, "false", None])
def test_non_boolean_safety_flags_fail_closed(value):
    assert not SafetyGate().allow_motion(
        NavigationState(0.95, 2.0, human_in_exclusion_zone=value)
    )
    assert not SafetyGate().allow_motion(NavigationState(0.95, 2.0, emergency_stop=value))


@pytest.mark.parametrize("value", [math.nan, math.inf, -math.inf, -0.1, 1.1, True, "0.7", None])
def test_invalid_localization_threshold_rejected_at_configuration(value):
    with pytest.raises(ValueError, match="min_localization_confidence"):
        SafetyGate(min_localization_confidence=value)


@pytest.mark.parametrize("value", [math.nan, math.inf, -math.inf, -0.1, True, "0.5", None])
def test_invalid_obstacle_threshold_rejected_at_configuration(value):
    with pytest.raises(ValueError, match="min_obstacle_distance_m"):
        SafetyGate(min_obstacle_distance_m=value)


def test_non_navigation_state_fails_closed():
    assert not SafetyGate().allow_motion(None)

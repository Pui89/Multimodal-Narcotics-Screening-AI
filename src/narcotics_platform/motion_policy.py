"""Deterministic speed policy for the synthetic quadruped screening demo.

This is a software policy example, not a certified safety controller and not
connected to robot hardware. Distances/confidence must come from validated
sensors before any real-world use.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class MotionObservation:
    requested_speed_mps: float
    speed_cap_mps: float
    obstacle_distance_m: float
    pedestrian_distance_m: float | None = None
    localization_confidence: float = 1.0
    obstacle_sensor_healthy: bool = True
    communications_healthy: bool = True
    emergency_stop: bool = False


@dataclass(frozen=True)
class MotionDecision:
    commanded_speed_mps: float
    state: str
    reasons: tuple[str, ...]


def _finite_nonnegative(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
        and value >= 0
    )


def decide_motion(observation: MotionObservation) -> MotionDecision:
    """Return a conservative speed command; malformed or unsafe input stops."""
    if not isinstance(observation, MotionObservation):
        return MotionDecision(0.0, "SAFE_STOP", ("invalid_observation",))

    o = observation
    if (
        not _finite_nonnegative(o.requested_speed_mps)
        or not _finite_nonnegative(o.speed_cap_mps)
        or not _finite_nonnegative(o.obstacle_distance_m)
        or (
            o.pedestrian_distance_m is not None
            and not _finite_nonnegative(o.pedestrian_distance_m)
        )
        or isinstance(o.localization_confidence, bool)
        or not isinstance(o.localization_confidence, (int, float))
        or not math.isfinite(o.localization_confidence)
        or not 0.0 <= o.localization_confidence <= 1.0
        or not isinstance(o.obstacle_sensor_healthy, bool)
        or not isinstance(o.communications_healthy, bool)
        or not isinstance(o.emergency_stop, bool)
    ):
        return MotionDecision(0.0, "SAFE_STOP", ("invalid_or_nonfinite_input",))

    reasons: list[str] = []
    if o.emergency_stop:
        reasons.append("emergency_stop")
    if not o.obstacle_sensor_healthy:
        reasons.append("obstacle_sensor_unhealthy")
    if not o.communications_healthy:
        reasons.append("communications_unhealthy")
    if o.localization_confidence < 0.70:
        reasons.append("localization_confidence_low")
    if o.obstacle_distance_m < 0.50:
        reasons.append("obstacle_too_close")
    if o.pedestrian_distance_m is not None and o.pedestrian_distance_m < 0.80:
        reasons.append("pedestrian_in_protective_zone")

    if reasons:
        return MotionDecision(0.0, "SAFE_STOP", tuple(reasons))

    command = min(o.requested_speed_mps, o.speed_cap_mps)
    if o.obstacle_distance_m < 1.50:
        command = min(command, 0.20)
        reasons.append("near_obstacle_slowdown")
    if o.pedestrian_distance_m is not None and o.pedestrian_distance_m < 2.00:
        command = min(command, 0.15)
        reasons.append("pedestrian_yield_speed")
    if o.localization_confidence < 0.85:
        command = min(command, 0.20)
        reasons.append("reduced_localization_confidence")

    state = "SLOW" if reasons else "CLEAR"
    return MotionDecision(round(max(0.0, command), 3), state, tuple(reasons))

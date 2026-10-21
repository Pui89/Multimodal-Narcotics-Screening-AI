"""Unit tests for the ROS 2 / Nav2 / Gazebo / Open3D environment preflight."""
import importlib.util
import subprocess
from pathlib import Path
from types import SimpleNamespace

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "check_robotics_stack.py"
SPEC = importlib.util.spec_from_file_location("check_robotics_stack", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


def test_command_check_reports_missing_executable(monkeypatch, capsys):
    monkeypatch.setattr(CHECKER.shutil, "which", lambda _name: None)

    assert CHECKER.command_check("ROS CLI", ["ros2", "--help"]) is False
    assert "executable 'ros2' not found" in capsys.readouterr().out


def test_command_check_reports_success(monkeypatch, capsys):
    monkeypatch.setattr(CHECKER.shutil, "which", lambda _name: "/usr/bin/ros2")
    monkeypatch.setattr(
        CHECKER.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0, stdout="", stderr=""),
    )

    assert CHECKER.command_check("ROS CLI", ["ros2", "--help"]) is True
    assert "OK       ROS CLI" in capsys.readouterr().out


def test_command_check_reports_nonzero_exit(monkeypatch, capsys):
    monkeypatch.setattr(CHECKER.shutil, "which", lambda _name: "/usr/bin/ros2")
    monkeypatch.setattr(
        CHECKER.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(
            returncode=2, stdout="", stderr="package unavailable\n"
        ),
    )

    assert CHECKER.command_check("Nav2", ["ros2", "pkg", "prefix", "nav2"]) is False
    assert "command exited 2 (package unavailable)" in capsys.readouterr().out


def test_command_check_handles_timeout(monkeypatch, capsys):
    monkeypatch.setattr(CHECKER.shutil, "which", lambda _name: "/usr/bin/ros2")

    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired(cmd="ros2 --help", timeout=10)

    monkeypatch.setattr(CHECKER.subprocess, "run", timeout)

    assert CHECKER.command_check("ROS CLI", ["ros2", "--help"]) is False
    assert "MISSING  ROS CLI" in capsys.readouterr().out

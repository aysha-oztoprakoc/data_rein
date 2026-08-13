from __future__ import annotations

import asyncio  # noqa: F401  # noqa: ANYIO_OK
import importlib.util
from pathlib import Path
from subprocess import CompletedProcess
from typing import cast

from textual.widgets import TabbedContent

from reins.harness import (
    sofia_controls,
    sofia_health,
    sofia_styles,
    sofia_types,
    sofia_widgets,
)


SOFIA_MODULES = (
    sofia_controls,
    sofia_health,
    sofia_styles,
    sofia_types,
    sofia_widgets,
)


def _dashboard_type():
    script = Path(__file__).parents[1] / "scripts" / "sofia_protocol.py"
    spec = importlib.util.spec_from_file_location("sofia_protocol", script)
    if spec is None or spec.loader is None:
        raise ImportError(f"could not load {script}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return cast(type, module.SofiaDashboard)


def test_sofia_number_keys_reach_every_tab(monkeypatch) -> None:
    assert all(module.__name__.startswith("reins.harness.sofia_") for module in SOFIA_MODULES)
    app = _dashboard_type()()
    monkeypatch.setattr(app, "_trigger_health_check", lambda: None)
    monkeypatch.setattr(app, "start_mqtt_listener", lambda: None)

    async def exercise() -> list[str]:
        observed: list[str] = []
        async with app.run_test(size=(100, 36)) as pilot:
            tabs = app.query_one(TabbedContent)
            for key in ("1", "2", "3", "4", "5"):
                await pilot.press(key)
                await pilot.pause()
                observed.append(tabs.active)
        return observed

    assert asyncio.run(exercise()) == [
        "agent-center",
        "process-monitor",
        "task-trail",
        "hardware-info",
        "kernel-tuning",
    ]


def test_privileged_controls_reject_hostile_values_without_execution(monkeypatch) -> None:
    # Given hostile values at each privileged control boundary.
    calls: list[tuple[list[str], str | None]] = []
    messages: list[str] = []
    monkeypatch.setattr(
        sofia_controls,
        "run_sudo_cmd",
        lambda command, *, input_text=None: calls.append((command, input_text))
        or CompletedProcess(command, 0, "", ""),
    )

    # When the dashboard receives shell-shaped governor, cap, and PID values.
    sofia_controls.set_cpu_governor("performance;id", messages.append)
    sofia_controls.set_gpu_power("1$(id)", messages.append)
    sofia_controls.kill_pid("-1", messages.append)
    sofia_controls.renice_pid("-1", messages.append)

    # Then no privileged process is started.
    assert calls == []
    assert len(messages) == 4


def test_privileged_controls_use_exact_tee_argv_and_stdin(monkeypatch, tmp_path) -> None:
    # Given readable governor and GPU sysfs controls with an explicit safe range.
    governor = tmp_path / "scaling_governor"
    governor.write_text("powersave\n", encoding="utf-8")
    hwmon = tmp_path / "hwmon0"
    hwmon.mkdir()
    (hwmon / "power1_cap").write_text("150\n", encoding="utf-8")
    (hwmon / "power1_cap_min").write_text("100\n", encoding="utf-8")
    (hwmon / "power1_cap_max").write_text("200\n", encoding="utf-8")
    calls: list[tuple[list[str], str | None]] = []
    monkeypatch.setattr(
        sofia_controls.glob,
        "glob",
        lambda pattern: [str(governor)] if "scaling_governor" in pattern else [str(hwmon)],
    )
    monkeypatch.setattr(
        sofia_controls,
        "run_sudo_cmd",
        lambda command, *, input_text=None: calls.append((command, input_text))
        or CompletedProcess(command, 0, "", ""),
    )

    # When valid settings cross the privileged boundary.
    sofia_controls.set_cpu_governor("performance", lambda _message: None)
    sofia_controls.set_gpu_power("175", lambda _message: None)

    # Then only exact tee argv receives the value over stdin, never a shell program.
    assert calls == [
        (["tee", str(governor)], "performance\n"),
        (["tee", str(hwmon / "power1_cap")], "175\n"),
    ]
    assert all("bash" not in command and "-c" not in command for command, _stdin in calls)


def test_agent_controls_reject_non_positive_discovered_pids(monkeypatch) -> None:
    # Given process discovery returns a hostile non-positive PID.
    calls: list[list[str]] = []
    monkeypatch.setattr(sofia_controls, "find_agent_pids", lambda _agent: [-1])
    monkeypatch.setattr(
        sofia_controls.external_io,
        "run",
        lambda *_args, **_kwargs: CompletedProcess([], 1, "", "missing window"),
    )
    monkeypatch.setattr(
        sofia_controls,
        "run_sudo_cmd",
        lambda command, *, input_text=None: calls.append(command)
        or CompletedProcess(command, 0, "", ""),
    )

    # When agent-wide kill and renice controls run.
    sofia_controls.kill_agent("data-hermes", lambda _message: None)
    sofia_controls.renice_agent("data-hermes", -10, lambda _message: None)

    # Then the discovered PID never crosses the privileged boundary.
    assert calls == []

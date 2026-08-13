from __future__ import annotations

import glob
from collections.abc import Callable
from enum import StrEnum
from pathlib import Path

from reins.harness import external_io
from reins.harness.sofia_types import find_agent_pids
from reins.services import resource_budgets
from reins.services.sudo_exec import run_sudo_cmd

LogEvent = Callable[[str], None]


class CpuGovernor(StrEnum):
    CONSERVATIVE = "conservative"
    ONDEMAND = "ondemand"
    PERFORMANCE = "performance"
    POWERSAVE = "powersave"
    SCHEDUTIL = "schedutil"
    USERSPACE = "userspace"


def _positive_pid(raw_pid: str) -> str | None:
    return raw_pid if raw_pid.isdecimal() and int(raw_pid) > 0 else None


def kill_pid(pid: str, log_event: LogEvent) -> None:
    valid_pid = _positive_pid(pid)
    if valid_pid is None:
        log_event("Invalid PID; expected a positive integer.")
        return
    log_event(f"[bold #ff1100][SUDO][/] Killing PID {valid_pid}...")
    result = run_sudo_cmd(["kill", "-9", valid_pid])
    log_event(f"Result: {result.stderr.strip() or 'Success'}")


def renice_pid(pid: str, log_event: LogEvent) -> None:
    valid_pid = _positive_pid(pid)
    if valid_pid is None:
        log_event("Invalid PID; expected a positive integer.")
        return
    log_event(f"[bold #ffcf3d][SUDO][/] Renicing PID {valid_pid} to -10...")
    result = run_sudo_cmd(["renice", "-n", "-10", "-p", valid_pid])
    log_event(f"Result: {result.stdout.strip()}")


def set_cpu_governor(governor: str, log_event: LogEvent) -> None:
    try:
        selected = CpuGovernor(governor)
    except ValueError:
        log_event("Invalid CPU governor.")
        return
    targets = glob.glob("/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")
    if not targets:
        log_event("Could not locate CPU governor controls.")
        return
    errors: list[str] = []
    for target in targets:
        result = run_sudo_cmd(["tee", target], input_text=f"{selected.value}\n")
        if result.returncode != 0:
            errors.append(result.stderr.strip() or target)
    suffix = "; ".join(errors)
    log_event(f"Governor set to {selected.value}. {suffix}")


def set_gpu_power(value: str, log_event: LogEvent) -> None:
    if not value.isdecimal() or int(value) <= 0:
        log_event("Invalid GPU power cap; expected a positive integer.")
        return
    hwmon_dirs = glob.glob("/sys/class/drm/card0/device/hwmon/hwmon*")
    if not hwmon_dirs:
        log_event("Could not locate GPU hwmon directory.")
        return
    target = Path(hwmon_dirs[0]) / "power1_cap"
    try:
        minimum = int(target.with_name("power1_cap_min").read_text(encoding="utf-8").strip())
        maximum = int(target.with_name("power1_cap_max").read_text(encoding="utf-8").strip())
    except (OSError, ValueError):
        log_event("Could not read GPU power-cap limits.")
        return
    cap = int(value)
    if not minimum <= cap <= maximum:
        log_event(f"GPU power cap must be between {minimum} and {maximum}.")
        return
    result = run_sudo_cmd(["tee", str(target)], input_text=f"{cap}\n")
    if result.returncode == 0:
        log_event(f"Successfully applied GPU powercap to {target}")
        return
    log_event(f"Failed to apply powercap: {result.stderr.strip()}")


def kill_agent(agent_name: str, log_event: LogEvent) -> None:
    result = external_io.run(
        ["tmux", "kill-window", "-t", f"data:{agent_name}"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        log_event(f"[bold #ff4040]Tmux window data:{agent_name} destroyed.[/]")
        return
    for pid in find_agent_pids(agent_name):
        if pid <= 0:
            log_event("Invalid discovered PID; refusing privileged kill.")
            continue
        _ = run_sudo_cmd(["kill", "-9", str(pid)])
        log_event(f"[bold #ff4040]Process {pid} hard-killed.[/]")


def renice_agent(agent_name: str, niceness: int, log_event: LogEvent) -> None:
    pids = find_agent_pids(agent_name)
    if not pids:
        log_event(f"[#5c5855]Could not find running process for {agent_name} to renice.[/]")
        return
    for pid in pids:
        if pid <= 0:
            log_event("Invalid discovered PID; refusing privileged renice.")
            continue
        result = run_sudo_cmd(["renice", "-n", str(niceness), "-p", str(pid)])
        log_event(f"Renice applied to PID {pid}: {result.stdout.strip()}")


def apply_agent_budget(
    agent_name: str,
    cpu_percent: int,
    gpu_vram_gb: float,
    log_event: LogEvent,
) -> None:
    _ = resource_budgets.save_budget(
        agent_name,
        cpu_pct=cpu_percent,
        gpu_vram_gb=gpu_vram_gb,
    )
    message = (
        f"[#5c5855]Budget saved: {agent_name} -> {cpu_percent}% CPU, "
        f"{gpu_vram_gb}GB GPU (advisory).[/]"
    )
    log_event(message)
    pids = find_agent_pids(agent_name)
    if not pids:
        message = (
            f"[#5c5855]{agent_name} has no running process right now; "
            "CPU quota will apply once it starts and is re-applied.[/]"
        )
        log_event(message)
        return
    ok, message = resource_budgets.apply_cpu_budget(agent_name, cpu_percent, pids)
    color = "#ff4040" if ok else "#5c5855"
    log_event(f"[{color}]{message}[/]")

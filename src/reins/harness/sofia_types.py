from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import psutil

from reins.harness.agents import KNOWN_AGENTS
from reins.services.task_trail import TaskRecord

AGENT_SIGNATURES = {agent["name"]: agent["signature"] for agent in KNOWN_AGENTS}


@dataclass(frozen=True, slots=True)
class ProcessView:
    pid: int
    username: str
    cpu_percent: float
    memory_percent: float
    name: str
    command: str


@dataclass(frozen=True, slots=True)
class TrailView:
    owner: str
    task_type: str
    status: str
    target_node: str
    attempts: str
    timestamp: float
    prompt: str


def task_text(task: TaskRecord, key: str, default: str = "") -> str:
    value = task.get(key, default)
    return value if isinstance(value, str) else str(value)


def task_timestamp(task: TaskRecord) -> float:
    value = task.get("timestamp", 0.0)
    return float(value) if isinstance(value, (int, float)) else 0.0


def task_view(task: TaskRecord) -> TrailView:
    task_type = task_text(task, "task_type", "generic")
    return TrailView(
        owner=task_type.split(":", 1)[0],
        task_type=task_type,
        status=task_text(task, "status", "unknown"),
        target_node=task_text(task, "target_node"),
        attempts=task_text(task, "attempts", "0"),
        timestamp=task_timestamp(task),
        prompt=task_text(task, "prompt"),
    )


def process_views() -> list[ProcessView]:
    views: list[ProcessView] = []
    for process in psutil.process_iter():
        try:
            command = process.cmdline()
            views.append(
                ProcessView(
                    pid=process.pid,
                    username=process.username(),
                    cpu_percent=process.cpu_percent(),
                    memory_percent=process.memory_percent(),
                    name=process.name(),
                    command=" ".join(command),
                )
            )
        except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess):
            continue
    return views


def find_agent_pids(agent_name: str) -> list[int]:
    signature = AGENT_SIGNATURES.get(agent_name, agent_name)
    return [
        process.pid
        for process in process_views()
        if signature in process.command and "tmux" not in process.name
    ]


def memory_usage_percent() -> float:
    total_pages = os.sysconf("SC_PHYS_PAGES")
    available_pages = os.sysconf("SC_AVPHYS_PAGES")
    if total_pages <= 0:
        return 0.0
    return 100.0 * (total_pages - available_pages) / total_pages


def total_memory_bytes() -> int:
    return os.sysconf("SC_PHYS_PAGES") * os.sysconf("SC_PAGE_SIZE")


def tail(path: Path, line_count: int = 50) -> str:
    try:
        with path.open(encoding="utf-8", errors="replace") as handle:
            return "".join(handle.readlines()[-line_count:])
    except OSError:
        return "Log file not found or unreadable."

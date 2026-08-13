from __future__ import annotations

import logging
import platform
import time
from typing import final

import psutil
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.css.query import NoMatches
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Button, DataTable, Input, Label, ProgressBar, Static
from typing_extensions import override

from reins.harness import external_io
from reins.harness.agents import KNOWN_AGENTS
from reins.harness.sofia_types import memory_usage_percent, process_views, task_view, total_memory_bytes
from reins.services import resource_budgets as rb
from reins.services.task_trail import TaskRecord, TaskTrail

logger = logging.getLogger(__name__)


@final
class StringDataTable(DataTable[str]):
    pass


@final
class TrailLoaded(Message):
    def __init__(self, tasks: list[TaskRecord]) -> None:
        super().__init__()
        self.tasks = tasks


@final
class SystemInfo(Static):
    @override
    def compose(self) -> ComposeResult:
        uname = platform.uname()
        cpu_info = "Unknown"
        try:
            with open("/proc/cpuinfo") as handle:
                for line in handle:
                    if "model name" in line:
                        cpu_info = line.split(":")[1].strip()
                        break
        except OSError as error:
            logger.warning("CPU profile unavailable: %s", error)

        gpu_info = "Unknown"
        try:
            result = external_io.run(["lspci"], capture_output=True, text=True)
            for line in result.stdout.splitlines():
                if "VGA" in line or "3D" in line:
                    gpu_info = line.split(": ", 1)[-1].strip()
                    break
        except (OSError, UnicodeError) as error:
            logger.warning("GPU profile unavailable: %s", error)

        yield Label("HARDWARE PROFILE", classes="panel-title")
        yield Label(f"CPU: {cpu_info}")
        yield Label(f"GPU: {gpu_info}")
        yield Label(f"RAM: {total_memory_bytes() / (1024**3):.2f} GB")
        yield Label(" ")
        yield Label("SOFTWARE PROFILE", classes="panel-title")
        yield Label(f"System: {uname.system} {uname.release} ({uname.machine})")
        yield Label(f"Node: {uname.node}")


@final
class SystemMetrics(Static):
    cpu_usage: reactive[float] = reactive(0.0)
    ram_usage: reactive[float] = reactive(0.0)

    @override
    def compose(self) -> ComposeResult:
        yield Label("SYSTEM METRICS", classes="panel-title")
        with Horizontal():
            yield Label("CPU Usage:", classes="metric-label")
            yield ProgressBar(total=100, id="cpu_bar", show_eta=False)
        with Horizontal():
            yield Label("RAM Usage:", classes="metric-label")
            yield ProgressBar(total=100, id="ram_bar", show_eta=False)

    def watch_cpu_usage(self, value: float) -> None:
        try:
            self.query_one("#cpu_bar", ProgressBar).progress = value
        except NoMatches as error:
            logger.warning("CPU metric could not be rendered: %s", error)

    def watch_ram_usage(self, value: float) -> None:
        try:
            self.query_one("#ram_bar", ProgressBar).progress = value
        except NoMatches as error:
            logger.warning("RAM metric could not be rendered: %s", error)

    def on_mount(self) -> None:
        self.update_metrics()

    def update_metrics(self) -> None:
        self.cpu_usage = psutil.cpu_percent()
        self.ram_usage = memory_usage_percent()


@final
class AgentCommandCenter(Static):
    @override
    def compose(self) -> ComposeResult:
        yield Label(
            "OMARCHY AGENT COMMAND CENTER [dim](TAB to navigate, ENTER to execute)[/]",
            classes="panel-title",
        )
        budgets = rb.load_budgets()
        for agent in KNOWN_AGENTS:
            name = agent["name"]
            budget = budgets.get(name, {"cpu_pct": 100, "gpu_vram_gb": 0.0})
            with Horizontal(id=f"row_{name.replace('-', '_')}"):
                yield Label(
                    f"🟢 {name} [dim]({agent['role']})[/]",
                    classes="status-active",
                    id=f"status_{name.replace('-', '_')}",
                )
                if name != "data-sofia":
                    yield Button("TERMINATE", id=f"kill_{name}", classes="btn-terminate")
                yield Button("+ CPU", id=f"prio_up_{name}", classes="btn-prio-up")
                yield Button("- CPU", id=f"prio_down_{name}", classes="btn-prio-down")
            with Horizontal(id=f"budget_row_{name.replace('-', '_')}"):
                yield Label("CPU %:", classes="budget-label")
                yield Input(
                    value=str(budget["cpu_pct"]),
                    id=f"cpu_input_{name}",
                    classes="budget-input",
                )
                yield Label("GPU GB:", classes="budget-label")
                yield Input(
                    value=str(budget["gpu_vram_gb"]),
                    id=f"gpu_input_{name}",
                    classes="budget-input",
                )
                yield Button("APPLY BUDGET", id=f"apply_budget_{name}", classes="btn-tune")


@final
class ProcessMonitor(Static):
    @override
    def compose(self) -> ComposeResult:
        yield Label(
            "PROCESS MONITOR [dim](Arrows to scroll, R=Renice, K=Kill)[/]",
            classes="panel-title",
        )
        yield StringDataTable(id="proc_table")

    def on_mount(self) -> None:
        table = self.query_one("#proc_table", StringDataTable)
        table.cursor_type = "row"
        add_process_columns = table.add_columns
        _ = add_process_columns("PID", "USER", "CPU%", "MEM%", "NAME", "CMD")
        self.update_processes()

    def update_processes(self) -> None:
        table = self.query_one("#proc_table", StringDataTable)
        clear_processes = table.clear
        _ = clear_processes()
        add_process = table.add_row
        processes = sorted(process_views(), key=lambda process: process.cpu_percent, reverse=True)
        for process in processes[:100]:
            _ = add_process(
                str(process.pid),
                process.username,
                f"{process.cpu_percent:.1f}",
                f"{process.memory_percent:.1f}",
                process.name[:15],
                (process.command or process.name)[:60],
            )


@final
class TaskTrailPanel(Static):
    @override
    def compose(self) -> ComposeResult:
        yield Label(
            "UNIVERSAL TASK TRAIL [dim](all tasks, agents & subagents)[/]",
            classes="panel-title",
        )
        yield Static(id="trail_summary")
        yield StringDataTable(id="trail_table")

    def on_mount(self) -> None:
        table = self.query_one("#trail_table", StringDataTable)
        table.cursor_type = "row"
        add_trail_columns = table.add_columns
        _ = add_trail_columns(
            "OWNER", "TASK TYPE", "STATUS", "NODE", "ATTEMPTS", "AGE", "PROMPT"
        )
        self.refresh_trail()

    def refresh_trail(self) -> None:
        _ = self.run_worker(self._load_trail, exclusive=True, thread=True)

    def _load_trail(self) -> None:
        tasks = TaskTrail().all_tasks()
        _ = self.post_message(TrailLoaded(tasks))

    def on_trail_loaded(self, message: TrailLoaded) -> None:
        views = [task_view(task) for task in message.tasks]
        by_owner: dict[str, dict[str, int]] = {}
        for view in views:
            bucket = by_owner.setdefault(view.owner, {})
            bucket[view.status] = bucket.get(view.status, 0) + 1

        parts = [
            f"[bold]{owner}[/]: " + ", ".join(f"{status}={count}" for status, count in states.items())
            for owner, states in sorted(by_owner.items())
        ]
        self.query_one("#trail_summary", Static).update(
            "  |  ".join(parts) if parts else "[dim]no tasks recorded yet[/]"
        )

        table = self.query_one("#trail_table", StringDataTable)
        clear_trail = table.clear
        _ = clear_trail()
        add_trail = table.add_row
        now = time.time()
        for view in sorted(views, key=lambda item: item.timestamp, reverse=True)[:200]:
            age_s = max(0.0, now - view.timestamp)
            age = (
                f"{age_s:.0f}s"
                if age_s < 60
                else f"{age_s / 60:.0f}m"
                if age_s < 3600
                else f"{age_s / 3600:.1f}h"
            )
            _ = add_trail(
                view.owner,
                view.task_type,
                view.status,
                view.target_node,
                view.attempts,
                age,
                view.prompt[:60],
            )


@final
class KernelTuning(Static):
    @override
    def compose(self) -> ComposeResult:
        yield Label("KERNEL TUNING & OVERCLOCKING [dim](DANGER ZONE)[/]", classes="panel-title")
        with Horizontal():
            yield Button("CPU: Performance", id="gov_perf", classes="btn-tune")
            yield Button("CPU: Powersave", id="gov_power", classes="btn-tune")
            yield Button("CPU: Schedutil", id="gov_sched", classes="btn-tune")
        yield Label(" ")
        yield Label("GPU Power Limit (Microwatts) - Requires reboot to reset if unstable:")
        with Horizontal():
            yield Input(placeholder="e.g. 200000000", id="gpu_power_input")
            yield Button("APPLY GPU LIMIT", id="apply_gpu_power", classes="btn-terminate")

from __future__ import annotations

import subprocess
import threading
from collections.abc import Callable
from typing import ClassVar, final

import paho.mqtt.client as mqtt
from textual.app import App, ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import VerticalScroll
from textual.css.query import NoMatches
from textual.widgets import Button, Footer, Header, Input, Label, RichLog, TabbedContent, TabPane
from textual.widgets._data_table import RowDoesNotExist
from typing_extensions import override

from reins.harness.resilience_types import CircuitOpenError
from reins.harness.sofia_controls import (
    apply_agent_budget,
    kill_agent,
    kill_pid,
    renice_agent,
    renice_pid,
    set_cpu_governor,
    set_gpu_power,
)
from reins.harness.sofia_health import HealthController
from reins.harness.sofia_styles import CSS
from reins.harness.sofia_widgets import (
    AgentCommandCenter,
    KernelTuning,
    ProcessMonitor,
    StringDataTable,
    SystemInfo,
    SystemMetrics,
    TaskTrailPanel,
)


@final
class SofiaDashboard(App[None]):
    CSS: ClassVar[str] = CSS
    TITLE: str | None = "Sofia Protocol Dashboard (PON) - Kernel Edition"
    BINDINGS: ClassVar[list[BindingType]] = [
        ("q", "quit", "Quit"),
        ("k", "kill_proc", "Kill Selected"),
        ("r", "renice_proc", "Renice Selected"),
        ("u", "refresh_views", "Refresh"),
        ("h", "health_check", "Health Check"),
        Binding("1", "show_tab('agent-center')", show=False),
        Binding("2", "show_tab('process-monitor')", show=False),
        Binding("3", "show_tab('task-trail')", show=False),
        Binding("4", "show_tab('hardware-info')", show=False),
        Binding("5", "show_tab('kernel-tuning')", show=False),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.log_widget = RichLog(highlight=True, markup=True, id="event-log")
        self.health = HealthController(self.log_event, self._schedule_agent_failure)
        self.mqtt_client: mqtt.Client | None = None

    @override
    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane("Agent Center", id="agent-center"):
                with VerticalScroll():
                    yield SystemMetrics(classes="panel")
                    yield AgentCommandCenter(classes="panel")
            with TabPane("Process Monitor", id="process-monitor"):
                with VerticalScroll():
                    yield ProcessMonitor(classes="panel")
            with TabPane("Task Trail", id="task-trail"):
                with VerticalScroll():
                    yield TaskTrailPanel(classes="panel")
            with TabPane("Hardware Info", id="hardware-info"):
                with VerticalScroll():
                    yield SystemInfo(classes="panel")
            with TabPane("Kernel Tuning", id="kernel-tuning"):
                with VerticalScroll():
                    yield KernelTuning(classes="panel")
        yield self.log_widget
        yield Footer()

    def on_mount(self) -> None:
        _ = self.log_widget.write("[bold #ff4040]SOFIA PROTOCOL (KERNEL EDITION) ONLINE[/]")
        _ = self.log_widget.write("[#ff3c3c]Monitoring data_rein universal harness...[/]")
        self.start_mqtt_listener()
        self._trigger_health_check()

    def start_mqtt_listener(self) -> None:
        self.mqtt_client = self.health.start_mqtt_listener()

    def log_event(self, message: str) -> None:
        if self._thread_id == threading.get_ident():
            _ = self.log_widget.write(message)
            return
        _ = self.call_from_thread(self.log_widget.write, message)

    def action_kill_proc(self) -> None:
        pid = self._selected_pid()
        if pid is not None:
            self._start_control(lambda: kill_pid(pid, self.log_event))

    def action_renice_proc(self) -> None:
        pid = self._selected_pid()
        if pid is not None:
            self._start_control(lambda: renice_pid(pid, self.log_event))

    def action_refresh_views(self) -> None:
        self.query_one(SystemMetrics).update_metrics()
        self.query_one(ProcessMonitor).update_processes()
        self.query_one(TaskTrailPanel).refresh_trail()
        self.log_event("[#ff4040]Dashboard state refreshed from current facts.[/]")

    def action_health_check(self) -> None:
        self._trigger_health_check()

    def action_show_tab(self, tab_id: str) -> None:
        self.query_one(TabbedContent).active = tab_id

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id is None:
            return
        if button_id.startswith("kill_"):
            agent_name = button_id[5:]
            self._start_control(lambda: kill_agent(agent_name, self.log_event))
        elif button_id.startswith("prio_up_"):
            agent_name = button_id[8:]
            self._start_control(lambda: renice_agent(agent_name, -10, self.log_event))
        elif button_id.startswith("prio_down_"):
            agent_name = button_id[10:]
            self._start_control(lambda: renice_agent(agent_name, 10, self.log_event))
        elif button_id.startswith("gov_"):
            governor = {"perf": "performance", "power": "powersave"}.get(
                button_id[4:], "schedutil"
            )
            self._start_control(lambda: set_cpu_governor(governor, self.log_event))
        elif button_id == "apply_gpu_power":
            value = self.query_one("#gpu_power_input", Input).value
            if value.isdigit():
                self._start_control(lambda: set_gpu_power(value, self.log_event))
        elif button_id.startswith("apply_budget_"):
            self._apply_budget_from_inputs(button_id.removeprefix("apply_budget_"))

    def _selected_pid(self) -> str | None:
        try:
            table = self.query_one("#proc_table", StringDataTable)
            row = table.get_row_at(table.cursor_coordinate.row)
            return row[0]
        except (IndexError, NoMatches, RowDoesNotExist) as error:
            self.log_event(f"[#5c5855]No process selected: {error}[/]")
            return None

    def _apply_budget_from_inputs(self, agent_name: str) -> None:
        try:
            cpu_percent = int(self.query_one(f"#cpu_input_{agent_name}", Input).value)
            gpu_vram_gb = float(self.query_one(f"#gpu_input_{agent_name}", Input).value)
        except (NoMatches, ValueError) as error:
            self.log_event(f"[#5c5855]Invalid budget input for {agent_name}: {error}[/]")
            return
        self._start_control(
            lambda: apply_agent_budget(
                agent_name,
                cpu_percent,
                gpu_vram_gb,
                self.log_event,
            )
        )

    def _start_control(self, operation: Callable[[], None]) -> None:
        _ = self.run_worker(
            lambda: self._run_control(operation),
            exit_on_error=False,
            thread=True,
        )

    def _run_control(self, operation: Callable[[], None]) -> None:
        try:
            operation()
        except (CircuitOpenError, OSError, subprocess.SubprocessError, ValueError) as error:
            self.log_event(f"[#5c5855]Control action failed: {error}[/]")

    def _trigger_health_check(self) -> None:
        _ = self.run_worker(
            self.health.run_health_check,
            exit_on_error=False,
            exclusive=True,
            thread=True,
        )

    def _schedule_agent_failure(self, agent_name: str) -> None:
        if self._thread_id == threading.get_ident():
            self._render_agent_failure(agent_name)
            return
        _ = self.call_from_thread(self._render_agent_failure, agent_name)

    def _render_agent_failure(self, agent_name: str) -> None:
        try:
            label = self.query_one(f"#status_{agent_name.replace('-', '_')}", Label)
            label.update(f"🔴 {agent_name} [CRASHED - HEALER DISPATCHED]")
        except NoMatches as error:
            self.log_event(f"[#5c5855]Agent status row unavailable: {error}[/]")
        self.query_one(TaskTrailPanel).refresh_trail()


if __name__ == "__main__":
    _ = SofiaDashboard().run(mouse=False)

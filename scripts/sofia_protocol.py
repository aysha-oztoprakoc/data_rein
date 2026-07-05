import os
import time
import psutil
import platform
import threading
import subprocess
import glob
import paho.mqtt.client as mqtt
from textual.app import App, ComposeResult
from textual.containers import Grid, Vertical, Horizontal, VerticalScroll
from textual.widgets import Header, Footer, RichLog, Static, Label, ProgressBar, Button, TabbedContent, TabPane, DataTable, Input
from textual.reactive import reactive
from textual.coordinate import Coordinate

from reins.harness.agents import KNOWN_AGENTS
from reins.services import resource_budgets as rb
from reins.services.sudo_exec import run_sudo_cmd
from reins.services.task_trail import TaskTrail

AGENT_SIGNATURES = {a["name"]: a["signature"] for a in KNOWN_AGENTS}

def tail(filename, n=50):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return "".join(lines[-n:])
    except Exception:
        return "Log file not found or unreadable."

def find_agent_pids(agent_name: str) -> list[int]:
    """PIDs of every running process matching this agent's cmdline signature."""
    sig = AGENT_SIGNATURES.get(agent_name, agent_name)
    pids = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        cmd = proc.info.get('cmdline')
        if cmd and sig in ' '.join(cmd) and 'tmux' not in proc.info.get('name', ''):
            pids.append(proc.info['pid'])
    return pids

TRUE_RED = "#ff4040"
BRIGHT_RED = "#ff1100"
BLOOD_BLACK = "#200000"
DIM_GRAY = "#5c5855"

CSS = f"""
SofiaDashboard {{
    background: transparent;
}}
.panel {{
    border: ascii {TRUE_RED};
    background: transparent;
    padding: 1;
    margin: 1;
}}
.panel-title {{
    text-style: bold;
    color: {TRUE_RED};
    margin-bottom: 1;
}}
.metric-label {{
    color: {TRUE_RED};
    width: 15;
}}
.status-active {{
    color: {TRUE_RED};
    text-style: bold;
    width: 30;
}}
.status-inactive {{
    color: {DIM_GRAY};
    width: 30;
}}
#event-log {{
    height: 12;
    border: ascii {DIM_GRAY};
    background: transparent;
}}
Button {{
    height: 1;
    border: none;
    margin-right: 1;
    min-width: 10;
}}
.btn-terminate {{
    background: {TRUE_RED};
    color: black;
}}
.btn-prio-up, .btn-prio-down, .btn-tune {{
    background: {DIM_GRAY};
    color: white;
}}
DataTable {{
    height: 1fr;
    border: ascii {DIM_GRAY};
}}
"""

class SystemInfo(Static):
    def compose(self) -> ComposeResult:
        uname = platform.uname()
        cpu_info = "Unknown"
        try:
            with open('/proc/cpuinfo') as f:
                for line in f:
                    if 'model name' in line:
                        cpu_info = line.split(':')[1].strip()
                        break
        except: pass
        
        gpu_info = "Unknown"
        try:
            res = subprocess.run(["lspci"], capture_output=True, text=True)
            for line in res.stdout.splitlines():
                if "VGA" in line or "3D" in line:
                    gpu_info = line.split(': ')[1].strip()
                    break
        except: pass
        
        mem = psutil.virtual_memory()
        total_ram = f"{mem.total / (1024**3):.2f} GB"
        
        yield Label("HARDWARE PROFILE", classes="panel-title")
        yield Label(f"CPU: {cpu_info}")
        yield Label(f"GPU: {gpu_info}")
        yield Label(f"RAM: {total_ram}")
        yield Label(" ")
        yield Label("SOFTWARE PROFILE", classes="panel-title")
        yield Label(f"System: {uname.system} {uname.release} ({uname.machine})")
        yield Label(f"Node: {uname.node}")

class SystemMetrics(Static):
    cpu_usage = reactive(0.0)
    ram_usage = reactive(0.0)
    
    def compose(self) -> ComposeResult:
        yield Label("SYSTEM METRICS", classes="panel-title")
        with Horizontal():
            yield Label("CPU Usage:", classes="metric-label")
            yield ProgressBar(total=100, id="cpu_bar", show_eta=False)
        with Horizontal():
            yield Label("RAM Usage:", classes="metric-label")
            yield ProgressBar(total=100, id="ram_bar", show_eta=False)

    def watch_cpu_usage(self, value: float) -> None:
        try: self.query_one("#cpu_bar", ProgressBar).progress = value
        except: pass

    def watch_ram_usage(self, value: float) -> None:
        try: self.query_one("#ram_bar", ProgressBar).progress = value
        except: pass

    def on_mount(self) -> None:
        self.set_interval(1.0, self.update_metrics)

    def update_metrics(self) -> None:
        self.cpu_usage = psutil.cpu_percent()
        self.ram_usage = psutil.virtual_memory().percent

class AgentCommandCenter(Static):
    def compose(self) -> ComposeResult:
        yield Label("OMARCHY AGENT COMMAND CENTER [dim](TAB to navigate, ENTER to execute)[/]", classes="panel-title")
        budgets = rb.load_budgets()
        for agent in KNOWN_AGENTS:
            name = agent["name"]
            budget = budgets.get(name, {"cpu_pct": 100, "gpu_vram_gb": 0})
            with Horizontal(id=f"row_{name.replace('-', '_')}"):
                yield Label(f"🟢 {name} [dim]({agent['role']})[/]", classes="status-active", id=f"status_{name.replace('-', '_')}")
                if name != "data-sofia":
                    yield Button("TERMINATE", id=f"kill_{name}", classes="btn-terminate")
                yield Button("+ CPU", id=f"prio_up_{name}", classes="btn-prio-up")
                yield Button("- CPU", id=f"prio_down_{name}", classes="btn-prio-down")
            with Horizontal(id=f"budget_row_{name.replace('-', '_')}"):
                yield Label("CPU %:", classes="metric-label")
                yield Input(value=str(budget["cpu_pct"]), id=f"cpu_input_{name}")
                yield Label("GPU GB:", classes="metric-label")
                yield Input(value=str(budget["gpu_vram_gb"]), id=f"gpu_input_{name}")
                yield Button("APPLY BUDGET", id=f"apply_budget_{name}", classes="btn-tune")

class ProcessMonitor(Static):
    def compose(self) -> ComposeResult:
        yield Label("PROCESS MONITOR [dim](Arrows to scroll, R=Renice, K=Kill)[/]", classes="panel-title")
        yield DataTable(id="proc_table")
        
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.add_columns("PID", "USER", "CPU%", "MEM%", "NAME", "CMD")
        self.update_processes()
        self.set_interval(3.0, self.update_processes)

    def update_processes(self) -> None:
        table = self.query_one(DataTable)
        try:
            row_key = table.cursor_coordinate.row if table.cursor_coordinate else 0
        except:
            row_key = 0
            
        table.clear()
        processes = []
        for p in psutil.process_iter(['pid', 'username', 'cpu_percent', 'memory_percent', 'name', 'cmdline']):
            try:
                processes.append(p.info)
            except: pass
            
        processes.sort(key=lambda x: x.get('cpu_percent', 0), reverse=True)
        for p in processes[:100]:
            cmd = " ".join(p.get('cmdline', []))[:60] if p.get('cmdline') else p.get('name', '')
            table.add_row(
                str(p['pid']), 
                p.get('username', ''), 
                f"{p.get('cpu_percent', 0.0):.1f}", 
                f"{p.get('memory_percent', 0.0):.1f}", 
                p.get('name', '')[:15], 
                cmd
            )
            
class TaskTrailPanel(Static):
    """Live view of every task/agent/subagent in the Universal Task Trail.

    Refreshed on Textual's own reactive timer (set_interval), matching the
    idiom already used by SystemMetrics/ProcessMonitor in this file - the
    trail read is dispatched to a worker thread so a slow disk never stalls
    the UI loop."""

    def compose(self) -> ComposeResult:
        yield Label("UNIVERSAL TASK TRAIL [dim](all tasks, agents & subagents)[/]", classes="panel-title")
        yield Static(id="trail_summary")
        yield DataTable(id="trail_table")

    def on_mount(self) -> None:
        table = self.query_one("#trail_table", DataTable)
        table.cursor_type = "row"
        table.add_columns("OWNER", "TASK TYPE", "STATUS", "NODE", "ATTEMPTS", "AGE", "PROMPT")
        self.refresh_trail()
        self.set_interval(3.0, self.refresh_trail)

    def refresh_trail(self) -> None:
        self.run_worker(self._load_trail, exclusive=True, thread=True)

    def _load_trail(self) -> None:
        try:
            tasks = TaskTrail().all_tasks()
        except Exception:
            tasks = []
        self.app.call_from_thread(self._render_trail, tasks)

    def _render_trail(self, tasks: list) -> None:
        by_owner: dict[str, dict[str, int]] = {}
        for t in tasks:
            owner = str(t.get("task_type", "generic")).split(":", 1)[0]
            bucket = by_owner.setdefault(owner, {})
            status = t.get("status", "unknown")
            bucket[status] = bucket.get(status, 0) + 1

        summary_parts = [
            f"[bold]{owner}[/]: " + ", ".join(f"{s}={n}" for s, n in statuses.items())
            for owner, statuses in sorted(by_owner.items())
        ]
        try:
            self.query_one("#trail_summary", Static).update(
                "  |  ".join(summary_parts) if summary_parts else "[dim]no tasks recorded yet[/]"
            )
        except Exception:
            pass

        try:
            table = self.query_one("#trail_table", DataTable)
        except Exception:
            return
        table.clear()
        now = time.time()
        for t in sorted(tasks, key=lambda x: x.get("timestamp", 0), reverse=True)[:200]:
            owner = str(t.get("task_type", "generic")).split(":", 1)[0]
            age_s = max(0, now - t.get("timestamp", now))
            age = f"{age_s:.0f}s" if age_s < 60 else f"{age_s / 60:.0f}m" if age_s < 3600 else f"{age_s / 3600:.1f}h"
            table.add_row(
                owner,
                str(t.get("task_type", "")),
                str(t.get("status", "")),
                str(t.get("target_node", "")),
                str(t.get("attempts", 0)),
                age,
                str(t.get("prompt", ""))[:60],
            )


class TerminalPanel(Static):
    """Placeholder for the embedded meta-harness terminal.

    Textual has no built-in PTY/terminal widget; wiring the openclaude CLI,
    the Odysseus graphical suite, and the Omnigent GUI in here needs either
    the third-party `textual-terminal` package or a hand-rolled PTY (none of
    which exist in this repo yet). Left as an explicit stub so this tab's
    presence documents the intended integration point without pretending
    it's wired up."""

    def compose(self) -> ComposeResult:
        yield Label("META-HARNESS TERMINAL [dim](coming soon)[/]", classes="panel-title")
        yield Label(
            "Planned integration points, not yet wired:\n"
            "  - openclaude CLI\n"
            "  - Odysseus graphical suite\n"
            "  - Omnigent GUI\n\n"
            "Needs a PTY-backed Textual widget (e.g. the `textual-terminal` package,\n"
            "or a hand-rolled os.forkpty() + Log widget) - none of that exists in this\n"
            "repo yet, so this tab is a marked placeholder rather than a fake control."
        )


class KernelTuning(Static):
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

class SofiaDashboard(App):
    CSS = CSS
    TITLE = "Sofia Protocol Dashboard (PON) - Kernel Edition"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("k", "kill_proc", "Kill Selected"),
        ("r", "renice_proc", "Renice Selected")
    ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane("Agent Center"):
                with VerticalScroll():
                    yield SystemMetrics(classes="panel")
                    yield AgentCommandCenter(classes="panel")
            with TabPane("Process Monitor"):
                with VerticalScroll():
                    yield ProcessMonitor(classes="panel")
            with TabPane("Task Trail"):
                with VerticalScroll():
                    yield TaskTrailPanel(classes="panel")
            with TabPane("Hardware Info"):
                with VerticalScroll():
                    yield SystemInfo(classes="panel")
            with TabPane("Kernel Tuning"):
                with VerticalScroll():
                    yield KernelTuning(classes="panel")
            with TabPane("Terminal"):
                with VerticalScroll():
                    yield TerminalPanel(classes="panel")
                    
        self.log_widget = RichLog(highlight=True, markup=True, id="event-log")
        yield self.log_widget
        yield Footer()

    def on_mount(self) -> None:
        self.log_widget.write("[bold #ff4040]SOFIA PROTOCOL (KERNEL EDITION) ONLINE[/]")
        self.log_widget.write("[#ff3c3c]Monitoring data_rein universal harness...[/]")

        self._last_heal_dispatch = 0.0
        self._heal_cooldown = 300.0
        self._last_failure_dispatch = 0.0
        self._failure_cooldown = 10.0

        self.set_interval(60.0, self._trigger_health_check)
        self.start_mqtt_listener()

    def log_event(self, message: str) -> None:
        if self._thread_id == threading.get_ident():
            self.log_widget.write(message)
        else:
            self.call_from_thread(self.log_widget.write, message)

    def action_kill_proc(self) -> None:
        try:
            table = self.query_one(DataTable)
            row = table.get_row_at(table.cursor_coordinate.row)
            pid = row[0]
            self.log_event(f"[bold #ff1100][SUDO][/] Killing PID {pid}...")
            res = run_sudo_cmd(["kill", "-9", str(pid)])
            self.log_event(f"Result: {res.stderr.strip() or 'Success'}")
        except Exception as e:
            self.log_event(f"Error: {e}")

    def action_renice_proc(self) -> None:
        try:
            table = self.query_one(DataTable)
            row = table.get_row_at(table.cursor_coordinate.row)
            pid = row[0]
            self.log_event(f"[bold #ffcf3d][SUDO][/] Renicing PID {pid} to -10...")
            res = run_sudo_cmd(["renice", "-n", "-10", "-p", str(pid)])
            self.log_event(f"Result: {res.stdout.strip()}")
        except Exception as e:
            self.log_event(f"Error: {e}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if not button_id: return
        
        if button_id.startswith("kill_"):
            agent_name = button_id[5:]
            self.log_event(f"[bold #ff1100][SUDO][/bold #ff1100] Terminating {agent_name}...")
            self.run_worker(lambda a=agent_name: self._kill_agent(a), exclusive=False, thread=True)
            
        elif button_id.startswith("prio_up_"):
            agent_name = button_id[8:]
            self.log_event(f"[bold #ffcf3d][SUDO][/bold #ffcf3d] Increasing CPU priority (renice -10) for {agent_name}...")
            self.run_worker(lambda a=agent_name: self._renice_agent(a, -10), exclusive=False, thread=True)
            
        elif button_id.startswith("prio_down_"):
            agent_name = button_id[10:]
            self.log_event(f"[bold #26bdfd][SUDO][/bold #26bdfd] Decreasing CPU priority (renice +10) for {agent_name}...")
            self.run_worker(lambda a=agent_name: self._renice_agent(a, 10), exclusive=False, thread=True)
            
        elif button_id.startswith("gov_"):
            gov = button_id[4:]
            full_gov = "performance" if gov == "perf" else "powersave" if gov == "power" else "schedutil"
            self.log_event(f"[bold #ffcf3d][SUDO][/] Changing CPU governor to {full_gov}...")
            self.run_worker(lambda g=full_gov: self._set_cpu_governor(g), exclusive=False, thread=True)
            
        elif button_id == "apply_gpu_power":
            try:
                val = self.query_one("#gpu_power_input", Input).value
                if val.isdigit():
                    self.log_event(f"[bold #ff1100][SUDO][/] Setting GPU power limit to {val} microwatts...")
                    self.run_worker(lambda v=val: self._set_gpu_power(v), exclusive=False, thread=True)
            except Exception as e:
                self.log_event(f"Error: {e}")

        elif button_id.startswith("apply_budget_"):
            agent_name = button_id[len("apply_budget_"):]
            try:
                cpu_pct = int(self.query_one(f"#cpu_input_{agent_name}", Input).value)
                gpu_gb = float(self.query_one(f"#gpu_input_{agent_name}", Input).value)
            except Exception as e:
                self.log_event(f"[#5c5855]Invalid budget input for {agent_name}: {e}[/]")
                return
            self.log_event(f"[bold #ffcf3d][SUDO][/] Applying budget for {agent_name}: {cpu_pct}% CPU, {gpu_gb}GB GPU (soft)...")
            self.run_worker(lambda a=agent_name, c=cpu_pct, g=gpu_gb: self._apply_agent_budget(a, c, g), exclusive=False, thread=True)

    def _set_cpu_governor(self, gov: str) -> None:
        script = f"for f in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do echo {gov} > $f; done"
        res = run_sudo_cmd(["bash", "-c", script])
        self.log_event(f"Governor set to {gov}. {res.stderr.strip()}")
        
    def _set_gpu_power(self, val: str) -> None:
        # Find the hwmon directory for card0
        hwmon_dirs = glob.glob("/sys/class/drm/card0/device/hwmon/hwmon*")
        if hwmon_dirs:
            target = f"{hwmon_dirs[0]}/power1_cap"
            res = run_sudo_cmd(["bash", "-c", f"echo {val} > {target}"])
            if res.returncode == 0:
                self.log_event(f"Successfully applied GPU powercap to {target}")
            else:
                self.log_event(f"Failed to apply powercap: {res.stderr.strip()}")
        else:
            self.log_event("Could not locate GPU hwmon directory.")

    def _kill_agent(self, agent_name: str) -> None:
        res = subprocess.run(["tmux", "kill-window", "-t", f"data:{agent_name}"], capture_output=True, text=True)
        if res.returncode == 0:
            self.log_event(f"[bold #ff4040]Tmux window data:{agent_name} destroyed.[/]")
        else:
            try:
                for pid in find_agent_pids(agent_name):
                    run_sudo_cmd(["kill", "-9", str(pid)])
                    self.log_event(f"[bold #ff4040]Process {pid} hard-killed.[/]")
            except Exception as e:
                self.log_event(f"[#5c5855]Error finding/killing process: {e}[/]")

    def _renice_agent(self, agent_name: str, niceness: int) -> None:
        try:
            pids = find_agent_pids(agent_name)
            if not pids:
                self.log_event(f"[#5c5855]Could not find running process for {agent_name} to renice.[/]")
                return
            for pid in pids:
                res = run_sudo_cmd(["renice", "-n", str(niceness), "-p", str(pid)])
                self.log_event(f"Renice applied to PID {pid}: {res.stdout.strip()}")
        except Exception as e:
            self.log_event(f"[#5c5855]Error applying renice: {e}[/]")

    def _apply_agent_budget(self, agent_name: str, cpu_pct: int, gpu_vram_gb: float) -> None:
        rb.save_budget(agent_name, cpu_pct=cpu_pct, gpu_vram_gb=gpu_vram_gb)
        self.log_event(f"[#5c5855]Budget saved: {agent_name} -> {cpu_pct}% CPU, {gpu_vram_gb}GB GPU (advisory).[/]")

        pids = find_agent_pids(agent_name)
        if not pids:
            self.log_event(f"[#5c5855]{agent_name} has no running process right now; CPU quota will apply once it starts and is re-applied.[/]")
            return
        ok, msg = rb.apply_cpu_budget(agent_name, cpu_pct, pids)
        color = "#ff4040" if ok else "#5c5855"
        self.log_event(f"[{color}]{msg}[/]")

    def _trigger_health_check(self) -> None:
        """Fired by Textual's own reactive timer (set_interval) - no thread, no sleep-loop.
        The actual pytest run is blocking I/O, so it's dispatched to a worker thread; the
        interval callback itself just decides whether it's time to kick one off."""
        self.run_worker(self._health_check_once, exclusive=True, thread=True)

    def _health_check_once(self) -> None:
        self.log_event("[bold #ffcf3d]Running sanity check suite...[/]")
        result = subprocess.run(
            ["uv", "run", "pytest", "tests/test_health_sanity.py"],
            cwd=os.path.expanduser("~/data_rein"),
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return

        now = time.monotonic()
        if now - self._last_heal_dispatch < self._heal_cooldown:
            self.log_event("[#5c5855]Sanity check still failing; auto-healer cooldown active.[/]")
            return
        self._last_heal_dispatch = now

        self.log_event("[bold #ff1100]CRITICAL: Sanity check failed! Deploying auto-healer...[/]")
        prompt = (
            "/goal SOFIA PROTOCOL HEALTH CHECK FAILED: The system sanity checks failed. "
            f"Here is the pytest output:\\n```\\n{result.stdout}\\n{result.stderr}\\n```\\n\\n"
            "Please fix the broken components or update the tests if the system architecture has changed. "
            "Ensure the data_rein harness runs stably 24/7./goal"
        )
        subprocess.Popen(
            ["bash", "scripts/launch_with_sudo.sh", "agy", "--dangerously-skip-permissions", "-c", prompt],
            cwd=os.path.expanduser("~/data_rein"),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def start_mqtt_listener(self) -> None:
        """PON-compliant fleet failure feed: a persistent paho-mqtt client whose own
        network thread blocks on the socket (loop_start()) and fires on_message
        reactively - no subprocess, no readline polling, no sleep."""
        topic = "data_rein/alerts/failure"
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

        def on_connect(c, userdata, flags, reason_code, properties=None):
            c.subscribe(topic)
            self.call_from_thread(self.log_event, f"Listening on MQTT topic: {topic}")

        def on_message(c, userdata, msg):
            self.call_from_thread(self._handle_failure_message, msg.payload.decode(errors="replace"))

        client.on_connect = on_connect
        client.on_message = on_message
        try:
            client.connect("localhost", 1883)
            client.loop_start()
            self.mqtt_client = client
        except Exception as e:  # graceful degradation - no broker, no crash
            self.log_event(f"[#5c5855]MQTT broker unreachable ({e}); fleet failure feed disabled.[/]")

    def _handle_failure_message(self, line: str) -> None:
        line = line.strip()
        if not ("CRITICAL: Agent" in line and "failed!" in line):
            return

        words = line.split()
        try:
            agent_idx = words.index("Agent") + 1
            agent_name = words[agent_idx]
        except ValueError:
            agent_name = "unknown"

        now = time.monotonic()
        if now - self._last_failure_dispatch < self._failure_cooldown:
            return
        self._last_failure_dispatch = now

        self.log_event(f"[bold #ff1100]Detected failure for {agent_name}![/]")
        self._update_agent_status_ui(agent_name)

        log_file = os.path.expanduser(f"~/data_rein/logs/{agent_name}.log")
        error_tail = tail(log_file)

        self.log_event("[bold #ffcf3d]Deploying Antigravity repair agent...[/]")

        prompt = (
            f"/goal SOFIA PROTOCOL ACTIVATED: The service {agent_name} just crashed. "
            f"Here is the tail of its log file:\\n```\\n{error_tail}\\n```\\n\\n"
            f"You must investigate this problem using the suite of tests (pytest). "
            f"Update the tests if needed, applying Test Driven Development (TDD), PON, and "
            f"graceful degradation principles. Your goal is to learn from this error, write "
            f"tests that catch it, fix the codebase, and ensure the service doesn't crash again./goal"
        )

        subprocess.Popen(
            ["bash", "scripts/launch_with_sudo.sh", "agy", "--dangerously-skip-permissions", "-c", prompt],
            cwd=os.path.expanduser("~/data_rein"),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def _update_agent_status_ui(self, agent_name: str) -> None:
        try:
            target_id = f"#status_{agent_name.replace('-', '_')}"
            label = self.query_one(target_id, Label)
            label.update(f"🔴 {agent_name} [CRASHED - HEALER DISPATCHED]")
        except Exception:
            pass

if __name__ == "__main__":
    app = SofiaDashboard()
    app.run(mouse=False)

from __future__ import annotations

import os
import subprocess
import time
from collections.abc import Callable
from pathlib import Path
from typing import final

import paho.mqtt.client as mqtt
from paho.mqtt.client import ConnectFlags, MQTTMessage
from paho.mqtt.enums import CallbackAPIVersion
from paho.mqtt.properties import Properties
from paho.mqtt.reasoncodes import ReasonCode

from reins.harness import external_io, paths
from reins.harness.resilience_types import CircuitOpenError
from reins.harness.sofia_types import tail

LogEvent = Callable[[str], None]
AgentFailure = Callable[[str], None]


@final
class HealthController:
    def __init__(self, log_event: LogEvent, agent_failure: AgentFailure) -> None:
        self._log_event = log_event
        self._agent_failure = agent_failure
        self._last_heal_dispatch = 0.0
        self._heal_cooldown = 300.0
        self._last_failure_dispatch = 0.0
        self._failure_cooldown = 10.0

    def run_health_check(self) -> None:
        self._log_event("[bold #ffcf3d]Running sanity check suite...[/]")
        try:
            result = external_io.run(
                ["uv", "run", "pytest", "tests/test_health_sanity.py"],
                cwd=paths.home(),
                capture_output=True,
                text=True,
            )
        except (CircuitOpenError, OSError, subprocess.SubprocessError) as error:
            self._log_event(f"[#5c5855]Sanity check unavailable: {error}[/]")
            return
        if result.returncode == 0:
            return

        now = time.monotonic()
        if now - self._last_heal_dispatch < self._heal_cooldown:
            self._log_event("[#5c5855]Sanity check still failing; auto-healer cooldown active.[/]")
            return
        self._last_heal_dispatch = now
        self._log_event("[bold #ff1100]CRITICAL: Sanity check failed! Deploying auto-healer...[/]")
        prompt = (
            "/goal SOFIA PROTOCOL HEALTH CHECK FAILED: The system sanity checks failed. "
            f"Here is the pytest output:\\n```\\n{result.stdout}\\n{result.stderr}\\n```\\n\\n"
            "Please fix the broken components or update the tests if the system architecture has "
            "changed. Ensure the data_rein harness runs stably 24/7./goal"
        )
        self._dispatch_repair(prompt)

    def start_mqtt_listener(self) -> mqtt.Client | None:
        topic = "data_rein/alerts/failure"
        client = mqtt.Client(CallbackAPIVersion.VERSION2)

        def on_connect(
            connected_client: mqtt.Client,
            _userdata: None,
            _flags: ConnectFlags,
            _reason_code: ReasonCode,
            _properties: Properties | None = None,
        ) -> None:
            _ = external_io.mqtt_subscribe(connected_client, topic)
            self._log_event(f"Listening on MQTT topic: {topic}")

        def on_message(
            _client: mqtt.Client,
            _userdata: None,
            message: MQTTMessage,
        ) -> None:
            self.handle_failure_message(message.payload.decode(errors="replace"))

        client.on_connect = on_connect
        client.on_message = on_message
        try:
            _ = external_io.mqtt_connect(client, "localhost", 1883)
            _ = client.loop_start()
        except (CircuitOpenError, OSError, ValueError) as error:
            self._log_event(
                f"[#5c5855]MQTT broker unreachable ({error}); fleet failure feed disabled.[/]"
            )
            return None
        return client

    def handle_failure_message(self, line: str) -> None:
        words = line.strip().split()
        if not ("CRITICAL:" in words and "Agent" in words and "failed!" in words):
            return
        try:
            agent_name = words[words.index("Agent") + 1]
        except (IndexError, ValueError):
            agent_name = "unknown"

        now = time.monotonic()
        if now - self._last_failure_dispatch < self._failure_cooldown:
            return
        self._last_failure_dispatch = now
        self._log_event(f"[bold #ff1100]Detected failure for {agent_name}![/]")
        self._agent_failure(agent_name)
        error_tail = tail(Path(paths.home()) / "logs" / f"{agent_name}.log")
        self._log_event("[bold #ffcf3d]Deploying Antigravity repair agent...[/]")
        prompt = (
            f"/goal SOFIA PROTOCOL ACTIVATED: The service {agent_name} just crashed. "
            f"Here is the tail of its log file:\\n```\\n{error_tail}\\n```\\n\\n"
            "Investigate with pytest, apply TDD, PON, and graceful degradation, and ensure the "
            "service does not crash again./goal"
        )
        self._dispatch_repair(prompt)

    def _dispatch_repair(self, prompt: str) -> None:
        try:
            _ = external_io.popen(
                [
                    "agy",
                    "--dangerously-skip-permissions",
                    "-c",
                    prompt,
                ],
                cwd=os.fspath(paths.home()),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except (CircuitOpenError, OSError, subprocess.SubprocessError) as error:
            self._log_event(f"[#5c5855]Repair agent could not start: {error}[/]")

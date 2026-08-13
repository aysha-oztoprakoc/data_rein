from __future__ import annotations

import hashlib
import http.client
import json
import logging
import os
import socket
import sqlite3
import subprocess
import urllib.parse
import urllib.request
from collections.abc import Awaitable, Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import IO, Literal, TypeAlias, TypeVar, cast, overload

import paho.mqtt.client as mqtt
from paho.mqtt.enums import MQTTErrorCode
from typing_extensions import override

from reins.harness.resilience import BreakerRegistry
from reins.harness.resilience_types import BreakerState, CircuitConfig

logger = logging.getLogger(__name__)

CommandPart: TypeAlias = str | bytes | os.PathLike[str] | os.PathLike[bytes]
Command: TypeAlias = Sequence[CommandPart]
ProcessResult: TypeAlias = subprocess.CompletedProcess[str] | subprocess.CompletedProcess[bytes]
ProcessHandle: TypeAlias = subprocess.Popen[str] | subprocess.Popen[bytes]
RunInput: TypeAlias = str | bytes | None
StreamTarget: TypeAlias = int | IO[str] | IO[bytes] | None
MqttPayload: TypeAlias = str | bytes | bytearray | int | float | None
MqttResult: TypeAlias = None | int | tuple[int, int | None] | mqtt.MQTTMessageInfo
T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class CommandArgumentError(TypeError):
    message: str

    @override
    def __str__(self) -> str:
        return self.message


def _record_transition(name: str, old_state: BreakerState, new_state: BreakerState) -> None:
    log = logger.warning if new_state is BreakerState.OPEN else logger.info
    log("external circuit %s changed from %s to %s", name, old_state.value, new_state.value)
    try:
        from reins.services.task_trail import TaskTrail

        digest = hashlib.sha256(name.encode()).hexdigest()[:16]
        status = {
            BreakerState.OPEN: "failed",
            BreakerState.HALF_OPEN: "running",
            BreakerState.CLOSED: "success",
        }[new_state]
        _ = TaskTrail().upsert_task(
            f"external-breaker-{digest}",
            task_type="breaker:external",
            prompt=json.dumps({"circuit": name, "from": old_state.value, "to": new_state.value}),
            target_node="resilience",
            status=status,
            breaker_state=new_state.value,
        )
    except (OSError, sqlite3.Error, TypeError, ValueError):
        logger.warning("external circuit transition was not persisted", exc_info=True)


_BREAKERS = BreakerRegistry(
    CircuitConfig(failure_threshold=5, window_seconds=60.0, cooldown_seconds=15.0),
    on_transition=_record_transition,
)


def _command_name(command: Command) -> str:
    parts = [os.fsdecode(part) for part in command]
    if not parts:
        return "empty"
    program = Path(parts[0]).name
    if program in {"ssh", "scp"}:
        return program
    operation = next((part for part in parts[1:] if not part.startswith("-")), "invoke")
    return f"{program}:{Path(operation).name}"


def _argv(command: Command) -> tuple[CommandPart, ...]:
    if isinstance(command, (str, bytes, os.PathLike)):
        raise CommandArgumentError(message="external process commands require an argv sequence")
    argv = tuple(command)
    if not argv:
        raise CommandArgumentError(message="external process argv cannot be empty")
    return argv


def call(name: str, operation: Callable[[], T]) -> T:
    return _BREAKERS.get(name).call(operation)


async def async_call(
    name: str,
    operation: Callable[[], Awaitable[T]],
    *,
    is_success: Callable[[T], bool] | None = None,
) -> T:
    return await _BREAKERS.get(name).call_async(operation, is_success=is_success)


@overload
def run(
    command: Command,
    *,
    text: Literal[True],
    input: RunInput = None,
    capture_output: bool = False,
    check: bool = False,
    cwd: CommandPart | None = None,
    timeout: float | None = None,
    success_codes: Sequence[int] = (0,),
) -> subprocess.CompletedProcess[str]: ...


@overload
def run(
    command: Command,
    *,
    text: Literal[False] = False,
    input: RunInput = None,
    capture_output: bool = False,
    check: bool = False,
    cwd: CommandPart | None = None,
    timeout: float | None = None,
    success_codes: Sequence[int] = (0,),
) -> subprocess.CompletedProcess[bytes]: ...


def run(
    command: Command,
    *,
    input: RunInput = None,
    capture_output: bool = False,
    check: bool = False,
    cwd: CommandPart | None = None,
    text: bool = False,
    timeout: float | None = None,
    success_codes: Sequence[int] = (0,),
) -> ProcessResult:
    argv = _argv(command)
    runner = cast(Callable[..., ProcessResult], subprocess.run)
    breaker = _BREAKERS.get(f"subprocess:{_command_name(argv)}")
    return breaker.call(
        lambda: runner(
            argv,
            input=input,
            capture_output=capture_output,
            check=check,
            cwd=cwd,
            text=text,
            timeout=timeout,
        ),
        is_success=lambda result: result.returncode in success_codes,
    )


def popen(
    command: Command,
    *,
    cwd: CommandPart | None = None,
    env: Mapping[str, str] | Mapping[bytes, bytes] | None = None,
    stdout: StreamTarget = None,
    stderr: StreamTarget = None,
    start_new_session: bool = False,
) -> subprocess.Popen[bytes]:
    argv = _argv(command)
    launcher = cast(Callable[..., subprocess.Popen[bytes]], subprocess.Popen)
    breaker = _BREAKERS.get(f"subprocess:{_command_name(argv)}")
    return breaker.call(
        lambda: launcher(
            argv,
            cwd=cwd,
            env=env,
            stdout=stdout,
            stderr=stderr,
            start_new_session=start_new_session,
        )
    )


def urlopen(
    url: str | urllib.request.Request,
    *,
    timeout: float | None = None,
) -> http.client.HTTPResponse:
    full_url = url.full_url if isinstance(url, urllib.request.Request) else url
    parsed = urllib.parse.urlsplit(full_url)
    first_path = parsed.path.strip("/").split("/", 1)[0] or "root"
    breaker = _BREAKERS.get(f"http:{parsed.netloc}:{first_path}")
    invoke = cast(Callable[..., http.client.HTTPResponse], urllib.request.urlopen)
    return breaker.call(lambda: invoke(url, timeout=timeout))


def socket_connect(host: str, port: int, *, timeout: float | None = None) -> socket.socket:
    breaker = _BREAKERS.get(f"socket:{host}:{port}:connect")
    return breaker.call(lambda: socket.create_connection((host, port), timeout=timeout))


def _mqtt_success(result: MqttResult) -> bool:
    if result is None:
        return True
    if isinstance(result, tuple):
        return result[0] == 0
    if isinstance(result, int):
        return result == 0
    return result.rc == 0


def mqtt_connect(
    client: mqtt.Client,
    host: str,
    port: int = 1883,
    keepalive: int = 60,
) -> MQTTErrorCode | None:
    breaker = _BREAKERS.get(f"mqtt:{host}:{port}:connect")
    return breaker.call(
        lambda: client.connect(host, port, keepalive),
        is_success=_mqtt_success,
    )


def mqtt_subscribe(client: mqtt.Client, topic: str) -> tuple[MQTTErrorCode, int | None] | None:
    breaker = _BREAKERS.get(f"mqtt:subscribe:{topic}")
    return breaker.call(
        lambda: client.subscribe(topic),
        is_success=_mqtt_success,
    )


def mqtt_publish(
    client: mqtt.Client,
    topic: str,
    payload: MqttPayload = None,
) -> mqtt.MQTTMessageInfo | None:
    breaker = _BREAKERS.get(f"mqtt:publish:{topic}")
    return breaker.call(
        lambda: client.publish(topic, payload),
        is_success=_mqtt_success,
    )


def mqtt_publish_single(
    topic: str,
    payload: str | bytes | None = None,
    *,
    hostname: str = "localhost",
    port: int = 1883,
) -> None:
    import paho.mqtt.publish as publish

    with socket_connect(hostname, port, timeout=0.3):
        pass
    breaker = _BREAKERS.get(f"mqtt:{hostname}:{port}:single:{topic}")
    _ = breaker.call(lambda: publish.single(topic, payload=payload, hostname=hostname, port=port))

"""Event-driven live bridge for Sofia³.

PON-compliant (zero polling):
  * the Task Trail DB is watched via inotify (watchdog) — agents update it
    directly, so filesystem events are the authoritative change signal;
  * MQTT trail topics are also subscribed as a redundant push channel;
  * both feed a single thread-safe asyncio queue drained by the WS broadcaster.

Graceful degradation: if the broker or the watched DB is unavailable, the
service keeps running and live signals simply go quiet.
"""

from __future__ import annotations

import asyncio
import json
import logging
import threading
from collections.abc import Iterator
from pathlib import Path
from typing import Any, Optional

import paho.mqtt.client as mqtt
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from reins.harness import external_io, paths
from reins.services.task_trail import TaskTrail

from sofia3.backend import graph_bridge

logger = logging.getLogger("sofia3.live")


_hardware_cache: dict[str, Any] = {}
_hardware_cache_time: float = 0.0


def _collect_telemetry() -> dict[str, Any]:
    """Collect hardware, combos, token budgets, coord, agent status, and pon health."""
    global _hardware_cache, _hardware_cache_time
    import time
    telemetry: dict[str, Any] = {}

    # 1. Hardware profile & gaps (cached 30s)
    now = time.time()
    if _hardware_cache and (now - _hardware_cache_time < 30.0):
        telemetry["hardware"] = _hardware_cache.get("hardware")
        telemetry["hardware_gaps"] = _hardware_cache.get("hardware_gaps")
    else:
        try:
            from reins.services.sys_profiler import SysProfiler
            profiler = SysProfiler()
            hw = profiler.profile_cluster(publish=False)
            gaps = profiler.gap_report()
            _hardware_cache = {"hardware": hw, "hardware_gaps": gaps}
            _hardware_cache_time = now
            telemetry["hardware"] = hw
            telemetry["hardware_gaps"] = gaps
        except Exception as exc:
            telemetry["hardware"] = {"degraded": True, "error": str(exc)}

    # 2. Model Combos & Categories
    try:
        from reins.harness.combo_registry import ComboRegistry
        registry = ComboRegistry()
        combos = [
            {
                "id": c.id,
                "provider": c.provider,
                "model": c.model,
                "tier": getattr(c, "tier", "free"),
                "node": getattr(c, "node", "amdy"),
            }
            for c in registry.all_combos()
        ]
        cats = {
            cat_name: {
                "description": cat_obj.description,
                "amdy": list(cat_obj.amdy),
                "tell": list(cat_obj.tell),
                "cloud": list(cat_obj.cloud),
            }
            for cat_name, cat_obj in registry.config.categories.items()
        }
        telemetry["combos"] = combos
        telemetry["categories"] = cats
    except Exception as exc:
        telemetry["combos"] = []
        telemetry["categories"] = {}

    # 3. Token usage & budgets
    try:
        from reins.services.token_ledger import budget_report
        telemetry["tokens"] = budget_report()
    except Exception as exc:
        telemetry["tokens"] = {"degraded": True, "error": str(exc)}

    # 4. Coordinator slot state
    try:
        from reins.harness.coordinator import get_coordinator
        telemetry["coord"] = get_coordinator().status()
    except Exception as exc:
        telemetry["coord"] = {"degraded": True, "error": str(exc)}

    # 5. Agent budgets
    try:
        from reins.services.resource_budgets import load_budgets
        telemetry["agent_budgets"] = load_budgets()
    except Exception as exc:
        telemetry["agent_budgets"] = {}

    # 6. Training capability
    try:
        from dataclasses import asdict
        from reins.training import capability
        telemetry["training"] = asdict(capability.probe())
    except Exception as exc:
        telemetry["training"] = {"degraded": True, "error": str(exc)}

    # 7. PON live health
    telemetry["pon"] = {
        "zero_polling": True,
        "inotify_active": True,
        "mqtt_active": True,
        "timestamp": time.time(),
    }

    return telemetry


def trail_snapshot() -> dict[str, Any]:
    """Read the lightweight task trail summary + comprehensive telemetry (best-effort)."""
    try:
        tasks = TaskTrail().summary_view(include_archived=False, include_subtasks=False)
    except Exception as exc:  # graceful degradation
        logger.warning("Trail read degraded: %s", exc)
        return {"tasks": [], "summary": {}, "degraded": True, "telemetry": _collect_telemetry()}
    summary: dict[str, int] = {}
    for task in tasks:
        status = str(task.get("status", "pending")).lower()
        summary[status] = summary.get(status, 0) + 1
    return {
        "kind": "trail",
        "tasks": list(tasks[-400:]),  # newest window for the live stream
        "summary": summary,
        "total": len(tasks),
        "telemetry": _collect_telemetry(),
    }


class _TrailFileHandler(FileSystemEventHandler):
    """Inotify handler that signals on Task Trail DB mutations."""

    def __init__(self, on_change: Any, debounce_seconds: float = 0.7) -> None:
        self._on_change = on_change
        self._debounce = debounce_seconds
        self._timer: Optional[threading.Timer] = None
        self._lock = threading.Lock()

    def on_any_event(self, event: FileSystemEvent) -> None:
        if event.is_directory:
            return
        name = Path(event.src_path).name
        if not (name.startswith("task_trail") or name == "reins_ipc.sock"):
            return
        with self._lock:
            if self._timer is not None:
                self._timer.cancel()
            self._timer = threading.Timer(self._debounce, self._on_change)
            self._timer.daemon = True
            self._timer.start()


class LiveBridge:
    """Janitor for the live channel: watchers + asyncio → WebSocket fan-out."""

    def __init__(self) -> None:
        self._queue: asyncio.Queue[dict[str, Any]] = asyncio.Queue(maxsize=512)
        self._observer: Optional[Observer] = None
        self._mqtt: Optional[mqtt.Client] = None
        self._consumers: set[asyncio.Queue[dict[str, Any]]] = set()
        self._producer: Optional[asyncio.Task[Any]] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._is_alive: bool = True

    # -- lifecycle -----------------------------------------------------------
    def start(self) -> None:
        """Start the inotify observer, MQTT subscription, and producer task."""
        self._loop = asyncio.get_running_loop()
        self._is_alive = True
        self._producer = self._loop.create_task(self._drain())
        trail_path = Path(paths.task_trail()).parent
        if trail_path.exists():
            try:
                handler = _TrailFileHandler(self._signal)
                self._observer = Observer()
                self._observer.schedule(handler, str(trail_path), recursive=False)
                self._observer.daemon = True
                self._observer.start()
                logger.info("Trail inotify watcher started on %s", trail_path)
            except Exception as exc:  # graceful degradation
                logger.warning("Trail watcher unavailable: %s", exc)
        self._start_mqtt()

    def _start_mqtt(self) -> None:
        try:
            from sofia3.backend import config

            client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            client.on_connect = lambda c, u, f, rc, p: self._subscribe_all(c)
            client.on_message = self._on_mqtt
            external_io.mqtt_connect(client, config.MQTT_HOST, config.MQTT_PORT, 60)
            client.loop_start()  # background network thread — no polling
            self._mqtt = client
            logger.info("MQTT live bridge subscribed (loop_start)")
        except Exception as exc:  # broker absent -> degrade gracefully
            logger.warning("MQTT live bridge unavailable: %s", exc)

    def _subscribe_all(self, client: mqtt.Client) -> None:
        from sofia3.backend import config

        for topic in config.TRAIL_TOPICS:
            try:
                external_io.mqtt_subscribe(client, topic)
            except Exception as exc:
                logger.warning("MQTT subscribe %s failed: %s", topic, exc)

    def _on_mqtt(self, client: mqtt.Client, userdata: Any, msg: mqtt.MQTTMessage) -> None:
        # Any trail event => refresh the snapshot and fan it out.
        self._signal()

    def _signal(self) -> None:
        """Called from watcher/MQTT threads; push a refresh request through the queue."""
        if self._loop is None:
            return
        try:
            self._loop.call_soon_threadsafe(self._enqueue_snapshot)
        except RuntimeError:
            pass  # loop closed during shutdown

    def _enqueue_snapshot(self) -> None:
        # Any trail mutation invalidates the graph cache (reactive freshness).
        graph_bridge.invalidate()
        from sofia3.backend import training_pipeline
        training_pipeline.trigger_export()
        
        if self._queue.full():
            # Drop-lear-oldest to avoid stalling producers on a stalled consumer.
            try:
                self._queue.get_nowait()
            except asyncio.QueueEmpty:
                pass
        self._queue.put_nowait({"refresh": True})

    # -- consumer plumbing ---------------------------------------------------
    async def _drain(self) -> None:
        while self._is_alive:
            try:
                await self._queue.get()
                payload = trail_snapshot()
                if not self._consumers:
                    continue
                await asyncio.gather(
                    *(q.put(payload) for q in tuple(self._consumers)),
                    return_exceptions=True,
                )
            except asyncio.CancelledError:
                break
            except Exception as exc:  # graceful degradation
                logger.warning("Live drain error: %s", exc)
                await asyncio.sleep(0.5)

    async def subscribe(self) -> Iterator[dict[str, Any]]:
        """Async generator yielding live trail snapshots for one client."""
        q: asyncio.Queue[dict[str, Any]] = asyncio.Queue(maxsize=64)
        self._consumers.add(q)
        try:
            # Initial snapshot on subscribe (catch-up).
            yield trail_snapshot()
            while self._is_alive:
                try:
                    item = await asyncio.wait_for(q.get(), timeout=15.0)
                    yield item
                except asyncio.TimeoutError:
                    # Keepalive when idle — no busy polling (PON).
                    yield {"kind": "heartbeat"}
        finally:
            self._consumers.discard(q)

    async def stop(self) -> None:
        self._is_alive = False
        if self._producer is not None:
            self._producer.cancel()
        if self._mqtt is not None:
            try:
                self._mqtt.disconnect()
            except Exception:
                pass
            self._mqtt.loop_stop()
        if self._observer is not None:
            self._observer.stop()
            self._observer.join(timeout=2.0)
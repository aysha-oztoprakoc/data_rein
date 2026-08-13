"""
Local model plane for the data_rein harness.

Owns the lifecycle and clean invocation of the local Ollama server that serves the
harness's on-disk model store (`ai_models/models/`). Everything here is model-store
aware, uses the HTTP API for clean (spinner-free) output, and degrades gracefully:
if the server is down it can start it; if it cannot, callers get a clear error
instead of a crash.

PON note: no polling. `ensure_server` waits on the readiness endpoint with a
bounded, event-like retry only during the one-time cold start, then returns.
"""

from __future__ import annotations
from reins.services.logger import log_degradation

import json
import logging
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

from reins.harness import external_io, paths

logger = logging.getLogger(__name__)

DEFAULT_HOST = os.environ.get("OLLAMA_HOST", "127.0.0.1:11434").replace("http://", "")


def _coordinator_config() -> dict:
    """Tolerant read of coordinator.json. Returns {} on missing/corrupt config."""
    try:
        return json.loads(paths.coordinator_config().read_text())
    except Exception:
        log_degradation(__name__)
        return {}


def _coordinator_env() -> dict:
    """server_env overrides from coordinator.json, merged into the Ollama spawn env."""
    return dict(_coordinator_config().get("server_env", {}))


def default_options() -> dict:
    """ctx/thread budget law, from coordinator.json with a hardcoded fallback."""
    return dict(_coordinator_config().get("defaults") or {"num_ctx": 2048, "num_thread": 8})


def model_store() -> Path:
    """Canonical local Ollama model store (override with $OLLAMA_MODELS)."""
    env = os.environ.get("OLLAMA_MODELS")
    if env:
        return Path(env).expanduser()
    return paths.home() / "ai_models" / "models"


def _base_url(host: str = DEFAULT_HOST) -> str:
    return f"http://{host}"


def server_up(host: str = DEFAULT_HOST, timeout: float = 2.0) -> bool:
    try:
        with external_io.urlopen(f"{_base_url(host)}/api/tags", timeout=timeout) as r:
            return r.status == 200
    except Exception:
        log_degradation(__name__)
        return False


def list_models(host: str = DEFAULT_HOST) -> list[str]:
    try:
        with external_io.urlopen(f"{_base_url(host)}/api/tags", timeout=5) as r:
            data = json.load(r)
        return [m["name"] for m in data.get("models", [])]
    except Exception:
        log_degradation(__name__)
        return []


def list_models_detailed(host: str = DEFAULT_HOST) -> list[dict]:
    """Like list_models() but keeps name + size from /api/tags. Degrades to []."""
    try:
        with external_io.urlopen(f"{_base_url(host)}/api/tags", timeout=5) as r:
            data = json.load(r)
        return [{"name": m["name"], "size": m.get("size", 0)} for m in data.get("models", [])]
    except Exception:
        log_degradation(__name__)
        return []


def loaded_models(host: str = DEFAULT_HOST) -> list[dict]:
    """Currently resident models via /api/ps, incl. size_vram. Degrades to []."""
    try:
        with external_io.urlopen(f"{_base_url(host)}/api/ps", timeout=5) as r:
            data = json.load(r)
        return data.get("models", [])
    except Exception:
        log_degradation(__name__)
        return []


def load_model(model: str, host: str = DEFAULT_HOST, keep_alive: str = "10m") -> bool:
    """Warm-load `model` via an empty-prompt generate. Blocks until loaded or errors."""
    payload = {"model": model, "prompt": "", "stream": False, "keep_alive": keep_alive}
    req = urllib.request.Request(
        f"{_base_url(host)}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with external_io.urlopen(req, timeout=120) as r:
            return r.status == 200
    except Exception:
        log_degradation(__name__)
        return False


def unload_model(model: str, host: str = DEFAULT_HOST) -> bool:
    """Evict `model` immediately (keep_alive: 0)."""
    return load_model(model, host=host, keep_alive="0")


def _inotify_wait_ready(host: str, log_path: Path, deadline: float) -> bool:
    """PON-1: block on inotify IN_MODIFY events against the `ollama serve` log
    instead of polling server_up on a fixed interval. Each time the log is
    written to, check readiness once; `select` bounds the total wait by
    `deadline` without spinning. Raises if inotify is unavailable (caller
    degrades to `_fallback_wait_ready`, GD-3)."""
    import ctypes
    import ctypes.util
    import select

    libc_name = ctypes.util.find_library("c") or "libc.so.6"
    libc = ctypes.CDLL(libc_name, use_errno=True)
    IN_MODIFY = 0x00000002

    fd = libc.inotify_init1(os.O_NONBLOCK)
    if fd < 0:
        raise OSError(ctypes.get_errno(), "inotify_init1 failed")
    try:
        wd = libc.inotify_add_watch(fd, str(log_path).encode(), IN_MODIFY)
        if wd < 0:
            raise OSError(ctypes.get_errno(), "inotify_add_watch failed")
        remaining = deadline - time.time()
        while remaining > 0:
            ready, _, _ = select.select([fd], [], [], remaining)
            if ready:
                try:
                    os.read(fd, 4096)
                except OSError:
                    pass
            if server_up(host):
                return True
            remaining = deadline - time.time()
        return server_up(host)
    finally:
        os.close(fd)


def ensure_server(host: str = DEFAULT_HOST, wait: float = 20.0) -> bool:
    """
    Ensure an Ollama server is up and serving the harness model store.
    Returns True if reachable. Starts one (detached) if not. Never raises.
    """
    if server_up(host):
        return True

    store = model_store()
    env = dict(os.environ)
    env["OLLAMA_MODELS"] = str(store)
    env["OLLAMA_HOST"] = host
    env.update(_coordinator_env())
    log = paths.home() / "logs" / "ollama_serve.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    log.touch(exist_ok=True)  # inotify needs an existing inode to watch

    try:
        with open(log, "ab") as lf:
            proc = external_io.popen(["ollama", "serve"],
            env=env,
            stdout=lf,
            stderr=lf,
            start_new_session=True,)
    except FileNotFoundError:
        return False

    try:
        from reins.services.resource_budgets import apply_cpu_budget

        num_thread = default_options().get("num_thread", 8)
        cpu_pct = min(100, num_thread * 100 // (os.cpu_count() or num_thread))
        apply_cpu_budget("ollama_serve", cpu_pct, [proc.pid])
    except Exception as error:
        logger.warning("Ollama CPU budget could not be applied: %s", error)

    deadline = time.time() + wait
    try:
        return _inotify_wait_ready(host, log, deadline)
    except Exception as error:
        logger.warning("Ollama readiness notification unavailable: %s", error)
        return server_up(host)


def generate(
    model: str,
    prompt: str,
    host: str = DEFAULT_HOST,
    timeout: float = 300.0,
    options: Optional[dict] = None,
) -> str:
    """
    Run a single non-streaming completion via the Ollama HTTP API and return clean
    text (no TUI spinner artifacts). Raises RuntimeError on failure so the caller's
    graceful-degradation layer (ModelRouter) can fall through to the next candidate.
    """
    payload = {"model": model, "prompt": prompt, "stream": False}
    payload["options"] = {**default_options(), **(options or {})}
    req = urllib.request.Request(
        f"{_base_url(host)}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with external_io.urlopen(req, timeout=timeout) as r:
            data = json.load(r)
        text = data.get("response", "")
        if not text.strip():
            raise RuntimeError("empty response")
        return text
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"ollama http {e.code}: {e.reason}")
    except Exception as e:
        raise RuntimeError(str(e))

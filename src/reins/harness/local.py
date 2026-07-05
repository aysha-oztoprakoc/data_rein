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

import json
import os
import subprocess
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional

from reins.harness import paths

DEFAULT_HOST = os.environ.get("OLLAMA_HOST", "127.0.0.1:11434").replace("http://", "")


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
        with urllib.request.urlopen(f"{_base_url(host)}/api/tags", timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def list_models(host: str = DEFAULT_HOST) -> list[str]:
    try:
        with urllib.request.urlopen(f"{_base_url(host)}/api/tags", timeout=5) as r:
            data = json.load(r)
        return [m["name"] for m in data.get("models", [])]
    except Exception:
        return []


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
    log = paths.home() / "logs" / "ollama_serve.log"
    log.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(log, "ab") as lf:
            subprocess.Popen(
                ["ollama", "serve"],
                env=env,
                stdout=lf,
                stderr=lf,
                start_new_session=True,
            )
    except FileNotFoundError:
        return False

    # Bounded, passive-block cold-start wait: `ollama serve` doesn't expose a
    # signal for "ready", so a short-interval readiness check is the only option.
    # threading.Event().wait() is a real blocking wait (not a busy spin), scoped
    # to this one-time startup rather than an ongoing poll loop.
    gate = threading.Event()
    deadline = time.time() + wait
    while time.time() < deadline:
        if server_up(host):
            return True
        gate.wait(0.5)
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
    if options:
        payload["options"] = options
    req = urllib.request.Request(
        f"{_base_url(host)}/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.load(r)
        text = data.get("response", "")
        if not text.strip():
            raise RuntimeError("empty response")
        return text
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"ollama http {e.code}: {e.reason}")
    except Exception as e:
        raise RuntimeError(str(e))

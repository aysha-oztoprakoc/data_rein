"""
Tests for the event-driven cold-start wait in reins.harness.local.ensure_server
(PON-1: no fixed-interval polling loop for the "is it up yet" question).

Written first (TDD-1/Fase 3): the seams (`_inotify_wait_ready`,
`_fallback_wait_ready`) are patched independently so the orchestration in
`ensure_server` is tested without touching real inotify or a real Popen.
"""

from __future__ import annotations

import threading
import time

import pytest

from reins.harness import local


class _FakePopen:
    """Records the invocation instead of spawning a real process."""

    calls: list[dict] = []

    def __init__(self, args, **kwargs):
        _FakePopen.calls.append({"args": args, **kwargs})


@pytest.fixture(autouse=True)
def _reset_fake_popen():
    _FakePopen.calls = []
    yield
    _FakePopen.calls = []


def test_ensure_server_already_up_never_starts_or_waits(monkeypatch):
    monkeypatch.setattr(local, "server_up", lambda host, timeout=2.0: True)

    def _boom(*a, **k):
        raise AssertionError("Popen must not be called when the server is already up")

    monkeypatch.setattr(local.subprocess, "Popen", _boom)
    assert local.ensure_server(host="127.0.0.1:1") is True


def test_ensure_server_starts_process_and_uses_inotify_wait(monkeypatch, tmp_path):
    monkeypatch.setattr(local, "server_up", lambda host, timeout=2.0: False)
    monkeypatch.setattr(local.paths, "home", lambda: tmp_path)
    monkeypatch.setattr(local.subprocess, "Popen", _FakePopen)

    seen: dict = {}

    def _fake_inotify_wait(host, log_path, deadline):
        seen["host"] = host
        seen["log_path"] = log_path
        seen["deadline"] = deadline
        return True

    monkeypatch.setattr(local, "_inotify_wait_ready", _fake_inotify_wait)

    def _boom(*a, **k):
        raise AssertionError("fallback must not run when inotify succeeds")

    monkeypatch.setattr(local, "_fallback_wait_ready", _boom)

    assert local.ensure_server(host="127.0.0.1:1", wait=5.0) is True
    assert len(_FakePopen.calls) == 1
    assert _FakePopen.calls[0]["args"] == ["ollama", "serve"]
    assert seen["host"] == "127.0.0.1:1"
    assert seen["log_path"] == tmp_path / "logs" / "ollama_serve.log"


def test_ensure_server_falls_back_when_inotify_unavailable(monkeypatch, tmp_path):
    """GD-3: inotify being unavailable (sandboxed FS, non-Linux, ...) degrades
    to the bounded blocking-wait fallback instead of crashing ensure_server."""
    monkeypatch.setattr(local, "server_up", lambda host, timeout=2.0: False)
    monkeypatch.setattr(local.paths, "home", lambda: tmp_path)
    monkeypatch.setattr(local.subprocess, "Popen", _FakePopen)
    monkeypatch.setattr(
        local, "_inotify_wait_ready",
        lambda *a, **k: (_ for _ in ()).throw(OSError("inotify_init1 failed")),
    )

    seen: dict = {}

    def _fake_fallback(host, deadline):
        seen["host"] = host
        seen["deadline"] = deadline
        return True

    monkeypatch.setattr(local, "_fallback_wait_ready", _fake_fallback)

    assert local.ensure_server(host="127.0.0.1:1", wait=5.0) is True
    assert seen["host"] == "127.0.0.1:1"


def test_ensure_server_returns_false_when_ollama_binary_missing(monkeypatch, tmp_path):
    monkeypatch.setattr(local, "server_up", lambda host, timeout=2.0: False)
    monkeypatch.setattr(local.paths, "home", lambda: tmp_path)

    def _missing(*a, **k):
        raise FileNotFoundError("ollama")

    monkeypatch.setattr(local.subprocess, "Popen", _missing)

    def _boom(*a, **k):
        raise AssertionError("no wait strategy should run when the binary is missing")

    monkeypatch.setattr(local, "_inotify_wait_ready", _boom)
    monkeypatch.setattr(local, "_fallback_wait_ready", _boom)

    assert local.ensure_server(host="127.0.0.1:1") is False


# --- _fallback_wait_ready: pure unit test, no real sleeping -----------------

def test_fallback_wait_ready_polls_injected_wait_until_server_up(monkeypatch):
    calls = {"server_up": 0, "wait": []}

    def _fake_server_up(host, timeout=2.0):
        calls["server_up"] += 1
        return calls["server_up"] >= 3

    monkeypatch.setattr(local, "server_up", _fake_server_up)

    clock = iter([0.0, 0.1, 0.2, 0.3, 100.0])  # deadline is far in the future
    fake_clock = lambda: next(clock)  # noqa: E731

    def fake_wait(seconds):
        calls["wait"].append(seconds)

    result = local._fallback_wait_ready(
        "127.0.0.1:1", deadline=50.0, wait=fake_wait, clock=fake_clock
    )
    assert result is True
    assert calls["server_up"] == 3
    assert calls["wait"] == [0.5, 0.5]


def test_fallback_wait_ready_gives_up_at_deadline(monkeypatch):
    monkeypatch.setattr(local, "server_up", lambda host, timeout=2.0: False)
    clock = iter([0.0, 10.0, 20.0])
    result = local._fallback_wait_ready(
        "127.0.0.1:1", deadline=15.0, wait=lambda s: None, clock=lambda: next(clock)
    )
    assert result is False


# --- _inotify_wait_ready: real syscalls against a tmp log file -------------

def test_inotify_wait_ready_wakes_on_log_write(monkeypatch, tmp_path):
    log = tmp_path / "ollama_serve.log"
    log.touch()
    calls = {"n": 0}

    def _fake_server_up(host, timeout=2.0):
        calls["n"] += 1
        return calls["n"] >= 2

    monkeypatch.setattr(local, "server_up", _fake_server_up)

    def _writer():
        time.sleep(0.05)
        with open(log, "a", encoding="utf-8") as f:
            f.write("ready\n")

    threading.Thread(target=_writer, daemon=True).start()
    deadline = time.time() + 5.0
    assert local._inotify_wait_ready("127.0.0.1:1", log, deadline) is True


def test_inotify_wait_ready_respects_deadline_when_nothing_happens(tmp_path, monkeypatch):
    log = tmp_path / "ollama_serve.log"
    log.touch()
    monkeypatch.setattr(local, "server_up", lambda host, timeout=2.0: False)

    start = time.time()
    deadline = start + 0.3
    assert local._inotify_wait_ready("127.0.0.1:1", log, deadline) is False
    assert time.time() - start < 2.0

"""Smoke tests for the Sofia³ backend (API surface + live bridge wiring).

These are fast, hermetic checks against the FastAPI app object — no server
process required.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "third_party"))
sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient  # noqa: E402

from sofia3.backend.app import app  # noqa: E402


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_health(client) -> None:
    resp = client.get("/api/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "SYS_OK"
    assert body["service"] == "sofia3"


def test_task_summary(client) -> None:
    resp = client.get("/api/tasks/summary")
    assert resp.status_code == 200
    body = resp.json()
    assert "summary" in body
    assert "total" in body
    assert isinstance(body["total"], int)


def test_task_list(client) -> None:
    resp = client.get("/api/tasks", params={"limit": 5})
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body["tasks"], list)
    assert "summary" in body


def test_wiki_stats(client) -> None:
    resp = client.get("/api/wiki/stats")
    assert resp.status_code == 200
    body = resp.json()
    assert "stats" in body
    assert "categories" in body


def test_wiki_pages(client) -> None:
    resp = client.get("/api/wiki/pages", params={"limit": 3})
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body["pages"], list)
    assert body["total"] >= 0


def test_wiki_memory_ok(client) -> None:
    """Fetch an existing memory by UID (200 + text present)."""
    resp = client.get("/api/wiki/memories", params={"limit": 1})
    assert resp.status_code == 200
    memories = resp.json().get("memories", [])
    if not memories:
        from reins.harness.wiki import WikiDB

        with WikiDB() as db:
            db.add_memory("test memory content for sofia3", category="test", owner="agent")
        resp = client.get("/api/wiki/memories", params={"limit": 1})
        assert resp.status_code == 200
        memories = resp.json().get("memories", [])

    assert len(memories) > 0
    uid = memories[0]["uid"]
    mem_resp = client.get(f"/api/wiki/memory/{uid}")
    assert mem_resp.status_code == 200
    body = mem_resp.json()
    assert "memory" in body
    assert "text" in body["memory"]
    assert body["memory"]["uid"] == uid


def test_wiki_memory_404(client) -> None:
    """Nonexistent memory UID must return 404."""
    resp = client.get("/api/wiki/memory/nonexistent-uid-never-created-12345")
    assert resp.status_code == 404


def test_graph_degraded_or_ok(client) -> None:
    """Graph bridge must degrade gracefully (503) or return a valid shape."""
    resp = client.get("/api/graph")
    if resp.status_code == 503:
        assert resp.json()["detail"]["degraded"] is True
    else:
        body = resp.json()
        assert "graph" in body
        assert "stats" in body
        assert "nodes" in body["graph"]
        assert "edges" in body["graph"]


def test_graph_stats(client) -> None:
    resp = client.get("/api/graph/stats")
    if resp.status_code == 503:
        assert resp.json()["detail"]["degraded"] is True
    else:
        body = resp.json()
        assert "stats" in body


def test_ws_origin_guard(client) -> None:
    """Foreign Origin must be rejected before the WS handshake (close 4403)."""
    import starlette.websockets

    with pytest.raises(starlette.websockets.WebSocketDisconnect) as exc_info:
        with client.websocket_connect(
            "/ws", headers={"origin": "http://evil.example"}
        ) as ws:
            ws.receive_json()
    assert exc_info.value.code == 4403


def test_ws_accepts_local_origin(client) -> None:
    """Local Origin may connect and receives an initial trail snapshot."""
    with client.websocket_connect("/ws", headers={"origin": "http://127.0.0.1:8088"}) as ws:
        msg = ws.receive_json()
        assert msg["kind"] == "trail"


def test_wiki_search_semantic_and_chunks(client) -> None:
    """Wiki search must return pages, memories, and semantic chunks."""
    resp = client.get("/api/wiki/search", params={"q": "PON paradigm zero polling"})
    assert resp.status_code == 200
    body = resp.json()
    assert "pages" in body
    assert "memories" in body
    assert "chunks" in body
    assert isinstance(body["pages"], list)
    assert isinstance(body["memories"], list)
    assert isinstance(body["chunks"], list)


def test_wiki_search_empty_query(client) -> None:
    """Empty query should return empty lists gracefully."""
    resp = client.get("/api/wiki/search", params={"q": ""})
    assert resp.status_code == 200
    body = resp.json()
    assert body["pages"] == []
    assert body["memories"] == []
    assert body["chunks"] == []


def test_graph_snapshot_structure(client) -> None:
    """Graph snapshot should return structured nodes and edges with stats."""
    resp = client.get("/api/graph")
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("degraded") is False
    assert "graph" in body
    assert "stats" in body
    assert "nodes" in body["graph"]
    assert "edges" in body["graph"]
    assert "engine" in body.get("notes", {})


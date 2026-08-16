from __future__ import annotations

import json
import time
from pathlib import Path

from reins.harness.wiki import WikiDB
from reins.harness.wiki_contract import WikiCrud


def test_page_lists_are_bounded_summaries_and_updates_are_explicit(tmp_path: Path) -> None:
    # Given
    with WikiDB(tmp_path / "wiki.db") as database:
        crud = WikiCrud(database)
        created = crud.create_page(title="Boundary", content="secret full body")

        # When
        listing = crud.list_pages(limit=10)
        updated = crud.update_page(created["slug"], title="Boundary", content="new body")

        # Then
        assert listing["total"] == 1
        assert "content" not in listing["items"][0]
        assert updated == created
        assert crud.get_page(created["slug"])["content"] == "new body"


def test_memory_revision_creates_replacement_without_mutating_old_fact(tmp_path: Path) -> None:
    # Given
    with WikiDB(tmp_path / "wiki.db") as database:
        crud = WikiCrud(database)
        old_uid = crud.create_memory(text="old immutable fact", category="facts")["uid"]

        # When
        revision = crud.revise_memory(old_uid, text="replacement fact", category="facts")

        # Then
        assert revision["old_retained"] is True
        assert revision["new_uid"] != old_uid
        assert crud.get_memory(old_uid)["text"] == "old immutable fact"
        assert crud.get_memory(revision["new_uid"])["text"] == "replacement fact"


def test_ten_thousand_record_lists_meet_latency_and_payload_bounds(tmp_path: Path) -> None:
    # Given
    with WikiDB(tmp_path / "wiki.db") as database:
        now = time.time()
        database.conn.executemany(
            "INSERT INTO memories(uid,text,category,source,owner,timestamp) VALUES(?,?,?,?,?,?)",
            [(f"uid-{index}", "x" * 500, "fixture", "test", "test", now + index) for index in range(10_000)],
        )
        database.conn.commit()
        crud = WikiCrud(database)

        # When
        durations = []
        result = crud.list_memories(limit=200)
        payload = json.dumps(result).encode("utf-8")
        for _ in range(20):
            started = time.perf_counter()
            result = crud.list_memories(limit=200)
            durations.append((time.perf_counter() - started) * 1000)
            payload = json.dumps(result).encode("utf-8")
        p95_ms = sorted(durations)[18]

        # Then
        assert p95_ms < 250
        assert len(payload) < 500_000
        assert all("text" not in item for item in result["items"])

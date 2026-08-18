from __future__ import annotations

import json
from pathlib import Path

import pytest

from reins.services.task_trail import TaskTrail


def test_indexed_operations_do_not_parse_json_history(
    trail: TaskTrail,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given one durable task and a guard that rejects full JSON history parsing.
    task_id = trail.create_task("audit", "inspect harness", "amdy")

    def reject_history_scan(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("indexed Task Trail operations must not parse JSON history")

    monkeypatch.setattr(json, "load", reject_history_scan)

    # When indexed status and identity operations run.
    trail.set_status(task_id, "running")
    task = trail.get_task(task_id)
    running = trail.by_status("running")

    # Then the exact record is updated without a total-history scan.
    assert task is not None
    assert task["status"] == "running"
    assert task["attempts"] == 1
    assert [row["task_id"] for row in running] == [task_id]


def test_legacy_json_trail_is_imported_once(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Given a pre-index Task Trail JSON file.
    state_dir = tmp_path / "state"
    _ = state_dir.mkdir()
    legacy = state_dir / "task_trail.json"
    _ = legacy.write_text(
        json.dumps(
            [
                {
                    "task_id": "legacy-task",
                    "task_type": "migration",
                    "prompt": "preserve me",
                    "target_node": "tell",
                    "status": "success",
                    "timestamp": 1.0,
                    "attempts": 2,
                    "custom": {"source": "json"},
                }
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.setenv("DATA_REIN_STATE_DIR", str(state_dir))

    # When the indexed trail opens twice.
    first = TaskTrail()
    second = TaskTrail()

    # Then the record and extension fields survive exactly once in SQLite.
    assert first.trail_path.endswith("task_trail.sqlite3")
    assert second.all_tasks() == first.all_tasks()
    assert first.get_task("legacy-task") == {
        "task_id": "legacy-task",
        "task_type": "migration",
        "prompt": "preserve me",
        "target_node": "tell",
        "status": "success",
        "timestamp": 1.0,
        "attempts": 2,
        "parent_task_id": None,
        "is_archived": False,
        "custom": {"source": "json"},
    }
    assert legacy.is_file()

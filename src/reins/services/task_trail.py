from __future__ import annotations

import json
import sqlite3
import time
import uuid
from pathlib import Path
from typing import TypeAlias, cast

from reins.harness import paths
from reins.services.logger import get_logger

logger = get_logger(__name__)

JsonValue: TypeAlias = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]
TaskRecord: TypeAlias = dict[str, JsonValue]

FALLBACK_TARGET = "data-ody"
FALLBACK_SOURCE_STATUSES = ("pending", "running")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    task_id TEXT PRIMARY KEY,
    status TEXT NOT NULL,
    target_node TEXT NOT NULL,
    timestamp REAL NOT NULL,
    record_json TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status, timestamp);
CREATE INDEX IF NOT EXISTS idx_tasks_fallback ON tasks(target_node, status, timestamp);
CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


class TaskTrail:
    def __init__(self) -> None:
        _ = paths.ensure_state_dir()
        self.trail_path: str = str(paths.task_trail())
        self.legacy_path: str = str(paths.legacy_task_trail())
        self._initialize()
        self._migrate_legacy_json()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.trail_path, timeout=5.0)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        try:
            with self._connect() as connection:
                _ = connection.executescript(_SCHEMA)
                _ = connection.execute("PRAGMA journal_mode=WAL")
                _ = connection.execute("PRAGMA synchronous=FULL")
        except sqlite3.Error:
            logger.warning("Task Trail database initialization failed", exc_info=True)

    @classmethod
    def _to_json_value(cls, value: object) -> JsonValue:
        if value is None or isinstance(value, (bool, int, float, str)):
            return value
        if isinstance(value, list):
            return [cls._to_json_value(item) for item in cast(list[object], value)]
        if isinstance(value, dict):
            mapping = cast(dict[object, object], value)
            if not all(isinstance(key, str) for key in mapping):
                raise TypeError("Task Trail object keys must be strings")
            return {
                cast(str, key): cls._to_json_value(item)
                for key, item in mapping.items()
            }
        raise TypeError(f"Task Trail value is not JSON-compatible: {type(value).__name__}")

    @classmethod
    def _decode(cls, row: sqlite3.Row) -> TaskRecord:
        encoded = cast(str, row["record_json"])
        record = cls._to_json_value(cast(object, json.loads(encoded)))
        if not isinstance(record, dict):
            raise TypeError("Task Trail record must decode to an object")
        return record

    @staticmethod
    def _store(connection: sqlite3.Connection, record: TaskRecord) -> None:
        raw_task_id = record.get("task_id")
        raw_status = record.get("status", "pending")
        raw_target = record.get("target_node", "amdy")
        raw_timestamp = record.get("timestamp", time.time())
        if not isinstance(raw_task_id, str):
            raise TypeError("Task Trail task_id must be a string")
        if not isinstance(raw_status, str) or not isinstance(raw_target, str):
            raise TypeError("Task Trail status and target_node must be strings")
        if not isinstance(raw_timestamp, (int, float)):
            raise TypeError("Task Trail timestamp must be numeric")
        timestamp = float(raw_timestamp)
        record["timestamp"] = timestamp
        _ = connection.execute(
            """
            INSERT INTO tasks(task_id, status, target_node, timestamp, record_json)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(task_id) DO UPDATE SET
                status=excluded.status,
                target_node=excluded.target_node,
                timestamp=excluded.timestamp,
                record_json=excluded.record_json
            """,
            (raw_task_id, raw_status, raw_target, timestamp, json.dumps(record)),
        )

    def _migrate_legacy_json(self) -> None:
        legacy = Path(self.legacy_path)
        if not legacy.is_file():
            return
        try:
            records = self._to_json_value(
                cast(object, json.loads(legacy.read_text(encoding="utf-8")))
            )
            if not isinstance(records, list):
                raise TypeError("legacy Task Trail must contain a list")
            with self._connect() as connection:
                migrated = cast(
                    sqlite3.Row | None,
                    connection.execute(
                        "SELECT 1 FROM metadata WHERE key = 'legacy_json_imported'"
                    ).fetchone(),
                )
                if migrated is not None:
                    return
                for record in records:
                    if isinstance(record, dict) and record.get("task_id"):
                        self._store(connection, record)
                _ = connection.execute(
                    "INSERT INTO metadata(key, value) VALUES ('legacy_json_imported', ?)",
                    (str(time.time()),),
                )
        except (json.JSONDecodeError, OSError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Legacy Task Trail import failed", exc_info=True)

    def _read(self, query: str, parameters: tuple[str, ...] = ()) -> list[TaskRecord]:
        try:
            with self._connect() as connection:
                rows = cast(list[sqlite3.Row], connection.execute(query, parameters).fetchall())
            return [self._decode(row) for row in rows]
        except (json.JSONDecodeError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Task Trail read degraded", exc_info=True)
            return []

    def _load(self) -> list[TaskRecord]:
        return self.all_tasks()

    def all_tasks(self) -> list[TaskRecord]:
        return self._read("SELECT record_json FROM tasks ORDER BY timestamp, task_id")

    def by_status(self, *statuses: str) -> list[TaskRecord]:
        if not statuses:
            return []
        placeholders = ", ".join("?" for _ in statuses)
        # Interpolation creates only literal placeholders; every status remains a bound parameter.
        query = f"SELECT record_json FROM tasks WHERE status IN ({placeholders}) ORDER BY timestamp, task_id"  # nosec B608
        return self._read(query, tuple(statuses))

    def get_task(self, task_id: str) -> TaskRecord | None:
        records = self._read(
            "SELECT record_json FROM tasks WHERE task_id = ?",
            (task_id,),
        )
        return records[0] if records else None

    def get_failed_tasks(self) -> list[TaskRecord]:
        return self.by_status("failed")

    def fallback_candidates(self) -> list[TaskRecord]:
        return self._read(
            """
            SELECT record_json FROM tasks
            WHERE target_node = ? AND status IN (?, ?)
            ORDER BY timestamp, task_id
            """,
            (FALLBACK_TARGET, *FALLBACK_SOURCE_STATUSES),
        )

    def create_task(self, task_type: str, prompt: str, target_node: str) -> str:
        task_id = str(uuid.uuid4())
        _ = self.upsert_task(task_id, task_type=task_type, prompt=prompt,
                             target_node=target_node, status="pending")
        return task_id

    def update_task(self, task_id: str, status: str) -> None:
        self.set_status(task_id, status)

    def set_status(self, task_id: str, status: str) -> None:
        try:
            with self._connect() as connection:
                _ = connection.execute("BEGIN IMMEDIATE")
                row = cast(
                    sqlite3.Row | None,
                    connection.execute(
                        "SELECT record_json FROM tasks WHERE task_id = ?",
                        (task_id,),
                    ).fetchone(),
                )
                if row is None:
                    return
                record = self._decode(row)
                record["status"] = status
                if status in ("running", "running_fallback"):
                    attempts = record.get("attempts", 0)
                    record["attempts"] = (attempts if isinstance(attempts, int) else 0) + 1
                self._store(connection, record)
        except (json.JSONDecodeError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Task Trail status update degraded", exc_info=True)

    def upsert_task(self, task_id: str, **fields: object) -> str:
        try:
            with self._connect() as connection:
                _ = connection.execute("BEGIN IMMEDIATE")
                row = cast(
                    sqlite3.Row | None,
                    connection.execute(
                        "SELECT record_json FROM tasks WHERE task_id = ?",
                        (task_id,),
                    ).fetchone(),
                )
                record: TaskRecord
                if row is not None:
                    record = self._decode(row)
                else:
                    record = {
                        "task_id": task_id,
                        "task_type": "generic",
                        "prompt": "",
                        "target_node": "amdy",
                        "status": "pending",
                        "timestamp": time.time(),
                        "attempts": 0,
                    }
                for key, value in fields.items():
                    record[key] = self._to_json_value(value)
                self._store(connection, record)
        except (json.JSONDecodeError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Task Trail upsert degraded", exc_info=True)
        return task_id

    def clear(self) -> None:
        try:
            with self._connect() as connection:
                _ = connection.execute("DELETE FROM tasks")
        except sqlite3.Error:
            logger.warning("Task Trail clear degraded", exc_info=True)

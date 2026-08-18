from __future__ import annotations

import json
import sqlite3
import time
import uuid
from pathlib import Path
from typing import TypeAlias, cast

from reins.harness import paths
from reins.services.logger import get_logger
from reins.harness import external_io

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
                
                # Check for and add parent_task_id
                cursor = connection.execute("PRAGMA table_info(tasks)")
                columns = [row["name"] for row in cursor.fetchall()]
                
                if "parent_task_id" not in columns:
                    connection.execute("ALTER TABLE tasks ADD COLUMN parent_task_id TEXT")
                    connection.execute("CREATE INDEX idx_tasks_parent ON tasks(parent_task_id)")
                
                if "is_archived" not in columns:
                    connection.execute("ALTER TABLE tasks ADD COLUMN is_archived INTEGER DEFAULT 0")
                    connection.execute("CREATE INDEX idx_tasks_archived ON tasks(is_archived)")

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
        
        # Populate DB-level columns into record if not already present
        if "parent_task_id" in row.keys() and "parent_task_id" not in record:
            record["parent_task_id"] = row["parent_task_id"]
        if "is_archived" in row.keys() and "is_archived" not in record:
            record["is_archived"] = bool(row["is_archived"])
            
        return record

    @staticmethod
    def _store(connection: sqlite3.Connection, record: TaskRecord) -> None:
        raw_task_id = record.get("task_id")
        raw_status = record.get("status", "pending")
        raw_target = record.get("target_node", "amdy")
        raw_timestamp = record.get("timestamp", time.time())
        raw_parent = record.get("parent_task_id")
        raw_archived = 1 if record.get("is_archived") else 0
        
        if not isinstance(raw_task_id, str):
            raise TypeError("Task Trail task_id must be a string")
        if not isinstance(raw_status, str) or not isinstance(raw_target, str):
            raise TypeError("Task Trail status and target_node must be strings")
        if not isinstance(raw_timestamp, (int, float)):
            raise TypeError("Task Trail timestamp must be numeric")
        
        timestamp = float(raw_timestamp)
        record["timestamp"] = timestamp
        parent_task_id = str(raw_parent) if raw_parent else None
        
        _ = connection.execute(
            """
            INSERT INTO tasks(task_id, status, target_node, timestamp, record_json, parent_task_id, is_archived)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(task_id) DO UPDATE SET
                status=excluded.status,
                target_node=excluded.target_node,
                timestamp=excluded.timestamp,
                record_json=excluded.record_json,
                parent_task_id=excluded.parent_task_id,
                is_archived=excluded.is_archived
            """,
            (raw_task_id, raw_status, raw_target, timestamp, json.dumps(record), parent_task_id, raw_archived),
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
        return self._read("SELECT * FROM tasks ORDER BY timestamp, task_id")

    def by_status(self, *statuses: str) -> list[TaskRecord]:
        if not statuses:
            return []
        placeholders = ", ".join("?" for _ in statuses)
        query = f"SELECT * FROM tasks WHERE status IN ({placeholders}) ORDER BY timestamp, task_id"  # nosec B608
        return self._read(query, tuple(statuses))

    def get_task(self, task_id: str) -> TaskRecord | None:
        records = self._read(
            "SELECT * FROM tasks WHERE task_id = ?",
            (task_id,),
        )
        return records[0] if records else None

    def get_failed_tasks(self) -> list[TaskRecord]:
        return self.by_status("failed")

    def fallback_candidates(self) -> list[TaskRecord]:
        return self._read(
            """
            SELECT * FROM tasks
            WHERE target_node = ? AND status IN (?, ?)
            ORDER BY timestamp, task_id
            """,
            (FALLBACK_TARGET, *FALLBACK_SOURCE_STATUSES),
        )

    def create_task(self, task_type: str, prompt: str, target_node: str, parent_task_id: str | None = None) -> str:
        task_id = str(uuid.uuid4())
        _ = self.upsert_task(task_id, task_type=task_type, prompt=prompt,
                             target_node=target_node, status="pending",
                             parent_task_id=parent_task_id)
        return task_id

    def _notify_update(self, task_id: str, status: str) -> None:
        try:
            payload = json.dumps({"task_id": task_id, "status": status})
            external_io.mqtt_publish_single(f"data_rein/trail/task/{task_id}", payload)
        except Exception:
            logger.warning("Failed to publish task update over MQTT", exc_info=True)

    def update_task(self, task_id: str, status: str) -> None:
        self.set_status(task_id, status)

    def set_status(self, task_id: str, status: str) -> None:
        try:
            with self._connect() as connection:
                _ = connection.execute("BEGIN IMMEDIATE")
                row = cast(
                    sqlite3.Row | None,
                    connection.execute(
                        "SELECT * FROM tasks WHERE task_id = ?",
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
            self._notify_update(task_id, status)
        except (json.JSONDecodeError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Task Trail status update degraded", exc_info=True)

    def upsert_task(self, task_id: str, **fields: object) -> str:
        status = "pending"
        try:
            with self._connect() as connection:
                _ = connection.execute("BEGIN IMMEDIATE")
                row = cast(
                    sqlite3.Row | None,
                    connection.execute(
                        "SELECT * FROM tasks WHERE task_id = ?",
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
                        "is_archived": False,
                    }
                for key, value in fields.items():
                    record[key] = self._to_json_value(value)
                self._store(connection, record)
                status = str(record.get("status", "pending"))
            self._notify_update(task_id, status)
        except (json.JSONDecodeError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Task Trail upsert degraded", exc_info=True)
        return task_id
        
    def summary_view(self, include_archived: bool = False, include_subtasks: bool = False) -> list[dict[str, str]]:
        query = "SELECT task_id, status, record_json FROM tasks WHERE 1=1"
        params = []
        
        if not include_archived:
            query += " AND is_archived = 0"
        
        if not include_subtasks:
            query += " AND parent_task_id IS NULL"
            
        query += " ORDER BY timestamp, task_id"
        
        results = []
        try:
            with self._connect() as connection:
                rows = connection.execute(query, params).fetchall()
                for row in rows:
                    encoded = row["record_json"]
                    record = json.loads(encoded)
                    title = record.get("prompt", "")
                    if len(title) > 80:
                        title = title[:77] + "..."
                    results.append({
                        "task_id": row["task_id"],
                        "status": row["status"],
                        "title": title,
                        "task_type": record.get("task_type", ""),
                        "target_node": record.get("target_node", ""),
                    })
        except (json.JSONDecodeError, sqlite3.Error, TypeError, ValueError):
            logger.warning("Task Trail summary view degraded", exc_info=True)
            
        return results

    def archive_task(self, task_id: str) -> None:
        try:
            with self._connect() as connection:
                _ = connection.execute("BEGIN IMMEDIATE")
                row = connection.execute("SELECT * FROM tasks WHERE task_id = ?", (task_id,)).fetchone()
                if row is None:
                    return
                record = self._decode(row)
                record["is_archived"] = True
                self._store(connection, record)
            self._notify_update(task_id, "archived")
        except sqlite3.Error:
            logger.warning("Task Trail archive degraded", exc_info=True)

    def clear(self) -> None:
        try:
            with self._connect() as connection:
                _ = connection.execute("DELETE FROM tasks")
        except sqlite3.Error:
            logger.warning("Task Trail clear degraded", exc_info=True)

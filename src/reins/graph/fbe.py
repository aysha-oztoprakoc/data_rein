"""
Fact Base Elements (FBE) and State Transition Definitions for PON Graph Engine.

Zero-polling state models: Nodes never store state in local variables;
they mutate and react to Attributes published to the FBE store and MQTT topics.
"""
from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional


class FBEState(str, Enum):
    TASK_CREATED = "TASK_CREATED"
    TASK_READY_FOR_EXECUTION = "TASK_READY_FOR_EXECUTION"
    RAW_DATA_AVAILABLE = "RAW_DATA_AVAILABLE"
    TRAINING_REQUIRED = "TRAINING_REQUIRED"
    ESCALATION_REQUIRED = "ESCALATION_REQUIRED"
    QC_REQUEST = "QC_REQUEST"
    QC_REPORT = "QC_REPORT"
    EXECUTION_COMPLETED = "EXECUTION_COMPLETED"
    BLOCKED = "BLOCKED"


@dataclass
class FBEAttribute:
    name: str
    value: Any
    task_id: str
    timestamp: float = field(default_factory=time.time)
    version: int = 1
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps({
            "name": self.name,
            "value": self.value,
            "task_id": self.task_id,
            "timestamp": self.timestamp,
            "version": self.version,
            "metadata": self.metadata,
        })

    @classmethod
    def from_json(cls, data: str | bytes) -> FBEAttribute:
        payload = json.loads(data)
        return cls(
            name=payload["name"],
            value=payload["value"],
            task_id=payload.get("task_id", str(uuid.uuid4())),
            timestamp=payload.get("timestamp", time.time()),
            version=payload.get("version", 1),
            metadata=payload.get("metadata", {}),
        )


class LoopBudgetExceededError(Exception):
    """Raised when a task exceeds its maximum allowed state transition iterations."""
    pass


class LoopBudget:
    """Tracks state transition counts per task ID to prevent infinite graph cycling."""

    def __init__(self, max_iterations: int = 10) -> None:
        self.max_iterations = max_iterations
        self._counts: Dict[str, int] = {}

    def record_step(self, task_id: str) -> int:
        current = self._counts.get(task_id, 0) + 1
        self._counts[task_id] = current
        if current > self.max_iterations:
            raise LoopBudgetExceededError(
                f"Task '{task_id}' exceeded max loop budget of {self.max_iterations} iterations."
            )
        return current

    def get_count(self, task_id: str) -> int:
        return self._counts.get(task_id, 0)

    def reset(self, task_id: str) -> None:
        self._counts.pop(task_id, None)

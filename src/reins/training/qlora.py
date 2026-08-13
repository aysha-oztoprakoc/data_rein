"""Validated QLoRA/LoRA orchestration with one bounded OOM degradation step."""

from __future__ import annotations

import time
import uuid
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, JsonValue, ValidationError

from reins.harness import paths
from reins.services.logger import log_degradation
from reins.training.capability import TrainBackend, probe
from reins.training.config import TrainingConfig, load_training_config
from reins.training.records import validate_jsonl


@dataclass(frozen=True, slots=True)
class TrainResult:
    ok: bool
    run_dir: str | None = None
    backend: str | None = None
    error: str | None = None
    steps: int = 0


class _CoordinatorStatus(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="ignore")

    slots: dict[str, dict[str, JsonValue]] = {}


def _log_trail(
    status: str,
    *,
    error: str | None = None,
    run_dir: str | None = None,
    backend: str | None = None,
    steps: int = 0,
) -> None:
    try:
        from reins.services.task_trail import TaskTrail

        _ = TaskTrail().upsert_task(
            str(uuid.uuid4()),
            task_type="training_run",
            status=status,
            target_node="amdy",
            error=error,
            run_dir=run_dir,
            backend=backend,
            steps=steps,
        )
    except (OSError, RuntimeError, TypeError, ValueError):
        log_degradation(__name__)


def _unload_all_models() -> None:
    try:
        from reins.harness.coordinator import get_coordinator

        coordinator = get_coordinator()
        status = _CoordinatorStatus.model_validate(coordinator.status())
        for name in status.slots:
            _ = coordinator.unload(name)
    except (OSError, RuntimeError, TypeError, ValidationError, ValueError):
        log_degradation(__name__)


def _train_once(
    config: TrainingConfig,
    backend: TrainBackend,
    dataset_path: str,
    run_dir: Path,
    batch_size: int,
    sequence_length: int,
) -> int:
    from reins.training.transformers_backend import train_once

    return train_once(config, backend, dataset_path, run_dir, batch_size, sequence_length)


def _is_oom(error: Exception) -> bool:
    name = type(error).__name__.lower()
    message = str(error).lower()
    return "outofmemory" in name or "out of memory" in message


def run_finetune(
    config: Mapping[str, JsonValue] | None = None,
    *,
    run_name: str | None = None,
) -> TrainResult:
    """Validate derived records, then run one local adapter-weight update."""
    try:
        settings = load_training_config(config)
    except ValidationError as error:
        message = f"invalid training configuration: {error}"
        _log_trail("failed", error=message)
        return TrainResult(ok=False, error=message)

    dataset_path = Path(settings.dataset_path).expanduser()
    if not settings.dataset_path or not dataset_path.exists():
        message = f"dataset_path missing or nonexistent: {settings.dataset_path!r}"
        _log_trail("failed", error=message)
        return TrainResult(ok=False, error=message)
    try:
        _ = validate_jsonl(dataset_path)
    except (OSError, ValueError) as error:
        message = f"invalid training record dataset: {error}"
        _log_trail("failed", error=message)
        return TrainResult(ok=False, error=message)

    backend = probe()
    name = run_name or f"run-{int(time.time())}"
    run_dir = Path(settings.output_dir or paths.training_runs_dir()) / name
    _unload_all_models()
    batch_size = settings.per_device_batch_size
    sequence_length = settings.max_seq_len

    for attempt in range(2):
        try:
            steps = _train_once(
                settings,
                backend,
                str(dataset_path),
                run_dir,
                batch_size,
                sequence_length,
            )
            _log_trail(
                "success",
                run_dir=str(run_dir),
                backend=backend.mode,
                steps=steps,
            )
            return TrainResult(True, str(run_dir), backend.mode, steps=steps)
        except Exception as error:
            log_degradation(__name__)
            if _is_oom(error) and attempt == 0:
                batch_size = max(1, batch_size // 2)
                sequence_length = max(256, sequence_length // 2)
                continue
            _log_trail("failed", error=str(error), backend=backend.mode)
            return TrainResult(False, backend=backend.mode, error=str(error))
    return TrainResult(False, backend=backend.mode, error="training failed after OOM retry")

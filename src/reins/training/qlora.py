"""
QLoRA fine-tuning loop. Torch/transformers/peft/datasets/bitsandbytes are all
imported inside functions - the harness core never hard-imports them.

Never crashes the harness: config errors, OOM, and missing deps all degrade
to a logged `TrainResult(ok=False)`.
"""

from __future__ import annotations

import json
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from reins.harness import paths
from reins.training.capability import TrainBackend, probe


@dataclass
class TrainResult:
    ok: bool
    run_dir: Optional[str] = None
    backend: Optional[str] = None
    error: Optional[str] = None
    steps: int = 0


def _config() -> dict:
    try:
        return json.loads(paths.training_config().read_text())
    except Exception:
        return {}


def _log_trail(status: str, **fields) -> None:
    try:
        from reins.services.task_trail import TaskTrail

        TaskTrail().upsert_task(str(uuid.uuid4()), task_type="training_run",
                                 status=status, target_node="amdy", **fields)
    except Exception:
        pass  # honest-failure logging is best-effort; never crash on it


def _unload_all_models() -> None:
    """Free the VRAM budget before training starts - best-effort handshake
    with the coordinator; a failure here just means training competes with
    whatever's resident instead of aborting the run."""
    try:
        from reins.harness.coordinator import get_coordinator

        coord = get_coordinator()
        status = coord.status()
        for name in list(status.get("slots", {})):
            coord.unload(name)
    except Exception:
        pass


def run_finetune(config: Optional[dict] = None, *, run_name: Optional[str] = None) -> TrainResult:
    """Run one QLoRA/LoRA fine-tune. `config` overrides `config/training.json`."""
    cfg = {**_config(), **(config or {})}
    dataset_path = cfg.get("dataset_path")
    if not dataset_path or not Path(dataset_path).expanduser().exists():
        err = f"dataset_path missing or nonexistent: {dataset_path!r}"
        _log_trail("failed", error=err)
        return TrainResult(ok=False, error=err)

    backend = probe()
    run_name = run_name or f"run-{int(time.time())}"
    run_dir = Path(cfg.get("output_dir") or paths.training_runs_dir()) / run_name

    _unload_all_models()

    batch_size = cfg.get("per_device_batch_size", 1)
    seq_len = cfg.get("max_seq_len", 2048)

    for attempt in range(2):
        try:
            steps = _train_once(cfg, backend, dataset_path, run_dir, batch_size, seq_len)
            _log_trail("success", run_dir=str(run_dir), backend=backend.mode, steps=steps)
            return TrainResult(ok=True, run_dir=str(run_dir), backend=backend.mode, steps=steps)
        except Exception as e:
            if _is_oom(e) and attempt == 0:
                batch_size = max(1, batch_size // 2) if batch_size > 1 else batch_size
                seq_len = max(256, seq_len // 2)
                continue
            _log_trail("failed", error=str(e), backend=backend.mode)
            return TrainResult(ok=False, error=str(e), backend=backend.mode)

    return TrainResult(ok=False, error="training failed after OOM retry", backend=backend.mode)


def _is_oom(e: Exception) -> bool:
    try:
        import torch

        if isinstance(e, torch.cuda.OutOfMemoryError):
            return True
    except Exception:
        pass
    return "out of memory" in str(e).lower()


def _train_once(cfg: dict, backend: TrainBackend, dataset_path: str, run_dir: Path,
                 batch_size: int, seq_len: int) -> int:
    """The actual training loop. Imports torch/transformers/peft/datasets
    lazily - raises ImportError if the `train` extra isn't installed, which
    `run_finetune` logs and degrades from."""
    import torch
    from datasets import load_dataset
    from peft import LoraConfig, get_peft_model
    from transformers import (
        AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments,
        BitsAndBytesConfig,
    )

    base_model = cfg.get(backend.base_model_key, cfg.get("base_model"))
    lora_cfg = cfg.get("lora", {})

    model_kwargs = {}
    if backend.mode == "qlora_nf4":
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16,
        )
        model_kwargs["device_map"] = "auto"
    elif backend.mode == "lora_fp16":
        model_kwargs["torch_dtype"] = torch.bfloat16
        model_kwargs["device_map"] = "auto"

    tokenizer = AutoTokenizer.from_pretrained(base_model)
    model = AutoModelForCausalLM.from_pretrained(base_model, **model_kwargs)

    peft_config = LoraConfig(
        r=lora_cfg.get("r", 16), lora_alpha=lora_cfg.get("alpha", 32),
        lora_dropout=lora_cfg.get("dropout", 0.05),
        target_modules=lora_cfg.get("target_modules", ["q_proj", "v_proj"]),
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, peft_config)
    if cfg.get("gradient_checkpointing", True):
        model.gradient_checkpointing_enable()

    dataset = load_dataset("json", data_files=dataset_path)["train"]

    def _tokenize(batch):
        return tokenizer(batch["text"], truncation=True, max_length=seq_len)

    tokenized = dataset.map(_tokenize, batched=True, remove_columns=dataset.column_names)

    run_dir.mkdir(parents=True, exist_ok=True)
    args = TrainingArguments(
        output_dir=str(run_dir),
        per_device_train_batch_size=batch_size,
        gradient_accumulation_steps=cfg.get("gradient_accumulation_steps", 16),
        num_train_epochs=cfg.get("num_train_epochs", 3),
        learning_rate=cfg.get("learning_rate", 2e-4),
        optim=cfg.get("optim", "paged_adamw_8bit") if backend.mode != "lora_cpu" else "adamw_torch",
        gradient_checkpointing=cfg.get("gradient_checkpointing", True),
        save_strategy="epoch",
        logging_steps=10,
        report_to=[],
    )
    trainer = Trainer(model=model, args=args, train_dataset=tokenized)
    result = trainer.train()
    model.save_pretrained(str(run_dir))
    tokenizer.save_pretrained(str(run_dir))
    return int(result.global_step) if hasattr(result, "global_step") else 0

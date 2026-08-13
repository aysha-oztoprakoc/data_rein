"""Optional Transformers/PEFT implementation behind the training contract."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Literal, TypeGuard

from reins.training.capability import TrainBackend
from reins.training.config import TrainingConfig

if TYPE_CHECKING:
    from transformers import PreTrainedModel

TrainMode = Literal["qlora_nf4", "lora_fp16", "lora_cpu"]


class UnsupportedTrainModeError(Exception):
    pass


def _is_train_mode(value: str) -> TypeGuard[TrainMode]:
    return value in {"qlora_nf4", "lora_fp16", "lora_cpu"}


def train_once(
    config: TrainingConfig,
    backend: TrainBackend,
    dataset_path: str,
    run_dir: Path,
    batch_size: int,
    sequence_length: int,
) -> int:
    """Manipulate local adapter weights once; optional imports fail honestly."""
    import torch
    from datasets import load_dataset
    from peft import LoraConfig, get_peft_model
    from transformers import (
        AutoModelForCausalLM,
        AutoTokenizer,
        BitsAndBytesConfig,
        Trainer,
        TrainingArguments,
    )

    base_model, revision = config.source_for(backend.base_model_key)
    if not _is_train_mode(backend.mode):
        raise UnsupportedTrainModeError(backend.mode)
    model_loaders: dict[TrainMode, Callable[[], PreTrainedModel]] = {
        "qlora_nf4": lambda: AutoModelForCausalLM.from_pretrained(
                base_model,
                quantization_config=BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_use_double_quant=True,
                    bnb_4bit_compute_dtype=torch.bfloat16,
                ),
                device_map="auto",
                revision=revision,
            ),
        "lora_fp16": lambda: AutoModelForCausalLM.from_pretrained(
                base_model,
                torch_dtype=torch.bfloat16,
                device_map="auto",
                revision=revision,
            ),
        "lora_cpu": lambda: AutoModelForCausalLM.from_pretrained(
            base_model,
            revision=revision,
        ),
    }
    model = model_loaders[backend.mode]()

    tokenizer = AutoTokenizer.from_pretrained(base_model, revision=revision)
    adapter = LoraConfig(
        r=config.lora.r,
        lora_alpha=config.lora.alpha,
        lora_dropout=config.lora.dropout,
        target_modules=list(config.lora.target_modules),
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, adapter)
    if config.gradient_checkpointing:
        model.gradient_checkpointing_enable()

    # The built-in JSON loader reads only the explicit local dataset path.
    dataset = load_dataset("json", data_files=dataset_path)["train"]  # nosec B615

    def tokenize(batch: dict[str, list[str]]) -> dict[str, list[list[int]]]:
        return tokenizer(batch["text"], truncation=True, max_length=sequence_length)

    tokenized = dataset.map(tokenize, batched=True, remove_columns=dataset.column_names)
    run_dir.mkdir(parents=True, exist_ok=True)
    arguments = TrainingArguments(
        output_dir=str(run_dir),
        per_device_train_batch_size=batch_size,
        gradient_accumulation_steps=config.gradient_accumulation_steps,
        num_train_epochs=config.num_train_epochs,
        learning_rate=config.learning_rate,
        optim=config.optim if backend.mode != "lora_cpu" else "adamw_torch",
        gradient_checkpointing=config.gradient_checkpointing,
        save_strategy="epoch",
        logging_steps=10,
        report_to=[],
    )
    result = Trainer(model=model, args=arguments, train_dataset=tokenized).train()
    model.save_pretrained(str(run_dir))
    tokenizer.save_pretrained(str(run_dir))
    return int(result.global_step)

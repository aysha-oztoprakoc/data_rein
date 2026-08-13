"""
Tests for `reins.training` (capability, qlora, export): QLoRA fine-tuning
degradation chain and config validation. Heavy deps (torch/peft/datasets/
bitsandbytes) are never imported at collection time - these tests mock them
so the suite runs without the optional `train` extra installed.
"""

import sys
import types

import pytest

from reins.training import capability, qlora
from reins.training.capability import TrainBackend
from reins.training.config import TrainingConfig
from reins.training.transformers_backend import train_once


def _fake_torch(cuda_available: bool, hip: object = None) -> types.ModuleType:
    mod = types.ModuleType("torch")
    mod.cuda = types.SimpleNamespace(is_available=lambda: cuda_available)
    mod.version = types.SimpleNamespace(hip=hip)
    return mod


def test_probe_degrades_to_cpu_when_torch_missing(monkeypatch):
    monkeypatch.setitem(sys.modules, "torch", None)
    monkeypatch.delitem(sys.modules, "torch", raising=False)

    import builtins
    real_import = builtins.__import__

    def _blocked(name, *a, **k):
        if name == "torch":
            raise ImportError("no torch")
        return real_import(name, *a, **k)

    monkeypatch.setattr(builtins, "__import__", _blocked)
    backend = capability.probe()
    assert backend.mode == "lora_cpu"
    assert backend.device == "cpu"


def test_probe_picks_qlora_nf4_when_bitsandbytes_usable(monkeypatch):
    monkeypatch.setitem(sys.modules, "torch", _fake_torch(True))
    fake_bnb = types.ModuleType("bitsandbytes")
    fake_bnb.nn = types.SimpleNamespace(Linear4bit=object())
    monkeypatch.setitem(sys.modules, "bitsandbytes", fake_bnb)

    backend = capability.probe()
    assert backend.mode == "qlora_nf4"
    assert backend.base_model_key == "base_model"


def test_probe_falls_back_to_lora_fp16_without_bitsandbytes(monkeypatch):
    monkeypatch.setitem(sys.modules, "torch", _fake_torch(True))
    monkeypatch.delitem(sys.modules, "bitsandbytes", raising=False)

    import builtins
    real_import = builtins.__import__

    def _blocked(name, *a, **k):
        if name == "bitsandbytes":
            raise ImportError("no bitsandbytes")
        return real_import(name, *a, **k)

    monkeypatch.setattr(builtins, "__import__", _blocked)
    backend = capability.probe()
    assert backend.mode == "lora_fp16"
    assert backend.base_model_key == "small_base_model"


def test_run_finetune_rejects_missing_dataset(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_REIN_CONFIG_DIR", str(tmp_path / "config"))
    result = qlora.run_finetune({"dataset_path": str(tmp_path / "nope.jsonl")})
    assert result.ok is False
    assert "dataset_path" in result.error


def test_run_finetune_retries_once_on_oom_then_fails(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_REIN_CONFIG_DIR", str(tmp_path / "config"))
    dataset = tmp_path / "train.jsonl"
    dataset.write_text('{"text": "hello"}\n')

    calls = []

    def _fake_train_once(cfg, backend, dataset_path, run_dir, batch_size, seq_len):
        calls.append((batch_size, seq_len))
        raise RuntimeError("CUDA out of memory")

    monkeypatch.setattr(qlora, "_train_once", _fake_train_once)
    monkeypatch.setattr(qlora, "_unload_all_models", lambda: None)

    result = qlora.run_finetune({
        "dataset_path": str(dataset), "output_dir": str(tmp_path / "runs"),
        "per_device_batch_size": 4, "max_seq_len": 2048,
    })

    assert result.ok is False
    assert len(calls) == 2  # one attempt, one retry after halving
    assert calls[1][0] <= calls[0][0]
    assert calls[1][1] <= calls[0][1]


def test_run_finetune_succeeds_with_fake_trainer(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_REIN_CONFIG_DIR", str(tmp_path / "config"))
    dataset = tmp_path / "train.jsonl"
    dataset.write_text('{"text": "hello"}\n')

    monkeypatch.setattr(qlora, "_train_once", lambda *a, **k: 42)
    monkeypatch.setattr(qlora, "_unload_all_models", lambda: None)

    result = qlora.run_finetune({
        "dataset_path": str(dataset), "output_dir": str(tmp_path / "runs"),
    })
    assert result.ok is True
    assert result.steps == 42


def test_run_finetune_rejects_malformed_training_records_before_loading_models(
    tmp_path,
    monkeypatch,
) -> None:
    # Given a derived dataset with a malformed record and a guarded training backend.
    dataset = tmp_path / "invalid.jsonl"
    dataset.write_text('{"meta": {"modality": "audio"}}\n', encoding="utf-8")
    monkeypatch.setattr(
        qlora,
        "_train_once",
        lambda *_args, **_kwargs: pytest.fail("invalid data must not reach model loading"),
    )

    # When local fine-tuning validates the dataset.
    result = qlora.run_finetune({"dataset_path": str(dataset)})

    # Then the run fails honestly before any weight manipulation begins.
    assert result.ok is False
    assert "training record" in (result.error or "")


def test_training_remote_models_require_immutable_revisions() -> None:
    config = TrainingConfig()

    for key in ("base_model", "small_base_model", "tiny_base_model"):
        _model, revision = config.source_for(key)
        assert len(revision) == 40
        assert all(character in "0123456789abcdef" for character in revision)


def test_training_rejects_mutable_revision() -> None:
    with pytest.raises(ValueError):
        TrainingConfig(base_model_revision="main")


def test_training_passes_pinned_revision_to_model_and_tokenizer(tmp_path, monkeypatch) -> None:
    calls: list[tuple[str, dict[str, str]]] = []

    class FakeModel:
        def gradient_checkpointing_enable(self) -> None:
            return None

        def save_pretrained(self, _path: str) -> None:
            return None

    class FakeLoader:
        @classmethod
        def from_pretrained(cls, model: str, **kwargs):
            calls.append((model, kwargs))
            return FakeModel()

    class FakeTokenizerLoader:
        @classmethod
        def from_pretrained(cls, model: str, **kwargs):
            calls.append((model, kwargs))
            return types.SimpleNamespace(
                __call__=lambda *_args, **_kwargs: {"input_ids": [[1]]},
                save_pretrained=lambda _path: None,
            )

    class FakeDataset:
        column_names = ["text"]

        def map(self, _function, **_kwargs):
            return self

    transformers = types.ModuleType("transformers")
    transformers.AutoModelForCausalLM = FakeLoader
    transformers.AutoTokenizer = FakeTokenizerLoader
    transformers.BitsAndBytesConfig = lambda **kwargs: kwargs
    transformers.TrainingArguments = lambda **kwargs: kwargs
    transformers.Trainer = lambda **kwargs: types.SimpleNamespace(
        train=lambda: types.SimpleNamespace(global_step=1)
    )
    datasets = types.ModuleType("datasets")
    datasets.load_dataset = lambda *_args, **_kwargs: {"train": FakeDataset()}
    peft = types.ModuleType("peft")
    peft.LoraConfig = lambda **kwargs: kwargs
    peft.get_peft_model = lambda model, _adapter: model
    torch = types.ModuleType("torch")
    torch.bfloat16 = "bfloat16"
    monkeypatch.setitem(sys.modules, "transformers", transformers)
    monkeypatch.setitem(sys.modules, "datasets", datasets)
    monkeypatch.setitem(sys.modules, "peft", peft)
    monkeypatch.setitem(sys.modules, "torch", torch)

    config = TrainingConfig(gradient_checkpointing=False)
    backend = TrainBackend("lora_cpu", "cpu", "tiny_base_model", "test")
    assert train_once(config, backend, "dataset.jsonl", tmp_path / "run", 1, 256) == 1
    assert calls == [
        (config.tiny_base_model, {"revision": config.tiny_base_model_revision}),
        (config.tiny_base_model, {"revision": config.tiny_base_model_revision}),
    ]

"""
Tests for `reins.training` (capability, qlora, export): QLoRA fine-tuning
degradation chain and config validation. Heavy deps (torch/peft/datasets/
bitsandbytes) are never imported at collection time - these tests mock them
so the suite runs without the optional `train` extra installed.
"""

import sys
import types

from reins.training import capability, qlora


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

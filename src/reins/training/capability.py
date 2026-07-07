"""
Runtime capability probing for QLoRA fine-tuning on the amdy hardware plane.

Heavy deps (torch/bitsandbytes) are the optional `train` extras group and are
never imported at module load - only inside `probe()`, so importing this
module is always safe even without the extra installed.

Degradation chain (best available wins, never raises):
  1. CUDA/ROCm + working bitsandbytes  -> literal QLoRA NF4
  2. torch-ROCm/CUDA without bitsandbytes -> LoRA fp16/bf16 on a small base
  3. no usable GPU                     -> CPU LoRA on a tiny base
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrainBackend:
    mode: str  # "qlora_nf4" | "lora_fp16" | "lora_cpu"
    device: str  # "cuda" | "rocm" | "cpu"
    base_model_key: str  # "base_model" | "small_base_model" | "tiny_base_model"
    reason: str


def probe() -> TrainBackend:
    """Never raises: any import/detection failure degrades to CPU LoRA."""
    try:
        import torch  # noqa: F401
    except Exception as e:
        return TrainBackend("lora_cpu", "cpu", "tiny_base_model",
                             f"torch not installed ({e}); falling back to CPU LoRA")

    try:
        if torch.cuda.is_available():
            device = "rocm" if _is_rocm(torch) else "cuda"
            if _bitsandbytes_usable():
                return TrainBackend("qlora_nf4", device, "base_model",
                                     f"{device} + bitsandbytes available - literal NF4 QLoRA")
            return TrainBackend("lora_fp16", device, "small_base_model",
                                 f"{device} available but bitsandbytes unusable - LoRA fp16/bf16 on small base")
    except Exception as e:
        return TrainBackend("lora_cpu", "cpu", "tiny_base_model",
                             f"GPU detection failed ({e}); falling back to CPU LoRA")

    return TrainBackend("lora_cpu", "cpu", "tiny_base_model",
                         "no usable GPU - CPU LoRA on tiny base")


def _is_rocm(torch_mod) -> bool:
    try:
        return getattr(torch_mod.version, "hip", None) is not None
    except Exception:
        return False


def _bitsandbytes_usable() -> bool:
    try:
        import bitsandbytes as bnb

        return hasattr(bnb, "nn") and hasattr(bnb.nn, "Linear4bit")
    except Exception:
        return False

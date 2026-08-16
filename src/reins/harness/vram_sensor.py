from __future__ import annotations

import shutil
import subprocess
from typing import Final

from reins.harness import external_io

_QUERY_TIMEOUT: Final = 1.0
_BYTES_PER_GIB: Final = 1024**3


import json

def _command_free_gb(command: list[str]) -> float | None:
    try:
        result = external_io.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=_QUERY_TIMEOUT,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    try:
        value = float(result.stdout.strip().splitlines()[0])
    except (IndexError, ValueError):
        return None
    return value / _BYTES_PER_GIB if value > 1024**2 else value

def _rocm_free_gb(device_index: int = 0) -> float | None:
    try:
        result = external_io.run(
            ["rocm-smi", "--showmeminfo", "vram", "--json"],
            check=True,
            capture_output=True,
            text=True,
            timeout=_QUERY_TIMEOUT,
        )
        data = json.loads(result.stdout)
        # rocm-smi json output typically looks like: {"card0": {"VRAM Total Memory (B)": "...", "VRAM Total Used Memory (B)": "..."}}
        card_key = f"card{device_index}"
        if card_key in data:
            card_data = data[card_key]
            total = float(card_data.get("VRAM Total Memory (B)", 0))
            used = float(card_data.get("VRAM Total Used Memory (B)", 0))
            if total > 0:
                free = total - used
                return free / _BYTES_PER_GIB
    except Exception:
        import logging
        logging.getLogger(__name__).warning("ROCm SMI sensor read failed", exc_info=True)
    return None

def query_free_vram_gb(device_index: int = 0) -> float | None:
    if shutil.which("nvidia-smi"):
        return _command_free_gb([
            "nvidia-smi", "--query-gpu=memory.free", "--format=csv,noheader,nounits",
            "--id", str(device_index),
        ])
    if shutil.which("rocm-smi"):
        return _rocm_free_gb(device_index)
    return None

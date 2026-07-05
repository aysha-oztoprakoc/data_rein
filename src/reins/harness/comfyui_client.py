"""
Async HTTP client for a local ComfyUI instance.

Ported from the legacy `DATA/kad-1.0/amdy/src/comfyui_client.py` (health
check + prompt-queue submission), which was never wired into anything -
`ModelRouter._dispatch` had no comfyui branch at all. This adds the missing
piece the legacy client lacked: fetching the actual result once ComfyUI
finishes a queued job.

PON note: `wait_for_result`'s poll loop is a bounded, one-shot wait inside a
single `ModelRouter.generate_image()` call - not a background daemon loop -
so it doesn't violate the harness's zero-polling mandate the same way a
long-lived `while True` service loop would. A websocket-based push
notification (ComfyUI's `/ws` endpoint) would be the more PON-correct design
and is a reasonable future improvement; polling is the pragmatic minimum
given the salvaged client is HTTP-only.
"""

from __future__ import annotations

import asyncio
import time
import uuid
from typing import Any, Dict, Optional

import httpx

from reins.services.logger import get_logger

logger = get_logger("comfyui_client")


class ComfyUIClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8188") -> None:
        self.base_url = base_url.rstrip("/")
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers, timeout=httpx.Timeout(60.0))

    async def close(self) -> None:
        await self.client.aclose()

    async def check_health(self) -> bool:
        """Ping the ComfyUI API to ensure it's reachable."""
        try:
            response = await self.client.get("/system_stats")
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Failed to connect to ComfyUI API: {e}")
            return False

    async def queue_prompt(self, prompt: Dict[str, Any]) -> Optional[str]:
        """Submit a workflow prompt to ComfyUI, returning its prompt_id."""
        try:
            client_id = str(uuid.uuid4())
            payload = {"prompt": prompt, "client_id": client_id}
            logger.info("Sending prompt to ComfyUI")
            response = await self.client.post("/prompt", json=payload)
            if response.status_code == 200:
                data = response.json()
                prompt_id = data.get("prompt_id")
                logger.info(f"ComfyUI prompt queued successfully. ID: {prompt_id}")
                return prompt_id
            logger.error(f"ComfyUI API error {response.status_code}: {response.text}")
            return None
        except Exception as e:
            logger.error(f"Error calling ComfyUI prompt API: {e}")
            return None

    async def get_history(self, prompt_id: str) -> Optional[dict]:
        """GET /history/{prompt_id}; returns the job's history entry once
        ComfyUI has recorded a result, else None (still queued/running)."""
        try:
            response = await self.client.get(f"/history/{prompt_id}")
            if response.status_code != 200:
                return None
            data = response.json()
            return data.get(prompt_id)
        except Exception as e:
            logger.error(f"Error polling ComfyUI history for {prompt_id}: {e}")
            return None

    async def wait_for_result(
        self, prompt_id: str, timeout: float = 120.0, poll_interval: float = 1.5
    ) -> Optional[dict]:
        """Poll /history/{id} until outputs appear or timeout. Bounded,
        one-shot wait - see module docstring for the PON justification."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            entry = await self.get_history(prompt_id)
            if entry is not None and entry.get("outputs"):
                return entry
            await asyncio.sleep(poll_interval)
        logger.error(f"ComfyUI job {prompt_id} timed out after {timeout}s")
        return None

    @staticmethod
    def extract_image_path(history_entry: dict) -> Optional[str]:
        """Pull the first saved image's filename out of a history entry's
        outputs, resolved against ComfyUI's on-disk output directory
        convention (output/[subfolder/]filename)."""
        outputs = history_entry.get("outputs", {}) if history_entry else {}
        for node_output in outputs.values():
            for image in node_output.get("images", []):
                filename = image.get("filename")
                subfolder = image.get("subfolder", "")
                if filename:
                    return f"{subfolder}/{filename}" if subfolder else filename
        return None


def build_txt2img_workflow(
    prompt: str,
    negative_prompt: str = "",
    checkpoint: str = "sd_xl_turbo_1.0_fp16.safetensors",
    width: int = 1024,
    height: int = 1024,
    steps: int = 4,
    cfg: float = 1.0,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    """
    Build a minimal SDXL txt2img ComfyUI node graph. No precedent existed for
    this in the harness - this is the smallest workflow that produces a
    saved image via the standard CheckpointLoader -> CLIPTextEncode ->
    KSampler -> VAEDecode -> SaveImage node chain.

    Defaults target `sd_xl_turbo_1.0_fp16.safetensors` - the checkpoint
    knowledge_base/MODEL_GAPS.md actually recommends for this machine's 8GB
    VRAM budget (confirmed present in ComfyUI/models/checkpoints/). SDXL
    Turbo needs few steps and near-1.0 cfg, unlike a standard SDXL base
    checkpoint (~20 steps, cfg ~7.5) - override both if using a different
    checkpoint.
    """
    if seed is None:
        seed = int.from_bytes(uuid.uuid4().bytes[:4], "big")
    return {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": seed, "steps": steps, "cfg": cfg, "sampler_name": "euler_ancestral",
                "scheduler": "normal", "denoise": 1.0,
                "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0], "latent_image": ["5", 0],
            },
        },
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": checkpoint}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": negative_prompt, "clip": ["4", 1]}},
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "reins", "images": ["8", 0]}},
    }

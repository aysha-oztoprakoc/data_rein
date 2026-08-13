"""
Async HTTP and WebSocket client for a local ComfyUI instance.

Ported from the legacy `DATA/kad-1.0/amdy/src/comfyui_client.py` (health
check + prompt-queue submission), which was never wired into anything -
`ModelRouter._dispatch` had no comfyui branch at all. This adds the missing
piece the legacy client lacked: fetching the actual result after ComfyUI
publishes completion on its `/ws` endpoint. No history polling is used.
"""

from __future__ import annotations

import asyncio
import json
import uuid
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import cast, final
from urllib.parse import urlsplit, urlunsplit

import httpx

from reins.harness import external_io
from reins.harness.provider_protocols import HistoryEntry, JsonValue, parse_json
from reins.services.logger import get_logger

logger = get_logger("comfyui_client")


@final
class ComfyUIClient:
    def __init__(self, base_url: str = "http://127.0.0.1:8188") -> None:
        self.base_url: str = base_url.rstrip("/")
        self.headers: dict[str, str] = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.client: httpx.AsyncClient = httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=httpx.Timeout(60.0),
        )

    async def close(self) -> None:
        await self.client.aclose()

    async def check_health(self) -> bool:
        """Ping the ComfyUI API to ensure it's reachable."""
        try:
            response = await external_io.async_call(
                "http:comfyui:system_stats",
                lambda: self.client.get("/system_stats"),
                is_success=lambda result: result.status_code == 200,
            )
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Failed to connect to ComfyUI API: {e}")
            return False

    async def queue_prompt(
        self,
        prompt: dict[str, JsonValue],
        client_id: str | None = None,
    ) -> str | None:
        """Submit a workflow prompt to ComfyUI, returning its prompt_id."""
        try:
            payload = {"prompt": prompt, "client_id": client_id or str(uuid.uuid4())}
            logger.info("Sending prompt to ComfyUI")
            response = await external_io.async_call(
                "http:comfyui:prompt",
                lambda: self.client.post("/prompt", json=payload),
                is_success=lambda result: result.status_code == 200,
            )
            if response.status_code == 200:
                data = parse_json(cast(object, response.json()))
                if not isinstance(data, dict):
                    raise TypeError("ComfyUI prompt response is not an object")
                prompt_id = data.get("prompt_id")
                logger.info(f"ComfyUI prompt queued successfully. ID: {prompt_id}")
                return prompt_id if isinstance(prompt_id, str) else None
            logger.error(f"ComfyUI API error {response.status_code}: {response.text}")
            return None
        except Exception as e:
            logger.error(f"Error calling ComfyUI prompt API: {e}")
            return None

    async def get_history(self, prompt_id: str) -> HistoryEntry | None:
        """GET /history/{prompt_id}; returns the job's history entry once
        ComfyUI has recorded a result, else None (still queued/running)."""
        try:
            response = await external_io.async_call(
                "http:comfyui:history",
                lambda: self.client.get(f"/history/{prompt_id}"),
                is_success=lambda result: result.status_code == 200,
            )
            if response.status_code != 200:
                return None
            data = parse_json(cast(object, response.json()))
            if not isinstance(data, dict):
                raise TypeError("ComfyUI history response is not an object")
            history = data.get(prompt_id)
            return history if isinstance(history, dict) else None
        except Exception as e:
            logger.error(f"Error fetching ComfyUI history for {prompt_id}: {e}")
            return None

    @asynccontextmanager
    async def execution_events(
        self,
        client_id: str,
    ) -> AsyncGenerator[AsyncIterator[str], None]:
        from websockets.asyncio.client import connect

        parsed = urlsplit(self.base_url)
        scheme = "wss" if parsed.scheme == "https" else "ws"
        websocket_url = urlunsplit((scheme, parsed.netloc, "/ws", f"clientId={client_id}", ""))
        websocket = await external_io.async_call(
            "websocket:comfyui:events", lambda: connect(websocket_url)
        )
        try:

            async def text_events() -> AsyncIterator[str]:
                async for message in websocket:
                    if isinstance(message, str):
                        yield message

            yield text_events()
        finally:
            await websocket.close()

    async def wait_for_result(
        self,
        prompt_id: str,
        events: AsyncIterator[str],
        timeout: float = 120.0,
    ) -> HistoryEntry | None:
        async def wait_for_completion() -> HistoryEntry | None:
            async for raw_event in events:
                try:
                    event = parse_json(cast(object, json.loads(raw_event)))
                except (json.JSONDecodeError, TypeError) as error:
                    logger.warning(f"Ignored malformed ComfyUI event: {error}")
                    continue
                if not isinstance(event, dict):
                    logger.warning("Ignored non-object ComfyUI event")
                    continue
                raw_data = event.get("data")
                data = raw_data if isinstance(raw_data, dict) else {}
                if data.get("prompt_id") != prompt_id:
                    continue
                event_type = event.get("type")
                if event_type in {"execution_error", "execution_interrupted"}:
                    logger.error(f"ComfyUI job {prompt_id} failed: {data}")
                    return None
                if event_type == "executing" and data.get("node") is None:
                    return await self.get_history(prompt_id)
            logger.error(f"ComfyUI event stream closed before job {prompt_id} completed")
            return None

        try:
            return await asyncio.wait_for(wait_for_completion(), timeout=timeout)
        except TimeoutError:
            logger.error(f"ComfyUI job {prompt_id} timed out after {timeout}s")
            return None

    @staticmethod
    def extract_image_path(history_entry: HistoryEntry) -> str | None:
        """Pull the first saved image's filename out of a history entry's
        outputs, resolved against ComfyUI's on-disk output directory
        convention (output/[subfolder/]filename)."""
        outputs = history_entry.get("outputs", {})
        if not isinstance(outputs, dict):
            return None
        for node_output in outputs.values():
            if not isinstance(node_output, dict):
                continue
            images = node_output.get("images", [])
            if not isinstance(images, list):
                continue
            for image in images:
                if not isinstance(image, dict):
                    continue
                filename = image.get("filename")
                subfolder = image.get("subfolder", "")
                if isinstance(filename, str):
                    prefix = subfolder if isinstance(subfolder, str) else ""
                    return f"{prefix}/{filename}" if prefix else filename
        return None


def build_txt2img_workflow(
    prompt: str,
    negative_prompt: str = "",
    checkpoint: str = "sd_xl_turbo_1.0_fp16.safetensors",
    width: int = 1024,
    height: int = 1024,
    steps: int = 4,
    cfg: float = 1.0,
    seed: int | None = None,
) -> dict[str, JsonValue]:
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
                "seed": seed,
                "steps": steps,
                "cfg": cfg,
                "sampler_name": "euler_ancestral",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0],
            },
        },
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": checkpoint}},
        "5": {
            "class_type": "EmptyLatentImage",
            "inputs": {"width": width, "height": height, "batch_size": 1},
        },
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
        "7": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": negative_prompt, "clip": ["4", 1]},
        },
        "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "9": {
            "class_type": "SaveImage",
            "inputs": {"filename_prefix": "reins", "images": ["8", 0]},
        },
    }

from __future__ import annotations

import logging
import os
import uuid
from collections.abc import Callable
from typing import TypeAlias

import anyio

from reins.harness import external_io

from reins.harness.provider_protocols import (
    HistoryEntry,
    load_claude,
    load_comfyui,
    load_coordinator,
    load_gemini,
    load_local,
    load_openai,
)

logger = logging.getLogger(__name__)

ProviderHandler: TypeAlias = Callable[[str, str, str], str | None]
SecretLookup: TypeAlias = Callable[[str], str | None]


def _decode_stream(value: str | bytes | None) -> str:
    if value is None:
        return ""
    return value.decode("utf-8", "replace") if isinstance(value, bytes) else value


class ProviderRuntime:
    def __init__(self, secret_lookup: SecretLookup) -> None:
        self._secret_lookup: SecretLookup = secret_lookup
        self.last_usage: dict[str, int] | None = None

    def comfyui(self, _model: str, prompt: str, _node: str) -> str | None:
        base_url = os.environ.get("COMFYUI_BASE_URL", "http://127.0.0.1:8188")

        async def run() -> str:
            module = load_comfyui()
            client = module.ComfyUIClient(base_url=base_url)
            try:
                if not await client.check_health():
                    raise RuntimeError(f"ComfyUI unreachable at {base_url}")
                workflow = module.build_txt2img_workflow(prompt)
                client_id = str(uuid.uuid4())
                async with client.execution_events(client_id) as events:
                    prompt_id = await client.queue_prompt(workflow, client_id=client_id)
                    if not prompt_id:
                        raise RuntimeError("ComfyUI rejected the prompt")
                    entry = await client.wait_for_result(prompt_id, events)
                if entry is None:
                    raise RuntimeError(f"ComfyUI job {prompt_id} ended without history")
                image_path = self._extract_image_path(entry)
                if not image_path:
                    raise RuntimeError(f"ComfyUI job {prompt_id} produced no image")
                return image_path
            finally:
                await client.close()

        return anyio.run(run)

    @staticmethod
    def _extract_image_path(entry: HistoryEntry) -> str | None:
        outputs = entry.get("outputs")
        if not isinstance(outputs, dict):
            return None
        for node_output in outputs.values():
            if not isinstance(node_output, dict):
                continue
            images = node_output.get("images")
            if not isinstance(images, list):
                continue
            for image in images:
                if not isinstance(image, dict):
                    continue
                filename = image.get("filename")
                subfolder = image.get("subfolder", "")
                if isinstance(filename, str):
                    return (
                        f"{subfolder}/{filename}"
                        if isinstance(subfolder, str) and subfolder
                        else filename
                    )
        return None

    def ollama(self, model: str, prompt: str, node: str) -> str | None:
        if node != "tell":
            try:
                result = load_coordinator().get_coordinator().generate(model, prompt)
                if result is not None and result.ok:
                    return result.text
            except (ImportError, RuntimeError, TypeError):
                logger.warning("coordinator generation failed; using direct Ollama", exc_info=True)
            local = load_local()
            _ = local.ensure_server()
            return local.generate(model, prompt)

        import json
        import urllib.request
        import urllib.error

        # Network-first API routing (avoids blocking interactive SSH overhead)
        url = "http://tell:11434/api/generate"
        payload = {"model": model, "prompt": prompt, "stream": False}
        headers = {"Content-Type": "application/json"}
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
        
        try:
            with external_io.urlopen(req, timeout=300) as response:
                result_json = json.loads(response.read().decode("utf-8"))
                return result_json.get("response", "")
        except (urllib.error.URLError, ConnectionError) as e:
            logger.warning(f"HTTP to tell:11434 failed ({e}). Falling back to SSH overlay.")
            
            command = ["ssh", "-o", "BatchMode=yes", "tell", "ollama", "run", model]
            result = external_io.run(command, input=prompt.encode(), capture_output=True, check=False)
            output = _decode_stream(result.stdout)
            if result.returncode == 0 and output.strip():
                return output
            error = _decode_stream(result.stderr) or "ollama failed"
            raise RuntimeError(error.strip()[:200])

    def gemini(self, model: str, prompt: str, _node: str) -> str | None:
        key = self._secret_lookup("GEMINI_API_KEY") or self._secret_lookup("GOOGLE_STUDIO_API_KEY")
        if not key:
            raise RuntimeError("no GEMINI_API_KEY")
        try:
            genai = load_gemini()
        except (ImportError, TypeError) as error:
            raise RuntimeError("google-generativeai not installed") from error
        genai.configure(api_key=key)
        response = genai.GenerativeModel(model).generate_content(prompt)
        metadata = response.usage_metadata
        if metadata is not None:
            self.last_usage = {
                "input_tokens": metadata.prompt_token_count,
                "output_tokens": metadata.candidates_token_count,
            }
        return response.text

    def claude(self, model: str, prompt: str, _node: str) -> str | None:
        key = self._secret_lookup("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("no ANTHROPIC_API_KEY")
        try:
            anthropic = load_claude()
        except (ImportError, TypeError) as error:
            raise RuntimeError("anthropic sdk not installed") from error
        message = anthropic.Anthropic(api_key=key).messages.create(
            model=model,
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        usage = message.usage
        if usage is not None:
            self.last_usage = {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
            }
        parts = [block.text for block in message.content if block.type == "text"]
        return "\n".join(parts) if parts else None

    def openai(self, model: str, prompt: str, _node: str) -> str | None:
        key = self._secret_lookup("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("no OPENAI_API_KEY")
        try:
            openai = load_openai()
        except (ImportError, TypeError) as error:
            raise RuntimeError("openai sdk not installed") from error
        response = openai.OpenAI(api_key=key).chat.completions.create(
            model=model.replace(":cloud", ""),
            messages=[{"role": "user", "content": prompt}],
        )
        if response.usage is not None:
            self.last_usage = {
                "input_tokens": response.usage.prompt_tokens,
                "output_tokens": response.usage.completion_tokens,
            }
        return response.choices[0].message.content

    def openai_compat(
        self, model: str, prompt: str, _node: str, *, base_url: str, secret_name: str
    ) -> str | None:
        key = self._secret_lookup(secret_name)
        if not key:
            raise RuntimeError(f"no {secret_name}")
        try:
            openai = load_openai()
        except (ImportError, TypeError) as error:
            raise RuntimeError("openai sdk not installed") from error
        response = openai.OpenAI(
            api_key=key,
            base_url=base_url,
            default_headers={"Authorization": f"Bearer {key}"},
        ).chat.completions.create(
            model=model.replace(":cloud", ""),
            messages=[{"role": "user", "content": prompt}],
        )
        if response.usage is not None:
            self.last_usage = {
                "input_tokens": response.usage.prompt_tokens,
                "output_tokens": response.usage.completion_tokens,
            }
        return response.choices[0].message.content

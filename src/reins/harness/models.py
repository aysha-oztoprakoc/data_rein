"""
Model-agnostic provider router for the data_rein universal harness.

The harness must not be welded to any single backend. This module lets the same
task category route to whatever model/provider is configured - a local Ollama
model on amdy or tell, Google Gemini, Anthropic Claude, or any OpenAI-compatible
endpoint - behind one uniform ``route()`` call.

Routing table:
    config/model_router.json  ->  categories -> {amdy|tell} -> [ranked models]

Provider is inferred from the model name (or an explicit ``provider`` key on the
entry):
    * ``gemini*``                      -> Gemini
    * ``claude*`` / ``anthropic*``     -> Claude
    * ``gpt*`` / ``openai*``           -> OpenAI-compatible
    * ``comfyui_*`` (backend=comfyui)  -> ComfyUI (image/audio, not chat)
    * everything else                  -> Ollama (local / ssh to tell)

Secrets are read through the existing encrypted vault (``scripts.get_secrets``),
never from plaintext. Cloud providers degrade gracefully to the next ranked
model / the other node when a key or SDK is unavailable - honoring the harness's
"local-first, graceful degradation" mandate.

PON note: this is a passive dispatcher. It performs one blocking call per request
and returns; it never polls.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))  # for scripts.get_secrets

from reins.harness import paths  # noqa: E402


def _get_secret(name: str) -> Optional[str]:
    """Fetch a secret from the encrypted vault, falling back to env vars."""
    try:
        from scripts.get_secrets import get_secret  # type: ignore

        val = get_secret(name)
        if val:
            return val
    except Exception:
        pass
    return os.environ.get(name)


@dataclass
class ModelSpec:
    model: str
    score: float = 0.0
    power: str = "medium"
    provider: str = ""
    backend: str = ""
    extra: dict = field(default_factory=dict)

    @classmethod
    def from_entry(cls, entry: dict) -> "ModelSpec":
        known = {"model", "score", "power", "provider", "backend"}
        return cls(
            model=entry.get("model", "unknown"),
            score=float(entry.get("score", 0.0)),
            power=entry.get("power", "medium"),
            provider=entry.get("provider", ""),
            backend=entry.get("backend", ""),
            extra={k: v for k, v in entry.items() if k not in known},
        )

    @property
    def resolved_provider(self) -> str:
        if self.provider:
            return self.provider.lower()
        m = self.model.lower()
        if self.backend == "comfyui" or m.startswith("comfyui"):
            return "comfyui"
        if m.startswith("gemini"):
            return "gemini"
        if m.startswith(("claude", "anthropic")):
            return "claude"
        if m.startswith(("gpt", "openai", "o1", "o3")) or ":cloud" in m:
            return "openai"
        return "ollama"


@dataclass
class RouteResult:
    text: Optional[str]
    model: str
    provider: str
    node: str
    ok: bool
    error: Optional[str] = None


class ModelRouter:
    """Reads model_router.json and dispatches to the right provider."""

    FALLBACK_MODEL = "llama3.1:8b"

    def __init__(self, router_path: Optional[Path] = None) -> None:
        self.router_path = router_path or paths.model_router()
        self.table: dict = {}
        self.remote_fallback: list[ModelSpec] = []
        self._last_usage: Optional[dict] = None
        self._load()

    def _load(self) -> None:
        try:
            data = json.loads(self.router_path.read_text(encoding="utf-8"))
            self.table = data.get("categories", data)
            self.remote_fallback = [ModelSpec.from_entry(e) for e in data.get("remote_fallback", [])]
        except Exception:
            self.table = {}
            self.remote_fallback = []

    # -- lookup -------------------------------------------------------------
    def candidates(self, category: str, node: str = "amdy") -> list[ModelSpec]:
        cat = self.table.get(category) or self.table.get(category.lower()) or {}
        entries = cat.get(node, []) if isinstance(cat, dict) else []
        specs = [ModelSpec.from_entry(e) for e in entries]
        if not specs:
            specs = [ModelSpec(model=self.FALLBACK_MODEL)]
        return specs

    def optimal(self, category: str, node: str = "amdy") -> ModelSpec:
        return self.candidates(category, node)[0]

    # -- dispatch -----------------------------------------------------------
    def route(
        self,
        category: str,
        prompt: str,
        node: str = "amdy",
        *,
        allow_fallback: bool = True,
        allow_cloud: bool = True,
    ) -> RouteResult:
        """
        Run ``prompt`` for ``category`` on ``node``, walking down the ranked list
        and finally over to the other node (graceful degradation) on failure.
        """
        tried: list[tuple[str, str, str]] = []
        for spec in self.candidates(category, node):
            provider = spec.resolved_provider
            if provider in ("comfyui",):
                # Generative backends are not chat; skip for text routing.
                continue
            text, err = self._dispatch(provider, spec.model, prompt, node)
            if text is not None:
                return RouteResult(text, spec.model, provider, node, ok=True)
            tried.append((node, spec.model, err or "empty"))

        if allow_fallback:
            other = "tell" if node == "amdy" else "amdy"
            res = self.route(category, prompt, other, allow_fallback=False, allow_cloud=False)
            if res.ok:
                return res
            tried.extend([(other, res.model, res.error or "empty")])

            # Tier 1 - last-resort remote fallback, tried only once both nodes
            # are fully exhausted for this category. Never a proactive path.
            for spec in (self.remote_fallback if allow_cloud else []):
                provider = spec.resolved_provider
                text, err = self._dispatch(provider, spec.model, prompt, node)
                if text is not None:
                    return RouteResult(text, spec.model, provider, "cloud", ok=True)
                tried.append(("cloud", spec.model, err or "empty"))

        return RouteResult(
            None, tried[-1][1] if tried else "none", "none", node, ok=False,
            error="; ".join(f"{n}/{m}: {e}" for n, m, e in tried),
        )

    def route_cloud(self, prompt: str, provider: Optional[str] = None) -> RouteResult:
        """
        Explicit, user-requested cloud call - skips every local candidate and goes
        straight to Tier 1 (``remote_fallback``). Used by callers (e.g. the OpenCode
        MCP bridge) that must only reach Claude/Gemini/OpenAI when a human asked for
        it, never as part of ordinary category routing.
        """
        specs = self.remote_fallback
        if provider:
            specs = [s for s in specs if s.resolved_provider == provider.lower()] or specs
        tried: list[tuple[str, str, str]] = []
        for spec in specs:
            p = spec.resolved_provider
            text, err = self._dispatch(p, spec.model, prompt, "cloud")
            if text is not None:
                return RouteResult(text, spec.model, p, "cloud", ok=True)
            tried.append(("cloud", spec.model, err or "empty"))
        return RouteResult(
            None, tried[-1][1] if tried else "none", provider or "none", "cloud", ok=False,
            error="; ".join(f"{n}/{m}: {e}" for n, m, e in tried) or "no remote_fallback configured",
        )

    def _dispatch(self, provider: str, model: str, prompt: str, node: str):
        try:
            if provider == "ollama":
                return self._ollama(model, prompt, node), None
            if provider in ("gemini", "claude", "openai"):
                self._last_usage = None
                text = getattr(self, f"_{provider}")(model, prompt)
                if text is not None:
                    self._record_usage(provider, model, self._last_usage)
                return text, None
            return None, f"unknown provider {provider}"
        except Exception as e:  # graceful degradation - never crash the harness
            return None, str(e)

    def _record_usage(self, provider: str, model: str, usage: Optional[dict]) -> None:
        """Log a cloud call to the shared TokenLedger. Never raises."""
        if not usage:
            return
        try:
            from reins.services.token_ledger import TokenLedger

            TokenLedger().record(
                provider, model,
                usage.get("input_tokens", 0), usage.get("output_tokens", 0),
            )
        except Exception:
            pass

    # -- providers ----------------------------------------------------------
    def _ollama(self, model: str, prompt: str, node: str) -> Optional[str]:
        # Local node: use the clean HTTP API (no TUI spinner artifacts), starting
        # the harness model server on demand.
        if node != "tell":
            from reins.harness import local

            local.ensure_server()
            return local.generate(model, prompt)

        # Remote node (tell): drive its Ollama over SSH.
        cmd = ["ssh", "-o", "BatchMode=yes", "tell", "ollama", "run", model]
        res = subprocess.run(cmd, input=prompt.encode("utf-8"), capture_output=True)
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.decode("utf-8", "replace")
        raise RuntimeError((res.stderr.decode("utf-8", "replace") or "ollama failed").strip()[:200])

    def _gemini(self, model: str, prompt: str) -> Optional[str]:
        key = _get_secret("GEMINI_API_KEY") or _get_secret("GOOGLE_STUDIO_API_KEY")
        if not key:
            raise RuntimeError("no GEMINI_API_KEY")
        try:
            import google.generativeai as genai  # type: ignore
        except ImportError:
            raise RuntimeError("google-generativeai not installed")
        genai.configure(api_key=key)
        resp = genai.GenerativeModel(model).generate_content(prompt)
        meta = getattr(resp, "usage_metadata", None)
        if meta is not None:
            self._last_usage = {
                "input_tokens": getattr(meta, "prompt_token_count", 0),
                "output_tokens": getattr(meta, "candidates_token_count", 0),
            }
        return getattr(resp, "text", None)

    def _claude(self, model: str, prompt: str) -> Optional[str]:
        key = _get_secret("ANTHROPIC_API_KEY")
        if not key:
            raise RuntimeError("no ANTHROPIC_API_KEY")
        try:
            import anthropic  # type: ignore
        except ImportError:
            raise RuntimeError("anthropic sdk not installed")
        client = anthropic.Anthropic(api_key=key)
        msg = client.messages.create(
            model=model, max_tokens=2048,
            messages=[{"role": "user", "content": prompt}],
        )
        usage = getattr(msg, "usage", None)
        if usage is not None:
            self._last_usage = {
                "input_tokens": getattr(usage, "input_tokens", 0),
                "output_tokens": getattr(usage, "output_tokens", 0),
            }
        parts = [b.text for b in msg.content if getattr(b, "type", "") == "text"]
        return "\n".join(parts) if parts else None

    def _openai(self, model: str, prompt: str) -> Optional[str]:
        key = _get_secret("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("no OPENAI_API_KEY")
        try:
            from openai import OpenAI  # type: ignore
        except ImportError:
            raise RuntimeError("openai sdk not installed")
        client = OpenAI(api_key=key)
        resp = client.chat.completions.create(
            model=model.replace(":cloud", ""),
            messages=[{"role": "user", "content": prompt}],
        )
        usage = getattr(resp, "usage", None)
        if usage is not None:
            self._last_usage = {
                "input_tokens": getattr(usage, "prompt_tokens", 0),
                "output_tokens": getattr(usage, "completion_tokens", 0),
            }
        return resp.choices[0].message.content

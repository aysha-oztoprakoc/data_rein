"""
Self-tracked usage ledger for cloud model calls (Claude/Gemini/OpenAI).

Anthropic/Google do not expose an API to read back your account's remaining
Pro/Max session quota or Gemini free-tier quota, so this is a local counter of
every cloud call the harness itself makes - the only complete picture available
without screen-scraping a billing dashboard. It logs one event per successful
``ModelRouter`` cloud dispatch (see ``ModelRouter._record_usage``), whether that
call came from `reins run`'s last-resort ``remote_fallback`` or from OpenCode's
``escalate_cloud`` MCP tool - one ledger, every cloud call, no blind spots.

Same hardening as ``TaskTrail``: ``fcntl`` advisory lock + atomic temp-file
``os.replace``, safe for concurrent agents.
"""

from __future__ import annotations

import fcntl
import json
import os
import time
from contextlib import contextmanager
from typing import Any, Dict, List, Optional

from reins.harness import paths

# Rolling windows tracked for every provider. Anthropic's Claude Pro/Max plans
# meter usage over a rolling 5-hour session window plus a weekly cap; Gemini's
# free/paid tiers meter daily (and sometimes monthly) request/token quotas.
# Tracking all four uniformly means either provider's actual policy is covered.
WINDOWS: Dict[str, float] = {
    "5h": 5 * 3600,
    "day": 24 * 3600,
    "week": 7 * 24 * 3600,
    "month": 30 * 24 * 3600,
}


class TokenLedger:
    """Persistent, lock-protected log of cloud token/request usage."""

    def __init__(self) -> None:
        paths.ensure_state_dir()
        self.path = str(paths.token_usage())
        self._lock_path = self.path + ".lock"
        if not os.path.exists(self.path):
            self._atomic_write([])

    @contextmanager
    def _flock(self):
        f = open(self._lock_path, "w")
        try:
            fcntl.flock(f, fcntl.LOCK_EX)
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

    def _load(self) -> List[Dict[str, Any]]:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []

    def _atomic_write(self, data: List[Dict[str, Any]]) -> None:
        tmp = f"{self.path}.{os.getpid()}.tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, self.path)

    # -- write --------------------------------------------------------------
    def record(
        self,
        provider: str,
        model: str,
        input_tokens: int = 0,
        output_tokens: int = 0,
        *,
        source: str = "reins",
    ) -> None:
        """Log one cloud call. Never raises - usage tracking must not break a call."""
        try:
            with self._flock():
                events = self._load()
                events.append({
                    "timestamp": time.time(),
                    "provider": provider,
                    "model": model,
                    "input_tokens": int(input_tokens or 0),
                    "output_tokens": int(output_tokens or 0),
                    "total_tokens": int(input_tokens or 0) + int(output_tokens or 0),
                    "source": source,
                })
                self._atomic_write(events)
        except Exception:
            pass

    # -- read -----------------------------------------------------------------
    def all_events(self) -> List[Dict[str, Any]]:
        return self._load()

    def usage_in(self, seconds: float, provider: Optional[str] = None) -> Dict[str, int]:
        """Aggregate requests/tokens in the trailing ``seconds`` window."""
        cutoff = time.time() - seconds
        requests = tokens_in = tokens_out = 0
        for e in self._load():
            if e.get("timestamp", 0) < cutoff:
                continue
            if provider and e.get("provider") != provider:
                continue
            requests += 1
            tokens_in += e.get("input_tokens", 0)
            tokens_out += e.get("output_tokens", 0)
        return {"requests": requests, "input_tokens": tokens_in, "output_tokens": tokens_out,
                "total_tokens": tokens_in + tokens_out}

    def providers(self) -> List[str]:
        return sorted({e.get("provider", "unknown") for e in self._load()})

    def window_summary(self, provider: Optional[str] = None) -> Dict[str, Dict[str, int]]:
        """Usage for every tracked rolling window (5h/day/week/month)."""
        return {name: self.usage_in(secs, provider) for name, secs in WINDOWS.items()}

    def clear(self) -> None:
        with self._flock():
            self._atomic_write([])


def load_budgets() -> Dict[str, Any]:
    """User-editable known plan limits (config/token_budgets.json). Missing/absent -> {}."""
    try:
        return json.loads(paths.token_budgets().read_text(encoding="utf-8"))
    except Exception:
        return {}


def budget_report() -> Dict[str, Any]:
    """
    Usage vs configured budget for every provider seen in the ledger, across every
    tracked window. Percentages are only included where a budget number exists for
    that provider+window - this is a self-tracked estimate, not authoritative
    billing data (neither Anthropic nor Google expose a remaining-quota API).
    """
    ledger = TokenLedger()
    budgets = {k: v for k, v in load_budgets().items() if isinstance(v, dict)}
    report: Dict[str, Any] = {}
    providers = set(ledger.providers()) | set(budgets.keys())
    for provider in sorted(providers):
        windows = ledger.window_summary(provider)
        provider_budget = budgets.get(provider, {})
        for name, usage in windows.items():
            limit = provider_budget.get(name, {})
            if "requests" in limit and limit["requests"]:
                usage["request_budget"] = limit["requests"]
                usage["request_pct"] = round(100 * usage["requests"] / limit["requests"], 1)
            if "tokens" in limit and limit["tokens"]:
                usage["token_budget"] = limit["tokens"]
                usage["token_pct"] = round(100 * usage["total_tokens"] / limit["tokens"], 1)
        report[provider] = windows
    return report

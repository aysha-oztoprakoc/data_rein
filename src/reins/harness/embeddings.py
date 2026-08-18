"""Embedding client for local model vectorization with fallback."""

from __future__ import annotations

import hashlib
import json
import math
import logging
import urllib.error
import urllib.request
from typing import List, Optional

from reins.harness import external_io

logger = logging.getLogger("reins.embeddings")


def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """Compute cosine similarity between two float vectors."""
    if len(vec1) != len(vec2) or not vec1:
        return 0.0
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0
    return dot / (norm1 * norm2)


def fallback_embed(text: str, dim: int = 128) -> List[float]:
    """Deterministic, local hash-feature embedding vectorizer for tests/offline fallbacks."""
    vec = [0.0] * dim
    words = text.lower().split()
    if not words:
        return vec
    for word in words:
        h = int(hashlib.md5(word.encode("utf-8", "replace")).hexdigest(), 16)
        slot = h % dim
        sign = 1.0 if (h >> 8) & 1 else -1.0
        vec[slot] += sign
    # Normalize
    norm = math.sqrt(sum(x * x for x in vec))
    if norm > 0:
        vec = [x / norm for x in vec]
    return vec


class EmbeddingClient:
    """Client for fetching embeddings from local Ollama/LM Studio with graceful fallback."""

    def __init__(
        self,
        model: str = "nomic-embed-text",
        endpoint: str = "http://127.0.0.1:11434/api/embeddings",
        fallback_dim: int = 128,
    ) -> None:
        self.model = model
        self.endpoint = endpoint
        self.fallback_dim = fallback_dim
        self._available: Optional[bool] = None

    def _check_available(self) -> bool:
        if self._available is not None:
            return self._available
        try:
            payload = json.dumps({"model": self.model, "prompt": "ping"}).encode("utf-8")
            req = urllib.request.Request(
                self.endpoint,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with external_io.call("ollama:probe", lambda: urllib.request.urlopen(req, timeout=0.2)) as resp:
                self._available = (resp.status == 200)
        except Exception as exc:
            logger.warning("Embedding probe failed: %s", exc)
            self._available = False
        return self._available

    def embed_text(self, text: str) -> List[float]:
        """Generate embedding vector for a single text chunk."""
        if not text or not text.strip():
            return [0.0] * self.fallback_dim

        if self._check_available():
            try:
                payload = json.dumps({"model": self.model, "prompt": text}).encode("utf-8")
                req = urllib.request.Request(
                    self.endpoint,
                    data=payload,
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with external_io.call("ollama:embed", lambda: urllib.request.urlopen(req, timeout=1.0)) as resp:
                    if resp.status == 200:
                        data = json.loads(resp.read().decode("utf-8"))
                        embedding = data.get("embedding")
                        if isinstance(embedding, list) and embedding:
                            return [float(x) for x in embedding]
            except Exception as exc:
                logger.warning("Embedding call failed: %s", exc)
                self._available = False

        # Graceful fallback to deterministic local feature vector
        return fallback_embed(text, dim=self.fallback_dim)

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Batch vectorization."""
        return [self.embed_text(t) for t in texts]


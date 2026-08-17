"""
Vendored subset of semantica (v0.6.5, MIT) — context engineering module.

Full upstream `semantica` pulls a multi-GB ML stack (torch, spacy, opencv,
librosa, faiss, sentence-transformers, ...) through its `embeddings`, `kg`,
`parse`, `vector_store` and `visualization` subpackages. The Sofia3 graph
bridge only needs the pure-stdlib/numpy `ContextGraph` core, so we vendor
`semantica.context` + `semantica.utils` verbatim and expose only the classes
we use. See `third_party/semantica/README.md` for provenance and rationale.
"""

from .context_graph import ContextEdge, ContextGraph, ContextNode
from .entity_linker import EntityLinker

__all__ = [
    "ContextEdge",
    "ContextGraph",
    "ContextNode",
    "EntityLinker",
]

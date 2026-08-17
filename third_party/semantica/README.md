# Vendored `semantica` subset — `third_party/semantica/`

**Upstream:** https://github.com/semantica-agi/semantica · **Version:** 0.6.5 ·
**License:** MIT (see `LICENSE`, copied from the upstream sdist/wheel).

## Why vendored instead of `uv add semantica`

The full `semantica` PyPI package declares a base dependency list that includes
`torch`, `transformers`, `spacy`, `opencv-python`, `librosa`, `faiss-cpu`,
`sentence-transformers`, `umap-learn`, and more — a multi-GB ML install that
violates this harness's resource discipline (the `train` extra is deliberately
opt-in for the same reason).

The actual `ContextGraph` code path is pure stdlib + numpy:

```
semantica/context/context_graph.py   -> semantica/utils/{logging,progress_tracker,helpers,skos}
                                       + semantica/context/entity_linker.py
semantica/context/entity_linker.py   -> semantica/utils/{logging,progress_tracker,types}
```

The heavy imports (`numpy`, `yaml`, `dateutil`, `IPython`) live only in
`context/agent_memory.py`, `context/decision_query.py`, `context/decision_context.py`,
`context/context_retriever.py`, and `vector_store/` — none of which the Sofia3
graph bridge touches.

## What we vendored

- `semantica/__init__.py` — upstream verbatim (lazy module proxies).
- `semantica/context/` — upstream verbatim **except** `__init__.py`, which we
  trimmed to export only `ContextGraph`, `ContextNode`, `ContextEdge`,
  `EntityLinker` (the upstream init eagerly imports `vector_store`, pulling
  the whole heavy graph). All other files are untouched.
- `semantica/utils/` — upstream verbatim.
- `LICENSE` — upstream MIT text.

## How it's imported

The Sofia3 backend inserts `third_party/` on `sys.path` (same pattern the
dashboard already uses for `src/`), then:

```python
from semantica.context.context_graph import ContextGraph  # or
from semantica.context import ContextGraph
```

Graceful degradation: the graph bridge wraps the import; if the vendored tree
is missing, `/api/graph` reports `{"degraded": true}` instead of crashing.

## Upgrading

When a new semantica release is needed: `pip download --no-deps`, copy
`semantica/__init__.py`, `semantica/context/` (re-apply the trimmed
`__init__.py`), `semantica/utils/`, and refresh `LICENSE`. Re-run the smoke
test in `sofia3/backend/tests/`.

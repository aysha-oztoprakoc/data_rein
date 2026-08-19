# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- (none)

### Changed
- (none)

### Fixed
- (none)

## [0.3.0] - 2026-08-18
### Added
- **Kùzu Graph & ChromaDB Unified Knowledge Engine (`KuzuWikiDB`):**
  - Replaced legacy SQLite as primary monolith knowledge store with embedded Kùzu graph database and ChromaDB vector store.
  - Native Node schemas (`Document`, `MemoryNode`, `Chunk`) and Relational schemas (`Contains`, `DerivesFrom`, `SimilarTo`) supporting hierarchical knowledge provenance and cosine similarity clustering.
  - Fast Cypher graph traversals and semantic vector search with cosine distance thresholding.
  - Sub-millisecond bulk insertion (`batch_insert_memories`) via CSV streaming copy.
  - Memory-safe bounded configuration: 128MB buffer pool and 1GB virtual memory mmap boundary.
- **Expanded Test Suite (400/400 Passing):**
  - Parameterized `test_wiki_contract.py` across SQLite and Kùzu backends verifying latency bounds (<250ms p95 on 10,000 records) and bounded summaries.
  - 100% test coverage across all 400 unit, integration, graph pipeline, and Ten Laws architectural compliance tests.

### Changed
- **Universal Harness Services Swapped to `KuzuWikiDB`:**
  - `reins.harness.wiki.WikiDB` aliased to `KuzuWikiDB` (`SQLiteWikiDB` preserved for legacy database compatibility).
  - Ingestion pipelines (`KnowledgeManager`, `KnowledgeIngestor`, `WikiGraphPipeline`), agents (`agents.py`, `judge.py`, `workflow.py`), MCP servers (`mcp_server.py`), dataset exporters (`dataset.py`, `export_to_obsidian.py`), and Sofia³ REST APIs updated to use unified `WikiDB` interfaces.

## [0.2.0] - 2026-08-16
### Added
- **None** — this is a hardening/productization pass on top of 0.1.0.

### Changed
- **Packaging is now production-validated.** Wheel verified installable with a
  working `reins` console-script entrypoint; declared the previously-missing
  `watchdog` runtime dependency (used by the PON `wiki_watcher`) so a clean
  install no longer fails; sdist scoped via `[tool.hatch.build.targets.sdist]`
  so the tarball shrank from ~291 MB to ~584 KB (no more vendored data trees).
- Added project **extras** documentation (`ingestion`, `media`, `train`) and a
  README refresh with a CI status badge, install guidance, and a Contributing
  section.
- Submodule: `reins-pon-engine` now published as a GitHub submodule.
- Native deployment config (NixOS) and OpenCode agent definitions added.

### Fixed
- **Security hardening:**
  - Vault **path-traversal** fix and repository-wide secret hygiene audit
    (no secrets in tracked history; `detect-secrets` baseline committed).
  - Dataset/export writes confined to a bounded export root.
  - PON gate hardening.
- **CI gate (`.github/workflows/ci.yml`, on every push/PR):**
  - Runs `uv sync --locked` → `compileall` → `pytest` → `ruff` → `bandit -ll`
    → `detect-secrets` (baselined) → `basedpyright` against a committed,
    ratcheting baseline.
  - Fixed 16 pre-existing lint blocking errors, including a real `F821`
    NameError-in-waiting in `workflow.py`.
  - Corrected the ratchet invocation (`--writebaseline`/`--baselinefile`, not
    the invalid `--verifybaseline`) and committed the 247-diagnostic baseline.

## [0.1.0] - unreleased
Initial harness: shared wiki DB (`reins wiki`), model-agnostic local-first router
(`ModelRouter` / OmniRouter combs), Universal Task Trail, canonical 154-skill
tree, autonomous workflows, completeness loop (RLM), Unix MCP server, wiki
watcher, VRAM sensor, Obsidian export, CLI (`reins`).

[Unreleased]: https://github.com/aysha-oztoprakoc/data_rein/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/aysha-oztoprakoc/data_rein/releases/tag/v0.2.0
[0.1.0]: https://github.com/aysha-oztoprakoc/data_rein/releases/tag/v0.1.0
# Source and Operations Reference

## Scope

This reference explains the tracked, executable, and configuration surfaces in
`/home/amdy/data_rein` and `/home/amdy/data-workspace`. Generated caches,
virtual environments, model weights, SQLite WAL files, downloaded corpora,
installer images, and third-party vendored trees are data rather than authored
system behavior and are intentionally not reproduced here.

Read this document with `MULTIMODAL_KNOWLEDGE_PIPELINE.md`, `TEN_LAWS.md`, and
the source. It is an ownership map for models that need to navigate or extend
the harness without inventing duplicate components.

## `data_rein` runtime packages

### Entry points and extraction

| Module | Responsibility and internal contract |
|---|---|
| `reins/__init__.py` | Package marker; contains no runtime state. |
| `reins/cli.py` | Top-level `reins` command. Registers legacy model/trail verbs, delegates universal verbs to `harness.cli`, and starts bounded local services when requested. |
| `reins/extraction/__init__.py` | Imports extractor modules exactly once so their classes register by extension; exports the registry and base contract. |
| `reins/extraction/registry.py` | Maps lowercase suffixes to extractor classes and creates a fresh extractor per request. It is selection only, never persistence. |
| `reins/extraction/artifacts.py` | Converts plugin-compatible results into frozen `KnowledgeArtifact` values, reads canonical output, and hashes source bytes. This is the trust boundary before Wiki writes. |
| `reins/extraction/serialization.py` | Writes and reads canonical `knowledge_document` XML while removing ANSI escapes and XML-illegal code points. |
| `reins/extraction/vision.py` | Selects the first hardware-admitted local Ollama candidate for image analysis and submits base64 image data with coordinator context limits. |
| `reins/extraction/extractors/base.py` | Defines discriminated success/failure results, metadata provenance, and the abstract extractor interface. |
| `reins/extraction/extractors/text_extractors.py` | Parsers for plain text, JSON, CSV, PDF, DOCX, HTML, XML, EPUB, RTF, XLSX/XLS, and PPTX. PDF follows MinerU, PyMuPDF, then command fallback. |
| `reins/extraction/extractors/archive_extractors.py` | Extracts supported textual members from ZIP and RAR containers into one knowledge document. Archives are containers, not a separate knowledge store. |
| `reins/extraction/extractors/media_extractors.py` | Combines Tesseract, routed local vision, faster-whisper, and FFmpeg frame/audio extraction into image, audio, and video artifacts. |
| `reins/extraction/extractors/__init__.py` | Extractor package marker without independent behavior. |

### Harness core

| Module | Responsibility and internal contract |
|---|---|
| `harness/action_gate.py` | Validates and sanitizes proposed tool calls through Socrates, Archimedes, and Sofia stages before dispatch. Rejections are durable Task Trail facts. |
| `harness/agents.py` | Base harness-agent adapter, model/budget selection, recall result shapes, and context-aware execution shared by service agents. |
| `harness/chunking.py` | Estimates token cost and creates bounded handoff chunks with reserve budgets; it prevents local context overflow. |
| `harness/cli.py` | Defines universal Wiki, digest, model, dataset, training, backup, hardware, token, skill, and MCP command surfaces. Handlers call core APIs rather than reimplementing them. |
| `harness/comfyui_client.py` | Async ComfyUI health, queue, websocket-event, history, and image-path client plus a bounded text-to-image workflow builder. |
| `harness/coordinator.py` | Model residency state machine. Accounts for VRAM, loads/unloads Ollama models, performs LRU eviction, and exposes typed status used before training. |
| `harness/dataset.py` | Queries Wiki pages or memories, reconstructs typed provenance, segments content, and writes disposable validated JSONL. |
| `harness/digest.py` | Sole file-to-Wiki orchestration path. Manages changed-file cache, extraction, artifact validation, optional local enrichment, Task Trail state, and MQTT result notification. |
| `harness/dispatch.py` | Implements typed local generation, authorized cloud generation, and file-read actions admitted by the action gate. |
| `harness/external_io.py` | Circuit-breaker choke point for subprocess, HTTP, socket, and MQTT I/O. Transport-specific helpers record breaker transitions. |
| `harness/handoff.py` | Queues token-bounded Task Trail chunks and retrieves the next compatible unit for local workers. |
| `harness/inference_compiler.py` | Builds model-specific prompt packages, remote compiler envelopes, deterministic fallbacks, and bounded context appendices. |
| `harness/inference_mcp.py` | Exposes prompt compilation and local execution as MCP tools; serialized schemas protect the transport boundary. |
| `harness/inference_protocol.py` | Selects remote optimization only when explicitly eligible and otherwise compiles locally with deterministic budgets. |
| `harness/inference_runtime.py` | Executes compiled packages against a router protocol and reports model/provider/node provenance. |
| `harness/inference_types.py` | Frozen Pydantic schemas for optimization requests, remote packages, compiled packages, targets, and results. |
| `harness/ipc.py` | Length-prefixed Unix-socket framing, shared coordinator state, bounded server dispatch, and client calls. Reads block on frames rather than polling. |
| `harness/judge.py` | Validates proposal graphs, rejects cycles/unsafe actions, records verdicts, and executes accepted nodes through the gate. |
| `harness/local.py` | Canonical Ollama store/server lifecycle and non-streaming HTTP generation. Startup readiness is driven by inotify with a bounded fallback. |
| `harness/mcp_server.py` | Universal tool bridge for Wiki, Trail, budgets, routing, inference compilation, judging, tokens, hardware, and coordinator status over stdio or HTTP. |
| `harness/memory_ingestion.py` | Converts curated Sofia and knowledge entries into deduplicated Wiki memories. |
| `harness/model_inventory.py` | Validates node/model availability against `model_registry.json`, rejects non-fitting candidates, and records rejections. |
| `harness/model_providers.py` | Provider runtime adapters for Ollama, ComfyUI, Gemini, Claude, and OpenAI. Cloud secrets and usage remain behind explicit paths. |
| `harness/model_types.py` | Router, inventory, model-specification, and route-result schemas. Provider resolution is derived from explicit provider/backend or model identity. |
| `harness/models.py` | Local-first category router with hardware admission, breaker/retry integration, explicit cloud escalation, and token accounting. |
| `harness/paths.py` | Resolves every canonical location from environment overrides or repository defaults; callers never hard-code mutable state paths. |
| `harness/provider_protocols.py` | Structural interfaces for optional SDKs plus safe JSON conversion, keeping cloud packages out of the core import graph. |
| `harness/resilience.py` | Synchronous/async circuit breaker registry and disciplined retry for idempotent operations only. |
| `harness/resilience_types.py` | Breaker states, open-circuit error, validated circuit settings, and retry policy. |
| `harness/sofia_controls.py` | Explicit operator controls for processes, CPU governor, GPU power, agent termination, niceness, and cgroup budgets. |
| `harness/sofia_health.py` | Textual health controller that converts system/Trail notifications into UI state. |
| `harness/sofia_styles.py` | Textual CSS tokens for the Sofia operational interface. |
| `harness/sofia_types.py` | Typed process/Trail views and bounded system metric readers used by Sofia widgets. |
| `harness/sofia_widgets.py` | Textual panels for system information, metrics, processes, agents, Trail tasks, and kernel controls. |
| `harness/wiki.py` | Canonical SQLite schema, migration, page/memory upserts, FTS5 search, statistics, and transactional context manager. Schema v2 stores extraction provenance. |
| `harness/workflow.py` | User-facing RAG, low-effort, and batch workflows over `ModelRouter`; Wiki context is bounded before prompt injection. |
| `harness/__init__.py` | Harness package marker without independent state. |

### Services

| Module | Responsibility and internal contract |
|---|---|
| `services/agy_bridge.py` | HarnessAgent specialization for AGY-compatible delegation. |
| `services/backup.py` | Health-gated workspace backup, rescue-script generation, restore, and power-action guard behavior. |
| `services/cookbook_evaluator.py` | Evaluates installed model choices against profiled hardware and model-catalog facts. |
| `services/data_nexus/knowledge_manager.py` | Writes reasoning insights through the knowledge-management compatibility surface. It is not the extraction persistence path. |
| `services/data_nexus/nexus_daemon.py` | Validates MQTT events and delegates extraction to digest; explicit trigger/dedup events dispatch bounded work. |
| `services/data_nexus/reasoning_engine.py` | HarnessAgent that generates optimization insights from canonical knowledge context. |
| `services/data_nexus/scraper.py` | Safely reduces HTML into extractable text and emits Nexus-compatible source material. |
| `services/fallback_agent.py` | Odysseus fallback HarnessAgent used when a preferred execution route degrades. |
| `services/harness_bootstrapper.py` | Performs bounded startup recovery and assigns pending fallback tasks without periodic scans. |
| `services/knowledge_ingestor.py` | Compatibility façade for adding knowledge through canonical Wiki APIs. |
| `services/logger.py` | Central logger construction and consistent graceful-degradation traceback reporting. |
| `services/resource_budgets.py` | Validates persistent agent CPU/GPU budgets and applies CPU cgroup limits when available. |
| `services/subagent_manager.py` | HarnessAgent specialization for managed local subagent work. |
| `services/sudo_exec.py` | Narrow privileged-command adapter with explicit argument vectors and diagnostics. |
| `services/sys_profiler.py` | Scans hardware/software, scores model fit, writes manifests, and identifies missing local capabilities. |
| `services/task_trail.py` | Canonical SQLite task ledger, legacy JSON migration, atomic upsert/status transitions, and fallback queries. |
| `services/token_ledger.py` | Persists cloud token/request usage and compares rolling windows with configured provider budgets. |
| `services/vault_manager.py` | Compatibility access to encrypted secrets and Wiki-backed knowledge. |
| `services/__init__.py`, `services/data_nexus/__init__.py`, `services/systemd/__init__.py` | Package markers; no separate runtime behavior. |

### Training

| Module | Responsibility and internal contract |
|---|---|
| `training/capability.py` | Probes Torch, GPU/ROCm, and bitsandbytes and selects NF4 QLoRA, GPU LoRA, or CPU LoRA without breaking core imports. |
| `training/config.py` | Validates base models, sequence/batch budgets, optimizer, epochs, and LoRA target settings. |
| `training/records.py` | Defines source-preserving `TrainingRecord` values, deterministic segmentation, and complete JSONL validation. |
| `training/qlora.py` | Validates inputs before residency changes, unloads local models, invokes one backend, retries one OOM at lower pressure, and records Trail outcomes. |
| `training/transformers_backend.py` | Optional Torch/Transformers/PEFT implementation that applies adapter weight updates and writes the run directory. |
| `training/export.py` | Merges adapters, converts/quantizes GGUF with llama.cpp tools, and creates an Ollama tag. |
| `training/__init__.py` | Training package marker; importing it does not load heavy dependencies. |

## `data_rein` configuration

| File | Authority |
|---|---|
| `pyproject.toml`, `uv.lock` | Runtime/dev/optional dependency declarations and deterministic resolution. `media` and `train` remain independent extras. |
| `config/agent_budgets.json` | Default/per-agent CPU and GPU budgets. |
| `config/backup_config.json` | Backup roots, destinations, and guard behavior. |
| `config/coordinator.json` | VRAM admission, Ollama server environment, context/thread defaults, and keep-alive policy. |
| `config/digest_watch_dirs.json` | Allowed network-trigger roots and pending-ingestion views. It does not start a polling watcher. |
| `config/model_catalog.json` | Candidate model capabilities and resource characteristics used by profiling. |
| `config/model_registry.json` | Observed node reachability, installed models, and models admitted by hardware fit. |
| `config/model_router.json` | Ranked category routes and explicit remote fallback roster. Image analysis uses its local vision candidates. |
| `config/mqtt_topics.json` | Named event topics shared by services. |
| `config/token_budgets.json` | Provider usage limits over rolling windows. |
| `config/training.json` | Base-model, sequence, batch, optimizer, epoch, and LoRA defaults. |
| `config/.secrets.enc`, `config/.secrets.key` | Encrypted secret material and its local key. Documentation never reproduces their contents. |
| `typings/**`, `src/reins/py.typed` | Narrow type contracts for optional untyped packages and the marker declaring `reins` typed. These do not install or emulate runtime dependencies. |

## `data_rein` operator scripts

| Script | Purpose |
|---|---|
| `battle_benchmark.sh` | Runs comparative local-model benchmark workloads. |
| `consolidate_wiki.py` | Idempotently imports tracked docs and legacy read-only sources into the one Wiki. |
| `digest_pipeline.py` | Compatibility command for extraction ingestion; new code should call `reins digest`. |
| `encrypt_secrets.py`, `get_secrets.py` | Encrypt and retrieve vault values without committing plaintext. |
| `extract_odysseus.py`, `extract_sofia_batch.py` | Bounded legacy/source extraction jobs feeding canonical knowledge. |
| `gen_report.py` | Generates an operational report from harness facts. |
| `generate_mock_internet.py` | Produces deterministic offline web fixtures. |
| `ingest_training_data.py`, `inject_sofia_memories.py`, `ody_neural_injection.py` | Compatibility ingestion jobs; permanent results must land in the Wiki. |
| `install_bin.sh`, `install_skills.sh` | Link canonical commands and skills into user-facing environments. |
| `launch_with_sudo.sh` | Starts the privileged control surface through the narrow sudo adapter. |
| `run_all_pedantic_tests.sh` | Executes the project law/quality battery. |
| `run_scraper_goal.py`, `sofia_protocol.py` | Event-driven scraper goal and Sofia protocol entry points. |

## `data_rein` verification map

| Tests | Behavior protected |
|---|---|
| `test_action_gate.py`, `test_dispatch.py`, `test_judge.py` | Typed action admission, graph judgment, rejection logging, and execution. |
| `test_agents.py`, `test_fallback_agent.py`, `test_handoff.py`, `test_chunking.py` | Agent contracts, fallback, Task Trail handoff, and context budgets. |
| `test_backup.py`, `test_health_sanity.py`, `test_omarchy_sanity.py`, `test_stress_battery.py` | Operational health, backup integrity, desktop assumptions, and stress behavior. |
| `test_comfyui_client.py`, `test_local_ensure_server.py`, `test_coordinator.py` | Image-generation transport, notification-driven Ollama startup, and VRAM residency. |
| `test_data_nexus.py`, `test_nexus_scraper.py` | MQTT Nexus behavior and safe scraper parsing. |
| `test_dataset.py`, `test_digest.py`, `test_extractors.py`, `test_multimodal_pipeline.py`, `test_memory_injection.py` | Knowledge parsing, canonical ingestion, provenance, segmentation, and memory writes. |
| `test_determinism.py`, `test_laws.py`, `test_resilience.py` | Lockfile determinism, PON/GD/TDD laws, breakers, and disciplined retry. |
| `test_harness.py`, `test_workflow.py`, `test_model_components.py`, `test_ody_models.py` | Wiki, router, RAG workflows, inventory, and model compatibility. |
| `test_inference_protocol.py`, `test_ipc.py` | Prompt compilation/execution schemas and framed IPC. |
| `test_sofia_protocol.py`, `test_task_trail.py` | Sofia controls/views and durable task transitions. |
| `test_training.py` | Capability degradation, JSONL pre-validation, OOM retry, and training orchestration. |

## `data-workspace` runtime packages

`data-workspace` depends on `../data_rein` in editable mode. Its code should
remain shell-oriented:

| Module | Responsibility and internal contract |
|---|---|
| `data_workspace/__init__.py` | Package marker without durable state. |
| `data_workspace/cli.py` | `data attach`, `data wiki`, and `data cookbook` operator entry point. Core ingestion/training remains available through the dependency's `reins` command. |
| `data_workspace/cookbook.py` | Benchmarks installed Ollama models, combines measured throughput with fit scores, and writes the roster manifest. |
| `data_workspace/living_wiki.py` | Renders skills, Wiki counts/categories, Task Trail workflows, and model matrix as a human-readable view; it never writes another DB. |
| `data_workspace/orchestrator.py` | Chooses the session orchestrator, records selection, and degrades remote choices to an admitted local model. |
| `data_workspace/providers.py` | Explicit Grok/Deepseek-compatible cloud adapters with vault secrets, breakers, and usage recording. |
| `data_workspace/resilience.py` | Workspace-side breaker and sync/async retry used at shell transport boundaries. Core resilience remains in `reins.harness.resilience`. |
| `data_workspace/skills.py` | Discovers canonical skill directories and links them into supported shells. |
| `data_workspace/shells/opencode.py` | Non-destructively merges the MCP command and Task Trail awareness plugin into an OpenCode checkout. |
| `data_workspace/shells/gui.py` | FastAPI router for Living Wiki and supervisor panels over injected MCP calls; unreachable core becomes a sanitized 502. |
| `data_workspace/shells/__init__.py` | Shell package marker without behavior. |

Workspace configuration lives in `pyproject.toml`, `uv.lock`, `flake.nix`, and
`opencode.json`. `COOKBOOK.md` is a generated model recommendation manifest.
`scripts/install_hooks.sh` installs the PON pre-push gate. The workspace tests
map as follows:

| Tests | Behavior protected |
|---|---|
| `test_laws.py`, `test_resilience.py`, `test_resilience_contract.py` | Workspace PON/GD/TDD rules and breaker semantics. |
| `test_shells.py`, `test_phase3.py` | OpenCode/GUI integration, Living Wiki, cookbook, and provider adapters. |
| `test_gaps.py`, `test_security.py`, `test_stability.py`, `test_perf.py` | Architectural gaps, sanitized failures, concurrency/stability, and bounded performance. |
| `test_backup_trigger.py`, `test_install_hooks.py` | Backup notification and reproducible hook installation. |

## Change-routing rules

1. New file format or modality: extend `reins.extraction`, then test through
   digest, Wiki provenance, dataset export, and preflight.
2. New durable fact: add it to the Wiki or Task Trail, never a third store.
3. New model/provider: update typed provider/router boundaries and hardware
   inventory; cloud remains explicit.
4. New shell or panel: implement it in `data-workspace` and consume MCP/core APIs.
5. New core capability useful to all shells: implement it in `data_rein` and
   expose a CLI/MCP/library contract; do not copy it into the workspace.
6. New training backend: consume `TrainingConfig` and validated
   `TrainingRecord` JSONL, preserve provenance, and return an honest result.

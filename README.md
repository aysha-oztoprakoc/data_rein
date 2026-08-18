# DATA_REIN // UNIVERSAL AI HARNESS & PON GRAPH ENGINE

<div align="center">

[![Live Web Portal](https://img.shields.io/badge/LIVE_HUD-Cyberpunk_Terminal-FCEE09?style=for-the-badge&logo=googlechrome&logoColor=black)](https://aysha-oztoprakoc.github.io/data_rein/)
[![License: MIT](https://img.shields.io/badge/LICENSE-MIT-00FFFF?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/PYTHON-3.11-FF003C?style=for-the-badge&logo=python&logoColor=white)](pyproject.toml)
[![Architecture](https://img.shields.io/badge/PARADIGM-PON_KAD_1.1-00FF66?style=for-the-badge)](knowledge_base/PRIME_DIRECTIVE.md)
[![Test Battery](https://img.shields.io/badge/TESTS-391%2F391_PASSING-00FFFF?style=for-the-badge)](tests/)

**[⚡ LAUNCH INTERACTIVE LIVE TERMINAL PORTAL ⚡](https://aysha-oztoprakoc.github.io/data_rein/)**

</div>

---

## ⚡ Executive Overview

**`data_rein`** is a distributed, model-agnostic orchestration harness built under the strict **Notification-Oriented Paradigm (PON KAD 1.1)**. It coordinates a fleet of autonomous agent environments (**Antigravity CLI**, **OpenCode**, **Claude Code**, **Codex**, and **Sofia³ UI**) across physical machines with **zero polling (0% CPU idle)**, central **KùzuDB / ChromaDB vector graph memory**, and an **Automated Quality Control Meta-Harness**.

```
                           ┌────────────────────────────────────────┐
                           │      CENTRAL FACT BASE (tell node)     │
                           │   Mosquitto MQTT v2 · NixOS Store      │
                           │   wiki.db · Kùzu Graph · Chroma Vector │
                           └───────────────────┬────────────────────┘
                                               │
                                      MQTT Reactive Topics
                                               │
               ┌───────────────────────────────┴───────────────────────────────┐
               │                                                               │
┌──────────────▼──────────────┐                                 ┌──────────────▼──────────────┐
│     amdy EXECUTION NODE     │                                 │      tell COMPUTE PLANE     │
│   Stateless Worker Nodes    │                                 │   CUDA Ollama Fleet (Port   │
│   AMD RX 9060 XT (8GB VRAM) │                                 │   11434) · GTX 1060 (6GB)   │
│   Sofia³ UI (FastAPI/React) │                                 │   Central Ingestion Engine  │
└──────────────┬──────────────┘                                 └─────────────────────────────┘
               │
   ┌───────────┴───────────┬───────────────────────┬───────────────────────┐
   │                       │                       │                       │
┌──▼─────────────────┐  ┌──▼─────────────────┐  ┌──▼─────────────────┐  ┌──▼─────────────────┐
│ PON Graph Engine   │  │ QC Meta-Harness    │  │ ModelCoordinator   │  │ Agent-as-a-Judge   │
│ Asynchronous FBE   │  │ Radon CC < 20      │  │ VRAM 8GB JIT Slot  │  │ Archimedes/Socrates│
│ Event Dispatcher   │  │ Cov Delta Ratchet  │  │ Entropy Evictions  │  │ Sofia Grounding    │
└────────────────────┘  └────────────────────┘  └────────────────────┘  └────────────────────┘
```

---

## 🛡️ The Three Propulsion Motors (Project Sofia)

1. **PON (Notification-Oriented Paradigm — Zero Polling):**  
   CPU utilization rests strictly at **0% idle**. Scan loops (`while True`) and polling timers are permanently eliminated. All inter-node and intra-node synchronization operates through blocking I/O (MQTT topics and inotify pipelines).
2. **Graceful Degradation (GD):**  
   The harness is resilient against network faults and I/O limits. All socket connections, subprocesses, and HTTP requests are shielded by **Circuit Breakers** (`CLOSED -> OPEN -> HALF_OPEN`), converting errors into passive diagnostic alerts logged in `task_trail.json`.
3. **Deterministic Quality Ratchet (TDD & QC Gate):**  
   A mathematical quality gate calculating Radon cyclomatic complexity and differential coverage. High complexity hotspots (>20) and negative coverage regressions are strictly blocked; qualifying `LOW` risk changes are merged autonomously via circuit-breaker protected git actions.

---

## 🚀 Key Systems & Architecture

### 1. PON Graph Engineering Engine (`src/reins/graph/`)
- **Fact Base Elements (FBEs):** Decoupled attributes and asynchronous state transitions (`TASK_CREATED` → `TASK_READY` → `VALIDATION` → `QC_REQUEST` → `AUTO_MERGE`).
- **Detached Execution Threads:** Methods run inside `threading.Thread(daemon=True)` fire-and-forget workers, preserving MQTT keepalives and zero-overhead listener loops.
- **LoopBudget Trap:** Prevents cyclical graph recursion with strict step budgets (max 12 iterations).

### 2. Automated Quality Control Meta-Harness (`reins.graph.qc_*`)
- **Radon Analyzer:** Measures cyclomatic complexity across modified files.
- **Pytest-Cov Ratchet:** Enforces the ratchet principle — coverage must never decrease.
- **Autonomous Merge Guard:** Automatically stages and merges low-risk patches if all gates pass.

### 3. Kùzu Graph & ChromaDB Vector RAG (`reins.services.wiki_graph_pipeline`)
- Ingests Markdown pages, memories, and ADRs into a unified **Kùzu Graph ContextGraph** and **ChromaDB vector store** with cosine similarity deduplication (90% threshold).
- Provides instant context injection during agent prompt routing.

### 4. VRAM Residency Coordinator (`src/reins/harness/coordinator.py`)
- Manages local LLM models on demand within strict **8GB VRAM hardware budgets**.
- Employs entropy and LRU heuristics to JIT-evict idle model weights before loading new workloads.

### 5. Sofia³ UI Dashboard (`sofia3/`)
- Greenfield FastAPI backend (`sofia3/backend/app.py`, default port `8088`) with real-time WebSocket push updates.
- High-performance Vite + React + TypeScript frontend (`sofia3/frontend/`) featuring live knowledge graph visualization, task monitoring, and zero-polling state streaming.

---

## ⚡ Canonical Command Reference

Install harness binaries globally into `~/.local/bin` via `reins bin install`:

```bash
# Display canonical paths and Prime Directive
reins paths
reins directive

# Model-Agnostic Execution (Local-First with Kùzu Graph RAG)
reins run "code" "Implement resilient FIFO buffer" --rag
reins ask "Explain PON Zero Polling laws"

# Knowledge & Wiki Search (FTS5 + Graph Neighborhood)
reins wiki search "PON KAD 1.1"
reins wiki stats

# Token Budget Telemetry (5h / 24h / 30d rolling windows)
reins tokens status

# Skill and Binary Management
reins bin list
reins skills list
reins skills install

# Task Trail State Machine
reins trail list
reins trail status
```

---

## 📊 Status Matrix

| Component / Subsystem | Implementation Layer | Status |
| :--- | :--- | :--- |
| **PON Graph Engine** | `src/reins/graph/engine.py` & `fbe.py` | ✅ **PROD LIVE (100%)** |
| **Deterministic QC Gate** | `src/reins/graph/qc_runner.py` & `qc_node.py` | ✅ **PROD LIVE (100%)** |
| **Kùzu Graph & Vector RAG** | `src/reins/services/wiki_graph_pipeline.py` | ✅ **PROD LIVE (100%)** |
| **Sofia³ Web Dashboard** | `sofia3/backend/` + `sofia3/frontend/` | ✅ **PROD LIVE (100%)** |
| **VRAM Coordinator** | `src/reins/harness/coordinator.py` | ✅ **PROD LIVE (100%)** |
| **Multi-Node MQTT Bus** | `tell` (192.168.0.4) ↔ `amdy` (192.168.0.3) | ✅ **PROD LIVE (100%)** |
| **Pre-Push Validation Gate** | `.git/hooks/pre-push` (`pon-testing-suite`) | ✅ **ENFORCED** |
| **Interactive Web Portal** | GitHub Pages (`https://aysha-oztoprakoc.github.io/data_rein/`) | ✅ **PROD LIVE (100%)** |

---

## 🧪 Verification & Test Suite

The entire codebase is verified against 391 strict unit, integration, resilience, and AST law tests:

```bash
# Run full test suite
uv run pytest

# Execute PON Compliance & Security Scanner
python3 ~/.agents/skills/pon_testing_suite/scripts/pon_tester.py src/reins/graph

# Check AST Constitutional Laws
uv run pytest tests/test_laws.py tests/test_production_hardening.py
```

```
============================== 391 passed in 20.75s ==============================
```

---

## 📜 License

MIT License — see [LICENSE](LICENSE).  
Governed by [The Prime Directive](knowledge_base/PRIME_DIRECTIVE.md) & [Omarchy Aesthetic Directive](knowledge_base/AESTHETIC_DIRECTIVE.md).

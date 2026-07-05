# data_rein — Universal AI Harness

[![License: MIT](https://img.shields.io/badge/license-MIT-ff4040)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%2B-ff4040)
![Architecture](https://img.shields.io/badge/architecture-PON-ff4040)
![Local--first](https://img.shields.io/badge/models-local--first-ff4040)

A personal, self-hosted harness that lets a fleet of AI agents — Claude Code, OpenCode,
Antigravity, and a graphical dashboard (Odysseus) — share one knowledge base, one
model router, and one task trail across two machines. Built around the **PON
(Notification-Oriented Paradigm)**: no polling, no `while True`, no spin-wait `sleep` —
everything reacts to events.

This repo is both the harness itself and its own knowledge base: it hosts the code, the
docs the agents read on boot, and a running record of what's built vs. what's still open.

## Why this exists

Running several AI coding assistants side by side usually means each one re-discovers
context from scratch, burns cloud tokens on work a small local model could do, and has
no shared memory of what the others already tried. `data_rein` fixes that by giving every
agent the same three things:

- **One knowledge store** — a single SQLite "wiki" (`knowledge_base/wiki.db`) with
  full-text search over pages and memories, rebuilt idempotently from tracked markdown.
- **One model router** — `ModelRouter` picks a provider per task category (local Ollama
  first, cloud only on explicit request or genuine complexity) and fails over gracefully
  between nodes instead of crashing.
- **One task trail** — a shared, queryable log of what every agent has done, so a new
  session can pick up exactly where the last one left off instead of guessing.

## Architecture

```
                     ┌─────────────────────────────┐
                     │        knowledge_base/       │
                     │   wiki.db · PRIME_DIRECTIVE   │
                     │   MODEL_HIERARCHY · HARDWARE  │
                     └───────────────┬───────────────┘
                                     │  reins wiki / trail
        ┌───────────────┬───────────┼───────────┬───────────────┐
        │               │           │           │               │
   Claude Code       OpenCode   Antigravity   Odysseus       (any agent
   (this repo's       (local     (Gemini      (Docker,        speaking
    CLI agent)      LM Studio)    CLI)      web dashboard)    AGENTS.md)
        │               │           │           │               │
        └───────────────┴───────────┼───────────┴───────────────┘
                                     │
                          ┌──────────┴──────────┐
                          │     ModelRouter      │
                          │  local-first, graceful│
                          │  amdy ↔ tell failover │
                          └──────────┬───────────┘
                     ┌───────────────┼───────────────┐
                Ollama (13 local           Cloud (Claude / Gemini /
                models, on-demand)          OpenAI — explicit only)
```

## Key features

- **Model-agnostic routing** (`src/reins/harness/models.py`) — task categories map to a
  provider preference list; local Ollama models are tried first, with automatic fallback
  across every locally-installed model before ever touching a cloud API.
- **Unified wiki + task trail** — every agent reads and writes the same store, so
  "what happened in the last session" is always answerable from inside the repo.
- **Ingestion pipeline** — PDF (mineru → PyMuPDF → pdftotext fallback chain), DOCX, EPUB,
  RTF, XLSX/XLS, PPTX, and web-scraped content all normalize into the same wiki.
- **Local-first economics** — 13 local Ollama models cover menial coding, summarization,
  classification, and RAG; cloud models (`escalate_cloud`) are reserved for work that's
  explicitly requested or genuinely too heavy for local hardware, and every cloud call is
  logged to the task trail for auditability.
- **Odysseus dashboard** — a Dockerized web UI (zero filesystem access into the harness)
  that talks to the harness over an HTTP MCP transport, rendering task trail activity,
  per-agent CPU/GPU budgets, and wiki search in one place.
- **PON-compliant throughout** — event-driven (inotify/MQTT), never polling; graceful
  degradation to a lesser model/node instead of crashing.

## Quick start

```bash
uv sync
reins directive          # print the Prime Directive (read this first)
reins wiki stats          # sanity-check the knowledge store
reins local status         # check the local Ollama model fleet
reins ask "hello"          # smoke-test the router end to end
```

See `AGENTS.md` for the full agent contract (boot sequence, CLI reference, skills) —
it's the same file every agent in this harness reads before doing anything else.

## Status & roadmap

A living snapshot of what's solid vs. what's still in progress — updated as work lands,
not aspirational.

| Area | Status |
|---|---|
| Wiki DB + task trail | ✅ Live, in daily use |
| Model router (local + cloud failover) | ✅ Live |
| Local-model delegation for menial coding | ✅ Live |
| PDF/DOCX/XLSX/PPTX ingestion pipeline | ✅ Live |
| Odysseus dashboard (Docker, MCP-HTTP bridge) | 🟡 Built, not yet run end-to-end |
| ComfyUI image generation | 🟡 Dispatch code wired; ComfyUI's own Python/torch env not set up yet |
| Repo security hardening (public-readiness) | ✅ Audited — no secrets in tracked history |
| Voice (TTS/STT) coverage | ⬜ Planned — see `knowledge_base/MODEL_GAPS.md` |
| Embedding-based (semantic) wiki search | ⬜ Planned — currently keyword (FTS5) only |

Track granular in-progress work as GitHub Issues; this table is the big-picture view.

## Repo layout

| Path | What it is |
|---|---|
| `src/reins/` | The harness itself — CLI, wiki, model router, extraction pipeline |
| `knowledge_base/` | Canonical docs the agents read: Prime Directive, hardware/model manifests, aesthetic directive |
| `skills/` | Canonical, tracked agent skills (`reins skills install` links them everywhere) |
| `odysseus/` | Vendored web dashboard, wired to the harness via MCP-over-HTTP |
| `scripts/` | Setup, backup, and secrets-vault tooling |
| `tests/` | Test suite (`.venv/bin/pytest -q`) |

## Principles (PON)

1. **Zero polling** — no `while True`, no spin-wait `sleep`; everything reacts to
   events (inotify, MQTT, file-system watches).
2. **Graceful degradation** — a failure degrades to a lesser model or node; it never
   crashes the caller.
3. **Strict role separation** — execution and state responsibilities are split across
   nodes rather than conflated.

## License

MIT — see [LICENSE](LICENSE).

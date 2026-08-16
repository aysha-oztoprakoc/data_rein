---
name: data_rein
description: "Universal data_rein harness — unified wiki DB, model-agnostic routing, PON, memory sync. Canonical skill for Odysseus and any harness agent."
tags: "harness, wiki, memory, pon, model-agnostic, sync"
---

# Data Rein — Universal Harness Skill

## ⚠️ MANDATORY INITIALIZATION (AUTO-PICKUP)
Before answering anything, synchronize your memory:
1. Read `/home/amdy/data_rein/knowledge_base/PRIME_DIRECTIVE.md` (master constitution).
2. Read `/home/amdy/data_rein/knowledge_base/SHARED_CONTEXT.md` (last agent's trail).
3. Run `reins wiki stats` and `reins trail list` to sync with shared state.
Do this immediately, without asking.

## The Continual Harness (Memory & State)
All knowledge lives in one durable store: `knowledge_base/wiki.db` (the Continual Harness).
Do not maintain static hierarchies of AGENTS.md files. Store memories, subagent patterns, and refinements here so they outlive single sessions. Never create another database.
```bash
reins wiki search "<query>"            # search everything
reins wiki get <slug>                  # read a page
reins wiki add-memory "<fact>" --category <cat>
reins wiki consolidate                 # rebuild from all sources (idempotent)
```
Python: `from reins.harness.wiki import WikiDB`.

## Prime Agent RLM & Model-Agnostic Routing
`from reins.harness.rlm import rlm` — Dispatch native subagents via the RLM paradigm.
Do not use verbose text instructions for subagents. Spawning a subagent is a function call:
`handle = rlm(prompt="Review auth", tier="rlm-worker-fast")`

`from reins.harness.models import ModelRouter` — Route by task category (`config/model_router.json`).
Routing maps to capability tiers (`rlm-primary`, `rlm-worker-fast`, `rlm-worker-heavy`), not static roles.
Provider is auto-selected (Ollama/Gemini/Claude/OpenAI/ComfyUI), local-first with graceful failover amdy↔tell.
Secrets only via `scripts.get_secrets.get_secret`.

Providers are admitted by an explicit execution-plane capability (`local_text`, `cloud_text`, or `image`).

## Protocol enforcement
- **PON**: no `while True` / `time.sleep` polling. Event-driven, exit gracefully.
- **Graceful Degradation**: degrade to a lesser model/node; never crash; log to Task Trail.
- **Aesthetic**: obey `knowledge_base/AESTHETIC_DIRECTIVE.md` on all output.
- **TDD**: `tests/` enforce these properties before execution.

> This canonical skill replaces the legacy copies buried under
> `DATA/kad-1.0/odysseus/data/skills/`. Point every environment here.

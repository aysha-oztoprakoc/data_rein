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

## The single monolith Wiki database
All knowledge lives in one store: `knowledge_base/wiki.db` (`pages` + `memories`,
FTS5). Never create another database.
```bash
reins wiki search "<query>"            # search everything
reins wiki get <slug>                  # read a page
reins wiki add-memory "<fact>" --category <cat>
reins wiki consolidate                 # rebuild from all sources (idempotent)
```
Python: `from reins.harness.wiki import WikiDB`.

## Model-agnostic routing
`from reins.harness.models import ModelRouter` — route by task category
(`config/model_router.json`), provider auto-selected (Ollama/Gemini/Claude/OpenAI/
ComfyUI), local-first with graceful failover amdy↔tell. Secrets only via
`scripts.get_secrets.get_secret`.

## Protocol enforcement
- **PON**: no `while True` / `time.sleep` polling. Event-driven, exit gracefully.
- **Graceful Degradation**: degrade to a lesser model/node; never crash; log to Task Trail.
- **Aesthetic**: obey `knowledge_base/AESTHETIC_DIRECTIVE.md` on all output.
- **TDD**: `tests/` enforce these properties before execution.

> This canonical skill replaces the legacy copies buried under
> `DATA/kad-1.0/odysseus/data/skills/`. Point every environment here.

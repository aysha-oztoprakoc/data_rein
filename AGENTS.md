# AGENTS.md — data_rein Universal Harness

> Universal agent contract, read by Antigravity, Cursor, VS Code agent tooling,
> Odysseus, and any AGENTS.md-aware assistant. Claude Code additionally reads
> `CLAUDE.md`; both defer to `knowledge_base/PRIME_DIRECTIVE.md`.

## Boot sequence (every session, before answering)

1. Read `knowledge_base/PRIME_DIRECTIVE.md` (the master constitution).
2. Read `knowledge_base/SHARED_CONTEXT.md` (trail from the previous agent).
3. `reins wiki stats` and `reins trail list` to sync with shared state.

## One harness, one database, any model

- **Single monolith Wiki DB:** `knowledge_base/wiki.db`. Access via the `reins
  wiki` CLI from any shell, or `reins.harness.wiki.WikiDB` in Python. Never spin
  up a second store. Rebuild it idempotently with `reins wiki consolidate`.
- **Model-agnostic routing:** `config/model_router.json` +
  `reins.harness.models.ModelRouter`. Route by task category; the router picks the
  provider (Ollama / Gemini / Claude / OpenAI / ComfyUI). Local-first, graceful
  failover to the other node.
- **Secrets:** only through `scripts.get_secrets.get_secret` (encrypted vault).
  Never read `config/api_keys.json` or hard-code keys.

## Laws (see the Prime Directive for the full text)

- **PON** — zero polling; event-driven; strict amdy(exec)/tell(state) split; FBE.
- **Graceful degradation** — degrade, never crash; log failures to the Task Trail.
- **Aesthetic** — `knowledge_base/AESTHETIC_DIRECTIVE.md` governs all output.

## Quick reference

```bash
reins paths                 # canonical locations
reins directive             # print the Prime Directive
reins wiki search "<q>"     # search unified knowledge
reins skills list           # canonical harness skills (source: skills/)
reins skills install        # link skills into every environment
reins trail list            # shared task state machine
```

## Skills

One canonical, tracked skills tree: `skills/` (see `skills/MANIFEST.md`). Edit
skills there only; `reins skills install` symlinks them into each environment's
scan path. Skills are also ingested into the wiki (`reins wiki search`).

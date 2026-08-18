# CLAUDE.md — data_rein Universal Harness

You are operating inside the **`data_rein` universal harness**. This repo is the
shared spine for a fleet of cooperating agents (Antigravity, Hermes, Odysseus,
and you — Claude Code) running across two nodes, `amdy` (execution) and `tell`
(state).

## Initialization protocol (do this first, every session)

1. Read **`knowledge_base/PRIME_DIRECTIVE.md`** — the master constitution that
   binds every environment. It supersedes local conventions.
2. Read **`knowledge_base/SHARED_CONTEXT.md`** — the live trail from the last agent.
3. Orient against the shared state:
   ```bash
   reins wiki stats      # the single monolith knowledge DB
   reins trail list      # what other agents are doing / what failed
   ```

## The one knowledge store

There is exactly one database: the **monolith Wiki DB** at
`knowledge_base/wiki.db`. Reach it from any shell:

```bash
reins wiki search "<query>"          # FTS over pages + memories
reins wiki get <slug>                # print a page
reins wiki add-memory "<fact>" --category system
reins wiki consolidate               # rebuild from all sources (idempotent)
```
In Python: `from reins.harness.wiki import WikiDB`. Do not create a second store.

## Model-agnostic execution

Route by task category, never by hard-coded model, via
`from reins.harness.models import ModelRouter`. Config lives in
`config/model_router.json`. Ordinary category routing is local-only with amdy/tell
failover. Cloud (Gemini/Claude/OpenAI) requires a separate, explicitly authorized
`route_cloud`/`escalate_cloud` call; secrets only via `scripts.get_secrets.get_secret`.

### Leverage local models (offload low-effort work here first)

Models under `ai_models/models/` are served by an on-demand Ollama server
(`reins local up` / auto-started). Use the live inventory for availability and
prefer hardware-admitted local models for trivial work:

```bash
reins local status                 # server + model store + count
reins run "deep search" "<q>" --rag   # route to best local model, inject wiki context
reins ask "<q>"                    # quick chat (small fast model, tell->amdy failover)
reins summarize file.md            # or: cat x | reins summarize
reins optimize "<prompt>"          # tighten a prompt
reins batch "data processing" prompts.txt   # unattended bulk run, logged to trail
```
All of this routes through `reins.harness.workflow`, inherits graceful failover,
and logs batch work to the shared Task Trail.

### Claude Code: delegate menial coding to local models

The `reins` MCP server (`.mcp.json`, `reins mcp`) exposes `route_local` and
`escalate_cloud`. For test-writing, boilerplate, and other small/fast/short
code changes, call `route_local("coding: menial", ...)` by default — it
reaches `qwen2.5-coder:7b` first, with automatic fallback to any other
locally-installed model, and never touches a cloud provider. Write such code
yourself, or call `escalate_cloud`, only when the user explicitly asks for
Claude/Gemini specifically. Reserve direct Claude Code involvement for
design/judgment work, review, and anything the user asked for by name.

## Skills

Canonical harness skills live in `skills/` (tracked, indexed by
`skills/MANIFEST.md`): `data_rein`, `agy-pon-compliance`, `kad_pon`,
`hermes-persona`, `omarchy-aesthetics`, `pon_testing_suite`, and
`prompt-optimizer`. `reins skills install` symlinks them into `~/.claude/skills/`
(and every other environment). Edit only the source in `skills/<name>/SKILL.md`,
then re-install. List: `reins skills list`.

## Non-negotiables (from the Prime Directive)

- **PON:** no polling, no `while True`, no `sleep` spin-waits. Event-driven only.
- **Graceful degradation:** degrade to a lesser model/node; never crash.
- **PLAN-1 (Planning Phase Separation):** When planning/grilling skills are invoked, research and generate the plan/interview ONLY. Do not edit code or execute commands before explicit user approval.
- **Aesthetic:** all generated text/UI/images obey `knowledge_base/AESTHETIC_DIRECTIVE.md`
  (Blood Red `#ff4040` on Black `#200000`, gritty synthetic voice).

## Agent skills

### Issue tracker

Issues live in GitHub Issues (`gh` CLI); external PRs are also triaged as a request surface. See `docs/agents/issue-tracker.md`.

### Triage labels

Default label vocabulary (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) — no repo-specific remapping. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.

## Repo conventions

- Harness code: `src/reins/harness/` (paths, wiki, models, cli).
- CLI entry point: `reins` (defined in `src/reins/cli.py`).
- Run tests: `.venv/bin/pytest -q`. Never commit `config/api_keys.json`,
  `.secrets*`, or the derived `knowledge_base/wiki.db` (all git-ignored).

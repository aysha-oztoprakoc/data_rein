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
reins bin list               # harness commands linked into ~/.local/bin
reins bin install            # symlink/wrap every harness command onto $PATH
reins trail list            # shared task state machine
```

## Local models (offload low-effort work)

13 local models in `ai_models/models/`, served on demand by Ollama.
```bash
reins local status | up | list
reins run "<category>" "<prompt>" [--rag] [--node amdy|tell]
reins ask|summarize|classify|optimize "<text|file>"   # low-effort shortcuts
reins batch "<category>" prompts.txt                   # unattended bulk, trail-logged
```
Routes through `reins.harness.workflow` → `ModelRouter` (local-first, graceful
amdy↔tell failover). Prefer local for trivial work; reserve cloud for heavy tasks.

## Skills

One canonical, tracked skills tree: `skills/` (see `skills/MANIFEST.md`). Edit
skills there only; `reins skills install` symlinks them into each environment's
scan path. Skills are also ingested into the wiki (`reins wiki search`).

## Commands on $PATH

`reins bin install` (`scripts/install_bin.sh`) symlinks every installed
console-script (`reins` itself) and wraps every custom dashboard/TUI script
(currently `sofia` → `scripts/sofia_protocol.py`) into `~/.local/bin`, so they
run from any shell without `cd`ing into the repo or typing `.venv/bin/<x>`.
Adding a new custom command: add one `wrapper <name> <path>` line to
`scripts/install_bin.sh`, then re-run `reins bin install` (idempotent).

## OpenCode: the interactive front end

OpenCode is the harness's main interactive CLI. Its default model is a local
LM Studio model (Qwen2.5-Coder-7B, JIT-loaded on port 1234) — the same local-first
policy as everything else here. It connects to the `reins` MCP server (registered
in `opencode.json`, `python -m reins.harness.mcp_server`) for structured access to
the shared state:

- `wiki_search` / `wiki_get` / `wiki_add_memory` — the same monolith wiki everyone else uses.
- `trail_list` / `trail_create` / `trail_update` / `agent_status` — the Universal Task Trail;
  check `agent_status`/`trail_list` before systemic actions, per the Rule of Awareness.
- `route_local` — delegate a menial subtask (summarize/classify/extract) to a cheap
  local Ollama model instead of spending an agent turn on it. Never reaches cloud.
- `escalate_cloud` — **the only** path to Claude/Gemini/OpenAI. Call it only when the
  user explicitly asks for Claude or Gemini by name; never as a default or automatic
  step. Every call is logged to the Task Trail (`task_type="opencode:cloud-escalation"`)
  so it stays exactly as auditable as `reins run`'s own last-resort cloud fallback.
- `token_usage_status` — self-tracked Claude/Gemini/OpenAI usage vs configured budgets
  (`config/token_budgets.json`) over 5h/day/week/month rolling windows. Also reachable
  from any shell via `reins tokens status`. Neither provider exposes a remaining-quota
  API, so this is a local counter of every cloud call the harness itself makes — not
  authoritative billing data, but the only complete picture available.

**Autostart:** `systemd/lmstudio-harness.service` brings up LM Studio's local server
at login (install like `ollama-harness.service` — see the file header). The tmux
`data` session (`~/.local/bin/data-harness-windows.sh`) has a `data-code` window
running `omni opencode --server "" --model lmstudio/qwen/qwen2.5-coder-7b --resume`
— OpenCode driven through Omnigent exactly like `data-omni` drives Claude, so the
user's main interactive session always resumes the last conversation, the same
way `data-agy` (`-c`) and `data-omni` (`--resume`) do.

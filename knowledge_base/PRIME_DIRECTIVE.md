# // PRIME DIRECTIVE — data_rein Universal Harness

> This is the single master constitution for every intelligence operating under
> the `data_rein` harness. It binds all environments — **Antigravity (data-agy)**,
> **Hermes (data-hermes)**, **Odysseus (data-ody)**, **Claude Code**, **OpenCode**,
> and the **VS Code** workspace — to one contract. If a rule here conflicts with a
> local convention, this file wins. Load it first. Obey it always.

---

## 0. MANDATORY INITIALIZATION PROTOCOL (do this before answering anything)

The executable engineering laws are defined in `knowledge_base/TEN_LAWS.md`.
They decompose this constitution into PON-1..3, GD-1..3, TDD-1..3, and NIX-1;
all clients load and apply them with this directive.

On every new session or invocation inside this workspace, **before** responding to
the user, you MUST synchronize:

1. Read this file (`knowledge_base/PRIME_DIRECTIVE.md`).
2. Read `knowledge_base/SHARED_CONTEXT.md` — the live trail left by the last agent.
3. If you have shell access, orient against the monolith:
   ```bash
   reins wiki stats          # what knowledge exists
   reins trail list          # what other agents are doing / what failed
   ```
Do not ask permission to read these. Synchronize immediately, silently, then work.

---

## 1. ONE HARNESS, MANY ENVIRONMENTS

Every environment is a *client* of the same harness. None of them owns the state.

| Environment    | Entry file it loads          | How it reaches the harness            |
|----------------|------------------------------|----------------------------------------|
| Antigravity    | `.agents/AGENTS.md`          | shell → `reins` CLI                    |
| Claude Code    | `CLAUDE.md`                  | shell → `reins` CLI                    |
| Odysseus       | `skills/data_rein/SKILL.md`  | shell / python `reins.harness`         |
| Hermes         | `agents/hermes/SOUL.xml`     | python `reins.harness`                 |
| OpenCode       | `AGENTS.md` + `opencode.json`| MCP (`reins.harness.mcp_server`) + shell |
| Codex          | `AGENTS.md` + `.codex/config.toml` | MCP (`reins.harness.mcp_server`) + shell |
| VS Code        | `AGENTS.md` + `.vscode/`     | integrated terminal → `reins` CLI      |

**OpenCode is the harness's interactive front end.** Its default model is a local
LM Studio model (Qwen2.5-Coder-7B, JIT-loaded), sharing amdy's 8GB VRAM slot with
Ollama the same way every other local model does. It reaches Claude/Gemini/OpenAI
**only** through explicit MCP cloud tools on user request — never natively, so cloud
access from an interactive session stays vault-gated and Task-Trail-logged. Use
`escalate_cloud` for a direct remote answer and `compile_prompt_remote` for the
remote compilation phase described below. Ordinary `ModelRouter.route` calls have
no cloud authorization parameter; the separate `route_cloud` API is the cloud
boundary (§3). Direct-answer trail entries appear under `task_type` prefix
`opencode:`.

The same explicit cloud boundary also supports the inspectable two-phase prompt
inference protocol. `compile_prompt_remote` uses one named cloud provider to produce
a strict, hardware-aware `data-rein.remote-local-inference/1` package;
`run_prompt_local` validates and executes that package without a cloud callable.
Remote compiler output is untrusted data and cannot change routing or authorization.

All of them resolve the *same* canonical paths via `reins.harness.paths`. There is
no per-environment copy of anything that matters.

**Codex is a client of the harness, not its model owner.** Project instructions
come from this repository's `AGENTS.md`; `.codex/config.toml` connects Codex to
the same `reins` MCP server used by the other clients. Codex may delegate by task
category through `route_local` or use `escalate_cloud` only after an explicit
user request. The active Codex model remains a host/user setting and is never
written into `config/model_router.json`.

### Skills

There is one canonical, tracked skills tree: **`skills/`** (indexed by
`skills/MANIFEST.md`). It is the single editable source for every harness skill —
`data_rein`, `agy-pon-compliance`, `deep-research-paper`, `hermes-persona`,
`kad_pon`, `omarchy-aesthetics`, `pon_testing_suite`, `prompt-optimizer`,
`utfpr-tcc-abnt`.
Skills are lean: their deep knowledge lives in the wiki, not embedded copies.

Each environment receives them as symlinks via `reins skills install` (idempotent),
which links `skills/*` into every environment's scan path (Odysseus
`data/skills/`, Claude Code `~/.claude/skills/`, Antigravity `.agents/skills/`,
Codex). Never edit an installed copy — edit `skills/<name>/SKILL.md` and re-install.
```bash
reins skills list      # registered skills + descriptions
reins skills install   # link them into every environment
```

---

## 2. THE SINGLE SHARED MONOLITH WIKI DATABASE

There is exactly **one** knowledge store: the monolith Wiki DB.

- **Location:** `knowledge_base/wiki.db` (override with `$DATA_REIN_WIKI_DB`).
- **Access:** `reins.harness.wiki.WikiDB` in Python, or the `reins wiki` CLI from
  any shell. Two logical stores in one file — `pages` (documents) and `memories`
  (atomic facts / the "Ody Memory Vault") — both full-text searchable (FTS5).
- **Rebuildable:** the DB is a *derived* artifact. Its sources of truth are
  `knowledge_base/**`, `data-oby/**`, and any Odysseus `app.db`. Rebuild/refresh
  at any time — idempotently — with:
  ```bash
  reins wiki consolidate          # or: python scripts/consolidate_wiki.py
  ```
- **Rule:** never invent a second database. If you need to persist knowledge,
  write a `page` or a `memory`. If you need to read knowledge, search the wiki.
  The DB file itself is git-ignored precisely because it is rebuildable from the
  tracked sources — commit the *source*, not the binary.

Universal access examples (work identically in every environment with a shell):
```bash
reins wiki search "graceful degradation"
reins wiki get <slug>
reins wiki add-memory "amdy GPU is RX 9060 XT, 8GB VRAM" --category system
```

---

## 3. MODEL AGNOSTICISM

The harness is not welded to any vendor. Route by *task category*, not by model.

- Routing table: `config/model_router.json` (12 categories × `amdy`/`tell` × ranked
  models). Dispatch through `reins.harness.models.ModelRouter`.
- Providers are inferred automatically — Ollama (local/ssh), Gemini, Claude,
  OpenAI-compatible, ComfyUI (image/audio). Add a model by adding a row; the
  router picks the provider. No code change to support a new backend of an
  existing provider family.
- **Local-first, graceful degradation:** background/autonomous work prefers local
  open-weights models. On failure the router walks down the ranked list, then
  fails over to the other node and returns an honest failure if both local planes
  are exhausted. Cloud models (Gemini/Claude/OpenAI) require a separate explicit
  `route_cloud`/`escalate_cloud` call authorized by the user. A requested cloud
  provider is never substituted with another vendor. Secrets come only from the
  encrypted vault (`scripts.get_secrets.get_secret`) — never from plaintext,
  never hard-coded.
- **Remote-to-local prompt inference:** selected prompts may use the separately
  authorized `compile_prompt_remote` tool for compression, context shaping, and
  target-model format adaptation under a 16,384-token ceiling. The returned package
  must cross the `run_prompt_local` validation boundary before local execution.
  Malformed, oversized, or unavailable remote compilation degrades to a deterministic
  bounded package and is recorded in the Task Trail. Full contract:
  `knowledge_base/REMOTE_LOCAL_INFERENCE_PROTOCOL.md`.

### 3a. Hardware manifest — the single source of truth for specs

Never hard-code hardware specs. The live cluster hardware lives in one place:
**`knowledge_base/HARDWARE.md`** (`reins.harness.paths.hardware_manifest`), regenerated
by the **`getinfo`** scan (`SysProfiler` → MQTT `data_rein/getinfo/trigger`, or
`python -m reins.services.sys_profiler`). Every model tier in `model_router.json`
must fit the VRAM budget the manifest reports. Current budget (auto-refreshed on the
next scan, so this is a pointer, not a copy):

| Node   | GPU              | VRAM | RAM   | CPU                        |
|--------|------------------|------|-------|----------------------------|
| `amdy` | AMD RX 9060 XT   | 8 GB | 16 GB | Ryzen 7 7700 (8c/16t)      |
| `tell` | NVIDIA GTX 1060  | 6 GB | 16 GB | Intel i5 7th-gen (4c/4t)   |

When hardware changes, run `getinfo`; the manifest, the mirrored `system` wiki memory,
and every downstream decision update from the scan — do not edit specs by hand elsewhere.

---

## 4. PON — THE ARCHITECTURAL LAW (Notification-Oriented Paradigm)

All code written under this harness obeys PON:

1. **Zero Polling.** No `while True`, no `time.sleep()` spin-waits, no active
   status polling. Wait via blocking I/O, reactive pipes, or MQTT subscription.
   Idle CPU cost must be ~0%.
2. **Strict role separation (amdy vs tell).** `amdy` executes (Methods); durable
   state belongs to `tell`. Execution nodes wake only when notified.
3. **FBE abstraction.** Model data/logic as Fact Base Elements. Entities do not
   chain-call each other; they change Attributes, which fire notifications to
   Rules and Methods reactively.
4. **Graceful degradation.** Wrap execution frames so a failure degrades, never
   crashes. Fall back to a lesser model/node and log the failure to the Task Trail.

---

## 5. THE UNIVERSAL TASK TRAIL

All agents share one indexed state machine: `~/.config/data_nexus/task_trail.sqlite3`
(`reins.harness.paths.task_trail`). Before a systemic action, check it (`reins trail
list`) to see what is `running`/`pending` and whether anything `failed` and needs
pickup. Log your own long-running work there so another agent can resume it.
On first use, the harness imports the former `task_trail.json` exactly once and
retains that file as migration evidence; active clients must use the `TaskTrail` API.
Fallback execution is opt-in: only active tasks whose `target_node` is `data-ody`
may be claimed by the Odysseus daemon. A generic `pending` or `running` status never
transfers ownership.

---

## 6. AESTHETIC DIRECTIVE (binding for all generated output)

All text, UI, and image generation obeys `knowledge_base/AESTHETIC_DIRECTIVE.md`:
Omarchy Cyberpunk — **True Blood Red `#ff4040` / `#ff1100` on Deep Blood Black
`#200000`**, extreme rounding (Hyprland `rounding = 50`), heavy glassmorphism, and
a gritty, synthetic, zero-fluff hacker voice. Cohesion across the whole ecosystem
is mandatory.

---

## 7. THE CONTRACT (one line)

> Sync first · one wiki · any model · zero polling · degrade, never crash · stay on-brand.

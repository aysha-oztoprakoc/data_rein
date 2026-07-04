# // PRIME DIRECTIVE — data_rein Universal Harness

> This is the single master constitution for every intelligence operating under
> the `data_rein` harness. It binds all environments — **Antigravity (data-agy)**,
> **Hermes (data-hermes)**, **Odysseus (data-ody)**, **Claude Code**, and the
> **VS Code** workspace — to one contract. If a rule here conflicts with a local
> convention, this file wins. Load it first. Obey it always.

---

## 0. MANDATORY INITIALIZATION PROTOCOL (do this before answering anything)

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
| VS Code        | `AGENTS.md` + `.vscode/`     | integrated terminal → `reins` CLI      |

All of them resolve the *same* canonical paths via `reins.harness.paths`. There is
no per-environment copy of anything that matters.

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
reins wiki add-memory "amdy GPU is RX 9060 XT, 16GB VRAM" --category system
```

---

## 3. MODEL AGNOSTICISM

The harness is not welded to any vendor. Route by *task category*, not by model.

- Routing table: `config/model_router.json` (11 categories × `amdy`/`tell` × ranked
  models). Dispatch through `reins.harness.models.ModelRouter`.
- Providers are inferred automatically — Ollama (local/ssh), Gemini, Claude,
  OpenAI-compatible, ComfyUI (image/audio). Add a model by adding a row; the
  router picks the provider. No code change to support a new backend of an
  existing provider family.
- **Local-first, graceful degradation:** background/autonomous work prefers local
  open-weights models. On failure the router walks down the ranked list, then
  fails over to the other node. Cloud models (Gemini/Claude/OpenAI) are for
  explicit, heavy, or user-authorized tasks. Secrets come only from the encrypted
  vault (`scripts.get_secrets.get_secret`) — never from plaintext, never hard-coded.

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

All agents share one state machine: `~/.config/data_nexus/task_trail.json`
(`reins.harness.paths.task_trail`). Before a systemic action, check it (`reins trail
list`) to see what is `running`/`pending` and whether anything `failed` and needs
pickup. Log your own long-running work there so another agent can resume it.

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

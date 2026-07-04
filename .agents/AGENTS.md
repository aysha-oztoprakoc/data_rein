# Universal Memory Synchronization — data_rein Harness

The following applies to **every** agent operating in the `~/data_rein` context
(Antigravity / data-agy, Hermes, Odysseus, Claude Code, VS Code tooling).

<RULE>
**MANDATORY INITIALIZATION PROTOCOL (MEMORY SYNC)**

Every time you begin a new session or receive a prompt in this workspace, you MUST,
before answering, proactively read — in order:

1. `~/data_rein/knowledge_base/PRIME_DIRECTIVE.md` — the master constitution that
   binds all environments (memory sync, the single wiki DB, model agnosticism,
   PON, graceful degradation, aesthetic).
2. `~/data_rein/knowledge_base/SHARED_CONTEXT.md` — the live trail left by the
   previous agent.

Then synchronize with shared state via the harness CLI:
`reins wiki stats` and `reins trail list`. Do not ask permission — do it immediately.
</RULE>

## The harness in one screen

- **One knowledge DB:** `knowledge_base/wiki.db` — reach it with `reins wiki ...`
  or `reins.harness.wiki.WikiDB`. Rebuild idempotently: `reins wiki consolidate`.
- **Any model:** route by category through `reins.harness.models.ModelRouter`
  (`config/model_router.json`); provider auto-selected; local-first with failover.
- **PON:** zero polling, event-driven, amdy=exec / tell=state, FBE, degrade-not-crash.
- **Aesthetic:** obey `knowledge_base/AESTHETIC_DIRECTIVE.md` for all output.

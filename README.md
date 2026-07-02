# Sovereign AI Data Harness

This is the central Data Harness and Knowledge Base for the Sovereign AI project, built on the PON (Notification-Oriented Paradigm).

## Architecture

This project is divided into several key components:
- **`knowledge_base/`**: Canonical hierarchy of all AI knowledge, synced in real-time.
- **`extraction_pipeline/`**: Scalable data extraction for text and media (distributed across `amdy` and `tell`).
- **`prompt_optimizer/`**: Agent for compressing and injecting context into prompts for ≤16k token models.
- **`sync/`**: Zero-polling `inotifywait` daemon that keeps knowledge synced.
- **`services/`**: Core orchestrators and background daemons.

## Setup

```bash
uv sync
uv run scripts/setup.sh
```

## PON Principles
1. **Zero Polling**: No `while True` or `time.sleep` loops. All logic is reactive via MQTT or inotify.
2. **Strict Role Separation**: Execution on `amdy`, state on `tell`.
3. **FBE Abstraction**: Data models trigger methods reactively.

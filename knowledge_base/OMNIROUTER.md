# OmniRouter — Unified Multi-Account & Multi-Provider Model Router

The **OmniRouter** is the unified routing subsystem inside `data_rein` (`reins.harness.models.ModelRouter`). It allows every agent (Antigravity, Codex, Claude Code, OpenCode, Hermes, Odysseus) to seamlessly access local and remote model accounts through a single, resilient dispatch pipeline.

---

## 1. Concepts

- **Combo**: A labeled `(provider, model, secret_key, base_url, tier)` triple representing one available endpoint/account. Example: `chatgpt-free`, `gemini-free`, `claude-free`, `grok-free`, `kimi-free`, `glm-free`.
- **Combo Chain**: An ordered list of combo IDs mapped to a task category (`rlm-primary`, `rlm-worker-fast`, `rlm-worker-heavy`, `rlm-vision`).
- **Quota-Aware Fallback**: If a combo hits a 429 (rate limit), 402/quota error, or exceeds 95% of its sliding-window token budget, OmniRouter automatically skips it and falls over to the next combo in the chain.

---

## 2. Vault Management (`reins secret`)

All API keys are encrypted at rest using AES-256 (Fernet) in `config/.secrets.enc`. Never store API keys in plain text files.

### CLI Usage

```bash
# List all registered secret keys (values hidden)
reins secret list

# Add or update an API key
reins secret set DEEPSEEK_API_KEY "sk-..."
reins secret set XAI_API_KEY "xai-..."
reins secret set MOONSHOT_API_KEY "sk-..."
reins secret set ZHIPU_API_KEY "..."

# Retrieve a secret value
reins secret get DEEPSEEK_API_KEY

# Remove a secret key
reins secret rm DEEPSEEK_API_KEY
```

### MCP Tools (for OpenCode/Codex/Agents)

- `vault_list()`: returns JSON list of key names
- `vault_set(key_name, value)`: sets secret in vault
- `vault_rm(key_name)`: deletes secret from vault

---

## 3. Combo Management (`reins combos`)

Combos are stored in `config/omnirouter.json`.

### CLI Usage

```bash
# List all combos and their current health / key bindings
reins combos list

# Add or update a combo
reins combos add chatgpt-alt --provider openai --model gpt-4o-mini --secret-key OPENAI_API_KEY_ALT --tier free

# Remove a combo
reins combos rm chatgpt-alt

# Test a prompt dispatch on a specific combo
reins combos test deepseek-free
```

### MCP Tools (for OpenCode/Codex/Agents)

- `combo_list()`: returns JSON of all combos with real-time rate limit cooldown status
- `combo_route(combo_id, prompt)`: explicitly dispatch a prompt to a target combo ID

---

## 4. Supported Providers

| Provider ID | Upstream Provider | Base URL | Vault Key |
|---|---|---|---|
| `ollama` | Ollama (Local) | `localhost:11434` | N/A |
| `gemini` | Google Gemini | Google SDK | `GEMINI_API_KEY` |
| `anthropic` / `claude` | Anthropic Claude | Anthropic SDK | `ANTHROPIC_API_KEY` |
| `openai` | OpenAI | `https://api.openai.com/v1` | `OPENAI_API_KEY` |
| `deepseek` | DeepSeek AI | `https://api.deepseek.com` | `DEEPSEEK_API_KEY` |
| `xai` | xAI Grok | `https://api.x.ai/v1` | `XAI_API_KEY` |
| `moonshot` | Moonshot Kimi | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY` |
| `zhipu` | ZhipuAI GLM | `https://open.bigmodel.cn/api/paas/v4` | `ZHIPU_API_KEY` |
| `openrouter` | OpenRouter | `https://openrouter.ai/api/v1` | `OPENROUTER_API_KEY` |
| `comfyui` | ComfyUI | `http://tell:8188` | N/A |

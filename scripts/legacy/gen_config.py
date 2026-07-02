import json
import os

registry_path = os.path.expanduser("~/DATA/data_rein/model_registry.json")
config_path = os.path.expanduser("~/.continue/config.json")
os.makedirs(os.path.dirname(config_path), exist_ok=True)

with open(registry_path, "r") as f:
    registry = json.load(f)

models = []
for node, data in registry.items():
    for tier, m_list in data.get("tiers", {}).items():
        for m in m_list:
            models.append({
                "title": f"[{tier}] {m['model']} (Score: {m['score']})",
                "provider": "openai",
                "model": m["model"],
                "apiBase": "http://localhost:8080/v1",
                "apiKey": "none"
            })

# Add Cloud models
cloud_models = [
    {"title": "[CLOUD] Gemini 1.5 Pro", "model": "gemini-1.5-pro"},
    {"title": "[CLOUD] Claude 3.5 Sonnet", "model": "claude-3-5-sonnet-20240620"},
    {"title": "[CLOUD] GPT-4o", "model": "gpt-4o"}
]

for cm in cloud_models:
    models.append({
        "title": cm["title"],
        "provider": "openai",
        "model": cm["model"],
        "apiBase": "http://localhost:8080/v1",
        "apiKey": "none"
    })

config = {
    "models": models,
    "customCommands": [
        {
            "name": "test",
            "prompt": "Test if you are receiving this.",
            "description": "Test Data Harness"
        }
    ],
    "tabAutocompleteModel": {
        "title": "Stacoder/Codegemma",
        "provider": "openai",
        "model": "qwen2.5-coder:7b",
        "apiBase": "http://localhost:8080/v1"
    }
}

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print("Continue config generated with Cloud models.")

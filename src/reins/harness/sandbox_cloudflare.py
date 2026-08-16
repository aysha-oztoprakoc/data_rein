from __future__ import annotations

import json


def execute_sandboxed(script_content: str, language: str = "bash") -> str:
    del script_content, language
    return json.dumps(
        {
            "ok": False,
            "status": "not_configured",
            "reason": "integration is not configured",
        }
    )

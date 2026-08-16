from __future__ import annotations

import json


def jcode_browser_action(
    action: str,
    url: str | None = None,
    selector: str | None = None,
    text: str | None = None,
) -> str:
    del action, url, selector, text
    return json.dumps(
        {
            "ok": False,
            "status": "not_configured",
            "reason": "integration is not configured",
        }
    )

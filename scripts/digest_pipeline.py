#!/usr/bin/env python3
"""
DEPRECATED SHIM — the digest pipeline now lives in the harness.

Historically this script extracted a folder and injected memories straight into
the legacy Odysseus ``app.db``, forking the knowledge write path. That fork is
retired: there is one ingestion path and one store now — ``reins digest`` ->
``knowledge_base/wiki.db`` (see ``reins.harness.digest``).

This wrapper is kept only so existing automation/muscle-memory keeps working. It
forwards to the canonical path. Prefer calling ``reins digest <path>`` directly.
"""

import sys
import argparse

# Make ``src`` importable when run as a loose script.
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from reins.harness import digest  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Digest a folder into the single wiki DB (shim over `reins digest`).")
    parser.add_argument("folder", nargs="?", default="~/Downloads/raw_data/", help="File or folder to digest")
    parser.add_argument("--no-enrich", action="store_true", help="Skip local-model fact enrichment")
    args = parser.parse_args()

    print(f"[*] Digesting {args.folder} into the monolith wiki (wiki.db)...")

    def _emit(item: "digest.DigestItem") -> None:
        mark = "+" if item.ok else "-"
        detail = f"{item.slug} (+{item.facts} facts)" if item.ok else item.error
        print(f"[{mark}] {item.path} -> {detail}")

    results = digest.digest_path(
        args.folder, recursive=True, enrich=not args.no_enrich, on_result=_emit
    )
    ok = sum(1 for r in results if r.ok)
    print(f"[+] Digest complete: {ok}/{len(results)} file(s) written to wiki.db.")


if __name__ == "__main__":
    main()

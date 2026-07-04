"""
Universal harness CLI verbs: `reins wiki ...`, `reins directive`, `reins paths`.

These give every environment with a shell (Antigravity, Claude Code, Odysseus,
VS Code terminal) one identical way to reach the single monolith Wiki DB and the
Prime Directive - no per-environment client code.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from reins.harness import paths
from reins.harness.wiki import WikiDB


def register(subparsers: "argparse._SubParsersAction") -> None:
    # reins wiki ...
    wiki = subparsers.add_parser("wiki", help="Query the single monolith Wiki DB")
    wsub = wiki.add_subparsers(dest="subcmd")

    wsub.add_parser("stats", help="Show page/memory counts and categories")
    wsub.add_parser("consolidate", help="Rebuild the wiki from all sources (idempotent)")

    p = wsub.add_parser("search", help="Full-text search pages + memories")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=8)

    p = wsub.add_parser("get", help="Print a page by slug")
    p.add_argument("slug")

    p = wsub.add_parser("add-memory", help="Store an atomic fact")
    p.add_argument("text")
    p.add_argument("--category", default="general")
    p.add_argument("--source", default="cli")

    # reins directive / paths
    subparsers.add_parser("directive", help="Print the Prime Directive")
    subparsers.add_parser("paths", help="Print canonical harness paths")


def handle(args: argparse.Namespace) -> bool:
    """Return True if this module handled the command."""
    if args.command == "wiki":
        return _handle_wiki(args)
    if args.command == "directive":
        pd = paths.prime_directive()
        print(pd.read_text(encoding="utf-8") if pd.exists() else f"// missing: {pd}")
        return True
    if args.command == "paths":
        for k, v in paths.summary().items():
            print(f"{k:20s} {v}")
        return True
    return False


def _handle_wiki(args: argparse.Namespace) -> bool:
    sub = getattr(args, "subcmd", None)

    if sub == "consolidate":
        script = paths.home() / "scripts" / "consolidate_wiki.py"
        subprocess.run([sys.executable, str(script)], check=False)
        return True

    db = WikiDB()
    try:
        if sub == "stats":
            print(f"// monolith wiki -> {db.path}")
            print(f"   pages    : {db.stats()['pages']}")
            print(f"   memories : {db.stats()['memories']}")
            print("   categories:")
            for cat, n in sorted(db.categories().items(), key=lambda kv: -kv[1]):
                print(f"     {n:5d}  {cat}")
        elif sub == "search":
            res = db.search(args.query, args.limit)
            print(f"// pages ({len(res['pages'])}):")
            for r in res["pages"]:
                print(f"  [{r['category']}] {r['slug']}\n      {r['snippet']}")
            print(f"// memories ({len(res['memories'])}):")
            for r in res["memories"]:
                print(f"  [{r['category']}] {r['snippet']}")
        elif sub == "get":
            row = db.get_page(args.slug)
            if not row:
                print(f"// no page: {args.slug}")
            else:
                print(f"# {row['title']}  [{row['category']}]  ({row['source_path']})\n")
                print(row["content"])
        elif sub == "add-memory":
            uid = db.add_memory(args.text, category=args.category, source=args.source)
            print(f"// stored memory {uid[:12]}")
        else:
            print("usage: reins wiki {stats|search|get|add-memory|consolidate}")
    finally:
        db.close()
    return True

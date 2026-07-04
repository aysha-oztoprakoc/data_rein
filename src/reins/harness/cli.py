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

    # reins skills ...
    skills = subparsers.add_parser("skills", help="List/install harness skills")
    ssub = skills.add_subparsers(dest="subcmd")
    ssub.add_parser("list", help="List registered canonical skills")
    ssub.add_parser("install", help="Link skills into every environment")

    # reins local ... (local model server lifecycle)
    local_p = subparsers.add_parser("local", help="Manage the local Ollama model plane")
    lsub = local_p.add_subparsers(dest="subcmd")
    lsub.add_parser("status", help="Show server status + model store")
    lsub.add_parser("list", help="List locally served models")
    lsub.add_parser("up", help="Start the local model server on the harness store")

    # reins run <category> [prompt]  (route a prompt to the best local model)
    run_p = subparsers.add_parser("run", help="Run a prompt on the best local model for a category")
    run_p.add_argument("category")
    run_p.add_argument("prompt", nargs="?", help="prompt text (or read from stdin)")
    run_p.add_argument("--node", default="amdy", choices=["amdy", "tell"])
    run_p.add_argument("--rag", action="store_true", help="inject wiki context")

    # low-effort shortcuts
    for verb, helptext in (
        ("ask", "Quick question -> small fast local model"),
        ("summarize", "Summarize a file or stdin"),
        ("classify", "Classify/label stdin or text"),
        ("optimize", "Optimize a prompt"),
    ):
        sp = subparsers.add_parser(verb, help=helptext)
        sp.add_argument("text", nargs="?", help="text/file (or read from stdin)")
        sp.add_argument("--rag", action="store_true", help="inject wiki context")

    # reins batch <category> [file]  (heavy automation)
    batch_p = subparsers.add_parser("batch", help="Run a model over many prompts (one per line)")
    batch_p.add_argument("category")
    batch_p.add_argument("file", nargs="?", help="file of prompts (or stdin)")
    batch_p.add_argument("--node", default="amdy", choices=["amdy", "tell"])
    batch_p.add_argument("--rag", action="store_true")

    # reins directive / paths
    subparsers.add_parser("directive", help="Print the Prime Directive")
    subparsers.add_parser("paths", help="Print canonical harness paths")


def handle(args: argparse.Namespace) -> bool:
    """Return True if this module handled the command."""
    if args.command == "wiki":
        return _handle_wiki(args)
    if args.command == "skills":
        return _handle_skills(args)
    if args.command in ("local", "run", "batch", "ask", "summarize", "classify", "optimize"):
        return _handle_workflow(args)
    if args.command == "directive":
        pd = paths.prime_directive()
        print(pd.read_text(encoding="utf-8") if pd.exists() else f"// missing: {pd}")
        return True
    if args.command == "paths":
        for k, v in paths.summary().items():
            print(f"{k:20s} {v}")
        return True
    return False


def _read_text_arg(value: Optional[str]) -> str:
    """A positional that is a file path -> file contents; '-' or None -> stdin; else literal."""
    import sys

    if value and value != "-" and Path(value).is_file():
        return Path(value).read_text(encoding="utf-8", errors="replace")
    if value and value != "-":
        return value
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def _handle_workflow(args: argparse.Namespace) -> bool:
    from reins.harness import local, workflow

    cmd = args.command

    if cmd == "local":
        sub = getattr(args, "subcmd", None)
        if sub == "up":
            ok = local.ensure_server()
            print(f"// local model server {'up' if ok else 'FAILED to start'} "
                  f"[store={local.model_store()}]")
        elif sub == "list":
            models = local.list_models()
            print(f"// {len(models)} local models served:")
            for m in models:
                print(f"  {m}")
        else:  # status
            up = local.server_up()
            print(f"// local model plane")
            print(f"   server   : {'UP' if up else 'down'} ({local.DEFAULT_HOST})")
            print(f"   store    : {local.model_store()}")
            print(f"   models   : {len(local.list_models()) if up else 0}")
        return True

    if cmd == "run":
        prompt = args.prompt or _read_text_arg(None)
        if not prompt.strip():
            print("// no prompt (pass an arg or pipe stdin)")
            return True
        res = workflow.run(args.category, prompt, node=args.node, rag=args.rag)
        _print_route(res)
        return True

    if cmd in ("ask", "summarize", "classify", "optimize"):
        text = _read_text_arg(getattr(args, "text", None))
        if not text.strip():
            print(f"// no input for {cmd} (pass text/file or pipe stdin)")
            return True
        if cmd == "summarize":
            text = "Summarize the following concisely:\n\n" + text
        elif cmd == "classify":
            text = "Classify/label the following. Reply with the label(s) only:\n\n" + text
        elif cmd == "optimize":
            text = "Rewrite this prompt to be clearer and more token-efficient:\n\n" + text
        res = workflow.low_effort(cmd, text, rag=getattr(args, "rag", False))
        _print_route(res)
        return True

    if cmd == "batch":
        text = _read_text_arg(getattr(args, "file", None))
        prompts = [ln for ln in text.splitlines() if ln.strip()]
        if not prompts:
            print("// no prompts (one per line via file or stdin)")
            return True
        print(f"// batch: {len(prompts)} prompts -> category '{args.category}' on {args.node}")

        def _emit(item: workflow.BatchItem) -> None:
            status = "ok " if item.ok else "ERR"
            body = (item.text or item.error or "").strip().replace("\n", " ")
            print(f"  [{status}] #{item.index} ({item.model}): {body[:120]}")

        results = workflow.batch(args.category, prompts, node=args.node,
                                 rag=args.rag, on_result=_emit)
        ok = sum(1 for r in results if r.ok)
        print(f"// done: {ok}/{len(results)} succeeded")
        return True

    return False


def _print_route(res) -> None:
    if res.ok:
        print(f"// {res.model} @ {res.node} [{res.provider}]")
        print(res.text.strip() if res.text else "")
    else:
        print(f"// all candidates degraded: {res.error}")


def _skills_dir() -> Path:
    return paths.home() / "skills"


def _handle_skills(args: argparse.Namespace) -> bool:
    sub = getattr(args, "subcmd", None)
    root = _skills_dir()

    if sub == "install":
        script = paths.home() / "scripts" / "install_skills.sh"
        subprocess.run(["bash", str(script)], check=False)
        return True

    # default / list
    if not root.is_dir():
        print(f"// no skills dir: {root}")
        return True
    print(f"// canonical harness skills -> {root}")
    for skill_md in sorted(root.glob("*/SKILL.md")):
        name = skill_md.parent.name
        desc = ""
        for line in skill_md.read_text(encoding="utf-8", errors="replace").splitlines():
            s = line.strip()
            if s.startswith("description:"):
                desc = s.split(":", 1)[1].strip().strip('">')
                break
        print(f"  {name:20s} {desc[:80]}")
    return True


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

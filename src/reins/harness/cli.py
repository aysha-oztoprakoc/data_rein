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

    # reins digest <path>  (raw files -> wiki knowledge)
    dig = subparsers.add_parser("digest", help="Extract files (text/audio/video/images) into the wiki")
    dig.add_argument("path", help="file or directory to digest")
    dig.add_argument("--recursive", action="store_true", help="recurse into subdirectories")
    dig.add_argument("--no-enrich", action="store_true", help="skip local-model fact enrichment (faster)")
    dig.add_argument("--no-trail", action="store_true", help="do not log to the Task Trail")

    # reins backup ...  (omarchy/workspace backup + shutdown guard)
    bak = subparsers.add_parser("backup", help="Backup + shutdown-guard for omarchy/workspace")
    bsub = bak.add_subparsers(dest="subcmd")
    bsub.add_parser("check", help="Run the health/integrity suite and report")
    bsub.add_parser("now", help="Back up if healthy (refresh rescue script + push dotfiles)")
    bsub.add_parser("status", help="Show backup config + last rescue script")
    bsub.add_parser("install", help="Wire the guard into bash/zsh + systemd (user-space)")
    bsub.add_parser("uninstall", help="Remove the guard wiring")
    g = bsub.add_parser("guard", help="Intercept a power action: health-gate + back up")
    g.add_argument("action", choices=["reboot", "poweroff", "shutdown"])
    g.add_argument("--force", action="store_true", help="proceed even if health checks fail")
    g.add_argument("--dry-run", action="store_true", help="do everything except the real power action")
    em = bsub.add_parser("emergency", help="Generate the portable single-file rescue script")
    em.add_argument("--out", help="output path (default from config)")
    rs = bsub.add_parser("restore", help="Restore the workspace")
    rs.add_argument("--source", default="local", choices=["local", "github", "gcloud"])

    # reins tokens ...  (self-tracked Claude/Gemini/OpenAI usage vs configured budgets)
    tok = subparsers.add_parser("tokens", help="Show cloud token/request usage vs configured budgets")
    tsub = tok.add_subparsers(dest="subcmd")
    tsub.add_parser("status", help="Usage vs budget for every provider, per rolling window")
    tsub.add_parser("clear", help="Wipe the usage ledger (does not touch config/token_budgets.json)")

    # reins secret <KEY>  (read one value from the encrypted vault)
    sec = subparsers.add_parser("secret", help="Print a secret value from the encrypted vault")
    sec.add_argument("key", help="secret name, e.g. GITHUB_TOKEN")

    # reins directive / paths
    subparsers.add_parser("directive", help="Print the Prime Directive")
    subparsers.add_parser("paths", help="Print canonical harness paths")

    # reins mcp  (stdio MCP server for interactive front ends, e.g. OpenCode)
    subparsers.add_parser("mcp", help="Run the reins MCP bridge (wiki/trail/router tools) over stdio")


def handle(args: argparse.Namespace) -> bool:
    """Return True if this module handled the command."""
    if args.command == "wiki":
        return _handle_wiki(args)
    if args.command == "skills":
        return _handle_skills(args)
    if args.command in ("local", "run", "batch", "ask", "summarize", "classify", "optimize"):
        return _handle_workflow(args)
    if args.command == "digest":
        return _handle_digest(args)
    if args.command == "backup":
        return _handle_backup(args)
    if args.command == "secret":
        return _handle_secret(args)
    if args.command == "tokens":
        return _handle_tokens(args)
    if args.command == "directive":
        pd = paths.prime_directive()
        print(pd.read_text(encoding="utf-8") if pd.exists() else f"// missing: {pd}")
        return True
    if args.command == "paths":
        for k, v in paths.summary().items():
            print(f"{k:20s} {v}")
        return True
    if args.command == "mcp":
        from reins.harness.mcp_server import main as mcp_main

        mcp_main()
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


def _handle_digest(args: argparse.Namespace) -> bool:
    from reins.harness import digest

    p = Path(args.path).expanduser()
    if not p.exists():
        print(f"// no such path: {p}")
        return True
    print(f"// digesting {p} -> wiki (enrich={not args.no_enrich})")

    def _emit(item: "digest.DigestItem") -> None:
        if item.ok:
            print(f"  [ok ] {item.node}: {item.slug} (+{item.facts} facts)  <- {item.path}")
        else:
            print(f"  [ERR] {item.path}: {item.error}")

    results = digest.digest_path(
        str(p), recursive=args.recursive, enrich=not args.no_enrich,
        on_result=_emit, log_trail=not args.no_trail,
    )
    ok = sum(1 for r in results if r.ok)
    print(f"// digested {ok}/{len(results)} file(s) into the wiki")
    return True


def _handle_backup(args: argparse.Namespace) -> bool:
    from reins.services.backup import BackupService

    svc = BackupService()
    sub = getattr(args, "subcmd", None)

    if sub == "check":
        rep = svc.health_check()
        for r in rep.results:
            mark = "\033[32m✓\033[0m" if r.ok else "\033[31m✗\033[0m"
            print(f"  {mark} {r.name:20s} {r.detail}")
        print(f"// health: {'OK' if rep.passed else 'FAILED (' + str(len(rep.failures)) + ')'}")
        return True
    if sub == "now":
        rep = svc.health_check()
        if not rep.passed:
            print(f"// health FAILED ({len(rep.failures)}); refusing to overwrite the good backup. "
                  "Run `reins backup check`.")
            svc.failsafe_backup()
            return True
        out = svc.backup_now()
        print(f"// backup OK -> rescue={out['emergency_script']} dotfiles_pushed={out['dotfiles_pushed']}")
        return True
    if sub == "guard":
        rc = svc.guard(args.action, force=args.force, dry_run=args.dry_run)
        raise SystemExit(rc)
    if sub == "emergency":
        p = svc.generate_emergency_script(dest=getattr(args, "out", None))
        print(f"// portable rescue script -> {p}  ({p.stat().st_size // 1024} KB)")
        print("   restore from a live USB with:  bash omarchy_rescue.sh --restore")
        return True
    if sub == "restore":
        ok = svc.restore(args.source)
        print(f"// restore from {args.source}: {'OK' if ok else 'FAILED'}")
        return True
    if sub == "install":
        for note in svc.install_hooks():
            print(f"  {note}")
        print("// guard installed. Open a new shell (or `source ~/.bashrc`) to activate.")
        return True
    if sub == "uninstall":
        for note in svc.uninstall_hooks():
            print(f"  {note}")
        return True
    # status / default
    cfg = svc.config
    print(f"// backup config -> {svc.config_path}")
    print(f"   dotfiles repo : {cfg.get('dotfiles', {}).get('git_dir')}")
    print(f"   rescue script : {cfg.get('emergency_script')}")
    print(f"   github restore: {cfg.get('remote_restore', {}).get('github', {}).get('repo')}")
    print(f"   gcloud restore: {'enabled' if cfg.get('remote_restore', {}).get('gcloud', {}).get('enabled') else 'disabled'}")
    return True


def _handle_secret(args: argparse.Namespace) -> bool:
    try:
        import sys as _sys
        _sys.path.insert(0, str(paths.home() / "scripts"))
        from get_secrets import get_secret  # type: ignore
        val = get_secret(args.key)
        if val:
            print(val)
        else:
            print(f"// no such secret: {args.key}", file=__import__("sys").stderr)
    except Exception as e:
        print(f"// vault error: {e}", file=__import__("sys").stderr)
    return True


def _handle_tokens(args: argparse.Namespace) -> bool:
    from reins.services.token_ledger import TokenLedger, budget_report

    sub = getattr(args, "subcmd", None)
    if sub == "clear":
        TokenLedger().clear()
        print("// token usage ledger cleared")
        return True

    report = budget_report()
    if not report:
        print("// no cloud usage recorded yet")
        return True
    print(f"// cloud usage vs budget -> {TokenLedger().path}")
    for provider, windows in report.items():
        print(f"  {provider}:")
        for window, usage in windows.items():
            line = f"    {window:6s} requests={usage['requests']:<4d} tokens={usage['total_tokens']}"
            if "request_pct" in usage:
                line += f"  ({usage['request_pct']}% of {usage['request_budget']} requests)"
            if "token_pct" in usage:
                line += f"  ({usage['token_pct']}% of {usage['token_budget']} tokens)"
            print(line)
    return True


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

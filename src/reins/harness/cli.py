"""
Universal harness CLI verbs: `reins wiki ...`, `reins directive`, `reins paths`.

These give every environment with a shell (Antigravity, Claude Code, Odysseus,
VS Code terminal) one identical way to reach the single monolith Wiki DB and the
Prime Directive - no per-environment client code.
"""

from __future__ import annotations
from reins.services.logger import log_degradation

import argparse
import sys
from pathlib import Path

from reins.harness import external_io, paths
from reins.harness.wiki import WikiDB


def register(
    subparsers: "argparse._SubParsersAction[argparse.ArgumentParser]",
) -> None:
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

    # reins bin ...  (make every custom command runnable from any shell)
    binp = subparsers.add_parser("bin", help="List/install harness commands on $PATH")
    bsub2 = binp.add_subparsers(dest="subcmd")
    bsub2.add_parser("list", help="List commands linked into ~/.local/bin")
    bsub2.add_parser("install", help="Symlink/wrap every harness command into ~/.local/bin")

    # reins combos ...
    cmb = subparsers.add_parser("combos", help="Manage model combos")
    csub = cmb.add_subparsers(dest="subcmd")
    csub.add_parser("list", help="List all combos")
    
    ca = csub.add_parser("add", help="Add or update a combo")
    ca.add_argument("id", help="Combo ID")
    ca.add_argument("--provider", required=True, help="Provider name")
    ca.add_argument("--model", required=True, help="Model name")
    ca.add_argument("--secret-key", default="", help="Secret key name")
    ca.add_argument("--base-url", default="", help="Base URL")
    ca.add_argument("--tier", default="free", help="Tier (free/paid/local)")
    
    crm = csub.add_parser("rm", help="Remove a combo")
    crm.add_argument("id", help="Combo ID")
    
    ctst = csub.add_parser("test", help="Test a combo")
    ctst.add_argument("id", help="Combo ID")

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
    dig.add_argument("--force", action="store_true", help="re-digest files even if unchanged since last run")

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

    # reins secret ... (manage the encrypted vault)
    sec = subparsers.add_parser("secret", help="Manage the encrypted vault")
    sec_sub = sec.add_subparsers(dest="subcmd")
    sg = sec_sub.add_parser("get", help="Print a secret value")
    sg.add_argument("key", help="secret name, e.g. GITHUB_TOKEN")
    ss = sec_sub.add_parser("set", help="Set a secret value")
    ss.add_argument("key", help="secret name")
    ss.add_argument("value", help="secret value")
    sec_sub.add_parser("list", help="List all secret names")
    sr = sec_sub.add_parser("rm", help="Remove a secret")
    sr.add_argument("key", help="secret name")

    # reins directive / paths
    subparsers.add_parser("directive", help="Print the Prime Directive")
    subparsers.add_parser("paths", help="Print canonical harness paths")

    # reins mcp  (stdio MCP server for interactive front ends, e.g. OpenCode;
    # --http for network clients that can't share a stdio pipe, e.g. Odysseus in Docker)
    mcp_p = subparsers.add_parser("mcp", help="Run the reins MCP bridge (wiki/trail/router tools)")
    mcp_p.add_argument("--http", action="store_true", help="serve over streamable-HTTP instead of stdio")
    mcp_p.add_argument("--host", default="127.0.0.1")
    mcp_p.add_argument("--port", type=int, default=8765)
    mcp_p.add_argument(
        "--allow-remote-http",
        action="store_true",
        help="allow an authenticated HTTP bind outside the loopback interface",
    )

    # reins coord ...  (model residency coordinator / IPC server)
    coord = subparsers.add_parser("coord", help="Manage the model residency coordinator (VRAM budget)")
    csub = coord.add_subparsers(dest="subcmd")
    csub.add_parser("status", help="Show slot state + VRAM usage vs budget")
    cl = csub.add_parser("load", help="Warm-load a model into residency")
    cl.add_argument("model")
    cu = csub.add_parser("unload", help="Evict a model immediately")
    cu.add_argument("model")
    csub.add_parser("serve", help="Run the same-node UDS IPC server in the foreground")

    # reins dataset export <out.jsonl>  (wiki -> training JSONL)
    ds = subparsers.add_parser("dataset", help="Export training datasets from the wiki")
    dsub = ds.add_subparsers(dest="subcmd")
    de = dsub.add_parser("export", help="Export wiki pages/memories to JSONL")
    de.add_argument("out", help="output .jsonl path")
    de.add_argument("--modality", help="filter to digested/<modality>")
    de.add_argument("--category", action="append", help="filter to this category prefix (repeatable)")
    de.add_argument("--kind", default="completion", choices=["completion", "memories"])
    de.add_argument("--min-chars", type=int, default=64)
    de.add_argument("--max-chars", type=int, default=8192)
    de.add_argument("--limit", type=int, default=0)

    # reins train ...  (QLoRA fine-tuning; optional `train` extras group)
    train = subparsers.add_parser("train", help="Fine-tune a local model on digested wiki data (QLoRA)")
    tsub = train.add_subparsers(dest="subcmd")
    tp = tsub.add_parser("prepare", help="Export a training JSONL (alias for `dataset export`)")
    tp.add_argument("out", help="output .jsonl path")
    tp.add_argument("--modality", help="filter to digested/<modality>")
    tp.add_argument("--max-chars", type=int, default=8192)
    tr = tsub.add_parser("run", help="Run a fine-tune")
    tr.add_argument("--dataset", help="override dataset_path from config/training.json")
    tr.add_argument("--name", help="run name (defaults to a timestamp)")
    tr.add_argument("--dry-run", action="store_true", help="probe capability + validate config, don't train")
    te = tsub.add_parser("export", help="Merge adapter + convert to GGUF + `ollama create`")
    te.add_argument("run_dir")
    te.add_argument("tag", help="ollama model tag to create")
    tsub.add_parser("status", help="Show capability probe result")





def handle(args: argparse.Namespace) -> bool:
    """Return True if this module handled the command."""
    if args.command == "wiki":
        return _handle_wiki(args)
    if args.command == "skills":
        return _handle_skills(args)
    if args.command == "bin":
        return _handle_bin(args)
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
        from reins.harness.mcp_security import McpHttpConfigurationError
        from reins.harness.mcp_server import main as mcp_main

        try:
            mcp_main(
                http=args.http,
                host=args.host,
                port=args.port,
                allow_remote_http=args.allow_remote_http,
            )
        except McpHttpConfigurationError as error:
            raise SystemExit(f"// MCP HTTP configuration refused: {error}") from None
        return True
    if args.command == "combos":
        return _handle_combos(args)
    if args.command == "hardware":
        return _handle_hardware(args)
    if args.command == "coord":
        return _handle_coord(args)
    if args.command == "dataset":
        return _handle_dataset(args)
    if args.command == "train":
        return _handle_train(args)
    return False


def _handle_coord(args: argparse.Namespace) -> bool:
    from reins.harness.coordinator import get_coordinator

    sub = getattr(args, "subcmd", None)
    coord = get_coordinator()

    if sub == "load":
        slot = coord.load(args.model)
        print(f"// load {args.model}: {slot.state.value}" + (f" ({slot.error})" if slot.error else ""))
        return True
    if sub == "unload":
        slot = coord.unload(args.model)
        print(f"// unload {args.model}: {slot.state.value}")
        return True
    if sub == "serve":
        from reins.harness.ipc import IPCServer
        import signal

        server = IPCServer()
        signal.signal(signal.SIGTERM, lambda *_: server.stop())
        signal.signal(signal.SIGINT, lambda *_: server.stop())
        print(f"// IPC server listening on {server.socket_path}")
        server.serve_forever()
        return True

    # default / status
    st = coord.status()
    print(f"// coordinator: {st['used_gb']}/{st['vram_budget_gb']}GB")
    for name, info in st["slots"].items():
        line = f"  {name:30s} {info['state']:10s} {info['est_gb']}GB"
        if info["error"]:
            line += f"  ({info['error']})"
        print(line)
    return True


def _handle_dataset(args: argparse.Namespace) -> bool:
    from reins.harness.dataset import export_jsonl

    sub = getattr(args, "subcmd", None)
    if sub != "export":
        print("usage: reins dataset export <out.jsonl> [--modality M] [--category C] [--kind completion|memories]")
        return True

    stats = export_jsonl(
        args.out, categories=args.category, modality=args.modality,
        kind=args.kind, min_chars=args.min_chars, max_chars=args.max_chars, limit=args.limit,
    )
    print(f"// exported {stats.written} record(s) -> {stats.out_path} ({stats.skipped} skipped)")
    return True


def _handle_train(args: argparse.Namespace) -> bool:
    from reins.training.capability import probe

    sub = getattr(args, "subcmd", None)

    if sub == "prepare":
        from reins.harness.dataset import export_jsonl

        stats = export_jsonl(
            args.out,
            modality=getattr(args, "modality", None),
            max_chars=args.max_chars,
        )
        print(f"// exported {stats.written} record(s) -> {stats.out_path} ({stats.skipped} skipped)")
        return True

    if sub == "run":
        from reins.training.qlora import run_finetune

        backend = probe()
        if args.dry_run:
            from reins.training.config import load_training_config
            from reins.training.records import validate_jsonl

            overrides = {"dataset_path": args.dataset} if args.dataset else None
            settings = load_training_config(overrides)
            dataset_path = Path(settings.dataset_path).expanduser()
            try:
                records = validate_jsonl(dataset_path)
                dataset_status = f"dataset={dataset_path} records={records} valid"
            except (OSError, ValueError) as error:
                dataset_status = f"dataset invalid: {error}"
            print(
                f"// capability probe: mode={backend.mode} device={backend.device} "
                f"base={backend.base_model_key} - {backend.reason}; {dataset_status}"
            )
            return True
        config = {"dataset_path": args.dataset} if args.dataset else None
        result = run_finetune(config, run_name=args.name)
        if result.ok:
            print(f"// training run '{result.run_dir}' complete ({result.backend}, {result.steps} steps)")
        else:
            print(f"// training run failed ({result.backend}): {result.error}")
        return True

    if sub == "export":
        from reins.training.export import to_ollama

        ok = to_ollama(args.run_dir, args.tag)
        print(f"// export {'succeeded' if ok else 'needs manual steps (see above)'} -> tag '{args.tag}'")
        return True

    # default / "status"
    backend = probe()
    print(f"// capability: mode={backend.mode} device={backend.device} "
          f"base={backend.base_model_key} - {backend.reason}")
    return True


def _handle_hardware(args: argparse.Namespace) -> bool:
    from reins.services.sys_profiler import SysProfiler

    sub = getattr(args, "subcmd", None)
    sp = SysProfiler()
    if sub == "gaps":
        report = sp.gap_report()
        sp.write_gap_manifest(report)
        print(f"// model-gap report -> {paths.model_gaps_manifest()}")
        print(f"   budget: {report['hardware']['vram_gb']}GB VRAM, "
              f"{report['hardware']['free_disk_gb']}GB free disk")
        print(f"   ready to install: {', '.join(c['model'] for c in report['ready']) or '(none)'}")
        return True
    # default / "scan"
    _ = sp.profile_cluster(publish=False)
    print(f"// hardware scan -> {paths.hardware_manifest()}")
    return True


def _read_text_arg(value: str | None) -> str:
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
            print("// local model plane")
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
        if item.skipped:
            print(f"  [skip] unchanged  <- {item.path}")
        elif item.ok:
            print(f"  [ok ] {item.node}: {item.slug} (+{item.facts} facts)  <- {item.path}")
        else:
            print(f"  [ERR] {item.path}: {item.error}")

    results = digest.digest_path(
        str(p), recursive=args.recursive, enrich=not args.no_enrich,
        on_result=_emit, log_trail=not args.no_trail, force=args.force,
    )
    ok = sum(1 for r in results if r.ok and not r.skipped)
    skipped = sum(1 for r in results if r.skipped)
    print(f"// digested {ok}/{len(results)} file(s) into the wiki ({skipped} unchanged, skipped)")
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
            svc._notify_unhealthy_backup(rep)
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
        from get_secrets import get_secret, set_secret, list_secrets, delete_secret  # type: ignore
        
        sub = getattr(args, "subcmd", "get")
        if not sub and hasattr(args, "key"):
            sub = "get"
            
        if sub == "get":
            val = get_secret(args.key)
            if val:
                print(val)
            else:
                print(f"// no such secret: {args.key}", file=_sys.stderr)
        elif sub == "set":
            set_secret(args.key, args.value)
            print(f"// set {args.key}")
        elif sub == "list":
            keys = list_secrets()
            print("// vault keys:")
            for k in keys:
                print(f"  {k}")
        elif sub == "rm":
            if delete_secret(args.key):
                print(f"// removed {args.key}")
            else:
                print(f"// no such secret: {args.key}", file=_sys.stderr)
        else:
            print("usage: reins secret {get|set|list|rm} ...")
    except Exception as e:
        log_degradation(__name__)
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
    from reins.harness.skill_registry import SkillRegistryError, canonical_skill_names

    sub = getattr(args, "subcmd", None)
    root = _skills_dir()

    if sub == "install":
        script = paths.home() / "scripts" / "install_skills.sh"
        try:
            result = external_io.run(["bash", str(script)], check=False)
        except OSError as error:
            print(f"// skill install failed: {type(error).__name__}", file=sys.stderr)
            return False
        if result.returncode != 0:
            print(f"// skill install failed: exit {result.returncode}", file=sys.stderr)
            return False
        return True

    try:
        names = canonical_skill_names(root)
    except (OSError, SkillRegistryError) as error:
        print(f"// skill registry failed: {type(error).__name__}", file=sys.stderr)
        return False
    print(f"// canonical harness skills -> {root}")
    for name in names:
        print(f"  {name}")
    return True


def _handle_bin(args: argparse.Namespace) -> bool:
    sub = getattr(args, "subcmd", None)
    bin_dir = Path("~/.local/bin").expanduser()

    if sub == "install":
        script = paths.home() / "scripts" / "install_bin.sh"
        external_io.run(["bash", str(script)], check=False)
        return True

    # default / list - anything in ~/.local/bin that symlinks/points into this repo
    print(f"// harness commands -> {bin_dir}")
    if not bin_dir.is_dir():
        return True
    home = str(paths.home())
    for entry in sorted(bin_dir.iterdir()):
        try:
            target = str(entry.resolve()) if entry.is_symlink() else ""
            text = entry.read_text(encoding="utf-8", errors="replace") if entry.is_file() and not entry.is_symlink() else ""
        except Exception:
            log_degradation(__name__)
            target = text = ""
        if home in target or home in text:
            print(f"  {entry.name}")
    return True


def _handle_wiki(args: argparse.Namespace) -> bool:
    sub = getattr(args, "subcmd", None)

    if sub == "consolidate":
        script = paths.home() / "scripts" / "consolidate_wiki.py"
        external_io.run([sys.executable, str(script)], check=False)
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

def _handle_combos(args: argparse.Namespace) -> bool:
    from reins.harness.combo_registry import ComboRegistry
    from reins.harness.model_types import Combo
    import time

    sub = getattr(args, "subcmd", "list")
    registry = ComboRegistry()

    if sub == "list":
        print("// combos:")
        print(f"  {'ID':<20} | {'Provider':<12} | {'Model':<30} | {'Tier':<6} | {'Secret Key':<15} | Base URL")
        print("  " + "-"*110)
        for c in registry.all_combos():
            print(f"  {c.id:<20} | {c.provider:<12} | {c.model:<30} | {c.tier:<6} | {c.secret_key:<15} | {c.base_url}")
        return True

    if sub == "add":
        combo = Combo(
            id=args.id,
            provider=args.provider,
            model=args.model,
            secret_key=args.secret_key,
            base_url=args.base_url,
            tier=args.tier,
        )
        registry.add_combo(combo)
        print(f"// added combo: {args.id}")
        return True

    if sub == "rm":
        if registry.remove_combo(args.id):
            print(f"// removed combo: {args.id}")
        else:
            print(f"// combo not found: {args.id}")
        return True

    if sub == "test":
        combo = registry.get_combo(args.id)
        if not combo:
            print(f"// combo not found: {args.id}")
            return True
            
        from reins.harness.models import ModelRouter
        router = ModelRouter()
        
        print(f"// testing combo {args.id} ({combo.provider}/{combo.model}) ...")
        t0 = time.time()
        spec = registry.combo_to_spec(combo)
        text, err = router._dispatch(combo.provider, combo.model, "Say 'Hello, World!' in exactly two words.", "amdy", spec)
        t1 = time.time()
        
        if not err and text:
            print(f"// success! ({t1-t0:.2f}s)")
            print(f"   response: {text.strip()}")
        else:
            print(f"// failure! ({t1-t0:.2f}s)")
            print(f"   error: {err}")
        return True

    return False

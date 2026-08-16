from reins.services.logger import log_degradation
import argparse
import json
import os
import subprocess
import time
from reins.services.task_trail import TaskTrail
from reins.harness import external_io


def list_models():
    from reins.harness import paths

    registry_path = str(paths.model_registry())
    if not os.path.exists(registry_path):
        print("Model registry not found. Run `getinfo` (sys_profiler) first.")
        return

    try:
        with open(registry_path, "r") as f:
            data = json.load(f)
        for node, label in (("amdy", "AMDY Local Models"), ("tell", "TELL Remote Models")):
            print(f"--- {label} ---")
            node_data = data.get(node, {})
            # New getinfo format: models_fit=[{model,size_gb,score}]; tolerate legacy `models`.
            for m in node_data.get("models_fit") or node_data.get("models") or []:
                size = f", {m['size_gb']}GB" if "size_gb" in m else ""
                print(f" - {m['model']} (score {m.get('score', '?')}{size})")
    except Exception as e:
        log_degradation(__name__)
        print(f"Error reading registry: {e}")


def add_model(name: str):
    print(f"Pulling {name} via Ollama...")
    external_io.run(["ollama", "pull", name])
    print(f"Model {name} installed successfully.")


def rm_model(name: str):
    print(f"Removing {name} from local node...")
    external_io.run(["ollama", "rm", name])
    print(f"Model {name} deleted.")


def train_model(name: str):
    # The MoE trainer bridge is not implemented. Be honest instead of claiming
    # a fake success — training data is staged under moe_training/ for a future
    # bridge, but no training loop runs here yet.
    print(f"// `models train {name}` is not implemented (no MoE trainer bridge yet).")
    print(
        "// Training corpus is staged under moe_training/; wire a real trainer before using this."
    )


def list_trail():
    trail = TaskTrail()
    tasks = trail.all_tasks()
    if not tasks:
        print("Task trail is empty.")
        return

    print(f"--- Task Trail ({len(tasks)} tasks) ---")
    for t in tasks[-10:]:  # Show last 10
        print(
            f"[{t['status'].upper()}] Task: {t['task_type']} | Node: {t['target_node']} | ID: {t['task_id']}"
        )


def clear_trail():
    trail = TaskTrail()
    trail.clear()
    print("Task trail cleared successfully.")


def record_plan_cmd(task_type: str, title: str) -> str:
    """reins trail plan <type> "<title>" — open a durable plan record."""
    from reins.services.trail_recorder import TrailRecorder

    task_id = TrailRecorder().record_plan(
        task_id=f"plan-{task_type}-{int(time.time())}",
        task_type=f"plan:{task_type}",
        prompt=title,
    )
    print(f"Plan recorded: {task_id}")
    return task_id


def record_step_cmd(
    plan_id: str,
    summary: str,
    status: str = "success",
    commits: list[str] | None = None,
    files: list[str] | None = None,
) -> None:
    """reins trail step <plan_id> "<summary>" — append an executed step."""
    from reins.services.trail_recorder import TrailRecorder

    TrailRecorder().append_step(
        plan_id,
        summary,
        status=status,
        commits=commits,
        files=files,
    )
    print(f"Step recorded on {plan_id}: {summary}")


def finish_plan_cmd(plan_id: str) -> None:
    """reins trail finish <plan_id> — mark a plan complete."""
    from reins.services.trail_recorder import TrailRecorder

    TrailRecorder().finish_plan(plan_id)
    print(f"Plan finished: {plan_id}")


def sync_trail():
    from reins.services.agy_bridge import AGYBridge

    print("Syncing AGY internal checklists into the Hermes Universal Trail...")
    bridge = AGYBridge()
    bridge.scan_and_sync()
    print("Sync complete.")


def _port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    try:
        with external_io.socket_connect(host, port, timeout=timeout):
            return True
    except (ConnectionError, OSError):
        return False


def _ensure_reins_mcp_http(port: int = 8765) -> bool:
    """The Odysseus dashboard (running in Docker) reaches the harness over
    streamable-HTTP MCP, not stdio - ensure that server is up before bringing
    Odysseus's containers up. Detached, idempotent, never raises."""
    if os.environ.get("DATA_REIN_MCP_HTTP_MANAGED") == "1":
        return _port_open("127.0.0.1", port)
    if _port_open("127.0.0.1", port):
        return True
    print(f"Starting reins mcp --http on port {port}...")
    try:
        external_io.popen(
            ["reins", "mcp", "--http", "--port", str(port)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except FileNotFoundError:
        print("Warning: `reins` not found on PATH; run `reins bin install` first.")
        return False

    return True


def _ensure_comfyui(port: int = 8188) -> bool:
    """Best-effort: start ComfyUI if it's not already serving. Its own Python
    environment (torch/ROCm) is a separate manual setup step this does not
    perform - degrades to a warning, never blocks `ody start`."""
    import os

    if _port_open("127.0.0.1", port):
        return True
    comfy_dir = "/home/amdy/data_rein/ComfyUI"
    if not os.path.isdir(comfy_dir):
        return False
    print(f"Starting ComfyUI on port {port}...")
    try:
        external_io.popen(
            ["python3", "main.py", "--port", str(port)],
            cwd=comfy_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except FileNotFoundError:
        return False

    return True


def main() -> None:
    try:
        from reins.services.harness_bootstrapper import HarnessBootstrapper

        bootstrapper = HarnessBootstrapper()
        bootstrapper.bootstrap()
    except Exception as e:
        log_degradation(__name__)
        print(f"Warning: Failed to bootstrap harness state: {e}")

    parser = argparse.ArgumentParser(description="Sovereign AI Data Harness CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Models commands
    models_parser = subparsers.add_parser("models", help="Manage models")
    models_sub = models_parser.add_subparsers(dest="subcmd")
    models_sub.add_parser("list", help="List models")
    add_parser = models_sub.add_parser("add", help="Add a model")
    add_parser.add_argument("name", help="Model name")
    rm_parser = models_sub.add_parser("rm", help="Remove a model")
    rm_parser.add_argument("name", help="Model name")
    train_parser = models_sub.add_parser("train", help="Train a model")
    train_parser.add_argument("name", help="Model name")

    # Trail commands
    trail_parser = subparsers.add_parser("trail", help="Manage task trail")
    trail_sub = trail_parser.add_subparsers(dest="subcmd")
    trail_sub.add_parser("list", help="List trail tasks")
    trail_sub.add_parser("clear", help="Clear trail")
    trail_sub.add_parser("sync", help="Sync AGY tasks into Hermes trail")
    plan_p = trail_sub.add_parser("plan", help="Record a plan (opens a durable plan entry)")
    plan_p.add_argument("task_type", help="plan category, e.g. production-readiness")
    plan_p.add_argument("title", help="short plan/title line")
    step_p = trail_sub.add_parser("step", help="Append an executed step to a plan")
    step_p.add_argument("plan_id", help="plan task id returned by `reins trail plan`")
    step_p.add_argument("summary", help="what was executed")
    step_p.add_argument("--status", default="success", help="success|failed|running")
    step_p.add_argument("--commit", action="append", default=[], help="commit sha (repeatable)")
    step_p.add_argument("--file", action="append", default=[], help="file path changed (repeatable)")
    finish_p = trail_sub.add_parser("finish", help="Mark a plan complete")
    finish_p.add_argument("plan_id", help="plan task id")
    queue_parser = trail_sub.add_parser("queue", help="Queue a chunked task for local-model pickup")
    queue_parser.add_argument("goal", help="task goal/prompt")
    queue_parser.add_argument("--type", dest="task_type", default="generic")
    queue_parser.add_argument(
        "--context", action="append", default=[], help="context file path (repeatable)"
    )
    queue_parser.add_argument("--node", default="amdy")
    queue_parser.add_argument(
        "--model",
        default=None,
        help="local model name to size chunks for (default qwen2.5-coder:7b)",
    )
    pickup_parser = trail_sub.add_parser(
        "pickup", help="Execute one chunk of the oldest queued task"
    )
    pickup_parser.add_argument("--category", default="coding: menial")
    pickup_parser.add_argument("--node", default="amdy")

    # Odysseus commands
    ody_parser = subparsers.add_parser("ody", help="Manage Odysseus AI daemon")
    ody_sub = ody_parser.add_subparsers(dest="subcmd")
    ody_sub.add_parser("start", help="Start Odysseus AI daemon")

    # Universal harness commands (wiki / directive / paths)
    try:
        from reins.harness import cli as harness_cli

        harness_cli.register(subparsers)
    except Exception as e:
        log_degradation(__name__)
        print(f"Warning: harness verbs unavailable: {e}")
        harness_cli = None

    args = parser.parse_args()

    _harness_cmds = (
        "wiki",
        "skills",
        "bin",
        "directive",
        "paths",
        "local",
        "run",
        "batch",
        "ask",
        "summarize",
        "classify",
        "optimize",
        "digest",
        "backup",
        "secret",
        "mcp",
        "tokens",
        "hardware",
        "coord",
        "dataset",
        "train",
        "combos",
    )
    if harness_cli is not None and args.command in _harness_cmds:
        if harness_cli.handle(args):
            return

    if args.command == "models":
        if args.subcmd == "list":
            list_models()
        elif args.subcmd == "add":
            add_model(args.name)
        elif args.subcmd == "rm":
            rm_model(args.name)
        elif args.subcmd == "train":
            train_model(args.name)
        else:
            models_parser.print_help()
    elif args.command == "trail":
        if args.subcmd == "list":
            list_trail()
        elif args.subcmd == "clear":
            clear_trail()
        elif args.subcmd == "sync":
            sync_trail()
        elif args.subcmd == "queue":
            from reins.harness.handoff import queue_chunked_task

            context_blocks = []
            for p in args.context:
                try:
                    with open(p, encoding="utf-8") as f:
                        context_blocks.append(f.read())
                except Exception as e:
                    log_degradation(__name__)
                    print(f"Warning: could not read context file {p}: {e}")
            task_id = queue_chunked_task(
                args.task_type, args.goal, context_blocks, node=args.node, model=args.model
            )
            print(f"Queued task {task_id}" if task_id else "Failed to queue task (see logs).")
        elif args.subcmd == "pickup":
            from reins.harness.handoff import pickup_next

            result = pickup_next(category=args.category, node=args.node)
            if result is None:
                print("No queued chunked tasks for this node.")
            else:
                print(json.dumps(result, indent=2))
        elif args.subcmd == "plan":
            recorded_id = record_plan_cmd(args.task_type, args.title)
            print(f"Plan task id: {recorded_id}")
        elif args.subcmd == "step":
            record_step_cmd(
                args.plan_id,
                args.summary,
                status=args.status,
                commits=args.commit or None,
                files=args.file or None,
            )
        elif args.subcmd == "finish":
            finish_plan_cmd(args.plan_id)
        else:
            trail_parser.print_help()
    elif args.command == "ody":
        if args.subcmd == "start":
            # Fix docker volume mount issue where settings.yml is created as a root-owned dir
            try:
                import os

                ody_dir = "/home/amdy/data_rein/odysseus"
                bad_dir = "/home/amdy/data_rein/odysseus/config/searxng/settings.yml"

                # Take back ownership of the entire odysseus directory from root
                external_io.run(
                    ["sudo", "chown", "-R", f"{os.getuid()}:{os.getgid()}", ody_dir], check=True
                )

                if os.path.isdir(bad_dir):
                    print("Repairing root-owned settings.yml directory...")
                    external_io.run(["sudo", "rm", "-rf", bad_dir], check=True)
                    with open(bad_dir, "w", encoding="utf-8") as f:
                        f.write("# Auto-generated to fix Docker mount\n")
                    print("Repair successful.")
            except Exception as e:
                log_degradation(__name__)
                print(f"Warning: Failed to auto-repair settings.yml: {e}")

            # The Odysseus dashboard reaches the harness over HTTP-MCP (it's in
            # Docker, no stdio pipe to share) and can render generated images
            # via ComfyUI - ensure both are up before the containers start.
            _ensure_reins_mcp_http()
            _ensure_comfyui()

            # Attempt to start the actual docker containers if they exist
            try:
                print("Starting Odysseus AI and Broker containers via docker compose...")
                external_io.run(
                    ["docker", "compose", "up", "-d"],
                    cwd="/home/amdy/data_rein/DATA/kad-1.0/broker",
                    check=True,
                )
                external_io.run(
                    ["docker", "compose", "up", "-d", "--build"],
                    cwd="/home/amdy/data_rein/odysseus",
                    check=True,
                )
                print("Graphical interface should now be available on localhost!")
            except Exception as e:
                log_degradation(__name__)
                print(f"Warning: Failed to start docker containers: {e}")

            # Start the fallback agent daemon
            from reins.services.fallback_agent import OdysseusAgent

            agent = OdysseusAgent()
            agent.run_daemon()
        else:
            ody_parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

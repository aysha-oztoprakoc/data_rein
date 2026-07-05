import argparse
import json
import os
import subprocess
from reins.services.task_trail import TaskTrail

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
        print(f"Error reading registry: {e}")

def add_model(name: str):
    print(f"Pulling {name} via Ollama...")
    subprocess.run(["ollama", "pull", name])
    print(f"Model {name} installed successfully.")

def rm_model(name: str):
    print(f"Removing {name} from local node...")
    subprocess.run(["ollama", "rm", name])
    print(f"Model {name} deleted.")

def train_model(name: str):
    # The MoE trainer bridge is not implemented. Be honest instead of claiming
    # a fake success — training data is staged under moe_training/ for a future
    # bridge, but no training loop runs here yet.
    print(f"// `models train {name}` is not implemented (no MoE trainer bridge yet).")
    print("// Training corpus is staged under moe_training/; wire a real trainer before using this.")

def list_trail():
    trail = TaskTrail()
    tasks = trail.all_tasks()
    if not tasks:
        print("Task trail is empty.")
        return
        
    print(f"--- Task Trail ({len(tasks)} tasks) ---")
    for t in tasks[-10:]: # Show last 10
        print(f"[{t['status'].upper()}] Task: {t['task_type']} | Node: {t['target_node']} | ID: {t['task_id']}")
        
def clear_trail():
    trail = TaskTrail()
    trail.clear()
    print("Task trail cleared successfully.")

def sync_trail():
    from reins.services.agy_bridge import AGYBridge
    print("Syncing AGY internal checklists into the Hermes Universal Trail...")
    bridge = AGYBridge()
    bridge.scan_and_sync()
    print("Sync complete.")

def main() -> None:
    try:
        from reins.services.harness_bootstrapper import HarnessBootstrapper
        bootstrapper = HarnessBootstrapper()
        bootstrapper.bootstrap()
    except Exception as e:
        print(f"Warning: Failed to bootstrap harness state: {e}")

    parser = argparse.ArgumentParser(description='Sovereign AI Data Harness CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Models commands
    models_parser = subparsers.add_parser('models', help='Manage models')
    models_sub = models_parser.add_subparsers(dest='subcmd')
    models_sub.add_parser('list', help='List models')
    add_parser = models_sub.add_parser('add', help='Add a model')
    add_parser.add_argument('name', help='Model name')
    rm_parser = models_sub.add_parser('rm', help='Remove a model')
    rm_parser.add_argument('name', help='Model name')
    train_parser = models_sub.add_parser('train', help='Train a model')
    train_parser.add_argument('name', help='Model name')

    # Trail commands
    trail_parser = subparsers.add_parser('trail', help='Manage task trail')
    trail_sub = trail_parser.add_subparsers(dest='subcmd')
    trail_sub.add_parser('list', help='List trail tasks')
    trail_sub.add_parser('clear', help='Clear trail')
    trail_sub.add_parser('sync', help='Sync AGY tasks into Hermes trail')

    # Odysseus commands
    ody_parser = subparsers.add_parser('ody', help='Manage Odysseus AI daemon')
    ody_sub = ody_parser.add_subparsers(dest='subcmd')
    ody_sub.add_parser('start', help='Start Odysseus AI daemon')

    # Universal harness commands (wiki / directive / paths)
    try:
        from reins.harness import cli as harness_cli
        harness_cli.register(subparsers)
    except Exception as e:
        print(f"Warning: harness verbs unavailable: {e}")
        harness_cli = None

    args = parser.parse_args()

    _harness_cmds = ('wiki', 'skills', 'directive', 'paths', 'local', 'run',
                     'batch', 'ask', 'summarize', 'classify', 'optimize', 'digest',
                     'backup', 'secret', 'mcp', 'tokens')
    if harness_cli is not None and args.command in _harness_cmds:
        if harness_cli.handle(args):
            return

    if args.command == 'models':
        if args.subcmd == 'list':
            list_models()
        elif args.subcmd == 'add':
            add_model(args.name)
        elif args.subcmd == 'rm':
            rm_model(args.name)
        elif args.subcmd == 'train':
            train_model(args.name)
        else:
            models_parser.print_help()
    elif args.command == 'trail':
        if args.subcmd == 'list':
            list_trail()
        elif args.subcmd == 'clear':
            clear_trail()
        elif args.subcmd == 'sync':
            sync_trail()
        else:
            trail_parser.print_help()
    elif args.command == 'ody':
        if args.subcmd == 'start':
            # Fix docker volume mount issue where settings.yml is created as a root-owned dir
            try:
                import os
                import subprocess
                ody_dir = "/home/amdy/data_rein/odysseus"
                bad_dir = "/home/amdy/data_rein/odysseus/config/searxng/settings.yml"
                
                # Take back ownership of the entire odysseus directory from root
                subprocess.run(["sudo", "chown", "-R", f"{os.getuid()}:{os.getgid()}", ody_dir], check=True)
                
                if os.path.isdir(bad_dir):
                    print("Repairing root-owned settings.yml directory...")
                    subprocess.run(["sudo", "rm", "-rf", bad_dir], check=True)
                    with open(bad_dir, "w", encoding="utf-8") as f:
                        f.write("# Auto-generated to fix Docker mount\n")
                    print("Repair successful.")
            except Exception as e:
                print(f"Warning: Failed to auto-repair settings.yml: {e}")

            # Attempt to start the actual docker containers if they exist
            try:
                print("Starting Odysseus AI and Broker containers via docker compose...")
                subprocess.run(["docker", "compose", "up", "-d"], cwd="/home/amdy/data_rein/DATA/kad-1.0/broker", check=True)
                subprocess.run(["docker", "compose", "up", "-d", "--build"], cwd="/home/amdy/data_rein/odysseus", check=True)
                print("Graphical interface should now be available on localhost!")
            except Exception as e:
                print(f"Warning: Failed to start docker containers: {e}")
            
            # Start the fallback agent daemon
            from reins.services.fallback_agent import OdysseusAgent
            agent = OdysseusAgent()
            agent.run_daemon()
        else:
            ody_parser.print_help()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

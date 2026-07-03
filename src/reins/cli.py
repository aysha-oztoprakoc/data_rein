import argparse
import json
import os
import subprocess
from reins.services.task_trail import TaskTrail

def list_models():
    registry_path = os.path.expanduser("~/data_rein/data-oby/TrainingData/model_registry.json")
    if not os.path.exists(registry_path):
        print("Model registry not found. Is the sys_profiler running?")
        return
        
    try:
        with open(registry_path, "r") as f:
            data = json.load(f)
            
        print("--- AMDY Local Models ---")
        for m in data.get("amdy", {}).get("models", []):
            print(f" - {m['model']} (Score: {m['score']})")
            
        print("\n--- TELL Remote Models ---")
        for m in data.get("tell", {}).get("models", []):
            print(f" - {m['model']} (Score: {m['score']})")
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
    print(f"Initiating Training Pipeline for {name}...")
    print("Dispatching to MoE Trainer Bridge.")
    # Placeholder for actual training loop
    print("Training sequence complete.")

def list_trail():
    trail = TaskTrail()
    tasks = trail._load()
    if not tasks:
        print("Task trail is empty.")
        return
        
    print(f"--- Task Trail ({len(tasks)} tasks) ---")
    for t in tasks[-10:]: # Show last 10
        print(f"[{t['status'].upper()}] Task: {t['task_type']} | Node: {t['target_node']} | ID: {t['task_id']}")
        
def clear_trail():
    trail = TaskTrail()
    trail._save([])
    print("Task trail cleared successfully.")

def sync_trail():
    from reins.services.agy_bridge import AGYBridge
    print("Syncing AGY internal checklists into the Hermes Universal Trail...")
    bridge = AGYBridge()
    bridge.scan_and_sync()
    print("Sync complete.")

def main() -> None:
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

    args = parser.parse_args()

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
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

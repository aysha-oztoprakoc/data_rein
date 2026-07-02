import os
import subprocess
import threading
import json
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_rein/backup/trigger"
RESULT_TOPIC = "data_rein/backup/result"
CONFIG_PATH = os.path.expanduser("~/data_rein/config/backup_config.json")

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def find_git_repos(base_paths, max_depth=4):
    repos = []
    for base in base_paths:
        base = os.path.expanduser(base)
        if not os.path.exists(base):
            continue
        for root, dirs, files in os.walk(base):
            depth = root[len(base):].count(os.sep)
            if depth >= max_depth:
                dirs[:] = []
                continue
            if '.git' in dirs:
                repos.append(root)
                dirs.remove('.git')
    return repos

def safe_git_commit(repo):
    repo_name = os.path.basename(repo)
    # 1. Check for merge conflict state
    if os.path.exists(os.path.join(repo, ".git", "MERGE_HEAD")) or \
       os.path.exists(os.path.join(repo, ".git", "CHERRY_PICK_HEAD")):
        return False, f"{repo_name} Git: Aborted due to active merge/conflict state."
    
    # 2. Check for actual changes
    res_status = subprocess.run(["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True)
    if not res_status.stdout.strip():
        # No changes to commit, but we should still try to push if ahead
        res_remote = subprocess.run(["git", "remote"], cwd=repo, capture_output=True, text=True)
        if "origin" in res_remote.stdout:
             subprocess.run(["git", "push", "origin", "HEAD"], cwd=repo, capture_output=True)
        return True, None
        
    # 3. Commit and push
    try:
        res_branch = subprocess.run(["git", "symbolic-ref", "-q", "HEAD"], cwd=repo, capture_output=True)
        if res_branch.returncode == 0:
            subprocess.run(["git", "add", "."], cwd=repo)
            commit_msg = f"Auto-backup bak-1.2 {int(time.time())}"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=repo, capture_output=True)
            
            res_remote = subprocess.run(["git", "remote"], cwd=repo, capture_output=True, text=True)
            if "origin" in res_remote.stdout:
                subprocess.run(["git", "push", "origin", "HEAD"], cwd=repo, capture_output=True)
        return True, None
    except Exception as e:
        return False, f"{repo_name} Git: {str(e)}"

def rsync_to_location_with_retry(client, name, src, dest_config, repo_name):
    max_retries = 3
    base_delay = 2
    
    is_remote = dest_config["type"] == "remote"
    dest_path_template = dest_config["path"]
    
    # Expand templates
    dest_path = dest_path_template.format(repo_name=repo_name)
    if is_remote:
        dest_full = f"{dest_config['host']}:{dest_path}"
    else:
        dest_full = os.path.expanduser(dest_path)
    
    for attempt in range(1, max_retries + 1):
        client.publish(RESULT_TOPIC, json.dumps({"event": "rsync_start", "location": name, "attempt": attempt}))
        
        cmd = ["rsync", "-az", "--delete"]
        if is_remote:
            cmd.extend(["-e", "ssh -o BatchMode=yes"])
            # Ensure remote dir exists
            host = dest_config["host"]
            subprocess.run(["ssh", "-o", "BatchMode=yes", host, "mkdir", "-p", dest_path], capture_output=True)
        else:
            os.makedirs(dest_full, exist_ok=True)
        
        cmd.extend([f"{src}/", dest_full])
        res = subprocess.run(cmd, capture_output=True)
        
        if res.returncode == 0:
            client.publish(RESULT_TOPIC, json.dumps({"event": "rsync_success", "location": name}))
            return True, None
            
        if attempt < max_retries:
            time.sleep(base_delay ** attempt)
            
    client.publish(RESULT_TOPIC, json.dumps({"event": "rsync_error", "location": name, "error": res.stderr.decode()}))
    return False, f"Rsync {name} failed after {max_retries} attempts."

def run_backup(client):
    report = {"errors": [], "success": 0}
    client.publish(RESULT_TOPIC, json.dumps({"event": "start", "message": "Initiating bak-1.2 Discovery Protocol..."}))
    
    try:
        config = load_config()
    except Exception as e:
        report["errors"].append(f"Config load error: {str(e)}")
        client.publish(RESULT_TOPIC, json.dumps({"event": "finish", "report": report}))
        return
        
    base_paths = config.get("base_paths", [])
    destinations = config.get("destinations", [])
    
    repos = find_git_repos(base_paths)
    client.publish(RESULT_TOPIC, json.dumps({"event": "discovery", "repos": len(repos), "message": f"Found {len(repos)} Repositories."}))
    
    # Run Git commits sequentially to avoid local disk thrashing
    for repo in repos:
        success, error = safe_git_commit(repo)
        if not success:
            report["errors"].append(error)
            
    # Run Rsyncs concurrently
    rsync_tasks = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for repo in repos:
            repo_name = os.path.basename(repo)
            for dest in destinations:
                task_name = f"{repo_name}_{dest['id']}"
                future = executor.submit(rsync_to_location_with_retry, client, task_name, repo, dest, repo_name)
                rsync_tasks.append(future)
                
        for future in as_completed(rsync_tasks):
            success, error = future.result()
            if success:
                report["success"] += 1
            else:
                report["errors"].append(error)

    client.publish(RESULT_TOPIC, json.dumps({"event": "finish", "report": report}))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)

def on_message(client, userdata, msg):
    if msg.topic == TRIGGER_TOPIC:
        threading.Thread(target=run_backup, args=(client,), daemon=True).start()

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="backup_service_bak_1_2")
    else:
        client = mqtt.Client(client_id="backup_service_bak_1_2")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()

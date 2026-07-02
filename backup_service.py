import subprocess
import threading
import os
import json
import time

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_harness/backup/trigger"
RESULT_TOPIC = "data_harness/backup/result"

def run_backup(client):
    report = {
        "local_git": False,
        "tell_rsync": False,
        "github_push": False,
        "gdrive_rclone": False,
        "errors": []
    }
    
    data_harness_dir = os.path.expanduser("~/DATA/data_harness")
    rclone_bin = os.path.expanduser("~/.local/bin/rclone")
    
    try:
        # 1. Local Git Commit
        subprocess.run(["git", "add", "."], cwd=data_harness_dir)
        res_commit = subprocess.run(["git", "commit", "-m", "Automated backup"], cwd=data_harness_dir, capture_output=True)
        # return code 0 = success, 1 = nothing to commit. Both are fine.
        report["local_git"] = True

        # 2. Tell Backup (Rsync over SSH)
        res_ssh = subprocess.run(["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", "mkdir", "-p", "~/DATA/data_harness_backup"], capture_output=True)
        if res_ssh.returncode == 0:
            res_rsync = subprocess.run(["rsync", "-avz", "-e", "ssh -o BatchMode=yes", f"{data_harness_dir}/", "tell@192.168.0.2:~/DATA/data_harness_backup/"], capture_output=True)
            if res_rsync.returncode == 0:
                report["tell_rsync"] = True
            else:
                report["errors"].append(f"Rsync failed: {res_rsync.stderr.decode('utf-8', errors='ignore')}")
        else:
            report["errors"].append("SSH to tell failed")

        # 3. GitHub
        res_push = subprocess.run(["git", "push", "origin", "main"], cwd=data_harness_dir, capture_output=True)
        if res_push.returncode == 0:
            report["github_push"] = True
        else:
            # Might fail if no origin exists, but that's fine if the user hasn't set it up yet.
            report["errors"].append(f"Git push failed: {res_push.stderr.decode('utf-8', errors='ignore')}")
            
        # 4. Google Drive
        if os.path.exists(rclone_bin):
            res_rclone = subprocess.run([rclone_bin, "sync", data_harness_dir, "gdrive:backup/data_harness"], capture_output=True, timeout=300)
            if res_rclone.returncode == 0:
                report["gdrive_rclone"] = True
            else:
                report["errors"].append(f"Rclone failed: {res_rclone.stderr.decode('utf-8', errors='ignore')}")
        else:
            report["errors"].append("Rclone binary not found")
            
    except Exception as e:
        report["errors"].append(f"Exception: {str(e)}")
        
    client.publish(RESULT_TOPIC, json.dumps(report))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)

def on_message(client, userdata, msg):
    if msg.topic == TRIGGER_TOPIC:
        threading.Thread(target=run_backup, args=(client,), daemon=True).start()

def main():
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="backup_service")
    else:
        client = mqtt.Client(client_id="backup_service")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()

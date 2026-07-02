import subprocess
import threading
import os
try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_harness/backup/trigger"

def run_backup(client):
    try:
        data_harness_dir = os.path.expanduser("~/DATA/data_harness")
        
        # 1. Local Git Commit
        subprocess.run(["git", "add", "."], cwd=data_harness_dir)
        subprocess.run(["git", "commit", "-m", "Automated backup"], cwd=data_harness_dir)
        
        # 2. Tell Backup (Rsync over SSH)
        # Ensure backup dir exists on tell
        subprocess.run(["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", "mkdir", "-p", "~/DATA/data_harness_backup"])
        subprocess.run(["rsync", "-avz", "-e", "ssh -o BatchMode=yes", f"{data_harness_dir}/", "tell@192.168.0.2:~/DATA/data_harness_backup/"])
        
        # 3. GitHub
        # We push to origin main if configured
        subprocess.run(["git", "push", "origin", "main"], cwd=data_harness_dir)
        
        # 4. Google Drive
        # rclone is required for this step. If not configured, it will gracefully fail.
        subprocess.run(["rclone", "sync", data_harness_dir, "gdrive:backup/data_harness"], timeout=300)
        
    except Exception as e:
        print(f"Backup failed: {e}")

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

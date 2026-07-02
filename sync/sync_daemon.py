import os
import json
import subprocess
import threading
import queue
from pathlib import Path

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

from src.data_harness.services.logger import get_logger

logger = get_logger("sync_daemon")

SYNC_CHANGED_TOPIC = "data_rein/sync/changed"
SYNC_CONFIG_PATH = Path(__file__).parent / "sync_config.json"

def load_config():
    if SYNC_CONFIG_PATH.exists():
        with open(SYNC_CONFIG_PATH, "r") as f:
            return json.load(f)
    return {"mappings": [], "exclude": []}

def run_rsync(mapping, excludes):
    source = mapping["source"]
    dest = mapping["destination"]
    
    if not source.endswith('/'):
        source += '/'
        
    os.makedirs(dest, exist_ok=True)
    
    cmd = ["rsync", "-av", "--update"]
    for ex in excludes:
        cmd.extend(["--exclude", ex])
    cmd.extend([source, dest])
    
    res = subprocess.run(cmd, capture_output=True)
    if res.returncode == 0:
        logger.info(f"Rsync completed for {source} -> {dest}")
    else:
        logger.error(f"Rsync failed for {source}: {res.stderr.decode()}")

class Debouncer:
    def __init__(self, client, mapping, excludes, wait_time=3.0):
        self.client = client
        self.mapping = mapping
        self.excludes = excludes
        self.wait_time = wait_time
        self.timer = None
        self.pending_events = set()
        self.lock = threading.Lock()
        
    def add_event(self, changed_file):
        with self.lock:
            self.pending_events.add(changed_file)
            if self.timer is not None:
                self.timer.cancel()
            self.timer = threading.Timer(self.wait_time, self._execute)
            self.timer.daemon = True
            self.timer.start()
            
    def _execute(self):
        with self.lock:
            events_to_process = list(self.pending_events)
            self.pending_events.clear()
            self.timer = None
            
        if not events_to_process:
            return
            
        logger.info(f"Debounce triggered for {self.mapping['source']}. Processing {len(events_to_process)} events.")
        run_rsync(self.mapping, self.excludes)
        
        for changed_file in events_to_process:
            payload = {
                "source": self.mapping["source"],
                "destination": self.mapping["destination"],
                "changed_file": changed_file
            }
            self.client.publish(SYNC_CHANGED_TOPIC, json.dumps(payload))

def watch_directory(client, mapping, excludes):
    source = mapping["source"]
    if not os.path.exists(source):
        logger.warning(f"Watch skipped, source does not exist: {source}")
        return

    # Initial sync
    run_rsync(mapping, excludes)

    # Setup the debouncer
    debouncer = Debouncer(client, mapping, excludes)

    # Watch loop using inotifywait (blocking I/O, PON compliant)
    # The output of inotifywait is processed iteratively without active polling.
    cmd = [
        "inotifywait",
        "-m", "-r",
        "-e", "modify,create,delete,move",
        "--format", "%w%f"
    ]
    for ex in excludes:
        cmd.extend(["--exclude", ex.replace(".", "\\.").replace("*", ".*")])
    cmd.append(source)

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ''):
            changed_file = line.strip()
            if changed_file:
                # Add to debouncer
                debouncer.add_event(changed_file)
    except FileNotFoundError:
        logger.error("inotifywait not found. Please install inotify-tools.")

def main():
    config = load_config()
    
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="sync_daemon")
    else:
        client = mqtt.Client(client_id="sync_daemon")
        
    client.connect("localhost", 1883, 300)
    logger.info("Sync Daemon connected.")
    
    threads = []
    for mapping in config.get("mappings", []):
        t = threading.Thread(
            target=watch_directory, 
            args=(client, mapping, config.get("exclude", [])),
            daemon=True
        )
        t.start()
        threads.append(t)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down sync daemon...")
        client.disconnect()

if __name__ == "__main__":
    main()

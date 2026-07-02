import subprocess
import threading
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

class HealthCheckRunner:
    def __init__(self):
        self.backup_result = None
        self.result_event = threading.Event()
        
        if PAHO_V2:
            self.client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="health_check")
        else:
            self.client = mqtt.Client(client_id="health_check")
            
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc, *args):
        if rc == 0:
            client.subscribe(RESULT_TOPIC)

    def on_message(self, client, userdata, msg):
        if msg.topic == RESULT_TOPIC:
            try:
                self.backup_result = json.loads(msg.payload.decode())
            except:
                self.backup_result = {"errors": ["Failed to decode JSON"]}
            self.result_event.set()

    def check_local_disk(self):
        print("[*] Checking local disk (amdy)...")
        res = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
        if res.returncode == 0:
            print("  [OK] Local disk check passed.")
        else:
            print(f"  [ERROR] Local disk check failed: {res.stderr}")

    def check_remote_disk(self):
        print("[*] Checking remote disk (tell)...")
        res = subprocess.run(["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", "df", "-h", "/"], capture_output=True, text=True)
        if res.returncode == 0:
            print("  [OK] Remote disk check passed.")
        else:
            print(f"  [ERROR] Remote disk check failed: {res.stderr}")

    def trigger_and_wait_backup(self):
        print("[*] Triggering Backup Service over MQTT...")
        self.result_event.clear()
        self.backup_result = None
        self.client.publish(TRIGGER_TOPIC, "trigger")
        
        # Block and wait for the event (0% CPU, PON compliant)
        self.result_event.wait(timeout=600)
        
        if self.backup_result:
            print("  [OK] Backup Report Received:")
            print(json.dumps(self.backup_result, indent=2))
        else:
            print("  [ERROR] Backup timed out or failed to return report.")

    def run(self):
        self.client.connect("localhost", 1883, 300)
        self.client.loop_start()
        
        try:
            print("=== SYSTEM HEALTH CHECK START ===")
            self.check_local_disk()
            self.check_remote_disk()
            self.trigger_and_wait_backup()
            print("=== SYSTEM HEALTH CHECK END ===\n")
        finally:
            self.client.loop_stop()
            self.client.disconnect()

if __name__ == "__main__":
    import sys
    iterations = 1
    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
        
    runner = HealthCheckRunner()
    for i in range(iterations):
        print(f"--- LOOP {i+1} OF {iterations} ---")
        runner.run()

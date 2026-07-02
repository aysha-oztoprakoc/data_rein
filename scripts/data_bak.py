#!/usr/bin/env python3
import json
import sys
import time

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_rein/backup/trigger"
RESULT_TOPIC = "data_rein/backup/result"

# Cyberpunk Colors
NEON_CYAN = "\033[38;5;51m"
NEON_YELLOW = "\033[38;5;226m"
NEON_PINK = "\033[38;5;201m"
NEON_RED = "\033[38;5;196m"
RESET = "\033[0m"

def print_cp(color, tag, msg):
    print(f"[{color}{tag}{RESET}] {msg}")

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(RESULT_TOPIC)
        # Trigger the backup
        print_cp(NEON_CYAN, "SYS", "Initializing Data Harness Backup Protocol...")
        client.publish(TRIGGER_TOPIC, '{"action":"backup"}')

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        event = data.get("event")
        
        if event == "start":
            print_cp(NEON_YELLOW, "INIT", data.get("message", ""))
        elif event == "discovery":
            print_cp(NEON_PINK, "SCAN", data.get("message", ""))
        elif event == "repo_start":
            print_cp(NEON_CYAN, "REPO", f"Analyzing >> {data.get('repo')}")
        elif event == "repo_push":
            print_cp(NEON_YELLOW, "UPLD", f"Pushing {data.get('repo')} to secure origin...")
        elif event == "repo_success":
            print_cp(NEON_CYAN, "DONE", f"{data.get('repo')} secured. [{data.get('message')}]")
        elif event == "repo_warn":
            print_cp(NEON_RED, "WARN", f"{data.get('repo')} warning: {data.get('message')}")
        elif event == "repo_error":
            print_cp(NEON_RED, "ERR!", f"{data.get('repo')} failure: {data.get('message')}")
        elif event == "tell_sync":
            print_cp(NEON_PINK, "SYNC", data.get("message", ""))
        elif event == "tell_success":
            print_cp(NEON_CYAN, "DONE", data.get("message", ""))
        elif event == "tell_error":
            print_cp(NEON_RED, "ERR!", data.get("message", ""))
        elif event == "finish":
            rep = data.get("report", {})
            succ = rep.get('success', 0)
            errs = len(rep.get('errors', []))
            print_cp(NEON_YELLOW, "STAT", f"Protocol Complete. Secured: {succ} | Errors: {errs}")
            for err in rep.get('errors', []):
                print_cp(NEON_RED, "DUMP", err)
            client.disconnect()
    except Exception as e:
        print_cp(NEON_RED, "ERR!", f"UI Parser Fault: {str(e)}")

def main():
    print(f"\n{NEON_PINK}>> DATA HARNESS UPLINK V1.0 <<{RESET}")
    print(f"{NEON_CYAN}=================================={RESET}")
    
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="data_bak_ui")
    else:
        client = mqtt.Client(client_id="data_bak_ui")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 60)
        client.loop_forever()
    except KeyboardInterrupt:
        print_cp(NEON_RED, "ABRT", "User terminated protocol.")
        client.disconnect()
        
if __name__ == "__main__":
    main()

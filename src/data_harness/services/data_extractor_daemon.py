import json
import subprocess
import threading
import os
import shutil

try:
    from paho.mqtt.client import CallbackAPIVersion
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_rein/extract/trigger"
RESULT_TOPIC = "data_rein/extract/result"
TRAINING_DATA_DIR = os.path.expanduser("~/data_rein/training_data")

def extract_local(filepath, ext, out_path):
    """ Handle Text, MD, JSON, CSV, PDF, DOCX locally on AMDY """
    if ext in [".txt", ".md", ".json", ".csv"]:
        shutil.copy(filepath, out_path)
        return True, "Copied plain text format."
    elif ext == ".pdf":
        res = subprocess.run(["pdftotext", filepath, out_path], capture_output=True)
        if res.returncode == 0:
            return True, "Extracted PDF text."
        return False, f"pdftotext failed: {res.stderr.decode()}"
    elif ext == ".docx":
        res = subprocess.run(["docx2txt", filepath, out_path], capture_output=True)
        if res.returncode == 0:
            return True, "Extracted DOCX text."
        return False, f"docx2txt failed: {res.stderr.decode()}"
    return False, "Unsupported local format"

def extract_remote(filepath, ext, out_path):
    """ Handle PNG, JPG, MP3, WAV remotely on TELL via SSH BatchMode """
    filename = os.path.basename(filepath)
    remote_path = f"/tmp/{filename}"
    
    # 1. SCP file to tell
    scp_res = subprocess.run(["scp", "-o", "BatchMode=yes", filepath, f"tell@192.168.0.2:{remote_path}"], capture_output=True)
    if scp_res.returncode != 0:
        return False, f"SCP failed: {scp_res.stderr.decode()}"
        
    remote_cmd = ""
    if ext in [".png", ".jpg"]:
        remote_cmd = f"tesseract {remote_path} {remote_path}_out && cat {remote_path}_out.txt"
    elif ext in [".mp3", ".wav"]:
        # Stub for whisper CLI
        remote_cmd = f"whisper {remote_path} --output_format txt --output_dir /tmp && cat {remote_path}.txt"
        
    # 2. Run extraction on tell
    ssh_res = subprocess.run(["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", remote_cmd], capture_output=True)
    
    # Cleanup
    subprocess.run(["ssh", "-o", "BatchMode=yes", "tell@192.168.0.2", f"rm -f {remote_path}*"])
    
    if ssh_res.returncode == 0:
        with open(out_path, "wb") as f:
            f.write(ssh_res.stdout)
        return True, "Extracted remotely on tell."
    else:
        return False, f"Remote extraction failed: {ssh_res.stderr.decode()}"

def process_extraction(client, payload):
    filepath = payload.get("filepath")
    if not filepath or not os.path.exists(filepath):
        client.publish(RESULT_TOPIC, json.dumps({"status": "error", "message": "File not found"}))
        return
        
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    
    filename = os.path.basename(filepath)
    out_path = os.path.join(TRAINING_DATA_DIR, f"{filename}.extracted.txt")
    
    local_formats = [".txt", ".md", ".json", ".csv", ".pdf", ".docx"]
    remote_formats = [".png", ".jpg", ".mp3", ".wav"]
    
    success = False
    msg = ""
    
    try:
        if ext in local_formats:
            success, msg = extract_local(filepath, ext, out_path)
        elif ext in remote_formats:
            success, msg = extract_remote(filepath, ext, out_path)
        else:
            msg = f"Unsupported format: {ext}"
    except Exception as e:
        msg = f"Exception: {str(e)}"
        
    client.publish(RESULT_TOPIC, json.dumps({
        "filepath": filepath,
        "status": "success" if success else "error",
        "message": msg,
        "output": out_path if success else None
    }))
    
    # Notify central intelligence (knowledge_ingestor)
    if success:
        client.publish("data_rein/sync/changed", json.dumps({"file": out_path}))

def process_batch(client):
    client.publish(RESULT_TOPIC, json.dumps({"status": "batch_start", "message": "Starting batch extraction of training_data"}))
    for root, _, files in os.walk(TRAINING_DATA_DIR):
        for file in files:
            # Skip already extracted files
            if file.endswith(".extracted.txt"):
                continue
            filepath = os.path.join(root, file)
            # Process each file individually
            process_extraction(client, {"filepath": filepath})
    client.publish(RESULT_TOPIC, json.dumps({"status": "batch_finish", "message": "Batch extraction completed"}))

def on_connect(client, userdata, flags, rc, *args):
    if rc == 0:
        client.subscribe(TRIGGER_TOPIC)
        client.subscribe("data_rein/extract/batch_trigger")

def on_message(client, userdata, msg):
    if msg.topic == TRIGGER_TOPIC:
        try:
            payload = json.loads(msg.payload.decode())
            threading.Thread(target=process_extraction, args=(client, payload), daemon=True).start()
        except json.JSONDecodeError:
            pass
    elif msg.topic == "data_rein/extract/batch_trigger":
        threading.Thread(target=process_batch, args=(client,), daemon=True).start()

def main():
    os.makedirs(TRAINING_DATA_DIR, exist_ok=True)
    
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1, client_id="data_extractor")
    else:
        client = mqtt.Client(client_id="data_extractor")
        
    client.on_connect = on_connect
    client.on_message = on_message
    
    try:
        client.connect("localhost", 1883, 300)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()

if __name__ == "__main__":
    main()

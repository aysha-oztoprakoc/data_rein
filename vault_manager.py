import os
import subprocess
import json
import time

SECRETS_FILE = os.path.expanduser("~/DATA/data_harness/.secrets.env")
BW_BIN = os.path.expanduser("~/.local/bin/bw")

class VaultManager:
    def __init__(self):
        self.email = None
        self.password = None
        self.session_key = None
        self._load_secrets()
        
    def _load_secrets(self):
        if not os.path.exists(SECRETS_FILE):
            return
        with open(SECRETS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("BW_EMAIL="):
                    self.email = line.split("=", 1)[1].strip('"')
                elif line.startswith("BW_PASSWORD="):
                    self.password = line.split("=", 1)[1].strip('"')

    def _configure_server(self):
        # The correct EU server API is usually vault.bitwarden.eu
        subprocess.run([BW_BIN, "config", "server", "vault.bitwarden.eu"], capture_output=True)

    def unlock(self):
        if not self.email or not self.password:
            return False
            
        self._configure_server()
        
        # Check login status
        res = subprocess.run([BW_BIN, "status", "--raw"], capture_output=True, text=True)
        try:
            status = json.loads(res.stdout)
            if status.get("status") == "unauthenticated":
                # Need to login
                env = os.environ.copy()
                env["BW_PASSWORD"] = self.password
                subprocess.run([BW_BIN, "login", self.email, "--passwordenv", "BW_PASSWORD", "--raw"], env=env, capture_output=True)
        except Exception:
            pass
            
        # Unlock
        env = os.environ.copy()
        env["BW_PASSWORD"] = self.password
        res = subprocess.run([BW_BIN, "unlock", "--passwordenv", "BW_PASSWORD", "--raw"], env=env, capture_output=True, text=True)
        
        if res.returncode == 0:
            self.session_key = res.stdout.strip()
            return True
        return False
        
    def get_api_keys(self):
        # Fallback to local file if vault not configured
        fallback_path = os.path.expanduser("~/DATA/data_harness/api_keys.json")
        keys = {}
        if os.path.exists(fallback_path):
            with open(fallback_path, "r") as f:
                keys = json.load(f)
                
        # If we have a session key, try to pull from Bitwarden
        # (Assuming the user stored an item named "Data Harness API Keys" as a secure note in JSON format)
        if self.session_key:
            env = os.environ.copy()
            env["BW_SESSION"] = self.session_key
            res = subprocess.run([BW_BIN, "get", "notes", "Data Harness API Keys"], env=env, capture_output=True, text=True)
            if res.returncode == 0:
                try:
                    vault_keys = json.loads(res.stdout.strip())
                    keys.update(vault_keys)
                except json.JSONDecodeError:
                    pass
        return keys

vault = VaultManager()

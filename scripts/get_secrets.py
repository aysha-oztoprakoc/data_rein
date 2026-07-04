from pathlib import Path
from cryptography.fernet import Fernet
import json

def get_secret(key_name: str) -> str:
    """
    Called by autonomous agents (Hermes, Odysseus, Antigravity) to fetch sensitive
    information (like SUDO_PASS) directly into memory without touching the disk.
    """
    key_path = Path("/home/amdy/data_rein/config/.secrets.key")
    enc_path = Path("/home/amdy/data_rein/config/.secrets.enc")

    if not key_path.exists() or not enc_path.exists():
        raise FileNotFoundError("Encrypted secrets vault is missing.")

    with open(key_path, "rb") as kf:
        key = kf.read()
    
    f = Fernet(key)
    
    with open(enc_path, "rb") as ef:
        encrypted_data = ef.read()
        
    decrypted = f.decrypt(encrypted_data).decode('utf-8')
    
    # Parse the .env format in memory
    for line in decrypted.splitlines():
        if line.startswith(f"{key_name}="):
            val = line.split("=", 1)[1].strip()
            # Remove surrounding quotes if they exist
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            return val
            
    return None

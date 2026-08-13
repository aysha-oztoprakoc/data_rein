import os
from pathlib import Path

from cryptography.fernet import Fernet


def setup_encryption() -> None:

    secrets_path = Path("/home/amdy/data_rein/config/.secrets.env")
    key_path = Path("/home/amdy/data_rein/config/.secrets.key")
    enc_path = Path("/home/amdy/data_rein/config/.secrets.enc")

    if not secrets_path.exists():
        print("No plaintext secrets found. Skipping encryption.")
        return

    # Generate a key and write it securely
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        _ = key_file.write(key)
    os.chmod(key_path, 0o400) # Read only by owner

    f = Fernet(key)
    
    with open(secrets_path, "rb") as sec_file:
        plaintext = sec_file.read()
        
    encrypted = f.encrypt(plaintext)
    
    with open(enc_path, "wb") as enc_file:
        _ = enc_file.write(encrypted)
    os.chmod(enc_path, 0o600)

    # Shred or remove the plaintext file for security
    os.remove(secrets_path)
    print("Secrets encrypted successfully. Plaintext destroyed.")

if __name__ == "__main__":
    setup_encryption()

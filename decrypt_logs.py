import os
from cryptography.fernet import Fernet
from datetime import datetime

# === 1. Load Key ===
key_file = "secret.key"
if not os.path.exists(key_file):
    print("❌ secret.key not found.")
    exit()

with open(key_file, "rb") as f:
    key = f.read()

cipher = Fernet(key)

# === 2. Find All Log Files ===
log_files = sorted([f for f in os.listdir() if f.startswith("log_") and f.endswith(".txt")])

if not log_files:
    print("📭 No log files found.")
    exit()

# === 3. Decrypt and Show Logs ===
for log_file in log_files:
    print(f"\n📂 Decrypting: {log_file}")
    output_lines = []

    try:
        with open(log_file, "rb") as f:
            for line in f:
                try:
                    decrypted = cipher.decrypt(line.strip()).decode()
                    output_lines.append(decrypted)
                except:
                    output_lines.append("[⚠️ Failed to decrypt a line]")

        for line in output_lines:
            print(line)

        # === 4. Save to Decrypted File ===
        date = log_file.replace("log_", "").replace(".txt", "")
        with open(f"decrypted_{date}.txt", "w", encoding="utf-8") as out:
            out.write("\n".join(output_lines))

        print(f"✅ Saved to decrypted_{date}.txt")

    except Exception as e:
        print(f"❌ Error reading {log_file}: {e}")

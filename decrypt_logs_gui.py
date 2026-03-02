import os
from datetime import datetime
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import ttk, messagebox

# === Load Key ===
def load_key():
    key_path = "secret.key"
    if not os.path.exists(key_path):
        messagebox.showerror("Error", "secret.key not found.")
        return None
    with open(key_path, "rb") as f:
        return f.read()

# === List Available Log Files ===
def get_log_files():
    return sorted([f for f in os.listdir() if f.startswith("log_") and f.endswith(".txt")])

# === Decrypt Selected Log File ===
def decrypt_log_file():
    selected_file = file_var.get()
    if not selected_file:
        messagebox.showwarning("Warning", "Please select a log file.")
        return

    key = load_key()
    if not key:
        return

    cipher = Fernet(key)
    output_lines = []

    try:
        with open(selected_file, "rb") as f:
            lines = f.readlines()

        for line in lines:
            try:
                decrypted = cipher.decrypt(line.strip()).decode()
                output_lines.append(decrypted)
            except:
                output_lines.append("[⚠️ Failed to decrypt a line]")

        # Show in GUI
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "\n".join(output_lines))

        # Save output
        date = selected_file.replace("log_", "").replace(".txt", "")
        output_filename = f"decrypted_{date}.txt"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))

        messagebox.showinfo("Success", f"Decrypted log saved to {output_filename}")

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{e}")

# === GUI Setup ===
root = tk.Tk()
root.title("🛡️ Log Decryptor")
root.geometry("650x500")

tk.Label(root, text="Select Encrypted Log File:", font=("Segoe UI", 10)).pack(pady=10)

file_var = tk.StringVar()
log_files = get_log_files()
file_dropdown = ttk.Combobox(root, textvariable=file_var, values=log_files, width=50)
file_dropdown.pack(pady=5)

tk.Button(root, text="🔓 Decrypt & Show", command=decrypt_log_file, bg="#4CAF50", fg="white").pack(pady=10)

output_text = tk.Text(root, wrap="word", height=20, width=80)
output_text.pack(padx=10, pady=10)

root.mainloop()

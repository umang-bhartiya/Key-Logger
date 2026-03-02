# 🔐 Encrypted Keylogger – Educational Cybersecurity Demonstration  

This project demonstrates how keylogging mechanisms function in controlled environments for cybersecurity education and awareness.  
The objective is to help learners understand:  
- How keystroke capture works at a system level  
- Why encryption is critical when handling sensitive data  
- How defensive security tools detect monitoring behavior  
- The importance of ethical boundaries in cybersecurity

All logged data is encrypted using symmetric encryption (Fernet) to reinforce secure design principles.  

---

## ⚠️ Ethical Use Notice  

This project is developed strictly for educational and authorized cybersecurity research purposes.  
It must only be used:  
* On systems you own, or  
* In environments where you have explicit written permission

Unauthorized use of monitoring software is illegal and unethical.  
The author does not endorse misuse, surveillance, or data exploitation.

---

## 🛠 Features  

- Real-time keystroke capture  
- AES-based symmetric encryption (Fernet)  
- Automatic daily log file generation  
- Secure key management via secret.key  
- CLI-based log decryption tool  
- GUI-based log decryption viewer (Tkinter)  
- Automatic decrypted file export  

---

## 🧩 Problem Statement & Solution

### 🔍 Real-Life Problem Statement

In modern computing environments, user input—particularly keyboard input—often contains highly sensitive information such as passwords, financial credentials, private communications, and confidential business data.  

One of the most common attack vectors used to exfiltrate such information is keystroke logging (keylogging).  

The core problem is twofold:  
1. Lack of awareness – Many users and developers do not fully understand how easily keystroke monitoring can be implemented.  
2. Insufficient defensive insight – Without understanding how keyloggers operate internally, it becomes difficult to design effective detection and mitigation strategies.  

Additionally, there is a technical gap in educational resources that:  
- Demonstrate keystroke capture mechanisms in a controlled environment  
- Show how sensitive data should be protected using encryption  
- Illustrate proper key management practices  
- Reinforce ethical and legal boundaries in cybersecurity  

To build stronger defensive systems, cybersecurity practitioners must first understand how such monitoring mechanisms work at a technical level.

---

### 💡 How This Project Provides a Solution

This project delivers a controlled, encrypted keylogging simulation designed strictly for cybersecurity education and authorized research.  
It provides the following solutions:  
#### 1️⃣ Controlled Demonstration of Keystroke Capture  
The system demonstrates how keyboard input events can be captured programmatically using system-level listeners.  
This enables learners to understand:  
* Event-driven input handling  
* Background process behavior  
* Data collection mechanisms used in monitoring software  

#### 2️⃣ Secure Data Handling via Encryption  
Unlike malicious keyloggers, this project encrypts all captured data using Fernet symmetric encryption.  
This demonstrates:  
* The importance of encryption when handling sensitive data  
* Secure storage practices  
* Cryptographic key management principles  
* Risks associated with key exposure  

#### 3️⃣ Practical Key Management Implementation  
The project introduces:  
* Automatic key generation  
* Secure local key storage (secret.key)  
* Dependency of decryption on key integrity

This reinforces a critical cybersecurity principle:  
If encryption keys are compromised, data confidentiality collapses.  

#### 4️⃣ Dual Decryption Interfaces 
The project provides two methods to retrieve encrypted logs:  
* CLI-based decryption tool (technical users)  
* GUI-based decryption tool (usability-focused interface)

This highlights the importance of:  
* Tool accessibility  
* User interface design in security tools  
* Multi-layered operational flexibility  

#### 5️⃣ Ethical Framing and Responsible Development  
The project is intentionally structured with:  
* Explicit ethical disclaimers  
* Exclusion of sensitive files via .gitignore  
* Local-only encryption key storage  
* Clear documentation on responsible usage

This reinforces the professional cybersecurity mindset:  
Understanding attack techniques is essential for building stronger defenses — but ethical boundaries must always be respected.  

---

### 👥 How Users and the Public Should Address This Problem

Understanding how keylogging works is only the first step. The real value lies in adopting preventative and defensive measures to protect personal and organizational data.  
Below are structured actions individuals and the public should take.  

#### 1️⃣ Increase Awareness and Digital Hygiene  
Many keylogging attacks succeed due to lack of awareness.  
Users should:  
* Avoid downloading unverified software  
* Refrain from installing cracked or pirated applications  
* Be cautious with browser extensions  
* Avoid clicking suspicious links or email attachments  
* Regularly update operating systems and applications

Basic digital hygiene significantly reduces exposure.  

-----

#### 2️⃣ Use Updated Antivirus and Endpoint Protection  
Modern security software includes behavioral detection mechanisms that can:  
* Detect abnormal keyboard hook behavior  
* Identify suspicious background processes  
* Block unauthorized input monitoring attempts

Users should:  
* Enable real-time protection  
* Keep virus definitions updated  
* Perform periodic system scans  

-----

#### 3️⃣ Enable Multi-Factor Authentication (MFA)  
Even if keystrokes are captured, MFA reduces the impact of credential theft.  
Users should:  
* Enable MFA on all critical accounts  
* Use authenticator apps instead of SMS where possible  
* Avoid storing passwords in plain text

This ensures that stolen passwords alone are insufficient for access.  

-----

#### 4️⃣ Use Password Managers  
Password managers:  
* Auto-fill credentials without manual typing  
* Reduce the amount of sensitive typing on compromised systems  
* Generate strong, unique passwords

This minimizes exposure to keystroke interception.  

-----

#### 5️⃣ Monitor System Behavior  
Users should stay alert to:  
* Unusual background processes  
* High CPU or memory usage without explanation  
* Unknown startup programs  
* Unexpected file creation

Tools like Task Manager and startup configuration panels should be periodically reviewed.  

-----

#### 6️⃣ Restrict Administrative Privileges  
Many keylogging tools require elevated privileges.  
Best practices:  
* Use standard user accounts for daily activities  
* Avoid running unknown applications as administrator  
* Implement user access control in shared environments  

Principle of least privilege reduces attack surface.  

-----

#### 7️⃣ Encrypt Sensitive Data  
Even if data is captured, encryption can prevent meaningful exploitation.  
Individuals and organizations should:  
* Encrypt local storage  
* Use secure communication channels (HTTPS, TLS)  
* Protect backups with encryption

Security should assume potential compromise and mitigate impact.  

-----

#### 8️⃣ Promote Cybersecurity Education  
Public awareness is the strongest defense.  
Educational institutions and organizations should:  
* Conduct cybersecurity awareness training  
* Teach ethical hacking principles responsibly  
* Promote understanding of attack mechanisms to build defensive skills

An informed public is harder to exploit.  

---

## 🧱 Project Structure

Keylogger_Project/  
│  
├── keylogger.py               # Encrypted keystroke logger  
├── decrypt_logs.py            # CLI decryption tool  
├── decrypt_logs_gui.py        # GUI decryption tool  
├── requirements.txt           # Project dependencies  
├── LICENSE                    # MIT License  
├── README.md                  # Project documentation  
└── .gitignore                 # Prevents sensitive files from being committed  

---

## 🛠️ Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name 
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### ▶️ Run The Application

Start the Keylogger:
```bash
python keylogger.py
```

Stop execution:
```bash
Ctrl + C
```

Encrypted logs are stored as:
```bash
log_YYYY-MM-DD.txt
```

Decrypt Logs (CLI):
```bash
python decrypt_logs.py
```
This will:  
* Decrypt all available log files  
* Display output in terminal  
* ## Save decrypted files as:  
```bash
decrypted_YYYY-MM-DD.txt
```

Decrypt Logs (GUI):
```bash
python decrypt_logs_gui.py
```
Features:  
Select log file from dropdown  
View decrypted content  
Automatically export decrypted file  

---

## 🔮 Future Enhancements
```bash  
├── SQLite encrypted password vault  
├── First-run master password setup  
├── Executable packaging (.exe)  
└── Cross-platform UI polish
```

---

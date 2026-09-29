# 🔐 SecureCLI: Password Manager & Policy Auditor

A lightweight, terminal-based password management and policy auditing utility built with Python. It provides centralized credential storage guarded by SHA-256 master key verification, paired with an automated password policy checker and vault vulnerability auditor.

---

## 🚀 Key Features

- **Master Key Protection:** Master password is never stored in plain text; authentication verifies against a salted/one-way SHA-256 hash.
- **Brute-Force Guard:** Strict attempt counter (maximum 3 failed tries) with automatic process termination on breach attempts.
- **Live Password Policy Checking:** Evaluates length, character variety (upper, lower, digits, symbols), and grades credential strength in real time.
- **Vault Vulnerability Audit:**
  - Identifies weak credentials stored across accounts.
  - Detects cross-account password reuse risks across all saved entries.
- **Zero External Dependencies:** Built completely with native Python modules (`os`, `sys`, `hashlib`).

---

## 📁 Repository Structure

```text
SecureCLI-Password-Manager-Policy-Auditor/
│
├── auth.py          # Master password creation, SHA-256 hashing, and access control
├── auditor.py       # Password strength scoring rules and vault security auditor
├── main.py          # Interactive CLI orchestration and credential storage handler
├── README.md        # Project documentation
└── .gitignore       # Prevents sensitive local credential files from getting committed
```

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+ installed on your system.
- Git installed (optional, for version control).

### Running the Application

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/SecureCLI-Password-Manager-Policy-Auditor.git
   cd SecureCLI-Password-Manager-Policy-Auditor
   ```

2. Run the entrypoint:
   ```bash
   python main.py
   ```

3. Follow the on-screen prompts:
   - On first launch, create a master password.
   - On subsequent launches, verify your master password to unlock the menu.

---

## 🛡️ Security Architecture

| Module | Primary Responsibility | Security Role |
| :--- | :--- | :--- |
| `auth.py` | Key derivation & verification | Stores digest in `masterhash.txt`, prevents unauthorized memory inspection |
| `auditor.py` | Policy enforcement | Flags passwords shorter than 8 chars, checks character entropy, catches duplicates |
| `main.py` | Vault I/O | Reads and writes formatted credentials (`website\|username\|password`) |

> **Security Note:** Generated local vault files (`masterhash.txt` and `Passwords.txt`) are excluded via `.gitignore` to avoid leaking personal credentials into public Git logs.

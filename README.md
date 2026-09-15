# 🔐 CLI Password Manager

A lightweight, beginner-friendly Command Line Interface (CLI) Password Manager built in Python. This tool allows users to securely store and view login credentials behind a Master Password protected by SHA-256 hashing.

---

## ✨ Features

* **Master Password Authentication**: Protects your saved credentials behind a single master key.
* **SHA-256 Security**: Master passwords are never stored in plain text; instead, a cryptographically secure SHA-256 hash is verified.
* **Brute-Force Protection**: Limits login attempts to 3 tries. Automatically terminates the session if authentication fails.
* **Simple File Storage**: Automatically manages local data storage using standard `.txt` files (`masterhash.txt` and `Passwords.txt`).
* **Zero External Dependencies**: Built entirely using Python standard libraries (`hashlib`, `os`, `sys`).

---

## 📁 Project Structure

```text
cli-password-manager/
├── auth.py          # Master password creation, SHA-256 hashing, and authentication
├── main.py          # Interactive CLI menu and password management logic
├── masterhash.txt   # Auto-created file storing the master password hash
└── Passwords.txt    # Auto-created file storing saved website credentials
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or higher installed on your system.

### Installation & Execution

1. **Clone or download** this repository to your local machine.
2. **Open your terminal** or command prompt in the project directory.
3. **Run the program**:

```bash
python main.py
```

---

## 💻 How It Works

1. **First-Time Setup**:
   When launched for the first time, the program detects that `masterhash.txt` does not exist and prompts you to create and confirm a Master Password.

2. **Authentication**:
   You will be asked for your Master Password. 
   * You are allowed **3 attempts**. 
   * If correct, access is granted. 
   * If incorrect 3 times, the program safely exits without revealing the menu.

3. **Main Menu Options**:
   * **`1` Add a new password**: Prompts for website/app name, username/email, and password, then appends it to `Passwords.txt`.
   * **`2` View stored passwords**: Reads and displays all saved credentials line by line.
   * **`3` Exit**: Safely quits the program loop.

---

## 🔒 Security & Implementation Details

* **Password Hashing**: Uses Python's `hashlib.sha256()` module to ensure master passwords are stored only as secure hex digests.
* **Session Guarding**: Utilizes `sys.exit()` to terminate execution immediately upon authentication failure, protecting the menu from unauthorized access.

---

## 📝 License & Purpose

This project was built for educational and portfolio presentation purposes to demonstrate basic Python authentication workflows and file handling techniques.

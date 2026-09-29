# Project Statement: SecureCLI – Modular Password Manager & Security Policy Auditor

---

## 1. Executive Summary

**SecureCLI** is a lightweight, terminal-native credential management vault and policy auditing system built entirely with the Python standard library. Designed as an offline-first, zero-dependency utility, SecureCLI addresses the critical trade-offs between usability and security in personal password management. By combining single-way SHA-256 master key derivation with real-time heuristic strength checks and vault-wide password reuse auditing, the system provides an auditable, secure, and performant alternative to cloud-dependent credential managers.

---

## 2. Problem Statement

### 2.1 Background & Context
In modern computing environments, users manage dozens to hundreds of disparate online accounts across web portals, remote servers, API keys, and corporate applications. The cognitive burden of remembering complex, unique passwords frequently leads to poor credential hygiene, such as:
1. **Password Reuse:** Using the same password across multiple independent services, causing a single data breach to compromise multiple accounts.
2. **Low Character Entropy:** Creating short, predictable passwords (e.g., dictionary words, lack of special symbols) vulnerable to dictionary and brute-force attacks.
3. **Third-Party/Cloud Over-reliance:** Relying on commercial cloud password managers that introduce centralized attack surfaces, closed-source black-box logic, and recurring costs.

### 2.2 Core Problem Formulation
There is a distinct need for a **self-contained, transparent, offline Command-Line Interface (CLI) credential vault** that:
- Guarantees zero plaintext exposure of master authentication credentials.
- Operates without external third-party package dependencies (e.g., `pip` packages), eliminating supply-chain security risks.
- Actively audits stored credentials for security vulnerabilities and duplicate usage across accounts.
- Enforces strict brute-force access throttling directly at the terminal execution layer.

---

## 3. Project Objectives

1. **Cryptographic Authentication Gate:** Implement master key creation and verification using irreversible SHA-256 hashing (`hashlib`) with a strict 3-attempt brute-force threshold before process termination.
2. **Live Password Strength Assessment:** Develop a heuristic evaluation engine (`auditor.py`) that checks password length, uppercase, lowercase, digit, and special character criteria in real-time, providing immediate feedback prior to storage.
3. **Automated Vault Vulnerability Scanning:** Build an $O(N)$ bulk-scanning audit engine to detect weak stored credentials and cross-domain password duplication across saved records.
4. **Lightweight Data Storage:** Implement a transparent, human-auditable flat-file delimiter storage protocol (`Passwords.txt` and `masterhash.txt`) requiring zero external database setup.
5. **Decoupled Architecture:** Maintain a clean 3-tier modular separation across authentication (`auth.py`), policy engine (`auditor.py`), and CLI orchestration (`main.py`).

---

## 4. System Requirements

### 4.1 Functional Requirements (FR)

| Requirement ID | Module | Feature Description |
| :--- | :--- | :--- |
| **FR-01** | `auth.py` | Prompt user for master password initialization on first run; generate SHA-256 digest and persist to `masterhash.txt`. |
| **FR-02** | `auth.py` | Verify entered master password against saved SHA-256 digest on subsequent launches; enforce maximum 3 login attempts before terminating execution via `sys.exit()`. |
| **FR-03** | `auditor.py` | Assess candidate password strength based on length ($\ge 8, \ge 12$), uppercase, lowercase, numerical, and special character presence. Assign ratings: `Weak`, `Medium`, or `Strong`. |
| **FR-04** | `auditor.py` | Scan stored credentials in `Passwords.txt` to identify all accounts utilizing weak passwords and list specific advice for each. |
| **FR-05** | `auditor.py` | Scan the stored vault to identify duplicate passwords used across different services and report matching domains. |
| **FR-06** | `main.py` | Provide an interactive CLI menu allowing users to: (1) Add a new credential with live auditing, (2) View all saved entries, (3) Execute a vault security audit, and (4) Exit safely. |

### 4.2 Non-Functional Requirements (NFR)

* **NFR-01: Security:** Master password must never be stored in plaintext. Master hash verification must use irreversible one-way SHA-256 digests. Sensitive files must be excluded from version control using `.gitignore`.
* **NFR-02: Zero External Dependencies:** Complete system execution must rely solely on native Python 3 standard library modules (`os`, `sys`, `hashlib`).
* **NFR-03: Performance:** Individual menu selections and bulk vault security audits must complete execution in under $15\text{ ms}$ for standard vault sizes ($N \le 1000$ entries).
* **NFR-04: Usability:** Output clear, human-readable terminal messages, structured audit reports, and informative error messages.

---

## 5. Architectural Scope & Module Breakdown

```text
SecureCLI Project Architecture
│
├── auth.py          # Authentication Guard: SHA-256 key derivation & 3-attempt lock
├── auditor.py       # Security Policy Engine: Live strength checks & duplication scanner
├── main.py          # Application Orchestrator: CLI menu loop & file stream coordinator
├── masterhash.txt   # Persistent Master Hash Storage (Git-ignored)
└── Passwords.txt    # Delimiter-Separated Vault Data (Git-ignored)
```

### Module Responsibilities:
1. **`auth.py` (Authentication Guard):** Handles initial system setup and subsequent access verification. Converts input passwords into SHA-256 hexadecimal digests using `hashlib.sha256()`.
2. **`auditor.py` (Policy & Audit Engine):** Performs character-set inspections using generator expressions for sub-millisecond heuristic scoring. Scans pipe-delimited records (`site|user|password`) to track password reuse using dictionary mapping.
3. **`main.py` (Orchestrator):** Controls the terminal execution loop, coordinates call handoffs between modules, and manages flat-file stream reads and appends.

---

## 6. Expected Outcomes & Impact

- **Improved Credential Hygiene:** Eliminates manual guessing of password strength by offering actionable feedback at creation time.
- **Vulnerability Remediation:** Enables users to quickly discover and replace duplicate or weak passwords stored across their accounts.
- **Lightweight Portability:** Runs seamlessly across Windows, macOS, and Linux without requiring package installation (`pip install`) or complex background database services.
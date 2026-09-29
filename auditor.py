import os

SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

def check_password_strength(pwd):
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(c in SPECIAL_CHARS for c in pwd)

    score = 0
    feedback = []

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Increase length (min 8 chars)")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if has_digit:
        score += 1
    else:
        feedback.append("Add digits")

    if has_special:
        score += 1
    else:
        feedback.append("Add special characters")

    # label assignment
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"

    return rating, feedback

def audit_vault(filepath="Passwords.txt"):
    if not os.path.exists(filepath):
        print("Passwords.txt not found. Add some passwords first.")
        return

    sites_by_pwd = {}
    total = 0
    weak_list = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or "|" not in line:
                continue
            
            parts = line.split("|")
            if len(parts) >= 3:
                site = parts[0]
                user = parts[1]
                pwd = parts[2]
                total += 1

                # check strength
                rating, feedback = check_password_strength(pwd)
                if rating == "Weak":
                    weak_list.append((site, user, feedback))

                # track reuse
                if pwd in sites_by_pwd:
                    sites_by_pwd[pwd].append(site)
                else:
                    sites_by_pwd[pwd] = [site]

    print("\n--- Vault Audit ---")
    print(f"Total entries scanned: {total}")

    if weak_list:
        print("\n[!] Weak Passwords Found:")
        for site, user, issues in weak_list:
            print(f" - {site} ({user}): {', '.join(issues)}")
    else:
        print("\n[+] No weak passwords detected.")

    reused = {p: s for p, s in sites_by_pwd.items() if len(s) > 1}
    if reused:
        print("\n[!] Reused Passwords Found:")
        for _, sites in reused.items():
            print(f" - Reused across: {', '.join(sites)}")
    else:
        print("[+] No reused passwords found.")
    print("-------------------\n")
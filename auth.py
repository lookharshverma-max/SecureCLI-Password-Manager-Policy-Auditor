import hashlib
import os
import sys

def set_master_password():
    pwd = input("Enter master password: ").strip()
    # hash using sha256 before saving
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    with open("masterhash.txt", "w") as f:
        f.write(hashed)
    print("Master password set.")

def verify_master_password():
    attempts = 3
    while attempts > 0:
        entered = input("Enter master password: ").strip()
        entered_hash = hashlib.sha256(entered.encode()).hexdigest()

        with open("masterhash.txt", "r") as f:
            saved_hash = f.read().strip()

        if entered_hash == saved_hash:
            print("Access granted.\n")
            return True
        
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. Attempts left: {attempts}")

    print("Too many failed attempts. Exiting.")
    sys.exit()

if __name__ == "__main__":
    if os.path.exists("masterhash.txt"):
        verify_master_password()
    else:
        set_master_password()
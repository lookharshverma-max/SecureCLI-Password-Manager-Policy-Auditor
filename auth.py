import hashlib
import os

def set_master_password():
    master_password = input("Enter master password: ").encode()
    masterhash = hashlib.sha256(master_password).hexdigest()

    with open("masterhash.txt", "w") as file:
        file.write(masterhash)

def verify_master_password():
    attempts = 3

    while attempts > 0:
        master_1password = input("Enter master password: ").encode()
        masterhash1 = hashlib.sha256(master_1password).hexdigest()

        with open("masterhash.txt", "r") as file:
            stored_masterhash = file.read()

        if masterhash1 == stored_masterhash:
            print("Master password verified successfully.")
            return

        attempts -= 1
        if attempts > 0:
            print(f"Incorrect password. {attempts} attempts remaining.")

    print("Incorrect master password. Access denied.")

if os.path.exists("masterhash.txt"):
    print("Master password already set. Please verify.")
    verify_master_password()

else:
    print("No master password found. Please set a new master password.")
    set_master_password()
import hashlib
import sys

def set_master_password():
    pwd = input("Enter master password: ")
    h = hashlib.sha256(pwd.encode()).hexdigest()
    
    file = open("masterhash.txt", "w")
    file.write(h)
    file.close()
    print("Master password saved successfully.")

def verify_master_password():
    attempts = 3
    while attempts > 0:
        guess = input("Enter master password: ")
        guess_hash = hashlib.sha256(guess.encode()).hexdigest()

        file = open("masterhash.txt", "r")
        saved_hash = file.read().strip()
        file.close()

        if guess_hash == saved_hash:
            print("Access granted.\n")
            return True

        attempts -= 1
        if attempts > 0:
            print("Wrong password! Attempts left:", attempts)

    print("Too many failed attempts. Exiting.")
    sys.exit()
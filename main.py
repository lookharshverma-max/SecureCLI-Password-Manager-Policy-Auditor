import auth
import os

if os.path.exists("masterhash.txt"):
    auth.verify_master_password()
    print("Enter the correct pass")
else:
    auth.set_master_password()

while True:
    print("1. Add a new password\n2. View stored passwords\n3. Exit")
    choice = input("Enter your choice 1-3: ")

    if choice == "1":
        with open("Passwords.txt", "a+") as file:
            website = input("Enter website/app name: ")
            username = input("Enter username/email: ")
            password = input("Enter password: ")
            file.write(f"{website}|{username}|{password}\n")
            print("Password saved.")

    elif choice == "2":
        if os.path.exists("Passwords.txt"):
            with open("Passwords.txt", "r") as file:
                contents = file.read()
                if contents:
                    print(contents)
                else:
                    print("No stored passwords.")
        else:
            print("No stored passwords.")

    elif choice == "3":
        print("Thanks For Using CLI Pass Manager!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")

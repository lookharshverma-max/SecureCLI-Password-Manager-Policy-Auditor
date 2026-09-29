import os
import auth
import auditor

def main():
    if os.path.exists("masterhash.txt"):
        auth.verify_master_password()
    else:
        print("No master password found.")
        auth.set_master_password()

    while True:
        print("1. Add a new password")
        print("2. View stored passwords")
        print("3. Audit password security")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            site = input("Enter website/app: ").strip()
            user = input("Enter username/email: ").strip()
            pwd = input("Enter password: ").strip()

            rating, feedback = auditor.check_password_strength(pwd)
            print(f"Strength assessment: {rating}")
            if feedback:
                print("Advice:", ", ".join(feedback))

            with open("Passwords.txt", "a+") as f:
                f.write(f"{site}|{user}|{pwd}\n")
            print("Saved successfully.\n")

        elif choice == "2":
            if os.path.exists("Passwords.txt"):
                with open("Passwords.txt", "r") as f:
                    data = f.read().strip()
                if data:
                    print("\n--- Saved Credentials ---")
                    print(data)
                    print("-------------------------\n")
                else:
                    print("File is empty.\n")
            else:
                print("No stored passwords found.\n")

        elif choice == "3":
            auditor.audit_vault()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
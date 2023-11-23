class ATM:
    def __init__(self):
        self.users = {}
        self.admin_username = "admin"
        self.admin_password = "admin123"
        self.max_login_attempts = 5

    def user_login(self):
        attempts = 0
        while attempts < self.max_login_attempts:
            print("\n===== User Login =====")
            print("1. Existing User")
            print("2. Create New Account")
            print("3. Exit")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                user_username = input("Enter your username: ")

                if user_username in self.users:
                    password = input("Enter your password: ")
                    if password == self.users[user_username]["password"]:
                        print("Login successful!")
                        return user_username
                    else:
                        print("Incorrect password. Please try again.")
                else:
                    print("User not found. Please try again.")
            elif choice == "2":
                user_username = input("Enter your new username: ")

                if user_username not in self.users:
                    password = input("Enter your password: ")
                    account_number = input("Enter your account number: ")
                    pin = input("Enter your PIN: ")

                    self.users[user_username] = {"account_number": account_number, "password": password,
                                                 "pin": pin, "balance": 0, "transactions": []}
                    print("Account created successfully! You can now log in.")
                    return user_username
                else:
                    print("Username already exists. Please choose a different username.")
            elif choice == "3":
                print("Exiting the ATM. Thank you!")
                exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

            attempts += 1

        print("Too many unsuccessful login attempts. Locking the ATM.")
        exit()

    def admin_login(self):
        admin_attempts = 0
        while admin_attempts < self.max_login_attempts:
            print("\n===== Admin Login =====")
            admin_username_input = input("Enter admin username: ")
            admin_password_input = input("Enter admin password: ")

            if admin_username_input == self.admin_username and admin_password_input == self.admin_password:
                print("Admin login successful!\n")
                self.display_user_balances()
                return True
            else:
                print("Incorrect admin username or password. Please try again.")
                admin_attempts += 1

        print("Too many unsuccessful admin login attempts. Locking the ATM.")
        exit()

    def display_user_balances(self):
        print("\n===== User Balances =====")
        for username, user_info in self.users.items():
            print(f"\nUser: {username}")
            print(f"Remaining Balance: Rs{user_info['balance']:.2f}")

    def main_menu(self, user):
        if user == "admin":
            if self.admin_login():
                return
        else:
            while True:
                print("\n===== User Menu =====")
                print("1. Display Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    print(f"Account Balance: Rs{self.users[user]['balance']:.2f}")
                elif choice == "2":
                    self.deposit(user)
                elif choice == "3":
                    self.withdraw(user)
                elif choice == "4":
                    print("Returning to the main menu.")
                    return
                else:
                    print("Invalid choice. Please enter a number between 1 and 4.")

    def deposit(self, user):
        pin = input("Enter your PIN: ")
        if pin == self.users[user]['pin']:
            amount = float(input("Enter the deposit amount: Rs"))
            if amount <= 100000:  # Maximum deposit limit of 1 lakh
                self.users[user]['balance'] += amount
                self.users[user]['transactions'].append(f"Deposited: Rs{amount:.2f}")
                print(f"Deposited: Rs{amount:.2f}")
                print(f"Account Balance: Rs{self.users[user]['balance']:.2f}")
            else:
                print("Maximum deposit limit exceeded. Please try again.")
        else:
            print("Incorrect PIN. Transaction canceled.")

    def withdraw(self, user):
        pin = input("Enter your PIN: ")
        if pin == self.users[user]['pin']:
            amount = float(input("Enter the withdrawal amount: Rs"))
            if amount <= 50000:  # Maximum withdrawal limit of 50,000
                if amount <= self.users[user]['balance']:
                    self.users[user]['balance'] -= amount
                    self.users[user]['transactions'].append(f"Withdrawn: Rs{amount:.2f}")
                    print(f"Withdrawn: Rs{amount:.2f}")
                    print(f"Account Balance: Rs{self.users[user]['balance']:.2f}")
                else:
                    print("Insufficient funds!")
            else:
                print("Maximum withdrawal limit exceeded. Please try again.")
        else:
            print("Incorrect PIN. Transaction canceled.")


if __name__ == "__main__":
    atm = ATM()

    while True:
        print("\n===== Welcome to the ATM =====")
        print("1. Login as User")
        print("2. Login as Admin")
        print("3. Exit")

        initial_choice = input("Enter your choice (1-3): ")

        if initial_choice == "1":
            user = atm.user_login()
            atm.main_menu(user)
        elif initial_choice == "2":
            user = atm.admin_login()
        elif initial_choice == "3":
            print("Exiting the ATM. Thank you!")
            exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

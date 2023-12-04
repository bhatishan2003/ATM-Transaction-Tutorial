class ATM:
    def __init__(self):
        self.users = {
            'user1': {'password': 'pass1', 'balance': 0},
            'user2': {'password': 'pass2', 'balance': 0},
            'user3': {'password': 'pass3', 'balance': 0},
            'user4': {'password': 'pass4', 'balance': 0},
            'user5': {'password': 'pass5', 'balance': 0},
        }
        self.admin = {'admin': {'password': 'admin123', 'attempts': 0}, 'total_balance': 0}
        self.locked_accounts = {}

    def login_user(self, user_id, password):
        if user_id in self.locked_accounts:
            print("Account is locked. Please contact the administrator.")
            return None

        if user_id in self.users and self.users[user_id]['password'] == password:
            return self.users[user_id]
        else:
            print("Invalid User ID or password.")
            return None

    def deposit(self, user, amount):
        denominations = [2000, 500, 200, 100]

        total_deposit = 0
        for denomination in denominations:
            count = int(input(f"Enter the number of {denomination}-rupee notes: "))
            total_deposit += denomination * count

        if total_deposit <= amount:
            user['balance'] += total_deposit
            print(f"Deposited successfully. Current balance: {user['balance']}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, user, amount):
        denominations = [2000, 500, 200, 100]

        total_withdraw = 0
        for denomination in denominations:
            count = int(input(f"Enter the number of {denomination}-rupee notes: "))
            total_withdraw += denomination * count

        if total_withdraw <= amount and total_withdraw <= user['balance']:
            user['balance'] -= total_withdraw
            print(f"Withdrawn successfully. Current balance: {user['balance']}")
        else:
            print("Invalid withdrawal amount.")

    def check_balance(self, user):
        print(f"Current balance: {user['balance']}")

    def change_password(self, user, new_password):
        user['password'] = new_password
        print("Password changed successfully.")

    def login_admin(self, admin_id, password):
        if admin_id in self.locked_accounts:
            print("Account is locked. Please contact the administrator.")
            return None

        if admin_id in self.admin and self.admin[admin_id]['password'] == password:
            self.admin[admin_id]['attempts'] = 0  # Reset unsuccessful attempts
            return True
        else:
            self.admin[admin_id]['attempts'] += 1
            print("Invalid Admin ID or password.")
            if self.admin[admin_id]['attempts'] >= 3:
                print("Too many unsuccessful attempts. Locking the admin account.")
                self.locked_accounts[admin_id] = True
            return None

    def check_total_balance(self):
        total_balance = self.admin['total_balance']
        print(f"Total balance: {total_balance}")

        if total_balance < 75000:
            print("WARNING: Total balance is less than 75,000.")

    def deposit_to_atm(self, amount):
        denominations = [2000, 500, 200, 100]

        total_deposit = 0
        for denomination in denominations:
            count = int(input(f"Enter the number of {denomination}-rupee notes: "))
            total_deposit += denomination * count

        if total_deposit <= amount:
            self.admin['total_balance'] += total_deposit
            print(f"Deposited to ATM successfully. Total balance: {self.admin['total_balance']}")
        else:
            print("Invalid deposit amount.")

    def admin_menu(self):
        print("\nAdmin Menu:")
        print("1. User Login")
        print("2. Check Total Balance")
        print("3. Deposit to ATM")
        print("4. Logout")

    def create_account(self, user_id, password):
        if user_id not in self.users:
            self.users[user_id] = {'password': password, 'balance': 0}
            print(f"Account created successfully for user: {user_id}")
        else:
            print("User ID already exists. Please choose a different User ID.")

    def lock_account(self, user_id):
        self.locked_accounts[user_id] = True
        print(f"Account for user {user_id} locked.")


def main():
    atm = ATM()

    while True:
        print("\n" + "||" + "*" * 26 + " Welcome to the ATM " + "*" * 26 + "||")
        print("||" + "1. User Login".center(52) + "||")
        print("||" + "2. Admin Login".center(52) + "||")
        print("||" + "3. Exit".center(52) + "||")
        print("||" + "-" * 52 + "||")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter User ID: ")
            password = input("Enter password: ")

            user = atm.login_user(user_id, password)

            if user:
                while True:
                    print("\n" + "*" * 30)
                    print("*** WELCOME TO ATM APPLICATION ***".center(30))
                    print("*" * 30)
                    print("\nUser Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Change Password")
                    print("5. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        amount = int(input("Enter the deposit amount: "))
                        atm.deposit(user, amount)
                    elif user_choice == '2':
                        amount = int(input("Enter the withdrawal amount: "))
                        atm.withdraw(user, amount)
                    elif user_choice == '3':
                        atm.check_balance(user)
                    elif user_choice == '4':
                        new_password = input("Enter new password: ")
                        atm.change_password(user, new_password)
                    elif user_choice == '5':
                        break
                    else:
                        print("Invalid choice. Try again.")

        elif choice == '2':
            admin_id = input("Enter Admin ID: ")
            admin_password = input("Enter admin password: ")

            if atm.login_admin(admin_id, admin_password):
                while True:
                    atm.admin_menu()
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        new_user_id = input("Enter User ID for the new account: ")
                        new_password = input("Enter password for the new account: ")
                        atm.create_account(new_user_id, new_password)
                    elif admin_choice == '2':
                        atm.check_total_balance()
                    elif admin_choice == '3':
                        amount = int(input("Enter the deposit amount to ATM: "))
                        atm.deposit_to_atm(amount)
                    elif admin_choice == '4':
                        break
                    else:
                        print("Invalid choice. Try again.")

        elif choice == '3':
            print("Exiting. Thank you!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

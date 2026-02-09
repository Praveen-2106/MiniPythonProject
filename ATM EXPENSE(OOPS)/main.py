# main.py

from atm import ATM
from expense import ExpenseManager

class BankApp:

    def __init__(self):
        self.user_pin = "1234"
        self.max_try = 3
        self.balance_file = "data.txt"

        self.atm = ATM()
        self.expense_manager = ExpenseManager()

    def load_balance(self):
        try:
            with open(self.balance_file, "r") as file:
                return int(file.read().strip())
        except:
            return 0

    def save_balance(self, balance):
        with open(self.balance_file, "w") as file:
            file.write(str(balance))

    def login(self):
        attempts = 0
        while attempts < self.max_try:
            pin = input("Enter your pin: ")
            if pin == self.user_pin:
                print("\nLogin Successful")
                return True
            else:
                attempts += 1
                print("Incorrect PIN")

        print("Too many login attempts")
        return False

    def menu(self):
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Add Expense")
        print("5. View Expenses")
        print("6. Exit")

    def run(self):
        balance = self.load_balance()

        if not self.login():
            return

        while True:
            self.menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                balance = self.atm.deposit(balance)
                self.save_balance(balance)

            elif choice == "2":
                balance = self.atm.withdraw(balance)
                self.save_balance(balance)

            elif choice == "3":
                self.atm.check_balance(balance)

            elif choice == "4":
                balance = self.expense_manager.add_expense(balance)
                self.save_balance(balance)

            elif choice == "5":
                self.expense_manager.view_expenses()

            elif choice == "6":
                print("Thanks for using our services")
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":
    app = BankApp()
    app.run()

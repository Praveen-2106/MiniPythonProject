# expense.py
import os

class ExpenseManager:

    FILE_PATH = os.path.join(os.path.dirname(__file__), "expenses.txt")

    def add_expense(self, balance):
        try:
            date = input("Enter date (YYYY/MM/DD): ")
            category = input("Enter category: ")
            amount = int(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero")
                return balance

            if amount > balance:
                print("Amount exceeds balance")
                return balance

            with open(self.FILE_PATH, "a") as file:
                file.write(f"{date},{category},{amount}\n")

            balance -= amount
            print("Expense added successfully")
            return balance

        except ValueError:
            print("Invalid amount")
            return balance

    def view_expenses(self):
        try:
            with open(self.FILE_PATH, "r") as file:
                lines = file.readlines()

                if not lines:
                    print("No expenses recorded")
                    return

                print("\nDate        Category    Amount")
                print("-" * 35)

                for line in lines:
                    date, category, amount = line.strip().split(",")
                    print(f"{date:<12} {category:<10} ₹{amount}")

        except FileNotFoundError:
            print("Expense file not found")

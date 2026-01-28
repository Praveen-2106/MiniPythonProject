# EXPENSES ADD, VIEW

import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "expenses.txt")


def add_expenses(balance):
    try:
        date = input("Enter the date (YYYY/MM/DD): ")
        category = input("Enter the category= ")
        # print("DEBUG: Balance before expense =", balance)
        amount = int(input("Enter the amount= "))
        # print("DEBUG: Amount entered =", amount)

        if amount <= 0:
            print("Amount must be greater than zero")
            return balance

        if amount > balance:
            print("Amount exceeds")
            return balance

        with open(FILE_PATH,"a") as file:
            file.write(f"{date},{category},{amount}\n")
            file.flush()

        balance -= amount
        print("Expenses added")
        return balance

    except ValueError:
        print("Invalid amount")
        return balance

# print("DEBUG: Writing to", FILE_PATH)


def view_expenses():
    # print("DEBUG: Reading from ->", FILE_PATH)
    try:
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
            # print("DEBUG: Raw lines ->", lines)

            if not lines:
                print("No expenses recorded")
                return

            print("\nDate        Category    Amount")
            print("-" * 35)

            for line in lines:
                line = line.strip()

                if not line or "," not in line:
                    continue

                parts = line.split(",")

                if len(parts) != 3:
                    continue

                date = parts[0].strip()
                category = parts[1].strip()
                amount = parts[2].strip()
                print(f"{date:<12} {category:<10} ₹{amount}")

    except FileNotFoundError:
        print("Expense file not found")



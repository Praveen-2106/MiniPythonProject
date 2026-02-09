# atm.py

class ATM:

    def deposit(self, balance):
        try:
            amount = int(input("Enter deposit amount: "))
            if amount <= 0:
                print("Amount must be greater than zero")
                return balance

            balance += amount
            print("Amount deposited successfully")
            return balance

        except ValueError:
            print("Invalid amount")
            return balance

    def withdraw(self, balance):
        try:
            amount = int(input("Enter withdraw amount: "))
            if amount <= 0:
                print("Amount must be greater than zero")

            elif amount > balance:
                print("Insufficient balance")

            else:
                balance -= amount
                print("Amount withdraw successfully")

            return balance

        except ValueError:
            print("Invalid amount")
            return balance

    def check_balance(self, balance):
        print(f"Your available balance = ₹ {balance}")

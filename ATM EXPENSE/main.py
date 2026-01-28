#MAIN SOURCE FILE

import atm
import expense
user_pin = "1234"
max_try = 3

def load_balance():
    try:
        with open("data.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_balance(balance):
    with open("data.txt","w") as file:
        file.write(str(balance))

def login():
    attempts = 0
    while attempts < max_try:
        pin = input("Enter your pin= ")
        if pin == user_pin:
            print("\n Login Successfully")
            return True
        else:
            attempts +=1
            print("Incorrect PIN")
    print("Too many login attempts")
    return False

def menu():
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Add Expense")
    print("5. View Expenses")
    print("6. Exit")

def main():
    balance = load_balance()

    if not login():
        return

    while True:
        menu()
        choice = input("Enter the choice: ")

        if choice == "1":
            balance = atm.deposit(balance)
            save_balance(balance)

        elif choice == "2":
            balance = atm.withdraw(balance)
            save_balance(balance)

        elif choice == "3":
           atm.check_balance(balance)

        elif choice == "4":
            balance = expense.add_expenses(balance)
            save_balance(balance)

        elif choice == "5":
            expense.view_expenses()

        elif choice == "6":
            print("Thanks fro using our services")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




import os

TRANSACTIONS_FILE = "transactions.txt"

# Make sure the file exists
if not os.path.exists(TRANSACTIONS_FILE):
    with open(TRANSACTIONS_FILE, "w") as f:
        f.write("")

def add_transaction(amount, type, description):
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(f"{type},{amount},{description}\n")

def view_balance():
    income = 0
    expenses = 0
    with open(TRANSACTIONS_FILE, "r") as file:
        for line in file:
            type, amount, _ = line.strip().split(",", 2)
            if type == "income":
                income += float(amount)
            elif type == "expense":
                expenses += float(amount)
    balance = income - expenses
    print(f"\n💰 Current Balance: R{balance:.2f}")

def view_history():
    print("\n📜 Transaction History:")
    with open(TRANSACTIONS_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No transactions yet.")
            return
        for line in lines:
            type, amount, description = line.strip().split(",", 2)
            print(f"{type.title()}: R{amount} - {description}")

def show_menu():
    while True:
        print("\n----- Budget Tracker Menu -----")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            amount = float(input("Enter income amount: R"))
            description = input("Enter income description: ")
            add_transaction(amount, "income", description)
            print("✅ Income added.")
        elif choice == "2":
            amount = float(input("Enter expense amount: R"))
            description = input("Enter expense description: ")
            add_transaction(amount, "expense", description)
            print("✅ Expense added.")
        elif choice == "3":
            view_balance()
        elif choice == "4":
            view_history()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1–5.")

# Run the app
show_menu()

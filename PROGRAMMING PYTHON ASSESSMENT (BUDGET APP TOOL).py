# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 18:18:30 2025

@author: anami
"""

#I am making a Budgeting App tool
#For the date, I want to keep data to be consistent sand saves user time

from datetime import datetime 
transactions = []     #empty list is for the client to input any transaction

def add_transaction():
    print('\n Add Transaction')
    transaction_type = input("Enter type (Income/Expense): ")
    amount = float(input("Enter amount: "))    #No dollar sign needed
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY) or leave blank for today: ")
    notes = input("Enter notes (optional): ")
    
    if not date:
        date = datetime.today().strftime("%dd-%mm-%YYYY")

    transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "date": date,
        "notes": notes
        
        }

    transactions.append(transaction)
    print("✅ Transaction added successfully!\n")

# View financial summary
def view_summary():
    income = sum(t["amount"] for t in transactions if t["type"] == "Income")
    expenses = sum(t["amount"] for t in transactions if t["type"] == "Expense")
    balance = income - expenses

    print("\n📊 Financial Summary")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}\n")

# Filter transactions by category
def filter_by_category():
    category = input("Enter category to filter by: ").strip()
    filtered = [t for t in transactions if t["category"].lower() == category.lower()]

    print(f"\n🔍 Transactions in category '{category}':")
    for t in filtered:
        print(f"{t['date']} - {t['type']}: ${t['amount']} ({t['notes']})")
    print()

# Main menu
def main():
    while True:
        print("=== Budgeting App ===")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Filter by Category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

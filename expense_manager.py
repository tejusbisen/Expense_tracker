# Functions that add, view, edit, delete and search expenses.
from validation import (get_valid_amount, get_valid_category,
                        get_valid_description, get_valid_date)

def add_expense(expenses):
    amount = get_valid_amount()
    category = get_valid_category()
    description = get_valid_description()
    date = get_valid_date()

    expenses.append({
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    })

    print("Expense added!")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i in range(len(expenses)):
        e = expenses[i]
        print(f"{i + 1}. {e['date']} | {e['category']} | Rs.{e['amount']} | {e['description']}")

def search_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\nSearch by:")
    print("1. Category")
    print("2. Keyword in description")
    choice = input("Enter choice (1-2): ")

    matches = []
    if choice == "1":
        category = get_valid_category()
        for i in range(len(expenses)):
            if expenses[i]["category"] == category:
                matches.append(i)
    elif choice == "2":
        keyword = input("Enter keyword: ").strip().lower()
        if keyword == "":
            print("Keyword cannot be empty.")
            return
        for i in range(len(expenses)):
            if keyword in expenses[i]["description"].lower():
                matches.append(i)
    else:
        print("Invalid option.")
        return

    if len(matches) == 0:
        print("No matching expenses found.")
        return

    print(f"\n--- {len(matches)} matching expense(s) ---")
    match_total = 0
    for i in matches:
        e = expenses[i]
        print(f"{i + 1}. {e['date']} | {e['category']} | Rs.{e['amount']} | {e['description']}")
        match_total += e["amount"]
    print(f"Total of matches: Rs.{match_total:.2f}")

def delete_expense(expenses):
    view_expenses(expenses)
    if len(expenses) == 0:
        return
    try:
        idx = int(input("\nEnter expense number to delete: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return
    if 0 <= idx < len(expenses):
        removed = expenses.pop(idx)
        print(f"Removed {removed['description']}")
    else:
        print("Invalid index.")

def edit_expense(expenses):
    view_expenses(expenses)
    if len(expenses) == 0:
        return
    try:
        idx = int(input("\nEnter expense number to edit: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return
    if idx < 0 or idx >= len(expenses):
        print("Invalid index.")
        return

    exp = expenses[idx]
    print("\nWhat do you want to change?")
    print("1. Amount")
    print("2. Category")
    print("3. Description")
    print("4. Date")
    choice = input("Enter choice (1-4): ")

    if choice == "1":
        exp["amount"] = get_valid_amount()
    elif choice == "2":
        exp["category"] = get_valid_category()
    elif choice == "3":
        exp["description"] = get_valid_description()
    elif choice == "4":
        exp["date"] = get_valid_date()
    else:
        print("Invalid option. Nothing changed.")
        return

    print("Expense updated!")
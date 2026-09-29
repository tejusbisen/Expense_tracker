from storage import load_expenses, save_expenses, load_budget, save_budget
from categories import CATEGORIES
from validation import (get_valid_amount, get_valid_category,
                        get_valid_description, get_valid_date,
                        get_valid_month)
expenses = []
settings = {"budget": 0.0}

expenses = []


def add_expense():
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

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    for i in range(len(expenses)):
        e = expenses[i]
        print(f"{i + 1}. {e['date']} | {e['category']} | Rs.{e['amount']} | {e['description']}")

def search_expenses():
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

def calculate_total():
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print(f"\nTotal Spent: Rs.{total}")

def category_summary():
    print("\n--- Category Summary ---")
    for cat in CATEGORIES:
        cat_total = 0
        for exp in expenses:
            if exp["category"] == cat:
                cat_total += exp["amount"]
        print(f"{cat}: Rs.{cat_total}")



def monthly_summary():
    month = get_valid_month()
    month_total = 0
    count = 0
    for exp in expenses:
        if exp["date"][3:] == month:
            month_total += exp["amount"]
            count += 1

    if count == 0:
        print(f"No expenses found for {month}.")
        return

    print(f"\n--- Summary for {month} ---")
    print(f"Number of expenses: {count}")
    print(f"Total spent: Rs.{month_total:.2f}")
    print("By category:")
    for cat in CATEGORIES:
        cat_total = 0
        for exp in expenses:
            if exp["date"][3:] == month and exp["category"] == cat:
                cat_total += exp["amount"]
        if cat_total > 0:
            print(f"  {cat}: Rs.{cat_total:.2f}")

def set_budget():
    print(f"Current monthly budget: Rs.{settings['budget']:.2f}")
    print("Enter the new monthly budget amount below.")
    settings["budget"] = get_valid_amount()
    print("Monthly budget updated!")

def budget_status():
    if settings["budget"] == 0:
        print("No budget set yet. Use the Set Budget option first.")
        return

    month = get_valid_month()
    month_total = 0
    for exp in expenses:
        if exp["date"][3:] == month:
            month_total += exp["amount"]

    remaining = settings["budget"] - month_total
    print(f"\n--- Budget for {month} ---")
    print(f"Budget: Rs.{settings['budget']:.2f}")
    print(f"Spent: Rs.{month_total:.2f}")
    if remaining >= 0:
        print(f"Remaining: Rs.{remaining:.2f}")
    else:
        print(f"WARNING: Over budget by Rs.{-remaining:.2f}")
def highest_expense():
    if len(expenses) == 0:
        print("No expenses yet.")
        return
        
    highest = expenses[0]
    for exp in expenses:
        if exp["amount"] > highest["amount"]:
            highest = exp
            
    print(f"\nHighest Expense: {highest['description']} (Rs.{highest['amount']})")

def delete_expense():
    view_expenses()
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

def edit_expense():
    view_expenses()
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

def main():
    load_expenses(expenses)
    settings["budget"] = load_budget()
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Category Summary")
        print("5. Highest Expense")
        print("6. Delete Expense")
        print("7. Edit Expense")
        print("8. Monthly Summary")
        print("9. Set Monthly Budget")
        print("10. Budget Status")
        print("11. Search Expenses")
        print("12. Save and Exit")

        choice = input("Enter choice (1-12): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            highest_expense()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            edit_expense()
        elif choice == "8":
            monthly_summary()
        elif choice == "9":
            set_budget()
        elif choice == "10":
            budget_status()
        elif choice == "11":
            search_expenses()
        elif choice == "12":
            save_expenses(expenses)
            save_budget(settings["budget"])
            print("Bye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
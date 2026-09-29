import csv
import os
from datetime import datetime
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
BUDGET_FILE = os.path.join(BASE_FOLDER, "budget.txt")
settings = {"budget": 0.0}
FILE_NAME = os.path.join(BASE_FOLDER, "expenses.csv")

CATEGORIES = ["Food", "Transport", "Education", "Shopping", "Entertainment", "Other"]
expenses = []

def load_expenses():
    skipped = 0
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)  # skip header
            for parts in reader:
                if len(parts) != 4:
                    skipped += 1
                    continue
                try:
                    amount = float(parts[0])
                    datetime.strptime(parts[3], "%d-%m-%Y")
                except ValueError:
                    skipped += 1
                    continue
                expenses.append({
                    "amount": amount,
                    "category": parts[1],
                    "description": parts[2],
                    "date": parts[3]
                })
    except FileNotFoundError:
        print("No existing expenses file found. Starting fresh.")
        return

    if skipped > 0:
        print(f"Warning: {skipped} invalid row(s) in the file were skipped.")


def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description", "Date"])
        for exp in expenses:
            writer.writerow([exp["amount"], exp["category"], exp["description"], exp["date"]])
    import os
    print("Saved to:", os.path.abspath("expenses.csv"))
    print("Expenses saved successfully!")

def load_budget():
    try:
        with open(BUDGET_FILE, "r") as file:
            settings["budget"] = float(file.read().strip())
    except (FileNotFoundError, ValueError):
        settings["budget"] = 0.0

def save_budget():
    with open(BUDGET_FILE, "w") as file:
        file.write(str(settings["budget"]))


def get_valid_date():
    while True:
        date_text = input("Enter date (DD-MM-YYYY): ").strip()
        try:
            date_obj = datetime.strptime(date_text, "%d-%m-%Y")
            return date_obj.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date. Use DD-MM-YYYY, for example 05-03-2026.")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def get_valid_category():
    print("\nCategories:")
    for i in range(len(CATEGORIES)):
        print(f"{i + 1}. {CATEGORIES[i]}")
    while True:
        try:
            cat_choice = int(input(f"Enter category choice (1-{len(CATEGORIES)}): "))
            if 1 <= cat_choice <= len(CATEGORIES):
                return CATEGORIES[cat_choice - 1]
            else:
                print(f"Please choose a number from 1 to {len(CATEGORIES)}.")
        except ValueError:
            print("Please enter a valid number.")

def get_valid_description():
    while True:
        description = input("Enter description: ").strip()
        if description == "":
            print("Description cannot be empty.")
        else:
            return description

def get_valid_date():
    while True:
        date_text = input("Enter date (DD-MM-YYYY): ").strip()
        try:
            date_obj = datetime.strptime(date_text, "%d-%m-%Y")
            return date_obj.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date. Use DD-MM-YYYY, for example 05-03-2026.")

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

def get_valid_month():
    while True:
        month_text = input("Enter month (MM-YYYY): ").strip()
        try:
            month_obj = datetime.strptime(month_text, "%m-%Y")
            return month_obj.strftime("%m-%Y")
        except ValueError:
            print("Invalid month. Use MM-YYYY, for example 09-2026.")

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
    load_expenses()
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
            save_expenses()
            save_budget()
            print("Bye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
from storage import load_expenses, save_expenses, load_budget, save_budget
from categories import CATEGORIES
from validation import (get_valid_amount, get_valid_category,
                        get_valid_description, get_valid_date,
                        get_valid_month)
from expense_manager import (add_expense, view_expenses, search_expenses,
                             delete_expense, edit_expense)
from analysis import (calculate_total, category_summary,
                      highest_expense, monthly_summary)
expenses = []
settings = {"budget": 0.0}

expenses = []



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
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            highest_expense(expenses)
        elif choice == "6":
            delete_expense(expenses)
        elif choice == "7":
            edit_expense(expenses)
        elif choice == "8":
            monthly_summary(expenses)
        elif choice == "9":
            set_budget()
        elif choice == "10":
            budget_status()
        elif choice == "11":
            search_expenses(expenses)
        elif choice == "12":
            save_expenses(expenses)
            save_budget(settings["budget"])
            print("Bye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
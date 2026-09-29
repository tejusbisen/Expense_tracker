from storage import load_expenses, save_expenses, load_budget, save_budget
from expense_manager import (add_expense, view_expenses, search_expenses,
                             delete_expense, edit_expense)
from analysis import (calculate_total, category_summary,
                      highest_expense, monthly_summary)
from budget import set_budget, budget_status
expenses = []
settings = {"budget": 0.0}

expenses = []

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
            set_budget(settings)
        elif choice == "10":
            budget_status(expenses, settings)
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
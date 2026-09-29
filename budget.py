# Functions for setting the monthly budget and checking it against spending.
from validation import get_valid_amount, get_valid_month

def set_budget(settings):
    print(f"Current monthly budget: Rs.{settings['budget']:.2f}")
    print("Enter the new monthly budget amount below.")
    settings["budget"] = get_valid_amount()
    print("Monthly budget updated!")

def budget_status(expenses, settings):
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
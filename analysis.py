# Functions that read the expenses and print reports. They never change the data.
from categories import CATEGORIES
from validation import get_valid_month

def calculate_total(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print(f"\nTotal Spent: Rs.{total:.2f}")

def category_summary(expenses):
    print("\n--- Category Summary ---")
    for cat in CATEGORIES:
        cat_total = 0
        for exp in expenses:
            if exp["category"] == cat:
                cat_total += exp["amount"]
        print(f"{cat}: Rs.{cat_total:.2f}")

def highest_expense(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return

    highest = expenses[0]
    for exp in expenses:
        if exp["amount"] > highest["amount"]:
            highest = exp

    print(f"\nHighest Expense: {highest['description']} (Rs.{highest['amount']:.2f})")

def monthly_summary(expenses):
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
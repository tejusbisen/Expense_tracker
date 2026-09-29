# Functions that ask the user for input and keep asking until it is valid.
from datetime import datetime
from categories import CATEGORIES

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

def get_valid_month():
    while True:
        month_text = input("Enter month (MM-YYYY): ").strip()
        try:
            month_obj = datetime.strptime(month_text, "%m-%Y")
            return month_obj.strftime("%m-%Y")
        except ValueError:
            print("Invalid month. Use MM-YYYY, for example 09-2026.")
# Functions that read and write the data files (expenses.csv and budget.txt).
import csv
import os
from datetime import datetime

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_FOLDER, "expenses.csv")
BUDGET_FILE = os.path.join(BASE_FOLDER, "budget.txt")

def load_expenses(expenses):
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

def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Description", "Date"])
        for exp in expenses:
            writer.writerow([exp["amount"], exp["category"], exp["description"], exp["date"]])
    print("Expenses saved successfully!")

def load_budget():
    try:
        with open(BUDGET_FILE, "r") as file:
            return float(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0.0

def save_budget(budget):
    with open(BUDGET_FILE, "w") as file:
        file.write(str(budget))
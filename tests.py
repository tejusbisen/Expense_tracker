# Simple automated tests. Run with:  python tests.py
import builtins
import os

import storage
from validation import (get_valid_amount, get_valid_category,
                        get_valid_description, get_valid_date,
                        get_valid_month)
from expense_manager import add_expense, delete_expense, edit_expense

TEST_FILE = os.path.join(storage.BASE_FOLDER, "test_expenses.csv")
TEST_BUDGET = os.path.join(storage.BASE_FOLDER, "test_budget.txt")

results = {"passed": 0, "failed": 0}
fake_answers = []


def check(name, actual, expected):
    if actual == expected:
        results["passed"] += 1
        print(f"PASS: {name}")
    else:
        results["failed"] += 1
        print(f"FAIL: {name} (expected {expected}, got {actual})")


def fake_input(prompt=""):
    # Gives back the next prepared answer instead of asking the user.
    return fake_answers.pop(0)


def set_inputs(answers):
    fake_answers.clear()
    for answer in answers:
        fake_answers.append(answer)


def remove_test_files():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    if os.path.exists(TEST_BUDGET):
        os.remove(TEST_BUDGET)


def test_storage():
    remove_test_files()

    loaded = []
    storage.load_expenses(loaded)
    check("load with missing file gives empty list", len(loaded), 0)

    original = [{"amount": 100.0, "category": "Food",
                 "description": "pens, notebook", "date": "05-09-2026"}]
    storage.save_expenses(original)
    loaded = []
    storage.load_expenses(loaded)
    check("save and load keeps a comma in the description", loaded, original)

    with open(TEST_FILE, "w") as file:
        file.write("Amount,Category,Description,Date\n")
        file.write("50,Food,good row,05-09-2026\n")
        file.write("abc,Food,bad amount,05-09-2026\n")
        file.write("50,Food,bad date,05/09/2026\n")
        file.write("50,Food\n")
    loaded = []
    storage.load_expenses(loaded)
    check("bad rows in the file are skipped", len(loaded), 1)

    check("missing budget file gives 0.0", storage.load_budget(), 0.0)
    storage.save_budget(1234.0)
    check("budget is saved and loaded", storage.load_budget(), 1234.0)
    with open(TEST_BUDGET, "w") as file:
        file.write("abc")
    check("damaged budget file gives 0.0", storage.load_budget(), 0.0)


def test_validation():
    set_inputs(["abc", "-5", "0", "25.5"])
    check("amount rejects text, negative and zero", get_valid_amount(), 25.5)

    set_inputs(["9", "abc", "2"])
    check("category rejects out-of-range and text", get_valid_category(), "Transport")

    set_inputs(["", "   ", "  lunch  "])
    check("description rejects empty and trims spaces", get_valid_description(), "lunch")

    set_inputs(["abc", "31-02-2026", "2026-03-05", "5-3-2026"])
    check("date rejects bad dates and fixes format", get_valid_date(), "05-03-2026")

    set_inputs(["13-2026", "abc", "9-2026"])
    check("month rejects bad months and fixes format", get_valid_month(), "09-2026")


def test_expense_manager():
    expenses = []

    set_inputs(["100", "1", "Lunch", "05-09-2026"])
    add_expense(expenses)
    check("add stores one expense", len(expenses), 1)
    check("add stores the correct data", expenses[0],
          {"amount": 100.0, "category": "Food",
           "description": "Lunch", "date": "05-09-2026"})

    set_inputs(["1", "1", "250"])
    edit_expense(expenses)
    check("edit changes the amount", expenses[0]["amount"], 250.0)

    set_inputs(["abc"])
    delete_expense(expenses)
    check("delete with text keeps the list", len(expenses), 1)

    set_inputs(["99"])
    delete_expense(expenses)
    check("delete with out-of-range number keeps the list", len(expenses), 1)

    set_inputs(["1"])
    delete_expense(expenses)
    check("delete removes the expense", len(expenses), 0)


def run_all_tests():
    builtins.input = fake_input
    storage.FILE_NAME = TEST_FILE
    storage.BUDGET_FILE = TEST_BUDGET

    test_storage()
    test_validation()
    test_expense_manager()

    remove_test_files()
    print(f"\n{results['passed']} passed, {results['failed']} failed")


if __name__ == "__main__":
    run_all_tests()
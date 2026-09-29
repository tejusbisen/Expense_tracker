# Expense Tracker

A simple command-line expense tracker written in Python. It lets a user record daily expenses, organise them by category, view summaries, set a monthly budget, and keep the data between runs in a CSV file.

Built as a first-year B.Tech CSE project for the VITyarthi "Build Your Own Project" course.

## Overview

Students often lose track of where their pocket money goes. This program is a small, offline tool for logging expenses and checking totals, category breakdowns, monthly spending, and budget status, with no internet, database, or extra libraries required.

## Features

- Add an expense with amount, category, description, and date
- View all expenses
- Edit any field of an existing expense
- Delete an expense
- Search expenses by category or by a keyword in the description
- View the total amount spent
- Category-wise summary
- Highest expense
- Monthly summary (total and category breakdown for a chosen month)
- Set a monthly budget and check budget status for any month, with a warning when it is exceeded
- Data is saved to `expenses.csv` and `budget.txt` and loaded on the next start

### Input validation and error handling

- Amount must be a positive number
- Category must be chosen from the numbered list
- Description cannot be empty
- Dates must be valid and in `DD-MM-YYYY` format; months in `MM-YYYY`
- Non-numeric input for menu numbers does not crash the program
- Invalid rows in `expenses.csv` are skipped with a warning
- A missing or damaged data file does not stop the program from starting

## Technologies

- Python 3 (developed with Python 3.14)
- Standard library only: `csv`, `os`, `datetime`
- Git for version control

## How to run

1. Install Python 3 from https://www.python.org
2. Download or clone this repository
3. Open a terminal in the project folder and run:

   python main.py

## Menu

| Option | Action |
|---|---|
| 1 | Add Expense |
| 2 | View Expenses |
| 3 | View Total |
| 4 | Category Summary |
| 5 | Highest Expense |
| 6 | Delete Expense |
| 7 | Edit Expense |
| 8 | Monthly Summary |
| 9 | Set Monthly Budget |
| 10 | Budget Status |
| 11 | Search Expenses |
| 12 | Save and Exit |

Note: data is written to disk only when you choose option 12.

## Data files

- `expenses.csv` with columns `Amount, Category, Description, Date`
- `budget.txt` containing a single number, the monthly budget

Both files are created in the same folder as the program.

## Testing

Run the automated tests from the project folder:

    python tests.py

The tests cover storage (save/load, commas in text, damaged rows, damaged budget file), input validation (amount, category, description, date, month) and the add, edit and delete functions. They use temporary test files, so your real data is never changed. All 17 tests should print PASS.

The report functions (total, category summary, highest expense, monthly summary, budget status) print their output, so they are checked manually with the testing checklist in the project report.
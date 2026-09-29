# Problem Statement

## Problem

Students and individuals often do not know where their money goes. Keeping records in a notebook is slow and easy to lose, and it makes it hard to see totals, category-wise spending or monthly spending. Many finance apps need internet access, accounts or ads, and are more complicated than a beginner needs.

## Proposed solution

Expense Tracker is a small offline command-line program in Python. The user records each expense with an amount, category, description and date, and the program stores it in a CSV file so it is available the next time the program runs.

## Scope

**Included**
- Recording, viewing, editing, deleting and searching expenses
- Total, category-wise and monthly summaries, and the highest expense
- A monthly budget with a warning when spending goes above it
- Input validation and safe handling of a missing or damaged data file
- Saving data to `expenses.csv` and `budget.txt`

**Not included**
- Graphical or web interface
- Multiple users, login or passwords
- Online sync or bank integration
- Charts and graphs
- Per-category budgets or recurring expenses
- Automatic backup of the data files

## Target users

- Students who want to track pocket money or a monthly allowance
- Beginners who need a simple, offline tool that runs with only Python installed

## High-level features

1. Add, view, edit, delete and search expenses
2. Total spent, category summary, highest expense
3. Monthly summary
4. Monthly budget and budget status with an over-budget warning
5. Persistent storage in CSV and text files
6. Input validation and error handling
7. Automated tests
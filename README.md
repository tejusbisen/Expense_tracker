# Expense Tracker - College Project Documentation

**Subject:** Computer Programming / Python Programming  
**Level:** First-Year B.Tech CSE  
**Application Type:** Console / CLI Application  
**Language:** Python 3 (Standard Library Only)  

---

## 1. Project Objective
The objective of the **Expense Tracker** project is to create an easy-to-use, console-based personal finance management application that allows students and individuals to record, categorize, inspect, and analyze their daily expenditures without requiring complex external software, databases, or internet connectivity.

---

## 2. Problem Statement
Many students and individuals struggle to track where their daily pocket money or monthly allowance goes. Manual record-keeping in notebooks is tedious, prone to loss, and lacks fast computation like category breakdowns or finding peak expenditures. Existing commercial apps are often overly complex, require internet, contain ads, or raise privacy concerns. There is a need for a lightweight, beginner-friendly, offline console tool to log, summarize, and persist daily expenses easily.

---

## 3. Python Concepts Used
This project strictly utilizes core, foundational Python concepts suitable for a first-year undergraduate student:

1. **Variables and Data Types:**
   - Float and integer for amounts (`float`, `int`).
   - Strings for descriptions, dates, and categories (`str`).
2. **Data Structures:**
   - **Dictionaries:** Each expense is stored as a dictionary mapping keys (`"amount"`, `"category"`, `"description"`, `"date"`) to values.
   - **Lists:** All expense dictionaries are stored inside a dynamic master list `expenses = [...]`.
3. **Control Flow Statements:**
   - `if`, `elif`, `else` conditions for menu choices and boundary checking.
4. **Loops:**
   - `while` loops for continuous menu navigation and robust input re-prompting.
   - `for` loops for iterating over expense records, calculating totals, finding highest expenses, and formatting output.
5. **Functions and Modular Programming:**
   - Each major requirement is isolated into an independent function with clear parameters and responsibilities.
6. **Exception Handling:**
   - `try-except ValueError` blocks to prevent crashes when non-numeric inputs are entered.
7. **File Handling & Built-in Modules:**
   - `csv` module for saving and loading tabular expense data into `expenses.csv`.
   - `os.path.exists()` to check file existence before attempting to read.
   - `sys.stdout.reconfigure()` for cross-platform UTF-8 terminal encoding.

---

## 4. Complete Program Architecture & Functions

| Function Name | Parameters | Purpose |
| :--- | :--- | :--- |
| `load_expenses()` | None | Reads existing data from `expenses.csv` at program start. Returns list of expense dicts. |
| `save_expenses(expenses)` | `expenses` (list) | Writes all recorded expense dicts into `expenses.csv`. |
| `format_amount(amount)` | `amount` (float) | Formats numeric amounts cleanly (e.g., `₹250` or `₹250.50`). |
| `add_expense(expenses)` | `expenses` (list) | Prompts user for positive amount, category (1-6), description, date, and appends dictionary. |
| `view_expenses(expenses)` | `expenses` (list) | Displays all recorded expenses in an aligned table format. |
| `calculate_total(expenses)`| `expenses` (list) | Sums all amounts using a loop and displays total expenditure. |
| `category_summary(expenses)`| `expenses` (list)| Aggregates expenditure per category and displays summary. |
| `highest_expense(expenses)`| `expenses` (list) | Finds and displays the expense with the maximum amount. |
| `delete_expense(expenses)` | `expenses` (list) | Displays numbered expenses and safely deletes the chosen entry. |
| `main()` | None | Displays menu and handles user selection in a continuous loop. |

---

## 5. Algorithm

### Overall Program Flow
1. **Start:** Launch program.
2. **Initialize:** Call `load_expenses()`. If `expenses.csv` exists, read records into `expenses` list; else, start with an empty list.
3. **Menu Loop:** Display menu options (1 to 8).
4. **User Choice:** Read choice from user:
   - **Choice 1 (Add):** Validate amount > 0, choose category 1-6, input non-empty description and date. Append `{amount, category, description, date}` to list.
   - **Choice 2 (View):** If empty, print message; otherwise loop and print aligned table.
   - **Choice 3 (Total):** Initialize `total = 0`. Iterate through list, `total += exp["amount"]`. Print `total`.
   - **Choice 4 (Category Summary):** Initialize summary dictionary for each category with 0. Iterate through expenses and accumulate. Print category totals.
   - **Choice 5 (Highest):** If list empty, notify. Otherwise, set `highest = expenses[0]`. Iterate from index 1 to end; if current amount > highest amount, update `highest`. Print details.
   - **Choice 6 (Delete):** Display expenses with index numbers. Take expense number. If valid, remove using `.pop(index - 1)`. If 0, cancel.
   - **Choice 7 (Save):** Open `expenses.csv` in write mode and write headers and rows using `csv.writer`.
   - **Choice 8 (Exit):** Ask if user wishes to save. Save if yes. Print exit message and break loop.
5. **Stop:** Program terminates.

---

## 6. Advantages, Limitations, and Future Scope

### Advantages
- **Lightweight & Fast:** Runs instantly in any standard terminal with zero external dependencies.
- **Data Persistence:** Expenses are preserved in CSV format between program restarts.
- **Robust Error Handling:** Invalid numbers, negative amounts, or out-of-range choices do not crash the program.
- **Easy to Explain:** Uses only clear procedural code and basic data structures without confusing abstractions.

### Limitations
- **Console Interface Only:** Does not feature a graphical window (GUI) or mobile app interface.
- **Single User:** Designed for personal local use; does not support multi-user authentication.
- **Basic Filtering:** Does not yet filter expenses by custom date ranges or search by keyword.

### Future Scope
- Add date filtering (e.g., view expenses for a particular month or year).
- Add monthly budget limits with warning alerts when budget is exceeded.
- Export visual charts using Python's `matplotlib` library.
- Build a lightweight graphical interface using `tkinter`.

---

## 7. Viva Questions & Answers

1. **Q: Why did you choose a list of dictionaries to store expenses?**  
   *A:* A dictionary allows us to store related attributes of an expense using key-value pairs (`amount`, `category`, `description`, `date`). A list allows us to maintain a dynamic, ordered collection of these expense records.

2. **Q: How does the program ensure it does not crash when a user types text instead of a number for the amount?**  
   *A:* We use a `try-except ValueError` block. When `float(user_input)` is called on invalid text, Python raises a `ValueError`, which is caught by the `except` block, displaying a friendly error message and prompting the user again.

3. **Q: How does data persistence work in this project?**  
   *A:* We use Python's built-in `csv` module. When saving, `csv.writer` writes each dictionary's values as a row in `expenses.csv`. On startup, `load_expenses()` reads the file back and populates the list.

4. **Q: Why do we use `newline=""` when opening a CSV file in Python?**  
   *A:* On Windows, omitting `newline=""` can cause the CSV writer to insert an extra blank line between rows due to differences in line-ending translations (`\r\n` vs `\n`).

5. **Q: What is the purpose of `if __name__ == "__main__":`?**  
   *A:* It ensures that `main()` runs only when the script is executed directly, and not when the script is imported as a module into another Python file.

6. **Q: How do you find the highest expense without using built-in functions like `max()`?**  
   *A:* We assume the first expense is the highest (`highest = expenses[0]`), and then use a `for` loop to compare each subsequent expense's amount. If an expense has a larger amount, we update `highest`.

7. **Q: How is the category summary calculated?**  
   *A:* We initialize a dictionary with all predefined categories having a sum of `0.0`. We iterate through the list of expenses, check the category of each record, and add the amount to that category's total.

8. **Q: How does the delete functionality work?**  
   *A:* The user chooses a 1-based number from the displayed list. We subtract 1 to get the 0-based index and use `expenses.pop(index)` to safely remove and return the selected item.

9. **Q: What happens if `expenses.csv` does not exist when the program starts?**  
   *A:* We check `if not os.path.exists(FILE_NAME):` using the `os` module. If it does not exist, `load_expenses()` simply returns an empty list without throwing a `FileNotFoundError`.

10. **Q: What is the time complexity of viewing total expenses or category summary?**  
    *A:* Both run in $O(N)$ linear time complexity, where $N$ is the number of expenses, because we iterate through the list once.

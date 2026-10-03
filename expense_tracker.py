"""Simple Personal Expense Tracker (command line).

Run with:  python expense_tracker.py
Data is saved to expenses.json in the same folder.
"""

import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


# ---------- Saving and loading ----------

def load_expenses():
    """Load expenses from the JSON file. Return an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("Could not read the data file. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Write all expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)


# ---------- Input helpers ----------

def get_amount():
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a number (for example 12.50).")


def get_date():
    """Ask for a date in YYYY-MM-DD format. Press Enter for today."""
    while True:
        text = input("Date (YYYY-MM-DD, Enter for today): ").strip()
        if not text:
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date. Use the format YYYY-MM-DD.")


# ---------- Features ----------

def add_expense(expenses):
    amount = get_amount()
    category = input("Category (food, transport, bills...): ").strip().lower() or "other"
    date = get_date()
    note = input("Note (optional): ").strip()

    expenses.append(
        {"amount": amount, "category": category, "date": date, "note": note}
    )
    save_expenses(expenses)
    print("Expense added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    print(f"\n{'#':<4}{'Date':<12}{'Category':<14}{'Amount':>10}  Note")
    print("-" * 56)
    for i, e in enumerate(sorted(expenses, key=lambda x: x["date"]), start=1):
        print(f"{i:<4}{e['date']:<12}{e['category']:<14}{e['amount']:>10.2f}  {e['note']}")
    print("-" * 56)
    print(f"{'Total':<30}{sum(e['amount'] for e in expenses):>10.2f}")


def summary(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    by_category = {}
    by_month = {}
    for e in expenses:
        by_category[e["category"]] = by_category.get(e["category"], 0) + e["amount"]
        month = e["date"][:7]  # "YYYY-MM"
        by_month[month] = by_month.get(month, 0) + e["amount"]

    print("\nTotals by category:")
    for cat, total in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<14}{total:>10.2f}")

    print("\nTotals by month:")
    for month, total in sorted(by_month.items()):
        print(f"  {month:<14}{total:>10.2f}")


def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)
    ordered = sorted(expenses, key=lambda x: x["date"])
    try:
        number = int(input("\nNumber of the expense to delete (0 to cancel): "))
    except ValueError:
        print("Please enter a number.")
        return

    if number == 0:
        return
    if 1 <= number <= len(ordered):
        expenses.remove(ordered[number - 1])
        save_expenses(expenses)
        print("Expense deleted.")
    else:
        print("That number is not in the list.")


# ---------- Main menu ----------

def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. Summary")
        print("4. Delete an expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()

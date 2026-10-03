# 💰 Personal Expense Tracker

A simple command-line expense tracker written in Python. Add your spending, view it in a table, and see totals by category and by month. Your data is saved automatically, so nothing is lost when you close the program.

## Features

- Add expenses with amount, category, date, and an optional note
- View all expenses in a neat table with a running total
- Summary of spending by category and by month
- Delete an expense you entered by mistake
- Data saved to a local `expenses.json` file
- Input validation for amounts and dates

## Requirements

- Python 3.7 or newer
- No external libraries needed (uses only the standard library)

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. **Run the program**
   ```bash
   python expense_tracker.py
   ```
   On Mac/Linux you may need `python3 expense_tracker.py`.

## Usage

When you start the program, you'll see this menu:

```
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Summary
4. Delete an expense
5. Exit
```

Type a number from 1 to 5 and press Enter.

### Example

```
#   Date        Category      Amount  Note
--------------------------------------------------------
1   2026-10-01  food           12.50  Lunch
2   2026-10-02  transport       3.00  Bus fare
--------------------------------------------------------
Total                          15.50
```

## Project Structure

```
expense-tracker/
├── expense_tracker.py   # main program
├── expenses.json        # created automatically when you add an expense
└── README.md
```

## Concepts Practiced

- Functions, loops, and conditionals
- Lists and dictionaries
- Reading and writing JSON files
- Working with dates using `datetime`
- Error handling with `try/except`

## Ideas for Improvement

- [ ] Edit an existing expense
- [ ] Set a monthly budget and warn when it is exceeded
- [ ] Export a report to CSV
- [ ] Add charts with `matplotlib`
- [ ] Filter expenses by date range or category

## Contributing

Suggestions and improvements are welcome. Fork the repo, make your changes, and open a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

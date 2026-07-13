# 💰 Expense Tracker

A simple command-line Expense Tracker written in Python.

## Features

- Add a new expense
- Categorize expenses
- Save expenses to a CSV file
- View spending by category
- View total spending
- Track remaining monthly budget
- Calculate daily budget remaining

## Project Structure

```
expense-tracker/
│── expense_tracker.py
│── expense.py
│── README.md
│── .gitignore
```

## Requirements

- Python 3.10+

No external libraries are required.

## How to Run

Clone the repository

```bash
git clone https://github.com/<your-username>/expense-tracker.git
```

Navigate to the project

```bash
cd expense-tracker
```

Run the application

```bash
python expense_tracker.py
```

## Example

```
Enter expense name: Coffee
Enter expense amount: 5.25

Select a category:
1. 🍔 Food
2. 🏠 Home
3. 💼 Work
4. 🎉 Fun
5. ✨ Misc

Expenses By Category
🍔 Food: $25.75

Total Spent: $125.75
Budget Remaining: $1874.25
Budget Per Day: $62.47
```

## Future Improvements

- Edit existing expenses
- Delete expenses
- Monthly reports


## License

MIT

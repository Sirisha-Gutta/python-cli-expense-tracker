from expense import Expense
import calendar
import datetime


def main():
    expense_file_path = "expenses.csv"
    budget = 2000

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. View Summary")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            expense = get_user_expense()
            save_expense_to_file(expense, expense_file_path)

        elif choice == "2":
            expenses = load_expenses(expense_file_path)
            display_expenses(expenses)

        elif choice == "3":
            edit_expense(expense_file_path)

        elif choice == "4":
            delete_expense(expense_file_path)

        elif choice == "5":
            summarize_expenses(expense_file_path, budget)

        elif choice == "6":
            break

        else:
            print("Invalid option.")


def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                new_expense = Expense(
                    name=expense_name, category=selected_category, amount=expense_amount
                )
                return new_expense
        except:
                print("Invalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path: str) -> None:
    print(f"🎯 Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def load_expenses(expense_file):
    expenses = []

    with open(expense_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                name, amount, category = line.strip().split(",")

                expenses.append(
                    Expense(
                        name=name,
                        amount=float(amount),
                        category=category,
                    )
                )

    return expenses


def save_all_expenses(expenses, expense_file):
    with open(expense_file, "w", encoding="utf-8") as f:
        for expense in expenses:
            f.write(
                f"{expense.name},{expense.amount},{expense.category}\n"
            )


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\nCurrent Expenses\n")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense.name} | "
            f"${expense.amount:.2f} | "
            f"{expense.category}"
        )


def edit_expense(expense_file):
    expenses = load_expenses(expense_file)

    if not expenses:
        print("No expenses to edit.")
        return

    display_expenses(expenses)

    try:
        index = int(input("\nExpense number to edit: ")) - 1

        if index not in range(len(expenses)):
            print("Invalid selection.")
            return

        expense = expenses[index]

        print("\nPress Enter to keep existing value.\n")

        name = input(f"Name ({expense.name}): ")
        if name:
            expense.name = name

        amount = input(f"Amount ({expense.amount}): ")
        if amount:
            expense.amount = float(amount)

        category = input(f"Category ({expense.category}): ")
        if category:
            expense.category = category

        save_all_expenses(expenses, expense_file)

        print("\nExpense updated successfully!")

    except ValueError:
        print("Invalid input.")


def delete_expense(expense_file):
    expenses = load_expenses(expense_file)

    if not expenses:
        print("No expenses to delete.")
        return

    display_expenses(expenses)

    try:
        index = int(input("\nExpense number to delete: ")) - 1

        if index not in range(len(expenses)):
            print("Invalid selection.")
            return

        deleted = expenses.pop(index)

        save_all_expenses(expenses, expense_file)

        print(f"\nDeleted '{deleted.name}' successfully.")

    except ValueError:
        print("Invalid input.")


def summarize_expenses(expense_file_path: str, budget: float) -> None:
    print(f"🎯 Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
    else:
        daily_budget = remaining_budget
    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
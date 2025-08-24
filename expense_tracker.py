from Expense import Expense   # Importing the Expense class from expense.py
import calendar
import datetime

def main():
    print(f"Running Expense Tracker! 💰💵")
    expense_file_path = "expenses.csv"  # File where all expenses will be stored
    budget = 2000                       # Fixed monthly budget

    # Step 1: Get expense details from user
    expense = get_user_expense()
    print(expense)   # This calls Expense.__repr__() and shows expense in readable format

    # Step 2: Save the expense to file
    save_expense_to_file(expense, expense_file_path)

    # Step 3: Summarize all expenses stored in file
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print(f"Getting user expense")

    # Ask user for name of expense and amount spent
    expense_name = input("Enter Expense name:")
    expense_amount = float(input("Enter Expense amount: "))

    # Categories (with emojis)
    expense_categories = [
        "🍔Food", 
        "🏠Home", 
        "👨‍💻Work", 
        "🥳Fun", 
        "✨Misc"
    ]

    # Keep asking until valid category is chosen
    while True:
        print(f"Select a Category: ")
        for i, category_name in enumerate(expense_categories):
            # Show numbered list like: 1. 🍔Food
            print(f"{i + 1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        # User selects a category by entering its number
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        # If input is valid, create Expense object and return it
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense              
        else:
            # If invalid, ask again
            print("Invalid category. Please try again!")  


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")

    # Open file in append mode ("a") so each expense is added at the end
    # encoding="utf-8" ensures emojis are saved correctly
    with open(expense_file_path, "a", encoding="utf-8") as f:
        # Write expense as CSV (comma-separated values)
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print(f"Summarizing user expense")
    expenses = []   # Will hold Expense objects read from file

    # Step 1: Read the file back into Expense objects
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)         

    # Step 2: Group expenses by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    # Step 3: Print summary by category
    print("Expense by category")
    for key, amount in amount_by_category.items():
        print(f"    {key}: ${amount:.2f}")
    
    # Step 4: Print total spent
    total_spent = sum([x.amount for x in expenses])
    print(f"You spent ${total_spent:.2f} this month!")

    # Step 5: Show remaining budget
    remaining_budget = budget - total_spent
    print(f"Budget Remaining: ${remaining_budget:.2f}")   

    # Step 6: Calculate daily budget for remaining days in month
    now = datetime.datetime.now()  # Current date and time
    days_in_month = calendar.monthrange(now.year, now.month)[1]  # total days in month
    remaining_days = days_in_month - now.day   # days left in current month

    daily_budget = remaining_budget / remaining_days
    print(f"Remaining budget per day : ${daily_budget:.2f}")


# Only run main() if this file is executed directly
if __name__ == "__main__":
    main()

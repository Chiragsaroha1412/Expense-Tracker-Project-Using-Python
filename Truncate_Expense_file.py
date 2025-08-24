def clear_expense_file(expense_file_path="expenses.csv"):
    # Open file in write mode 'w' → this will clear all data
    with open(expense_file_path, "w", encoding="utf-8") as f:
        pass  # just open and close, no need to write anything
    print(f"✅ All expense records deleted from {expense_file_path}")

if __name__ == "__main__":
    clear_expense_file()

#This file just defines a class called Expense (a blueprint for an expense entry).

class Expense:
    # Constructor method to initialize an Expense object
    def __init__(self, name, category, amount) -> None:
        self.name = name          # expense name (string)
        self.category = category  # category chosen by user (Food, Home, etc.)
        self.amount = amount      # amount spent (float)

    # Representation method -> tells Python how to display Expense objects when printed
    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"

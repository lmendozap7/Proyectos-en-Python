class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        self.balance -= amount
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount) and self.withdraw(
            amount, f"Transfer to {category.name}"
        ):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            amount = f"{entry['amount']:.2f}"
            description = entry["description"][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.balance:.2f}"
        return title + items + total


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spent_per_category = []
    for category in categories:
        spent = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                spent += -entry["amount"]
        spent_per_category.append(spent)
    total_spent = sum(spent_per_category)

    percentages = []
    for spent in spent_per_category:
        if total_spent == 0:
            percentage = 0
        else:
            percentage = int((spent / total_spent) * 100)
            percentage = percentage - (percentage % 10)
        percentages.append(percentage)

    for level in range(100, -1, -10):
        chart += f"{level:>3}|"
        for percentage in percentages:
            if percentage >= level:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_len = max(len(category.name) for category in categories)
    for i in range(max_name_len):
        chart += "    "
        for category in categories:
            if i < len(category.name):
                chart += f" {category.name[i]} "
            else:
                chart += "   "
        chart += " "
        if i < max_name_len - 1:
            chart += "\n"

    return chart


food = Category("Food")
food.deposit(500, "deposit")
food.withdraw(12.15, "groceries")
food.withdraw(60.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
auto = Category("Auto")


food.deposit(1000, "initial deposit")
clothing.deposit(1000, "initial deposit")
auto.deposit(1000, "initial deposit")


food.withdraw(60, "groceries")
clothing.withdraw(20, "clothes")
auto.withdraw(10, "maintenance")

print(create_spend_chart([food, clothing, auto]))

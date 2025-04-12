import csv
import os

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = ['Food', 'Transport', 'Entertainment', 'Bills', 'Others']
        self.file_path = 'expenses.csv'
        self.load_expenses()

    def add_expense(self, amount, category, date='', description=''):
        if category not in self.categories:
            category = 'Others'
        
        expense = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        return True

    def get_expenses_by_category(self, category):
        result = []
        for exp in self.expenses:
            if exp['category'] == category:
                result.append(exp)
        return result

    def get_expenses_by_date(self, date):
        result = []
        for exp in self.expenses:
            if exp['date'] == date:
                result.append(exp)
        return result

    def get_total_by_category(self):
        totals = {}
        for category in self.categories:
            category_expenses = self.get_expenses_by_category(category)
            totals[category] = sum(exp['amount'] for exp in category_expenses)
        return totals

    def save_expenses(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'amount', 'category', 'description'])
            writer.writeheader()
            writer.writerows(self.expenses)

    def load_expenses(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            self.expenses = []
            for row in reader:
                row['amount'] = float(row['amount'])
                self.expenses.append(row)

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nSimple Expense Tracker Menu:")
        print("1. Add New Expense")
        print("2. View Expenses by Category")
        print("3. View Expenses by Date")
        print("4. View Category Totals")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                amount = float(input("How much did you spend? ₦"))
                print("\nAvailable Categories:")
                for i, cat in enumerate(tracker.categories, 1):
                    print(f"{i}. {cat}")
                category = input("Enter category name: ")
                date = input("Enter date (e.g., 2023-12-25): ")
                description = input("What did you buy? (optional): ")
                
                tracker.add_expense(amount, category, date, description)
                print("Expense saved!")
            except ValueError:
                print("Please enter a valid amount!")

        elif choice == '2':
            print("\nAvailable Categories:")
            for cat in tracker.categories:
                print(f"- {cat}")
            category = input("Which category do you want to see? ")
            expenses = tracker.get_expenses_by_category(category)
            if expenses:
                print(f"\nExpenses for {category}:")
                for exp in expenses:
                    print(f"₦{exp['amount']:.2f} on {exp['date']} - {exp['description']}")
            else:
                print("No expenses found in this category.")

        elif choice == '3':
            date = input("Enter date to view (e.g., 2023-12-25): ")
            expenses = tracker.get_expenses_by_date(date)
            if expenses:
                print(f"\nExpenses on {date}:")
                for exp in expenses:
                    print(f"₦{exp['amount']:.2f} for {exp['category']} - {exp['description']}")
            else:
                print("No expenses found on this date.")

        elif choice == '4':
            totals = tracker.get_total_by_category()
            for category, total in totals.items():
                print(f"{category}: ₦{total:.2f}")

        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"
        self.categories = ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]
        self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.expenses = json.load(file)
                print("Loaded existing expenses")
            except:
                self.expenses = []
        else:
            self.expenses = []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=2)
    
    def add_expense(self):
        """Add a new expense"""
        print("\n" + "="*40)
        print("          ADD NEW EXPENSE")
        print("="*40)
        
        try:
            # Get amount in INR
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            # Show categories
            print("\nCategories:")
            for i, category in enumerate(self.categories, 1):
                print(f"{i}. {category}")
            
            # Get category choice
            try:
                choice = int(input("\nChoose category (1-6): "))
                if 1 <= choice <= 6:
                    category = self.categories[choice - 1]
                else:
                    print("❌ Please choose 1-6!")
                    return
            except ValueError:
                print("❌ Please enter a number!")
                return
            
            # Get description
            description = input("Enter description: ").strip()
            if not description:
                description = "No description"
            
            # Create expense
            expense = {
                'amount': amount,
                'category': category,
                'description': description,
                'date': datetime.now().strftime("%Y-%m-%d")
            }
            
            self.expenses.append(expense)
            self.save_expenses()
            print(f"✅ Expense added: {category} - ₹{amount:.2f}")
            
        except ValueError:
            print("❌ Please enter a valid number for amount!")
    
    def view_expenses(self):
        """View all expenses"""
        if not self.expenses:
            print("\n📭 No expenses found!")
            return
        
        print("\n" + "="*50)
        print("                 ALL EXPENSES")
        print("="*50)
        
        total = 0
        for i, expense in enumerate(self.expenses, 1):
            print(f"{i:2}. {expense['date']} | {expense['category']:12} | ₹{expense['amount']:7.2f} | {expense['description']}")
            total += expense['amount']
        
        print("="*50)
        print(f"TOTAL: ₹{total:.2f}")
    
    def view_by_category(self):
        """View expenses by category"""
        if not self.expenses:
            print("\n📭 No expenses found!")
            return
        
        category_totals = {}
        for expense in self.expenses:
            category = expense['category']
            if category in category_totals:
                category_totals[category] += expense['amount']
            else:
                category_totals[category] = expense['amount']
        
        print("\n" + "="*40)
        print("       SPENDING BY CATEGORY")
        print("="*40)
        
        total = 0
        for category, amount in category_totals.items():
            print(f"  {category}: ₹{amount:.2f}")
            total += amount
        
        print("-" * 40)
        print(f"  TOTAL: ₹{total:.2f}")
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*40)
        print("    💰 MONTHLY EXPENSE TRACKER (INR)")
        print("="*40)
        print("1. ➕ Add New Expense")
        print("2. 📋 View All Expenses")
        print("3. 📊 View by Category")
        print("4. 🚪 Exit")
        print("="*40)
    
    def run(self):
        """Main program loop"""
        print("🎉 Welcome to Monthly Expense Tracker!")
        print("💵 All amounts in Indian Rupees (INR)")
        print("💾 Your data is automatically saved!")
        
        while True:
            self.show_menu()
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.view_by_category()
            elif choice == '4':
                print("\n👋 Thank you for using Expense Tracker!")
                print("💾 Your data has been saved to 'expenses.json'")
                break
            else:
                print("Please enter 1, 2, 3, or 4!")

# Run the program
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
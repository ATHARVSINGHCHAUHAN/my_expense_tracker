# Class Diagram

## Main Class: ExpenseTracker

### Class Description
The `ExpenseTracker` class is the core component that manages all expense tracking operations, data persistence, and user interactions.

### Class Structure
```python
class ExpenseTracker:
    # Attributes
    expenses: List[Dict]
    filename: str
    categories: List[str]
    
    # Methods

    
    __init__(self)

    load_expenses(self) -> None

    save_expenses(self) -> None

    add_expense(self) -> None

    view_expenses(self) -> 
    
    view_by_category(self) -> None

    backup_data(self) -> None

    show_menu(self) -> None

    run(self) -> None

Attribute Details

expenses: List[Dict]

Type: List of dictionaries

Description: Stores all expense records in memory

Structure: Each dictionary contains:

amount: float - Expense amount

category: str - Expense category

description: str - Expense description

date: str - Date in YYYY-MM-DD format

filename: str
Type: String

Description: Name of the JSON file for data storage

Default Value: "expenses.json"

categories: List[str]
Type: List of strings

Description: Available expense categories

Values: ["Food", "Transport", "Entertainment", "Bills", "Shopping", "Other"]

Method Details
__init__(self)
Purpose: Constructor method to initialize the object

Operations:

Initializes empty expenses list

Sets filename to "expenses.json"

Defines expense categories

Loads existing expenses from file

load_expenses(self) -> None
Purpose: Load expenses from JSON file into memory

Error Handling: If file doesn't exist or is corrupted, starts with empty list

File Operations: Reads from expenses.json

save_expenses(self) -> None
Purpose: Save current expenses to JSON file

File Operations: Writes to expenses.json with indentation for readability

Data Format: JSON array of expense objects

add_expense(self) -> None
Purpose: Add a new expense with user input

User Interaction:

Prompts for amount, category, description

Validates all inputs

Shows success/error messages

Validation:

Amount must be positive number

Category must be valid choice (1-6)

Description cannot be empty

view_expenses(self) -> None
Purpose: Display all expenses in formatted table

Formatting: Shows date, category, amount, description in columns

Calculations: Computes and displays total spending

view_by_category(self) -> None
Purpose: Show spending breakdown by category

Calculations: Groups expenses by category and sums amounts

Output: Category-wise totals and grand total

backup_data(self) -> None
Purpose: Create timestamped backup of expense data

File Naming: expenses_backup_YYYYMMDD_HHMM.json

Use Case: Data protection and recovery

show_menu(self) -> None
Purpose: Display main navigation menu

Layout: Clear numbered options with emojis for better UX

Options: Add, View, Analyze, Backup, Exit

run(self) -> None
Purpose: Main program execution loop

Flow Control: Continuous menu display until user exits

Error Handling: Catches invalid menu choices



Data Relationships
Composition Relationship
text
ExpenseTracker "has" 1..* Expense records
Dependency Relationship
text
ExpenseTracker "depends on" JSON file storage
Association Relationship
text
ExpenseTracker "uses" Category list for classification
Class Diagram in Text Format
text
┌─────────────────────────────────────┐
│           ExpenseTracker            │
├─────────────────────────────────────┤
│ - expenses: List[Dict]              │
│ - filename: str = "expenses.json"   │
│ - categories: List[str]             │
├─────────────────────────────────────┤
│ + __init__()                        │
│ + load_expenses() -> None           │
│ + save_expenses() -> None           │
│ + add_expense() -> None             │
│ + view_expenses() -> None           │
│ + view_by_category() -> None        │
│ + backup_data() -> None             │
│ + show_menu() -> None               │
│ + run() -> None                     │
└─────────────────────────────────────┘
Design Patterns Used
Singleton Pattern
Only one instance of ExpenseTracker runs at a time

Manages all application state centrally

Repository Pattern
Separates data persistence logic from business logic

JSON file acts as the data repository
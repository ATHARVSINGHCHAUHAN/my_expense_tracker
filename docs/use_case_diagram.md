# Use Case Diagram

## Actors
- **Primary Actor**: User (student/individual managing expenses)

## Use Cases

### UC1: Add New Expense
- **Description**: User adds a new financial expense record
- **Pre-condition**: Application is running
- **Post-condition**: Expense is saved to persistent storage
- **Main Flow**:
  1. User selects "Add Expense" from menu
  2. System prompts for amount, category, description
  3. User provides required information
  4. System validates and saves expense
  5. System confirms successful addition

### UC2: View All Expenses
- **Description**: User views complete expense history
- **Pre-condition**: At least one expense exists
- **Post-condition**: Expenses are displayed in formatted list
- **Main Flow**:
  1. User selects "View All Expenses"
  2. System retrieves all expenses from storage
  3. System formats and displays expenses chronologically
  4. System shows total expenditure

### UC3: View Category-wise Summary
- **Description**: User analyzes spending by category
- **Pre-condition**: At least one expense exists
- **Post-condition**: Category breakdown is displayed
- **Main Flow**:
  1. User selects "View by Category"
  2. System groups expenses by category
  3. System calculates category totals
  4. System displays category-wise summary

### UC4: Exit Application
- **Description**: User safely exits the application
- **Pre-condition**: Application is running
- **Post-condition**: All data is saved, application closes

## Relationships
- User can initiate all use cases
- All use cases depend on system being operational
- View use cases (UC2, UC3) depend on expense data existence
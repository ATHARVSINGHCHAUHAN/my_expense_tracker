# Workflow Diagram

## Main Program Workflow
Start Application → Load Existing Data → Display Main Menu →
↓
User Selection → Process Selection → Display Results →
↓
(Repeat until Exit) → Save Data → Close Application



## Detailed Workflows

### Add Expense Workflow
[Start Add Expense]
↓
[Prompt for Amount] → [Validate Amount] → If Invalid: Show Error → Return to Menu
↓
[Valid Amount] → [Display Categories] → [Get Category Choice]
↓
[Validate Choice] → If Invalid: Show Error → Return to Menu
↓
[Valid Choice] → [Prompt for Description] → [Create Expense Object]
↓
[Save to JSON File] → [Show Success Message] → [Return to Menu]



### View Expenses Workflow
[Start View Expenses]
↓
[Check if Expenses Exist] → If None: Show "No Expenses" → Return to Menu
↓
[Expenses Exist] → [Retrieve All Expenses] → [Calculate Total]
↓
[Format Display] → [Show Expense List] → [Show Total] → [Return to Menu]



### View by Category Workflow
[Start Category View]
↓
[Check if Expenses Exist] → If None: Show "No Expenses" → Return to Menu
↓
[Expenses Exist] → [Group by Category] → [Calculate Category Totals]
↓
[Calculate Grand Total] → [Display Category Breakdown] → [Return to Menu]



### Exit Application Workflow
[Start Exit Process]
↓
[Save All Data] → [Create Backup] → [Close Application]



## Error Handling Workflow
[User Input Received] → [Validate Input] → If Valid: Process Normally
↓
[If Invalid] → [Show Error Message] → [Return to Previous Step]



## Data Flow Description

### Normal Flow
1. **User initiates action** through menu selection
2. **System validates input** and processes request
3. **Data is retrieved/manipulated** as needed
4. **Results are formatted** and displayed to user
5. **Control returns** to main menu

### Alternative Flow (Errors)
1. **Invalid input detected** during validation
2. **Error message displayed** with guidance
3. **User returned to previous step** to correct input
4. **Process repeats** until valid input provided

### Data Persistence Flow
1. **Data changes occur** (add/modify expenses)
2. **Immediate save triggered** to JSON file
3. **Backup created** for important operations
4. **Confirmation provided** to user
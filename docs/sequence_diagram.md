# Sequence Diagram

## Sequence Diagram: Add New Expense

### Participants
- **User**: Application user
- **UI Layer**: User interface component
- **Business Logic**: ExpenseTracker class methods
- **Data Storage**: JSON file system

### Sequence Flow

User UI Layer Business Logic Data Storage
| | | |
|--1. Select Add Expense-->| | |
| | | |
| |--2. show_menu()-->| |
| | | |
| |<-3. Display Menu--| |
| | | |
|--4. Enter Amount-------->| | |
| | | |
| |--5. validate_input()-->| |
| | | |
| |<-6. Valid Amount--| |
| | | |
| |--7. display_categories()-->| |
| | | |
|--8. Select Category----->| | |
| | | |
| |--9. validate_category()-->| |
| | | |
| |<-10. Valid Category-------| |
| | | |
|--11. Enter Description-->| | |
| | | |
| |--12. create_expense()-->| |
| | | |
| | |--13. save_expenses()-->|
| | | |
| | |<-14. Write to JSON---|
| | | |
| |<-15. Success Msg--| |
| | | |
|<-16. Show Confirmation---| | |




### Step-by-Step Description

#### 1-3: Menu Display
1. **User** selects "Add Expense" option from main menu
2. **UI Layer** calls `show_menu()` method
3. **Business Logic** returns formatted menu display

#### 4-6: Amount Input & Validation
4. **User** enters expense amount
5. **UI Layer** validates input using `validate_input()` method
6. **Business Logic** returns validation result

#### 7-10: Category Selection
7. **UI Layer** displays available categories
8. **User** selects category number
9. **Business Logic** validates category choice
10. Returns valid category name

#### 11-16: Description & Saving
11. **User** enters expense description
12. **Business Logic** creates expense object with current date
13. Calls `save_expenses()` to persist data
14. **Data Storage** writes to JSON file
15. **Business Logic** returns success message
16. **UI Layer** displays confirmation to user

## Sequence Diagram: View All Expenses

### Sequence Flow


User UI Layer Business Logic Data Storage
| | | |
|--1. Select View Expenses->| | |
| | | |
| |--2. load_expenses()-->| |
| | | |
| | |--3. Read JSON File->|
| | | |
| | |<-4. Return Data----|
| | | |
| |--5. calculate_totals()-->| |
| | | |
| |<-6. Formatted Data-------| |
| | | |
|<-7. Display Expenses-----| | |



## Sequence Diagram: Error Handling

### Sequence Flow (Invalid Input)

User UI Layer Business Logic Data Storage
| | | |
|--1. Enter Invalid Input-->| | |
| | | |
| |--2. validate_input()-->| |
| | | |
| |<-3. Validation Error--| |
| | | |
| |--4. show_error()-->| |
| | | |
|<-5. Error Message---------| | |
| | | |
|--6. Retry Input---------->| | |



## Key Interactions

### Data Flow
- **User Input** → Validation → Processing → Storage
- **Data Retrieval** → Processing → Formatting → Display

### Error Flow
- **Invalid Input** → Validation → Error Message → Retry Opportunity

### Success Flow
- **Valid Input** → Processing → Storage → Confirmation

## Timing Considerations

### Optimal Timing
- **User Response**: Expected within 10 seconds per input
- **System Processing**: Less than 1 second for all operations
- **File I/O**: Less than 500ms for read/write operations

### Error Timing
- **Validation**: Immediate feedback (less than 100ms)
- **Error Recovery**: User can retry immediately




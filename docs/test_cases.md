# Test Cases

## Test Category 1: Core Functionality Tests

### TC-001: Add Valid Expense
**Test Case ID**: TC-001  
**Test Objective**: Verify that a valid expense can be added successfully  
**Pre-condition**: Application is running, no specific data requirements  
**Test Steps**:
1. Launch the application
2. Select "Add New Expense" option (1)
3. Enter amount: 150.50
4. Select category: 1 (Food)
5. Enter description: "Lunch at cafeteria"
6. Observe confirmation message

**Expected Result**: 
- Success message: "Expense added: Food - ₹150.50"
- Expense appears in view list
- Data saved to expenses.json file

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

### TC-002: Add Expense with Zero Amount
**Test Case ID**: TC-002  
**Test Objective**: Verify system rejects zero or negative amounts  
**Pre-condition**: Application is running  
**Test Steps**:
1. Select "Add New Expense"
2. Enter amount: 0
3. Attempt to proceed

**Expected Result**: 
- Error message: " Amount must be positive!"
- Return to main menu
- No expense created

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

### TC-003: Add Expense with Invalid Category
**Test Case ID**: TC-003  
**Test Objective**: Verify system handles invalid category selection  
**Pre-condition**: Application is running  
**Test Steps**:
1. Select "Add New Expense"
2. Enter valid amount: 100
3. Enter invalid category: 7
4. Observe system response

**Expected Result**: 
- Error message: " Please choose 1-6!"
- Return to main menu
- No expense created

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

## Test Category 2: Data Viewing Tests

### TC-004: View Empty Expenses List
**Test Case ID**: TC-004  
**Test Objective**: Verify proper message when no expenses exist  
**Pre-condition**: No expenses in the system (fresh installation or data cleared)  
**Test Steps**:
1. Launch application
2. Select "View All Expenses" (2)
3. Observe display

**Expected Result**: 
- Message: "📭 No expenses found!"
- Clean return to main menu

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

### TC-005: View Expenses with Data
**Test Case ID**: TC-005  
**Test Objective**: Verify expenses display correctly with proper formatting  
**Pre-condition**: At least 2 expenses added to system  
**Test Steps**:
1. Add multiple expenses with different categories
2. Select "View All Expenses"
3. Verify display format and calculations

**Expected Result**: 
- All expenses displayed in chronological order
- Proper column formatting (Date, Category, Amount, Description)
- Correct total calculation displayed
- Clear section headers and borders

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

### TC-006: Category-wise Analysis
**Test Case ID**: TC-006  
**Test Objective**: Verify category breakdown calculation  
**Pre-condition**: Multiple expenses in different categories  
**Test Steps**:
1. Add expenses: Food ₹200, Transport ₹100, Food ₹150
2. Select "View by Category" (3)
3. Verify category totals

**Expected Result**: 
- Food: ₹350.00
- Transport: ₹100.00
- Grand Total: ₹450.00
- Proper formatting with section headers

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

## Test Category 3: Data Persistence Tests

### TC-007: Data Persistence Across Sessions
**Test Case ID**: TC-007  
**Test Objective**: Verify data survives application restart  
**Pre-condition**: Several expenses added in previous session  
**Test Steps**:
1. Add multiple expenses
2. Exit application properly
3. Restart application
4. View all expenses

**Expected Result**: 
- All previously added expenses visible
- Data intact and accurately loaded
- No data corruption or loss

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

### TC-008: Backup File Creation
**Test Case ID**: TC-008  
**Test Objective**: Verify backup functionality works  
**Pre-condition**: Some expenses in the system  
**Test Steps**:
1. Select backup option (if available) or trigger backup
2. Check file system for backup file
3. Verify backup file content

**Expected Result**: 
- Backup file created with timestamped name
- Backup contains all current expenses
- File in valid JSON format

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

## Test Category 4: Error Handling Tests

### TC-009: Invalid Menu Selection
**Test Case ID**: TC-009  
**Test Objective**: Verify system handles invalid menu choices  
**Pre-condition**: Application running at main menu  
**Test Steps**:
1. Enter invalid menu option: 9
2. Observe system response
3. Verify application doesn't crash

**Expected Result**: 
- Error message: "Please enter 1, 2, 3, or 4!"
- Return to main menu
- Application continues running normally

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

### TC-010: Non-numeric Amount Input
**Test Case ID**: TC-010  
**Test Objective**: Verify system handles text input for amounts  
**Pre-condition**: Application at amount prompt  
**Test Steps**:
1. Select "Add New Expense"
2. Enter text instead of number: "one hundred"
3. Observe system response

**Expected Result**: 
- Error message: " Please enter a valid number for amount!"
- Return to main menu
- No application crash

**Actual Result**: [To be filled after execution]  
**Status**: [Pass/Fail]  
**Notes**: [Any observations during testing]

## Test Execution Summary

### Test Results
| Test Case | Objective | Status | Notes |
|-----------|-----------|--------|-------|
| TC-001 | Add Valid Expense | | |
| TC-002 | Zero Amount Rejection | | |
| TC-003 | Invalid Category Handling | | |
| TC-004 | Empty List View | | |
| TC-005 | Data Display | | |
| TC-006 | Category Analysis | | |
| TC-007 | Data Persistence | | |
| TC-008 | Backup Functionality | | |
| TC-009 | Invalid Menu Handling | | |
| TC-010 | Text Input Handling | | |

### Test Coverage
- **Functional Coverage**: 100% of core features tested
- **Error Handling**: All major error scenarios covered
- **Data Integrity**: Complete data lifecycle verification
- **User Interface**: All user interactions validated
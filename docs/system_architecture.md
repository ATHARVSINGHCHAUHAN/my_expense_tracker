# System Architecture Design

## Architecture Overview
The Expense Tracker follows a **3-Tier Layered Architecture** for clear separation of concerns.

## Architecture Diagram

## Component Details

### 1. Presentation Layer
- **Responsibility**: User interaction and display
- **Components**: 
  - Command-line interface
  - Menu navigation system
  - Input/output formatting

### 2. Business Logic Layer
- **Responsibility**: Core application functionality
- **Components**:
  - ExpenseTracker class
  - Expense management operations
  - Category analysis algorithms
  - Input validation rules

### 3. Data Storage Layer
- **Responsibility**: Data persistence and retrieval
- **Components**:
  - JSON file handler
  - Data serialization/deserialization
  - Backup file management

## Data Flow
1. **User Input** → Presentation Layer (receives and validates)
2. **Valid Data** → Business Logic (processes and computes)
3. **Processed Data** → Data Storage (saves persistently)
4. **Retrieved Data** → Business Logic (for analysis)
5. **Formatted Results** → Presentation Layer (displays to user)
# Monthly Budget Calculator

This project helps users calculate their monthly budget based on their income and expenses. It calculates the tax based of South Africa's personal income tax bracket then calculates the expenses based on the average amount spent on expenses in each category.
## Features

- Calculate annual tx based on user's monthly income.
- Break down expenses into categories such as utilities, rent, transport, and more.
- Display net income after tax and expenses.
- Option to enter a new user code and income.

## Requirements

- Python 3.12.9

## How It Works

1. **Enter Income**: You can enter your gross monthly income (before tax).
2. **Tax Calculation**: The program calculates tax based on predefined tax brackets for different income levels.
3. **Expense Calculation**: The program calculates expenses for different categories (e.g., rent, transport, healthcare) based on percentages of the income.
4. **Display Results**: The program displays the total expenses and net income after tax and expenses.

## Usage

1. Clone or download the repository. (```
```
 git clone [Ko5quer/Budget_Calculator](https://github.com/Ko5quer/Budget_Calculator)
```
2. Open a terminal and navigate to the directory containing the Python file.
3. Run the Python script and follow the prompts:
   ```bash
   python Main.py
   ```

# Sample Output
Budget Portal
________________________

    1. Create New Entry 
    0. Exit 

Select an option: 1
Enter user code: user123
Enter gross income before tax: 50000

------------------------------------------------------------
                    Monthly Budget
____________________________________________________________

                        Income
------------------------------------------------------------
Gross Monthly Income (Before Tax): R50000.0
Gross Monthly Income (After Tax): R46000.0
------------------------------------------------------------

                        Expenses
------------------------------------------------------------
Utilities:         R2300.00
Rent/housing:     R6900.00
Transport:        R13800.00
Healthcare:       R1380.00
Groceries:        R4600.00
Communication:    R920.00
Total Expenses:   R33500.00
------------------------------------------------------------

Net Income: R12500.0
____________________________________________________________


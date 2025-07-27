# Monthly Budget Calculator Program
# Author: [Wisit Malaob]
# Date: [27/7/2025]
# Purpose: To calculate and report user's monthly income and expenses

# ===== 1. Get user input =====
monthly_income = float(input("Monthly income (THB): "))
rent_cost = float(input("Monthly rent/housing cost (THB): "))
food_budget = int(input("Monthly food budget (THB): "))
transportation_cost = float(input("Monthly transportation expenses (THB): "))
entertainment_budget = int(input("Monthly entertainment budget (THB): "))
emergency_fund_percent = float(input("Emergency fund (%): "))
investment_percent = float(input("Investment (%): "))

# ===== 2. Calculate all values =====

# Fixed and variable expenses
fixed_expenses = rent_cost + transportation_cost
variable_expenses = food_budget + entertainment_budget
total_expenses = fixed_expenses + variable_expenses

# Remaining income after expenses
remaining_income = monthly_income - total_expenses

# Emergency fund and investment
emergency_fund = monthly_income * (emergency_fund_percent / 100)
investment_amount = monthly_income * (investment_percent / 100)

# Available money for savings
available_for_savings = remaining_income - emergency_fund - investment_amount

# Expense ratio (as percentage of income)
expense_ratio = (total_expenses / monthly_income) * 100

# ===== 3. Display the output =====

print("\n=== MONTHLY BUDGET REPORT ===")
print("Income: {:.2f} THB".format(monthly_income))
print("Fixed Expenses: {:.2f} THB".format(fixed_expenses))
print("Variable Expenses: {:.2f} THB".format(variable_expenses))
print("Total Expenses: {:.2f} THB".format(total_expenses))
print("Remaining: {:.2f} THB".format(remaining_income))

print("\n=== SAVINGS SUMMARY ===")
print("Emergency Fund ({:.1f}%): {:.2f} THB".format(emergency_fund_percent, emergency_fund))
print("Investment ({:.1f}%): {:.2f} THB".format(investment_percent, investment_amount))
print("Available for Savings: {:.2f} THB".format(available_for_savings))

print("\n=== ANALYSIS ===")
print("Expense-to-Income Ratio: {:.2f}%".format(expense_ratio))

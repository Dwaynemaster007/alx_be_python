# Get user input for income and expenses
monthly_income_str = input("Enter your monthly income: ")
monthly_expenses_str = input("Enter your total monthly expenses: ")

# Convert input strings to floating-point numbers for calculations
monthly_income = float(monthly_income_str)
monthly_expenses = float(monthly_expenses_str)

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05

# Project annual savings, including interest
projected_annual_savings = monthly_savings * 12 * (1 + annual_interest_rate)

# Print the results in the required format
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")

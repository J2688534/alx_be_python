# Ask the user how much money they earn each month
monthly_income = input("Enter your monthly income: ")

# Ask how much they spend each month
monthly_expenses = input("Enter your total monthly expenses: ")

# Convert the input to numbers
monthly_income = float(monthly_income)
monthly_expenses = float(monthly_expenses)

# Calculate how much money they save each month
monthly_savings = monthly_income - monthly_expenses

# Calculate savings for a year (12 months)
yearly_savings = monthly_savings * 12

# Add 5% interest to the yearly savings
projected_savings = yearly_savings + (yearly_savings * 0.05)

# Show the results
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")

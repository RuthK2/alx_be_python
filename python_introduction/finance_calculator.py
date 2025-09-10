monthly_income = float(input("Enter your monthly income: "))
total_monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
print("Your monthly savings are: $" + str(monthly_savings))
interest = monthly_savings * 12 * 0.05
projected_savings = (monthly_savings * 12) + interest
print("Projected savings after one year, with interest, is: $" + str(projected_savings))

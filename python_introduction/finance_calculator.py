#Ask user to input financial details

monthly_income = int(input("Enter your monthly income: "))

monthly_expenses = int(input("Enter your monthly expenses: "))

#Calculating monthly savings

monthly_savings = monthly_income - monthly_expenses

#Projecting annual savings

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Print the results
print(f"Your monthly savings are: {monthly_savings}")

print(f"Projected savings after one year, with interest, is: {projected_annual_savings}")
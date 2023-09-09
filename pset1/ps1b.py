# inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# state variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
months = 0

# loop
while current_savings < down_payment:
    if months != 0 and months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += monthly_salary * portion_saved + current_savings * r / 12
    months += 1

# result
print("Number of months: " + str(months))

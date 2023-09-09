# input
starting_salary = float(input("Enter the starting salary: "))

# state variables
semi_annual_rate = 0.07
r = 0.04
house_cost = 1000000
down_payment = 0.25 * house_cost
current_savings = 0
months = 36
epsilon = 100
num_guesses = 0
low = 0
high = 10000
portion_saved = (high + low) / 2

# bisection search
while abs(current_savings - down_payment) >= epsilon:
    current_savings = 0
    annual_salary = starting_salary
    monthly_salary = annual_salary / 12
    for month in range(1, months + 1):
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * portion_saved / 10000
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_rate
            monthly_salary = annual_salary / 12
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved
    portion_saved = (high + low) / 2
    num_guesses += 1
    if num_guesses > 13:
        break

# output
if num_guesses > 13:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: " + str(portion_saved / 10000))
    print("Steps in bisection search: " + str(num_guesses))

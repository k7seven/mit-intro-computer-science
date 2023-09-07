import math

# ask user for input for x and y
x = input("Enter number for x: ")
y = input("Enter number for y: ")

# transform x and y into integers
x = int(x)
y = int(y)

# calculate x**y and log(x)
power_result = int(x) ** int(y)
log_result = math.log(x, 2)

# print results
print("x**y = ", power_result)
print("log(x) = ", log_result)

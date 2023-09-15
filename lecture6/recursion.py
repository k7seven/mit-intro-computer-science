'''
Recursion ->
          ->
          ->
          ->
'''

# problem 1 - print name n times
def print_name(n, name):
    if(n == 0):
        return
    print(name)
    print_name(n - 1, name)

# print_name(2, "k77")

# problem 2 - print from 1 to n
def print_1_to_n(i, n):
    print(i)
    if(i >= n):
        return
    print_1_to_n(i + 1, n)

# print_1_to_n(1, 10)

# problem 3 - print from n to 1
def print_n_to_1(n):
    if(n == 0):
        return
    print(n)
    print_n_to_1(n - 1)

# print_n_to_1(20)

# problem 4 - print from 1 to n using backtracking
def print_1_to_n_backtracking(n):
    if(n < 1):
        return
    print_1_to_n_backtracking(n - 1)
    print(n)

# print_1_to_n_backtracking(10)

# problem 5 - print from n to 1 using backtracking
def print_n_to_1_backtracking(i, n):
    if(i > n):
        return
    print_n_to_1_backtracking(i + 1, n)
    print(i)

# print_n_to_1_backtracking(1, 10)

# problem 6 - print the sum of 1 to i (Parameterised way)
def sum_1_to_n(i, sum):
    if (i < 1):
        print(sum)
        return
    sum_1_to_n(i - 1, sum + i)

# sum_1_to_n(6, 0)

# problem 7 - print the sum of 1 to i (Functional way)
def sum_1_to_n_functional_way(n):
    if (n == 0):
        return 0
    return n + sum_1_to_n_functional_way(n - 1)

# print(sum_1_to_n_functional_way(5))

# problem 8 - print the factorial of n
def factorial(n):
    if (n == 1):
        return 1
    return n * factorial(n - 1)

print(factorial(4))

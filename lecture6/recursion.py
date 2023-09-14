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

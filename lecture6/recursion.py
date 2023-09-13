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

print_name(2, "k77")

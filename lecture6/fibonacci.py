def fibonacci(n):
    if(n <= 1):
        return n
    last = fibonacci(n - 1)
    second_last = fibonacci(n - 2)
    return last + second_last

print(fibonacci(10))

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
fib_n = fibonacci(n)
print(f"The {n}th element of the Fibonacci sequence is: {fib_n}")

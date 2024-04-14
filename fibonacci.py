def fibonacci(n):
    if n <= 0:
        raise ValueError("Invalid input. Input must be a positive integer.")

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example usage
n = 10
fib = fibonacci(n)
print(f"The {n}th Fibonacci number is: {fib}")

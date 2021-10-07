n = int(input())

def factorial_recursive(n):
    return n * factorial_recursive(n-1) if n > 1 else 1

print(factorial_recursive(n))

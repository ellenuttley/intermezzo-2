# File: lib/factorial.py

def factorial(n):
    product = 1
    while n > 0:
        n -= 1
        product *= n
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 0

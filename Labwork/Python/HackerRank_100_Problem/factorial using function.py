def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact

num = 5
print("Problem 42 - Factorial:", factorial(num))

# Output:
# Problem 42 - Factorial: 120

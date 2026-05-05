a, b = 56, 98
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
print(f"Problem 29 - GCD of {a} and {b} is {gcd}")


# Output inside code:
# Problem 29 - GCD of 56 and 98 is 14

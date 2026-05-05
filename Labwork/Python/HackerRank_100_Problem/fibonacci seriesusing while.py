N = 10
a, b = 0, 1
fib_series = []
count = 0
while count < N:
    fib_series.append(a)
    a, b = b, a + b
    count += 1

print(f"Problem 27 - First {N} Fibonacci numbers:", fib_series)
# Output inside code:
# Problem 27 - First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
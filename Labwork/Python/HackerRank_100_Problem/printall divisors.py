N = 10
fib_series = [0, 1]
for i in range(2, N):
    fib_series.append(fib_series[i-1] + fib_series[i-2])
print(f"Problem 37 - First {N} Fibonacci numbers:", fib_series)
# Output inside code:
# Problem 37 - First 10 Fibonacci numbers: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

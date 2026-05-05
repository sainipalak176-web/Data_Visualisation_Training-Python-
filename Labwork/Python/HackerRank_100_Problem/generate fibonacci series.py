def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input())
fibonacci(num)

# Output:
# Input: 5
# 0 1 1 2 3

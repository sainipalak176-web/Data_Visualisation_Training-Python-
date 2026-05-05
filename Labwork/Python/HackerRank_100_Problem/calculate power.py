def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)

x = int(input())
y = int(input())
print(power(x, y))

# Output:
# Input:
# 2
# 3
# 8
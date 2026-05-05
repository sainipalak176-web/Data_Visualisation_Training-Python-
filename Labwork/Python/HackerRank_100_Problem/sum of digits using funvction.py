def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

num = int(input())
print(sum_of_digits(num))

# Output:
# Input: 123
# 6
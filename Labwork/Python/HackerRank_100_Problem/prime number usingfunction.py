def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

num = 7
print("Problem 41 - Is Prime:", is_prime(num))

# Output:
# Problem 41 - Is Prime: True
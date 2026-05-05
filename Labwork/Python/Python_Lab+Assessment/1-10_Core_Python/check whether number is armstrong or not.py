def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** power
    
    return total == n

# Input
n = 153

# Output
print(is_armstrong(n))
# True
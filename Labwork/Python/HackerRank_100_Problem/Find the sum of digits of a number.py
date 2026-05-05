# Find the sum of digits of a number.
# Given number
num = 1234
original_num = num
sum_digits = 0

# Calculate sum of digits
while num > 0:
    sum_digits += num % 10
    num //= 10

print(f"Sum of digits of {original_num} is:", sum_digits)



#output:
"""Sum of digits of 1234 is: 10"""
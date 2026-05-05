#reverse a given number.
# Given number
num = 12345
original_num = num
reversed_num = 0

# Reverse the number
while num > 0:
    reversed_num = reversed_num * 10 + (num % 10)
    num //= 10

print(f" Reverse of {original_num} is:", reversed_num)



#output:
"""Reverse of 12345 is: 54321"""
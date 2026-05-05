#find the largest of three number.
# Test numbers
num1 = 12
num2 = 45
num3 = 30

# Finding largest
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is", largest)

#output:
""" the largest number is 45"""


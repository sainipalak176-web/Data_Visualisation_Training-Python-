#check whether a number is divisible by both 3 and 5.
# List of numbers to test
numbers = [15]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(f" {num} is divisible by both 3 and 5")
    else:
        print(f" {num} is NOT divisible by both 3 and 5")



        #output:
        """15 is divisible by both 3 and 5"""



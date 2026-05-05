# Check whether a number is even or odd without modulus operator.
# Given numbers to test
numbers = [4, 7, 0, -5]

for num in numbers:
    # Using bitwise AND operator to check even/odd
    if num & 1 == 0:
        print(f"Problem 8 - {num} is Even")
    else:
        print(f"Problem 8 - {num} is Odd")


        #output:
        """4 is even"""
        """7 is odd"""
        """0 is even"""
        """-5 is odd"""

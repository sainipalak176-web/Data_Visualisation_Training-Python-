# Define range
lower = 10
upper = 50

# List of numbers to test
numbers = [5, 10, 25, 50, 60]

for num in numbers:
    if lower <= num <= upper:
        print(f"Problem 19 - {num} lies within the range {lower}-{upper}")
    else:
        print(f"Problem 19 - {num} does NOT lie within the range {lower}-{upper}")

# Output inside code:
# Problem 19 - 5 does NOT lie within the range 10-50
# Problem 19 - 10 lies within the range 10-50
# Problem 19 - 25 lies within the range 10-50
# Problem 19 - 50 lies within the range 10-50
# Problem 19 - 60 does NOT lie within the range 10-50
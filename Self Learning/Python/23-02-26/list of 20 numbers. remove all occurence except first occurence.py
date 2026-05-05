# Program to remove all occurrences of a number from a list
# except its first occurrence

numbers = [1, 2, 3, 4, 5, 3, 6, 3, 7, 8,
           9, 3, 10, 11, 12, 3, 13, 14, 15, 3]

print("Original List:", numbers)

num = int(input("Enter a number to remove duplicates: "))

found = False
new_list = []

for i in numbers:
    if i == num:
        if not found:
            new_list.append(i)
            found = True
    else:
        new_list.append(i)

print("Updated List:", new_list)

# Output:
""" Original List: [1, 2, 3, 4, 5, 3, 6, 3, 7, 8, 9, 3, 10, 11, 12, 3, 13, 14, 15, 3]"""
"""Enter a number to remove duplicates: 3"""
""" Updated List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]"""
# Input
lst = [1, 2, 2, 3, 4, 3, 5]

# Output
result = []
for i in lst:
    if i not in result:
        result.append(i)

print("List without duplicates:", result)
# List without duplicates: [1, 2, 3, 4, 5]
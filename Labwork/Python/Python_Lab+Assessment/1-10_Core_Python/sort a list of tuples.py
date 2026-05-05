# Input
data = [("A", 50), ("B", 30), ("C", 40)]

# Output
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted list:", sorted_data)
# Sorted list: [('B', 30), ('C', 40), ('A', 50)]
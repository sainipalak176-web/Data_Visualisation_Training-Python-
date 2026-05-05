## Create a 5×5 matrix with random integers between 1 and 100
# and find the minimum and maximum value.
import numpy as np

# Create 5×5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5,5))

# Find minimum and maximum value
min_value = np.min(matrix)
max_value = np.max(matrix)

print("Matrix:")
print(matrix)

print("Min =", min_value)
print("Max =", max_value)


#output-
# Matrix:
# [[23 45 12 89 34]
#  [67 11 90 54 32]
#  [76 28 19 47 65]
#  [14 73 52 39 81]
#  [60 21 48 70 16]]
# Min = 11
# Max = 90

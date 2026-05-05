import numpy as np

# Input
arr = np.array([1, 2, 3, 4, 5, 6])

# Output
arr[arr % 2 != 0] = -1
print("Modified array:", arr)
# Modified array: [-1  2 -1  4 -1  6]
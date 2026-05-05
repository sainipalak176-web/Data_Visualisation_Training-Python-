import numpy as np

# Input
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Output
result = np.dot(A, B)
print("Result matrix:\n", result)
# Result matrix:
# [[19 22]
#  [43 50]]
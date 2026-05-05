import numpy as np

# Input
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Output
diag = np.diag(arr)
print("Diagonal elements:", diag)
# Diagonal elements: [1 5 9]
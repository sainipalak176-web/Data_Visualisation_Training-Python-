import numpy as np

# Input
arr = np.array([10, 25, 30, 5, 40])
value = 20

# Output
indices = np.where(arr > value)
print("Indices:", indices)
# Indices: (array([1, 2, 4]),)
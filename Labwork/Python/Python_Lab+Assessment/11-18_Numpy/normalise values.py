import numpy as np

# Input
arr = np.array([10, 20, 30, 40, 50])

# Output
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Normalized array:", normalized)
# Normalized array: [0.   0.25 0.5  0.75 1.  ]
# Input
d = {'a': 1, 'b': 2, 'c': 3}

# Output
swapped = {v: k for k, v in d.items()}
print("Swapped dictionary:", swapped)
# Swapped dictionary: {1: 'a', 2: 'b', 3: 'c'}
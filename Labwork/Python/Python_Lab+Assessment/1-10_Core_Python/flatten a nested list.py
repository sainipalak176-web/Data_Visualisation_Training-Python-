def flatten_list(nested):
    flat = []
    
    for i in nested:
        if isinstance(i, list):
            flat.extend(flatten_list(i))
        else:
            flat.append(i)
    
    return flat

# Input
nested_list = [1, [2, [3, 4], 5], 6]

# Output
print("Flattened list:", flatten_list(nested_list))
# Flattened list: [1, 2, 3, 4, 5, 6]
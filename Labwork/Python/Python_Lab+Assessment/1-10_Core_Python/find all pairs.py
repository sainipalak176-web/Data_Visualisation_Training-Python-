def find_pairs(lst, target):
    pairs = []
    
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    
    return pairs

# Input
lst = [2, 4, 3, 5, 7]
target = 7

# Output
print("Pairs:", find_pairs(lst, target))
# Pairs: [(2, 5), (4, 3)]
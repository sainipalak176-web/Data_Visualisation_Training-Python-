def sort_by_values(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

print(sort_by_values(d))

# Output:
# Input:
# 3
# Ram
# 85
# Shyam
# 92
# Mohan
# 88
# {'Ram': 85, 'Mohan': 88, 'Shyam': 92}
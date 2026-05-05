def sort_by_keys(d):
    return dict(sorted(d.items()))

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

print(sort_by_keys(d))

# Output:
# Input:
# 3
# c
# 30
# a
# 10
# b
# 20
# {'a': 10, 'b': 20, 'c': 30}
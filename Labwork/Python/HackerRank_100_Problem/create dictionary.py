def create_dict(keys, values):
    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d

n = int(input())
keys = []
values = []
for i in range(n):
    keys.append(input())
for i in range(n):
    values.append(int(input()))

print(create_dict(keys, values))

# Output:
# Input:
# 3
# a b c
# 10 20 30
# {'a': 10, 'b': 20, 'c': 30}
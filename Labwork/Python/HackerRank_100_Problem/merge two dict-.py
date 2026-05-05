def merge_dict(d1, d2):
    result = {}
    for k in d1:
        result[k] = d1[k]
    for k in d2:
        result[k] = d2[k]
    return result

n1 = int(input())
d1 = {}
for i in range(n1):
    key = input()
    value = int(input())
    d1[key] = value

n2 = int(input())
d2 = {}
for i in range(n2):
    key = input()
    value = int(input())
    d2[key] = value

print(merge_dict(d1, d2))

# Output:
# Input:
# 2
# a
# 10
# b
# 20
# 2
# b
# 30
# c
# 40
# {'a': 10, 'b': 30, 'c': 40}
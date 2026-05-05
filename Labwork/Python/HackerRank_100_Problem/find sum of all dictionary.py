def sum_values(d):
    total = 0
    for v in d.values():
        total += v
    return total

n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

print(sum_values(d))

# Output:
# Input:
# 3
# a
# 10
# b
# 20
# c
# 30
# 60
def key_with_max_value(d):
    return max(d, key=d.get)

n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

print(key_with_max_value(d))

# Output:
# Input:
# 3
# a
# 10
# b
# 25
# c
# 15
# b
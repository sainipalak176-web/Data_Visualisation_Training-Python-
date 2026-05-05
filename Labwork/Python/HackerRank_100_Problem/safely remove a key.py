def safe_remove(d, key):
    d.pop(key, None)
    return d

n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

key_to_remove = input()
print(safe_remove(d, key_to_remove))

# Output:
# Input:
# 2
# a
# 10
# b
# 20
# a
# {'b': 20}
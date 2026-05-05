def key_exists(d, key):
    return key in d

n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

search_key = input()
if key_exists(d, search_key):
    print("Key Exists")
else:
    print("Key Does Not Exist")

# Output:
# Input:
# 2
# a
# 10
# b
# 20
# b
# Key Exists
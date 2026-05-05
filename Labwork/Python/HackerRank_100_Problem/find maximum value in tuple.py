def max_in_tuple(t):
    return max(t)

n = int(input())
tpl = ()
lst = []
for i in range(n):
    lst.append(int(input()))
tpl = tuple(lst)

print(max_in_tuple(tpl))

# Output:
# Input:
# 4
# 10 25 5 40
# 40
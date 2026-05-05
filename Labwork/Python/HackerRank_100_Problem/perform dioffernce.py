def difference_set(s1, s2):
    return s1 - s2

n1 = int(input())
s1 = set()
for i in range(n1):
    s1.add(int(input()))

n2 = int(input())
s2 = set()
for i in range(n2):
    s2.add(int(input()))

print(difference_set(s1, s2))

# Output:
# Input:
# 3
# 1 2 3
# 3
# 2 3 4
# {1}
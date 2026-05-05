def largest(lst):
    return max(lst)

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(largest(lst))

# Output:
# Input:
# 5
# 10 25 5 40 15
# 40
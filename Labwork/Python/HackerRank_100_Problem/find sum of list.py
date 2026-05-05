def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(sum_list(lst))

# Output:
# Input:
# 4
# 10 20 30 40
# 100
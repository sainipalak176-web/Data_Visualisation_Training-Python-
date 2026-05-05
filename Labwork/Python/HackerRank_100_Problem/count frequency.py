def frequency(lst):
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    return freq

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

print(frequency(lst))

# Output:
# Input:
# 5
# 1 2 2 3 1
# {1: 2, 2: 2, 3: 1}
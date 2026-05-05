def find_topper(d):
    topper = max(d, key=d.get)
    return topper, d[topper]

n = int(input())
marks = {}
for i in range(n):
    name = input()
    score = int(input())
    marks[name] = score

name, score = find_topper(marks)
print(name, score)

# Output:
# Input:
# 3
# Ram
# 85
# Shyam
# 92
# Mohan
# 88
# Shyam 92
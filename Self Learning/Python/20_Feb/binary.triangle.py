n = 4
for i in range(1, n+1):
    for j in range(i):
        print((i+j) % 2, end="")
    print()

#output
#1
#01
#101
#0101
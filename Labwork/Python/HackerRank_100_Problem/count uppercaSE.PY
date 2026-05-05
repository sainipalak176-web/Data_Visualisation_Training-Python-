def count_upper_lower(s):
    upper = lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

text = input()
u, l = count_upper_lower(text)
print("Uppercase:", u)
print("Lowercase:", l)

# Output:
# Input:
# PyThOn
# Uppercase: 3
# Lowercase: 3
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

text = input()
print(count_vowels(text))

# Output:
# Input: education
# 5
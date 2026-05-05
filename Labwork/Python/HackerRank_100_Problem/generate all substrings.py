def substrings(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            print(s[i:j])

text = input()
substrings(text)

# Output:
# Input:
# abc
# a
# ab
# abc
# b
# bc
# c
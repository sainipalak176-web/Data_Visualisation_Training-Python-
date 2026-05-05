def are_anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

str1 = input()
str2 = input()

if are_anagrams(str1, str2):
    print("Anagrams")
else:
    print("Not Anagrams")

# Output:
# Input:
# listen
# silent
# Anagrams
def longest_word(s):
    words = s.split()
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

sentence = input()
print(longest_word(sentence))

# Output:
# Input:
# python is very powerful
# powerful
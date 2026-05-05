def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

text = input()
print(char_frequency(text))

# Output:
# Input:
# hello
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
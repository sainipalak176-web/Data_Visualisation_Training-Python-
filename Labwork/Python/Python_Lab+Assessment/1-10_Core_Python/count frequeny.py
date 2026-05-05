def char_frequency(s):
    freq = {}
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    return freq

# Input
string = "hello"

# Output
print("Character Frequency:", char_frequency(string))


# Expected Output:
# Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
def remove_spaces(s):
    result = ""
    for ch in s:
        if ch != ' ':
            result += ch
    return result

text = input()
print(remove_spaces(text))

# Output:
# Input:
# hello world
# helloworld
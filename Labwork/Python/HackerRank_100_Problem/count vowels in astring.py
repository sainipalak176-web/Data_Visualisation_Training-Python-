string = "Hello World"
vowels = 'aeiouAEIOU'
count = sum(1 for ch in string if ch in vowels)
print(f"Problem 35 - Number of vowels in '{string}' is {count}")
# Output inside code:
# Problem 35 - Number of vowels in 'Hello World' is 3
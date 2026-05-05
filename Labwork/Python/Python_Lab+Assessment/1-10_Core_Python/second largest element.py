def second_largest(arr):
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second

# Input
arr = [10, 20, 4, 45, 99]

# Output
print("Second largest element is:", second_largest(arr))


# Expected Output:
# Second largest element is: 45
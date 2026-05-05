def common_elements(list1, list2):
    result = []
    
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    
    return result

# Input
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Output
print("Common elements:", common_elements(list1, list2))
# Common elements: [3, 4, 5]
def find_min(my_list):
    if len(my_list) == 0:  # If the list is empty, return None
        return None
    if len(my_list) == 1:  # Base case: if there's only one element, return it
        return my_list[0]
    
    # Compare the first two elements and store the smaller one in the second index
    temp = my_list[0] if my_list[0] < my_list[1] else my_list[1]
    my_list[1] = temp  # Replace the second element with the smaller value
    
    # Recursive call to process the remaining list
    return find_min(my_list[1:])

# Test cases
print(find_min([]))  # Output: None (empty list)
print(find_min([42, 17, 2, -1, 67]))  # Output: -1
print(find_min([10, 10, 10, 10]))  # Output: 10
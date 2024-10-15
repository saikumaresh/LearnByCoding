def sum_of_list(my_list):
    total = 0  # Initialize total sum to 0
    if not my_list:  # Base case: if the list is empty, return 0
        return 0
    for i in my_list:  # Iterate over each element in the list
        if type(i) == list:  # If an element is a list, recursively calculate its sum
            total += sum_of_list(i)
        else:
            total += i  # If the element is not a list, add it to the total
    return total  # Return the total sum

# Example with a nested list
print(sum_of_list([1, 2, [3, 4], [5, 6]]))  # Output: 21
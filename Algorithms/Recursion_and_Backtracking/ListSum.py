def sum_of_list(my_list):
    total = 0  # Initialize total sum to 0
    if not my_list:  # Base case: if the list is empty, return 0
        return 0
    # Recursive step: add the first element to the sum of the rest of the list
    total = my_list[0] + sum_of_list(my_list[1:])
    return total  # Return the total sum

# Example with a simple list
print(sum_of_list([1, 2, 3, 4]))  # Output: 10
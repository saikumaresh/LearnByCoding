# Largest Pair Sum

# https://www.geeksforgeeks.org/problems/pair-sum--120604/1

# Difficulty: Easy

# Problem Statement
# Find the largest pair sum in an array of distinct integers.

# Examples :

# Input: arr[] = [12, 34, 10, 6, 40]
# Output: 74
# Explanation: Sum of 34 and 40 is the largest, i.e, 34 + 40 = 74.

# Input: arr[] = [10, 20, 30]
# Output: 50
# Explanation: 20 + 30 = 50.

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 2 ≤ arr.size() ≤ 106
# 0 ≤ arr[i] ≤ 106

def largest_pair_sum(arr):
    # Initialize the first and second largest to a very small value
    first_max = float('-inf')
    second_max = float('-inf')
    
    # Traverse through all elements in the array
    for num in arr:
        # Update the first and second largest if needed
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max:
            second_max = num
    
    # Return the sum of the two largest numbers
    return first_max + second_max

# Example usage:
arr = [12, 34, 10, 6, 40]
print(largest_pair_sum(arr))  # Output: 74

arr = [10, 20, 30]
print(largest_pair_sum(arr))  # Output: 50

# Remove duplicates in array

# https://www.geeksforgeeks.org/problems/remove-duplicates-in-small-prime-array/1

# Problem Statement
# Given an array arr consisting of positive integer numbers, remove all duplicate numbers.

# Example:

# Input: arr[] = [2, 2, 3, 3, 7, 5] 
# Output: [2, 3, 7, 5]
# Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.

# Input: arr[] = [2, 2, 5, 5, 7, 7] 
# Output: [2, 5, 7]

# Input: arr[] = [8, 7] 
# Output: [8, 7]

# Constraints:
# 1<= arr.size() <=106
# 2<= arr[i] <=100

class Solution:
    def removeDuplicates(self, arr):
        """
        Removes duplicates from the input array and returns a list with unique elements in the same order as they appeared in the original list.

        Parameters:
        arr (list): List of integers which may contain duplicates.

        Returns:
        list: A list with duplicates removed, maintaining the original order.
        """
        
        # Initialize an empty list to store unique elements
        li = []
        
        # Iterate through each element in the input list 'arr'
        for i in arr:
            # Check if the element is not already in the list 'li'
            if i not in li:
                # Append the element to 'li' if it's not a duplicate
                li.append(i)
        
        # Return the list with duplicates removed
        return li


# Sample test cases
solution = Solution()

# Test Case 1: List with duplicates
arr1 = [1, 2, 2, 3, 4, 4, 5]
# Expected output: [1, 2, 3, 4, 5]
print("Test Case 1:", solution.removeDuplicates(arr1))  # Output: [1, 2, 3, 4, 5]

# Test Case 2: List without duplicates
arr2 = [1, 2, 3, 4, 5]
# Expected output: [1, 2, 3, 4, 5]
print("Test Case 2:", solution.removeDuplicates(arr2))  # Output: [1, 2, 3, 4, 5]

# Test Case 3: List with all elements the same
arr3 = [1, 1, 1, 1, 1]
# Expected output: [1]
print("Test Case 3:", solution.removeDuplicates(arr3))  # Output: [1]

# Test Case 4: Empty list
arr4 = []
# Expected output: []
print("Test Case 4:", solution.removeDuplicates(arr4))  # Output: []

# Test Case 5: Large list with mixed duplicates
arr5 = [5, 1, 5, 2, 3, 4, 2, 4, 6, 7, 8, 8, 6]
# Expected output: [5, 1, 2, 3, 4, 6, 7, 8]
print("Test Case 5:", solution.removeDuplicates(arr5))  # Output: [5, 1, 2, 3, 4, 6, 7, 8]

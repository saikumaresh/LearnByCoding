# Make array elements unique
# Difficulty: Medium

# https://www.geeksforgeeks.org/problems/make-array-elements-unique--170645/1

# Problem Statement
# Given an array arr[ ], your task is to find the minimum number of increment operations required to make all the elements of the array unique. 
# i.e.- no value in the array should occur more than once. In one operation, a value can be incremented by 1 only.

# Examples :

# Input: arr[] = [1, 2, 2]
# Output: 1
# Explanation: If we increase arr[2] by 1 then the resulting array becomes {1, 2, 3} and has all unique values.Hence, the answer is 1 in this case.

# Input: arr[] = [1, 1, 2, 3]
# Output: 3
# Explanation: If we increase arr[0] by 3, then all array elements will be unique. Hence, the answer is 3 in this case.

# Input: arr[] = [5, 4, 3, 2, 1]
# Output: 0
# Explanation: All elements are unique.

# Constraints:
# 1 ≤ arr.size() ≤ 106
# 0 ≤ arr[i] ≤ 106

# Expected Complexities
# Time Complexity: O(n log n)Auxiliary Space: O(1)

class Solution:
    def minIncrements(self, arr):
        """
        Calculates the minimum increments needed to make all elements in the array unique.
        
        Parameters:
        arr (List[int]): List of integers
        
        Returns:
        int: Minimum number of increments required
        """
        # Step 1: Sort the array to bring duplicate or conflicting values together
        arr.sort()
        
        # Initialize the count of increments
        increments = 0
        
        # Step 2: Traverse through the sorted array and adjust values as necessary
        for i in range(1, len(arr)):
            # If the current element is not greater than the previous one,
            # increment it to make it unique
            if arr[i] <= arr[i-1]:
                # Calculate the number of increments needed to make arr[i] unique
                required_increment = arr[i-1] + 1 - arr[i]
                
                # Update the current element to make it unique
                arr[i] += required_increment
                
                # Accumulate the total increments
                increments += required_increment
                
        return increments

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Multiple duplicates
    arr1 = [3, 3, 3]
    # Explanation: Increment 3 to 4 and then to 5, total increments = 3.
    print("Test Case 1:", solution.minIncrements(arr1))  # Expected output: 3
    
    # Test Case 2: Already unique elements
    arr2 = [1, 2, 3]
    # Explanation: No increments needed, array is already unique.
    print("Test Case 2:", solution.minIncrements(arr2))  # Expected output: 0
    
    # Test Case 3: Some duplicates
    arr3 = [2, 2, 3, 5, 5]
    # Explanation: Increment second 2 to 4, and second 5 to 6. Total increments = 3.
    print("Test Case 3:", solution.minIncrements(arr3))  # Expected output: 3
    
    # Test Case 4: Random order with duplicates
    arr4 = [4, 3, 2, 2, 1]
    # Explanation: Increment second 2 to 5 and 1 to 6, total increments = 6.
    print("Test Case 4:", solution.minIncrements(arr4))  # Expected output: 6
    
    # Test Case 5: All elements are the same
    arr5 = [1, 1, 1, 1]
    # Explanation: Increment elements to make them [1, 2, 3, 4], total increments = 6.
    print("Test Case 5:", solution.minIncrements(arr5))  # Expected output: 6

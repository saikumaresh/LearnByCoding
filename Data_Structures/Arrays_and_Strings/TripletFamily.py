# Triplet Family

# https://www.geeksforgeeks.org/problems/triplet-family/1

# Problem Statement
# Given an array arr of integers. Find whether three numbers are such that the sum of two elements equals the third element.

# Example:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: true
# Explanation: The pair (1, 2) sums to 3.

# Input: arr[] = [5, 3, 4]
# Output: false
# Explanation: No triplets satisfy the condition.

# Expected Time Complexity: O(n2)
# Expected Auxilary Space: O(1)

# Constraints:
# 1 <= arr.size() <= 103
# 0 <= arr[i] <= 105

class Solution:
    def findTriplet(self, arr):
        """
        Given an array of integers, this function checks if there exists a triplet (i, j, k) such that
        arr[i] + arr[j] = arr[k], where i, j, and k are indices and i < j < k.
        
        Args:
        arr (list): List of integers.
        
        Returns:
        bool: True if such a triplet exists, False otherwise.
        """
        
        # Sort the array to enable two-pointer approach
        arr.sort()
        
        # Iterate backwards to use each element as the potential sum target
        for i in reversed(range(len(arr))):
            target = arr[i]  # Set the target sum as the current element
            left, right = 0, i - 1  # Initialize two pointers for two-sum approach
            
            # Use two-pointer approach to find if there are two numbers that sum to target
            while left < right:
                if arr[left] + arr[right] == target:
                    # Triplet found where arr[left] + arr[right] = arr[i]
                    return True
                elif arr[left] + arr[right] > target:
                    # If sum is greater than target, move right pointer leftward
                    right -= 1
                else:
                    # If sum is less than target, move left pointer rightward
                    left += 1
        
        # No such triplet found in the array
        return False

# Test cases
solution = Solution()

# Test Case 1
# Explanation: 1 + 5 = 6
print(solution.findTriplet([1, 5, 3, 2, 6]))  # Expected output: True

# Test Case 2
# Explanation: No such triplet exists
print(solution.findTriplet([1, 2, 3, 4]))  # Expected output: False

# Test Case 3
# Explanation: 2 + 7 = 9
print(solution.findTriplet([2, 3, 7, 9, 5]))  # Expected output: True

# Test Case 4
# Explanation: No such triplet exists
print(solution.findTriplet([1]))  # Expected output: False

# Test Case 5
# Explanation: -5 + 2 = -3
print(solution.findTriplet([-5, -3, 2, 7, 8]))  # Expected output: True

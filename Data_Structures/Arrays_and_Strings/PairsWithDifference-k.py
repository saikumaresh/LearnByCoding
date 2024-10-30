# Pairs with difference k

# https://www.geeksforgeeks.org/problems/pairs-with-difference-k1713/1

# Problem Statement
# Given an array arr[] of positive integers. Find the number of pairs of integers whose difference equals a given number k.
# Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

# Examples:

# Input: arr[] = [1, 5, 3, 4, 2], k = 3
# Output: 2
# Explanation: There are 2 pairs with difference 3,the pairs are {1, 4} and {5, 2} 

# Input: arr[] = [8, 12, 16, 4, 0, 20], k = 4
# Output: 5
# Explanation: There are 5 pairs with difference 4, the pairs are {0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20}.

# Constraints:
# 1 <= arr.size() <= 106
# 1 <= k <= 106
# 1 <= arri <= 106

class Solution:
    def countPairsWithDiffK(self, arr, k):
        """
        Counts the number of unique pairs with a given difference 'k'.

        Parameters:
        arr (list): List of integers.
        k (int): The difference to check between pairs.

        Returns:
        int: Count of pairs with the given difference 'k'.
        """
        
        # Initialize the count for pairs
        count = 0
        
        # Dictionary to store the frequency of each element in the array
        freq = {}
        
        # Populate the dictionary with element frequencies
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        # Check for each element if a pair with the required difference exists
        for num in arr:
            if num + k in freq:
                # If such an element exists, add its frequency to the count
                count += freq[num + k]
        
        return count


# Example test case
solution = Solution()

# Test Case 1
arr1 = [1, 5, 3, 4, 2]
k1 = 2
# Expected output: 3 (pairs: (1,3), (3,5), (2,4))
print("Test Case 1:", solution.countPairsWithDiffK(arr1, k1))  # Output: 3

# Test Case 2
arr2 = [8, 12, 16, 4, 0, 20]
k2 = 4
# Expected output: 5 (pairs: (8,12), (12,16), (16,20), (4,8), (0,4))
print("Test Case 2:", solution.countPairsWithDiffK(arr2, k2))  # Output: 5

# Test Case 3: No pairs with difference 'k'
arr3 = [1, 1, 1, 1]
k3 = 2
# Expected output: 0 (no pairs with difference 2)
print("Test Case 3:", solution.countPairsWithDiffK(arr3, k3))  # Output: 0

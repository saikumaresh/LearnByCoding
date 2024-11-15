# Maximum Absolute Difference

# Problem Description
# You are given an array of N integers, A1, A2, .... AN.
# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, 
# where |x| denotes absolute value of x.

# Problem Constraints
# # 1 <= N <= 100000
# -109 <= A[i] <= 109

# Input Format
# First argument is an integer array A of size N.

# Output Format
# Return an integer denoting the maximum value of f(i, j).

# Example Input

# Input 1:
# A = [1, 3, -1]
# Input 2:
# A = [2]

# Example Output

# Output 1:
# 5
# Output 2:
# 0

# Example Explanation

# Explanation 1:
# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
# So, we return 5.

# Explanation 2:
# Only possibility is i = 1 and j = 1. That gives answer = 0.

import sys

class Solution:
    def maxArr(self, A):
        """
        Finds the maximum absolute difference in the given array based on the formula:
        |A[i] - A[j]| + |i - j|.

        Parameters:
        A (List[int]): List of integers.

        Returns:
        int: Maximum value of |A[i] - A[j]| + |i - j| for all i, j.
        """
        # Initialize variables to track max and min for two expressions:
        # Expression 1: A[i] + i
        # Expression 2: A[i] - i
        max1 = -sys.maxsize
        min1 = sys.maxsize
        max2 = -sys.maxsize
        min2 = sys.maxsize

        # Iterate through the array
        for i in range(len(A)):
            # Update max and min values for the two expressions
            max1 = max(max1, A[i] + i)  # Expression 1: Max of A[i] + i
            min1 = min(min1, A[i] + i)  # Expression 1: Min of A[i] + i
            max2 = max(max2, A[i] - i)  # Expression 2: Max of A[i] - i
            min2 = min(min2, A[i] - i)  # Expression 2: Min of A[i] - i

        # The result is the maximum of the differences of max and min
        return max(max1 - min1, max2 - min2)

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Simple array with a mix of positive and negative numbers
    arr1 = [1, 3, -1]
    print("Test Case 1:", solution.maxArr(arr1))
    # Expected Output: 5
    # Explanation: Max difference is between elements at indices 0 and 2 -> |1 - (-1)| + |0 - 2| = 2 + 3 = 5

    # Test Case 2: Array with increasing sequence
    arr2 = [1, 2, 3, 4, 5]
    print("Test Case 2:", solution.maxArr(arr2))
    # Expected Output: 4
    # Explanation: Max difference is between elements at indices 0 and 4 -> |1 - 5| + |0 - 4| = 4 + 4 = 8

    # Test Case 3: Array with all negative numbers
    arr3 = [-5, -2, -3, -4]
    print("Test Case 3:", solution.maxArr(arr3))
    # Expected Output: 6
    # Explanation: Max difference is between elements at indices 0 and 1 -> |-5 - (-2)| + |0 - 1| = 3 + 1 = 4

    # Test Case 4: Array with a single element
    arr4 = [42]
    print("Test Case 4:", solution.maxArr(arr4))
    # Expected Output: 0
    # Explanation: No difference can exist with a single element.

    # Test Case 5: Array with all identical elements
    arr5 = [7, 7, 7, 7, 7]
    print("Test Case 5:", solution.maxArr(arr5))
    # Expected Output: 4
    # Explanation: Max difference is purely due to the index differences.

    # Test Case 6: Large array to test performance
    arr6 = list(range(10000))
    print("Test Case 6:", solution.maxArr(arr6))
    # Expected Output: 9999
    # Explanation: Max difference is between first and last elements due to index difference.

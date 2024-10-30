# Max Non Negative SubArray

# Problem Statement
# Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
# The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
# Maximum sub-array is defined in terms of the sum of the elements in the sub-array.
# Find and return the required subarray.
# NOTE:
#     1. If there is a tie, then compare with segment's length and return segment which has maximum length.
#     2. If there is still a tie, then return the segment with minimum starting index.

# Input Format:
# The first and the only argument of input contains an integer array A, of length N.

# Output Format:
# Return an array of integers, that is a subarray of A that satisfies the given conditions.

# Constraints:
# 1 <= N <= 1e5
# -INT_MAX < A[i] <= INT_MAX

# Examples:

# Input 1:
#     A = [1, 2, 5, -7, 2, 3]
# Output 1:
#     [1, 2, 5]
# Explanation 1:
#     The two sub-arrays are [1, 2, 5] [2, 3].
#     The answer is [1, 2, 5] as its sum is larger than [2, 3].

# Input 2:
#     A = [10, -1, 2, 3, -4, 100]
# Output 2:
#     [100]
# Explanation 2:
#     The three sub-arrays are [10], [2, 3], [100].
#     The answer is [100] as its sum is larger than the other two.

class Solution:
    def maxset(self, A):
        # Initialize variables to track current and maximum sums and their indices
        currsum = 0  # Current sum of the ongoing subarray
        max_sum = 0  # Maximum sum found so far
        max_start = max_end = -1  # Start and end indices of the maximum sum subarray
        current_start = -1  # Start index of the ongoing subarray

        for i in range(len(A)):
            if A[i] >= 0:  # If the current element is non-negative
                if current_start == -1:
                    current_start = i  # Set the start of a new subarray
                currsum += A[i]  # Add the element to the current sum

                # Update max_sum and indices if a larger sum or a longer subarray with the same sum is found
                if currsum > max_sum or (currsum == max_sum and i - current_start > max_end - max_start):
                    max_sum = currsum
                    max_start = current_start
                    max_end = i
            else:
                # Reset current sum and start index if a negative element is encountered
                currsum = 0
                current_start = -1

        # If no valid subarray was found, return an empty list
        if max_start == -1: 
            return []

        # Return the subarray with the maximum sum
        return A[max_start:max_end + 1]

# Test cases
solution = Solution()

# Test case 1: Basic case with positive numbers and negatives
print(solution.maxset([1, 2, 5, -7, 2, 3]))  # Expected output: [1, 2, 5]

# Test case 2: All positive numbers
print(solution.maxset([1, 2, 5, 7, 8]))  # Expected output: [1, 2, 5, 7, 8]

# Test case 3: No non-negative numbers
print(solution.maxset([-1, -2, -3]))  # Expected output: []

# Test case 4: Multiple subarrays with the same sum, longest one preferred
print(solution.maxset([1, 2, -1, 2, 2]))  # Expected output: [2, 2]

# Test case 5: Edge case with single element
print(solution.maxset([5]))  # Expected output: [5]

# Test case 6: Edge case with empty input
print(solution.maxset([]))  # Expected output: []

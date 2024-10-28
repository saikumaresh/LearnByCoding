# Max Sum Contiguous Subarray

# Problem Description
# Find the maximum sum of contiguous non-empty subarray within an array A of length N.

# Problem Constraints
# 1 <= N <= 1e6
# -1000 <= A[i] <= 1000

# Input Format
# The first and the only argument contains an integer array, A.

# Output Format
# Return an integer representing the maximum possible sum of the contiguous subarray.

# Example Input

# Input 1:
#  A = [1, 2, 3, 4, -10] 
# Input 2:
#  A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 

# Example Output

# Output 1:
#  10 
# Output 2:
#  6 

# Example Explanation

# Explanation 1:
#  The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
# Explanation 2:
#  The subarray [4,-1,2,1] has the maximum possible sum of 6. 

class Solution:
    # Function to find the maximum sum of a contiguous subarray
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # Initialize current sum and max sum
        currSum = 0  # Tracks the sum of the current subarray
        maxSum = -100000  # Initialize to a very low value to handle negative-only arrays
        
        # Iterate over each element in the array
        for i in A:
            currSum += i  # Add the current element to currSum
            maxSum = max(maxSum, currSum)  # Update maxSum if currSum is larger
            
            # If currSum becomes negative, reset it to zero
            # This is because a negative sum would decrease any future subarray sums
            if currSum < 0:
                currSum = 0

        return maxSum  # Return the maximum sum found

# Testing the function with various test cases

# Test case 1: Mixed positive and negative numbers
print(Solution().maxSubArray((1, -3, 2, 1, -1)))  # Expected output: 3 (subarray: [2, 1])

# Test case 2: All positive numbers
print(Solution().maxSubArray((2, 3, 4)))  # Expected output: 9 (subarray: [2, 3, 4])

# Test case 3: All negative numbers
print(Solution().maxSubArray((-1, -2, -3, -4)))  # Expected output: -1 (subarray: [-1])

# Test case 4: Single positive number
print(Solution().maxSubArray((5,)))  # Expected output: 5 (subarray: [5])

# Test case 5: Single negative number
print(Solution().maxSubArray((-5,)))  # Expected output: -5 (subarray: [-5])

# Test case 6: Large array with mixed numbers
print(Solution().maxSubArray((1, -2, 3, 4, -1, 2, 1, -5, 4)))  # Expected output: 10 (subarray: [3, 4, -1, 2, 1])

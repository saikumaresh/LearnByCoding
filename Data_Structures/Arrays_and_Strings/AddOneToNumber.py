# Add One To Number

# Problem Description
# Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
# The digits are stored such that the most significant digit is at the head of the list.
# NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. 
# For example: for this problem, the following are some good questions to ask :
# Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
# A: For the purpose of this question, YES
# Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
# A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


# Problem Constraints
# 1 <= size of the array <= 1000000

# Input Format
# First argument is an array of digits.

# Output Format
# Return the array of digits after adding one.

# Example Input
# [1, 2, 3]

# Example Output
# [1, 2, 4]

# Example Explanation
# Given vector is [1, 2, 3].
# The returned vector should be [1, 2, 4] as 123 + 1 = 124.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def addOneToNumber(self, A):
        # Remove any leading zeros in the input array
        while len(A) > 1 and A[0] == 0:
            A.pop(0)
        
        n = len(A)
        
        # Start from the least significant digit (end of list)
        for i in range(n - 1, -1, -1):
            # If current digit is less than 9, just add 1 and return the result
            if A[i] < 9:
                A[i] += 1
                return A
            
            # If current digit is 9, set it to 0 and carry over the 1
            A[i] = 0
        
        # If all digits were 9, add a new leading 1 at the start
        # This handles cases like [9, 9, 9] turning into [1, 0, 0, 0]
        return [1] + A

# Testing the function with the custom test case provided
solution = Solution()

# Test case 1: Custom input with leading zeros
print(solution.addOneToNumber([0, 3, 7, 6, 4, 0, 5, 5, 5]))  # Expected output: [3, 7, 6, 4, 0, 5, 5, 6]

# Other test cases for additional verification
print(solution.addOneToNumber([1, 2, 3]))  # Expected output: [1, 2, 4]
print(solution.addOneToNumber([9, 9, 9]))  # Expected output: [1, 0, 0, 0]
print(solution.addOneToNumber([0, 0, 1, 2, 3]))  # Expected output: [1, 2, 4]

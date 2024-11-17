# Single Number II

# Problem Description
# Given an array of integers, every element appears thrice except for one, which occurs once.
# Find that element that does not appear thrice.
# NOTE: Your algorithm should have a linear runtime complexity.
# Could you implement it without using extra memory?

# Problem Constraints
# 2 <= A <= 5*106
# 0 <= A <= INTMAX

# Input Format
# First and only argument of input contains an integer array A.

# Output Format
# Return a single integer.

# Example Input
# Input 1:
#  A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
# Input 2:
#  A = [0, 0, 0, 1]

# Example Output
# Output 1:
#  4
# Output 2:
#  1

# Example Explanation
#  4 occurs exactly once in Input 1.
#  1 occurs exactly once in Input 2.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        """
        Finds the number that appears exactly once in an array where every other number appears thrice.

        Parameters:
        A (tuple): A tuple of integers.

        Returns:
        int: The integer that appears exactly once.
        """
        # Variables to track bits that appear once and twice
        ones, twos = 0, 0

        for num in A:
            # Update 'twos' to include bits appearing twice
            twos |= ones & num
            
            # Update 'ones' to include bits appearing once
            ones ^= num
            
            # Mask to remove bits appearing three times
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        # 'ones' now holds the number that appears exactly once
        return ones

# Test cases
def test_singleNumber():
    solution = Solution()
    
    # Test Case 1
    A1 = (2, 2, 3, 2)
    print("Test Case 1:", solution.singleNumber(A1))  # Expected Output: 3

    # Test Case 2
    A2 = (0, 1, 0, 1, 0, 1, 99)
    print("Test Case 2:", solution.singleNumber(A2))  # Expected Output: 99

    # Test Case 3
    A3 = (30000, 500, 100, 30000, 100, 30000, 100)
    print("Test Case 3:", solution.singleNumber(A3))  # Expected Output: 500

    # Test Case 4
    A4 = (7, 7, 7, 8)
    print("Test Case 4:", solution.singleNumber(A4))  # Expected Output: 8

    # Test Case 5
    A5 = (-2, -2, 1, -2)
    print("Test Case 5:", solution.singleNumber(A5))  # Expected Output: 1

test_singleNumber()

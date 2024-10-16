# Is magic?

# Problem Description
# Given a number A, check if it is a magic number or not.
# A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition. 
# If the single digit comes out to be 1, then the number is a magic number.

# Problem Constraints
# 1 <= A <= 109

# Input Format
# The first and only argument is an integer A.

# Output Format
# Return an 1 if the given number is magic else return 0.

# Example Input

# Input 1:
#  A = 83557
# Input 2:
#  A = 1291

# Example Output
# Output 1:
#  1
# Output 2:
#  0

# Example Explanation

# Explanation 1:
#  Sum of digits of (83557) = 28
#  Sum of digits of (28) = 10
#  Sum of digits of (10) = 1. 
#  Single digit is 1, so it's a magic number. Return 1.

# Explanation 2:
#  Sum of digits of (1291) = 13
#  Sum of digits of (13) = 4
#  Single digit is not 1, so it's not a magic number. Return 0.

class Solution:
    # Method to calculate the sum of digits of a given integer A
    # @param A : integer
    # @return an integer
    def sumofdigits(self, A):
        # Base case: if A is 0, return 0
        if A == 0:
            return 0
        # Recursive case: sum the last digit (A % 10) with the sum of digits of A // 10
        return self.sumofdigits(A // 10) + (A % 10)

    # Method to compute the "magic" number by recursively summing the digits
    def magic(self, A):
        # Base case: if A has a single digit, return A
        if len(str(A)) == 1:
            return A
        # Recursive case: return magic of the sum of digits
        else:
            return self.magic(self.sumofdigits(A))

    # Method to solve the problem and determine if the magic number is 1
    def solve(self, A):
        # Check if the magic number is 1
        if self.magic(A) == 1:
            return 1
        return 0
sol = Solution()
print(sol.solve(83557))
print(sol.solve(1291))
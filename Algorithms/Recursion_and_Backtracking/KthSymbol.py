# Kth Symbol

# Problem Description
# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).

# Problem Constraints
# 1 <= A <= 20
# 1 <= B <= 2A - 1

# Input Format
# First argument is an integer A.
# Second argument is an integer B.

# Output Format
# Return an integer denoting the Bth indexed symbol in row A.

# Example Input

# Input 1:
#  A = 2
#  B = 1
# Input 2:
#  A = 2
#  B = 2

# Example Output

# Output 1:
#  0
# Output 2:
#  1


# Example Explanation

# Explanation 1:
#  Row 1: 0
#  Row 2: 01
# Explanation 2:
#  Row 1: 0
#  Row 2: 01

class Solution:
    # Method to find the B-th symbol in the A-th row
    # @param A : integer (row number)
    # @param B : integer (index number)
    # @return an integer (0 or 1)
    def solve(self, A, B):
        # Base case: Row 1 has only a single symbol, which is 0
        if A == 1:
            return 0
        
        # Calculate the parent in the previous row (A-1)
        parent = self.solve(A - 1, (B + 1) // 2)
        
        # If B is even, the current symbol is the complement of the parent
        if B % 2 == 0:
            return 1 - parent
        # If B is odd, the current symbol is the same as the parent
        else:
            return parent

# Solution Approach
# The key observation is that the pattern in each row follows a recursive structure. The value at position B in row A can be derived from its "parent" in row A-1:

# Parent Concept:

# Every position B in row A has a "parent" in row A-1. The parent position is at index (B+1)//2.
# If B is odd, the symbol at B is the same as its parent.
# If B is even, the symbol at B is the opposite of its parent (i.e., 0 becomes 1, and 1 becomes 0).

# Recursive Approach:
# The base case occurs when A = 1. In row 1, the only symbol is 0.
# For every other row, recursively compute the value of the parent and determine the current value based on whether B is odd or even.


# Base Case:
# When A == 1, we directly return 0 because row 1 contains only 0.

# Recursive Case:
# We calculate the parent in the previous row using (B + 1) // 2. This formula helps identify the index of the parent symbol in the previous row.
# If B is even, the current symbol is the opposite of its parent. If B is odd, the current symbol is the same as the parent.

# Examples

# Example 1:

# Input:
# A = 2
# B = 1

# Explanation:
# Row 1: 0
# Row 2: 01 (derived by replacing 0 with 01)
# We are asked for the 1st symbol in the 2nd row, which is 0.

# Code Execution:
solution = Solution()
print(solution.solve(2, 1))
# Output:
# 0

# Example 2:

# Input:
# A = 2
# B = 2

# Explanation:
# Row 1: 0
# Row 2: 01 (derived by replacing 0 with 01)
# We are asked for the 2nd symbol in the 2nd row, which is 1.

# Code Execution:
solution = Solution()
print(solution.solve(2, 2))
# Output:
# 1

# Efficiency
# Time Complexity: The recursive function calls itself for each level of row A, which means the time complexity is O(A). Since A <= 20, this is efficient.
# Space Complexity: The space complexity is O(A) because of the recursion stack.
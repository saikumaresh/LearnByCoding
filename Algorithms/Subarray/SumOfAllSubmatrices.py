# Sum of all Submatrices

# Problem Description
# Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.

# Problem Constraints
# 1 <= N <=30
# 0 <= A[i][j] <= 10

# Input Format
# Single argument representing a 2-D array A of size N x N.

# Output Format
# Return an integer denoting the sum of all possible submatrices in the given matrix.

# Example Input

# Input 1:
# A = [ [1, 1]
#       [1, 1] ]
# Input 2:
# A = [ [1, 2]
#       [3, 4] ]

# Example Output

# Output 1:
# 16
# Output 2:
# 40

# Example Explanation

# Example 1:
# Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4 * 1 = 4
# Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4 * 2 = 8
# Number of submatrices with 3 elements = 0
# Number of submatrices with 4 elements = 1, so sum of such submatrix = 4
# Total Sum = 4+8+4 = 16

# Example 2:
# The submatrices are [1], [2], [3], [4], [1, 2], [3, 4], [1, 3], [2, 4] and [[1, 2], [3, 4]].
# Total sum = 40

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        total = 0
        n = len(A)  # Size of the matrix (n x n)
        
        # Iterate through each element of the matrix
        for i in range(n):
            for j in range(n):
                # Calculate the weight of A[i][j] based on the number of submatrices it can contribute to
                weight = (i + 1) * (j + 1) * (n - i) * (n - j)
                
                # Multiply A[i][j] by its weight and add to the total sum
                total += weight * A[i][j]
                
        return total

# Test Case 1: Small matrix 1x1
A = [[5]]
# Explanation: Only one submatrix exists containing the single element.
# Expected Output: 5
print("Output:", Solution().solve(A))  # Expected: 5

# Test Case 2: 2x2 matrix
A = [
    [1, 2],
    [3, 4]
]
# Explanation: Each element has its own weight based on the number of submatrices it appears in.
# Expected Output: 1*4 + 2*4 + 3*4 + 4*4 = 40
print("Output:", Solution().solve(A))  # Expected: 40

# Test Case 3: 3x3 matrix
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# The weights vary, contributing different values based on position.
# This is a more complex example to verify if the function is correctly summing weighted values.
print("Output:", Solution().solve(A))  # Expected: Output should match calculated total based on the formula

# Test Case 4: Matrix with zeros
A = [
    [0, 0],
    [0, 0]
]
# All elements are zero, so total should be zero.
print("Output:", Solution().solve(A))  # Expected: 0

# Test Case 5: 2x2 matrix with negative numbers
A = [
    [-1, -2],
    [-3, -4]
]
# The function should handle negative values correctly.
# Expected Output: -1*4 + -2*4 + -3*4 + -4*4 = -40
print("Output:", Solution().solve(A))  # Expected: -40

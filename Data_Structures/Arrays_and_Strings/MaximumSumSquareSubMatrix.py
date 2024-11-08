# Maximum Sum Square SubMatrix

# Problem Description
# Given a 2D integer matrix A of size N x N, find a B x B submatrix where B<= N and B>= 1, 
# such that the sum of all the elements in the submatrix is maximum.

# Problem Constraints
# 1 <= N <= 103.
# 1 <= B <= N
# -102 <= A[i][j] <= 102.

# Input Format
# First arguement is an 2D integer matrix A.
# Second argument is an integer B.

# Output Format
# Return a single integer denoting the maximum sum of submatrix of size B x B.

# Example Input

# Input 1:
#  A = [
#         [1, 1, 1, 1, 1]
#         [2, 2, 2, 2, 2]
#         [3, 8, 6, 7, 3]
#         [4, 4, 4, 4, 4]
#         [5, 5, 5, 5, 5]
#      ]
#  B = 3

# Input 2:
#  A = [
#         [2, 2]
#         [2, 2]
#     ]
#  B = 2

# Example Output

# Output 1:
#  48
# Output 2:
#  8

# Example Explanation

# Explanation 1:
#     Maximum sum 3 x 3 matrix is
#     8 6 7
#     4 4 4
#     5 5 5
#     Sum = 48

# Explanation 2:
#  Maximum sum 2 x 2 matrix is
#   2 2
#   2 2
#   Sum = 8

class Solution:
    # @param A : list of list of integers (2D matrix)
    # @param B : integer (size of the submatrix)
    # @return an integer (maximum sum of submatrix of size B x B)
    
    def solve(self, A, B):
        n = len(A)  # The size of the input matrix
        
        # Create a 2D list to store prefix sums for submatrices
        pf = [[0] * n for _ in range(n)]
        
        # Fill the prefix sum array
        pf[0][0] = A[0][0]
        
        # First row prefix sum
        for i in range(1, n):
            pf[0][i] = pf[0][i-1] + A[0][i]
        
        # First column prefix sum
        for i in range(1, n):
            pf[i][0] = pf[i-1][0] + A[i][0]
        
        # Fill the rest of the prefix sum array
        for i in range(1, n):
            for j in range(1, n):
                pf[i][j] = pf[i-1][j] + pf[i][j-1] - pf[i-1][j-1] + A[i][j]
        
        # Initialize the variable to store the maximum submatrix sum
        maxSum = float('-inf')
        
        # Iterate over all possible top-left corners of BxB submatrices
        for i in range(n-B+1):
            for j in range(n-B+1):
                # Calculate the sum of the current BxB submatrix using the prefix sum array
                curr_sum = pf[i+B-1][j+B-1]
                if i > 0:
                    curr_sum -= pf[i-1][j+B-1]
                if j > 0:
                    curr_sum -= pf[i+B-1][j-1]
                if i > 0 and j > 0:
                    curr_sum += pf[i-1][j-1]
                
                # Update the maximum sum encountered
                maxSum = max(maxSum, curr_sum)
        
        return maxSum


# Test cases
if __name__ == "__main__":
    # Test case 1
    A1 = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]
    B1 = 3
    solution = Solution()
    print("Test Case 1 - Expected Output: 48")
    print("Output:", solution.solve(A1, B1))  # Expected output: 48

    # Test case 2
    A2 = [
        [2, 2],
        [2, 2]
    ]
    B2 = 2
    print("\nTest Case 2 - Expected Output: 8")
    print("Output:", solution.solve(A2, B2))  # Expected output: 8

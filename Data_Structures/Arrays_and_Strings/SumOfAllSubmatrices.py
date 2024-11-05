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
    # Function to calculate the total weighted sum of submatrices
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        """
        Given a 2D matrix A, calculate the total sum where each element
        is weighted by its contribution to all possible submatrices.

        Parameters:
        A (List[List[int]]): 2D matrix of integers.

        Returns:
        int: The calculated total sum of all submatrices.
        """
        total = 0
        n = len(A)  # Get the size of the matrix (assuming square matrix)
        
        # Iterate over each element in the matrix
        for i in range(n):
            for j in range(n):
                # (i + 1) * (j + 1) is the count of submatrices where A[i][j] is the top-left corner
                # (n - i) * (n - j) is the count of submatrices where A[i][j] is the bottom-right corner
                # Each submatrix containing A[i][j] contributes its value A[i][j] to the total sum
                total += (i + 1) * (j + 1) * (n - i) * (n - j) * A[i][j]
        
        return total


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: 2x2 matrix
    A1 = [
        [1, 2],
        [3, 4]
    ]
    print("Test Case 1 Output:", solution.solve(A1))  # Expected Output: Sum of all submatrices containing each element

    # Test Case 2: 3x3 matrix
    A2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Test Case 2 Output:", solution.solve(A2))  # Expected Output: Total sum considering submatrices with weights

    # Test Case 3: Single element matrix
    A3 = [[5]]
    print("Test Case 3 Output:", solution.solve(A3))  # Expected Output: 5, as there's only one element and submatrix

    # Test Case 4: Matrix with larger values
    A4 = [
        [10, 20],
        [30, 40]
    ]
    print("Test Case 4 Output:", solution.solve(A4))  # Expected Output: Weighted sum of submatrices with larger values

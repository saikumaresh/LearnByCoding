# Maximum Submatrix Sum

# Problem Description
# Given a row-wise and column-wise sorted matrix A of size N * M.
# Return the maximum non-empty submatrix sum of this matrix.

# Problem Constraints
# 1 <= N, M <= 1000
# -109 <= A[i][j] <= 109

# Input Format
# The first argument is a 2D integer array A.

# Output Format
# Return a single integer that is the maximum non-empty submatrix sum of this matrix.

# Example Input

# Input 1:-
#     -5 -4 -3
# A = -1  2  3
#      2  2  4
# Input 2:-
#     1 2 3
# A = 4 5 6
#     7 8 9

# Example Output

# Output 1:-
# 12
# Output 2:-
# 45

# Example Explanation

# Expanation 1:-
# The submatrix with max sum is 
# -1 2 3
#  2 2 4
#  Sum is 12.

# Explanation 2:-
# The largest submatrix with max sum is 
# 1 2 3
# 4 5 6
# 7 8 9
# The sum is 45.

###################################################### Implementation 1: Using Prefix Sum Array ######################################################

class Solution1:
    # Function to find the maximum submatrix sum using a prefix sum approach
    # @param A : list of list of integers (matrix)
    # @return an integer (maximum submatrix sum)
    def solve(self, A):
        n, m = len(A), len(A[0])  # Matrix dimensions
        pf = [[0] * m for _ in range(n)]  # Prefix sum matrix initialization

        # Step 1: Fill the prefix sum matrix
        pf[0][0] = A[0][0]  # Initialize the first element
        # Compute prefix sums for the first column
        for i in range(1, n):
            pf[i][0] = pf[i - 1][0] + A[i][0]
        # Compute prefix sums for the first row
        for i in range(1, m):
            pf[0][i] = pf[0][i - 1] + A[0][i]
        # Compute prefix sums for the rest of the matrix
        for i in range(1, n):
            for j in range(1, m):
                pf[i][j] = pf[i - 1][j] + pf[i][j - 1] - pf[i - 1][j - 1] + A[i][j]

        # Step 2: Calculate maximum submatrix sum using the prefix sum matrix
        maxsum = float('-inf')  # Initialize maxsum to the smallest possible value
        for i in range(n - 1, -1, -1):  # Traverse from bottom-right to top-left
            for j in range(m - 1, -1, -1):
                # Define the start and end points of submatrix
                start = [i, j]
                end = [n - 1, m - 1]
                
                # Calculate the sum of the submatrix from start to end
                currsum = pf[end[0]][end[1]]
                if start[0] > 0:
                    currsum -= pf[start[0] - 1][end[1]]
                if start[1] > 0:
                    currsum -= pf[end[0]][start[1] - 1]
                if start[0] > 0 and start[1] > 0:
                    currsum += pf[start[0] - 1][start[1] - 1]

                # Update maxsum if the current sum is larger
                maxsum = max(maxsum, currsum)

        return maxsum

s = Solution1()

# Test Case 1: Simple positive matrix
A1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(s.solve(A1))  # Expected output: 45 (entire matrix sum)

# Test Case 2: Matrix with mixed values
A2 = [
    [-1, -2, -3],
    [-4, 5, -6],
    [-7, -8, 9]
]
print(s.solve(A2))  # Expected output: 9 (single element 9)

# Test Case 3: Larger matrix with varied values
A3 = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]
print(s.solve(A3))  # Expected output: 14 (from submatrix [5, -6, -8, 9])

# Test Case 4: All negative values
A4 = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]
print(s.solve(A4))  # Expected output: -1 (maximum is the single element -1)

# Test Case 5: Single row matrix
A5 = [[1, 2, 3, 4]]
print(s.solve(A5))  # Expected output: 10 (entire row sum)


###################################################### Implementation 2: Using Suffix Sum Array ######################################################

class Solution2:
    # Function to find the maximum submatrix sum using a suffix sum approach
    # @param A : list of list of integers (matrix)
    # @return an integer (maximum submatrix sum)
    def solve(self, A):
        n = len(A)       # Number of rows in matrix
        m = len(A[0])    # Number of columns in matrix
        
        # Step 1: Initialize suffix sum matrix
        suff = [[0] * m for _ in range(n)]
        suff[n - 1][m - 1] = A[n - 1][m - 1]  # Start with the bottom-right corner element
        res = suff[n - 1][m - 1]              # Initialize result with the last element

        # Step 2: Fill the last row in the suffix sum matrix
        for j in range(m - 2, -1, -1):
            suff[n - 1][j] = suff[n - 1][j + 1] + A[n - 1][j]
            res = max(res, suff[n - 1][j])

        # Step 3: Fill the last column in the suffix sum matrix
        for i in range(n - 2, -1, -1):
            suff[i][m - 1] = suff[i + 1][m - 1] + A[i][m - 1]
            res = max(res, suff[i][m - 1])

        # Step 4: Fill the rest of the suffix sum matrix
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                suff[i][j] = suff[i][j + 1] + suff[i + 1][j] - suff[i + 1][j + 1] + A[i][j]
                res = max(res, suff[i][j])

        return res


s = Solution2()

# Test Case 1: Simple positive matrix
A1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(s.solve(A1))  # Expected output: 45 (entire matrix sum)

# Test Case 2: Matrix with mixed values
A2 = [
    [-1, -2, -3],
    [-4, 5, -6],
    [-7, -8, 9]
]
print(s.solve(A2))  # Expected output: 9 (single element 9)

# Test Case 3: Larger matrix with varied values
A3 = [
    [1, -2, 3],
    [-4, 5, -6],
    [7, -8, 9]
]
print(s.solve(A3))  # Expected output: 14 (from submatrix [5, -6, -8, 9])

# Test Case 4: All negative values
A4 = [
    [-1, -2, -3],
    [-4, -5, -6],
    [-7, -8, -9]
]
print(s.solve(A4))  # Expected output: -1 (maximum is the single element -1)

# Test Case 5: Single row matrix
A5 = [[1, 2, 3, 4]]
print(s.solve(A5))  # Expected output: 10 (entire row sum)

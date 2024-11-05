# Search in a row wise and column wise sorted matrix

# Problem Description
# Given a matrix of integers A of size N x M and an integer B.
# In the given matrix every row and column is sorted in non-decreasing order. Find and return the position of B in the matrix in the given form:
# If A[i][j] = B then return (i * 1009 + j)
# If B is not present return -1.
# Note 1: Rows are numbered from top to bottom and columns are numbered from left to right.
# Note 2: If there are multiple B in A then return the smallest value of i*1009 +j such that A[i][j]=B.
# Note 3: Expected time complexity is linear
# Note 4: Use 1-based indexing

# Problem Constraints
# 1 <= N, M <= 1000
# -100000 <= A[i] <= 100000
# -100000 <= B <= 100000

# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer B.

# Output Format
# Return the position of B and if it is not present in A return -1 instead.

# Example Input

# Input 1:-
# A = [[1, 2, 3]
#      [4, 5, 6]
#      [7, 8, 9]]
# B = 2

# Input 2:-
# A = [[1, 2]
#      [3, 3]]
# B = 3

# Example Output

# Output 1:-
# 1011
# Output 2:-
# 2019

# Example Explanation

# Expanation 1:-
# A[1][2] = 2
# 1 * 1009 + 2 = 1011

# Explanation 2:-
# A[2][1] = 3
# 2 * 1009 + 1 = 2019
# A[2][2] = 3
# 2 * 1009 + 2 = 2020
# The minimum value is 2019

class Solution:
    # Function to find the smallest position of target B in matrix A (sorted in rows and columns)
    # @param A : 2D list of integers (matrix sorted row-wise and column-wise)
    # @param B : integer (target value to search for)
    # @return an integer (encoded position or -1 if not found)
    def solve(self, A, B):
        n, m = len(A), len(A[0])  # Dimensions of the matrix
        i, j = 0, m - 1  # Start from the top-right corner
        ans = float('inf')  # Initialize answer to infinity to find minimum encoding

        # Traverse the matrix until the bounds are exceeded
        while i < n and j >= 0:
            # If the current element is less than target, move down to the next row
            if A[i][j] < B:
                i += 1
            # If the current element is greater than target, move left to the next column
            elif A[i][j] > B:
                j -= 1
            # If the target is found
            else:
                # Calculate encoded position using 1-based indexing: (i+1) * 1009 + (j+1)
                ans = min(ans, (i + 1) * 1009 + (j + 1))
                # Move left to find any smaller encoded value in the same row
                j -= 1
        
        # Return the minimum encoded position if found; otherwise, return -1
        return ans if ans != float('inf') else -1

# Test cases
s = Solution()

# Test case 1: Target is present in the matrix with unique occurrence
A1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B1 = 2
print(s.solve(A1, B1))  # Expected output: 1011 (i=0, j=1 -> (1)*1009 + (2))

# Test case 2: Target has multiple occurrences in the matrix
A2 = [
    [1, 2],
    [3, 3]
]
B2 = 3
print(s.solve(A2, B2))  # Expected output: 2019 (first occurrence at i=1, j=0)

# Test case 3: Target is not present in the matrix
A3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B3 = 10
print(s.solve(A3, B3))  # Expected output: -1

# Test case 4: Target is the first element in the matrix
A4 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
B4 = 10
print(s.solve(A4, B4))  # Expected output: 1010 (i=0, j=0 -> (1)*1009 + (1))

# Test case 5: Target is the last element in the matrix
A5 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
B5 = 9
print(s.solve(A5, B5))  # Expected output: 3021 (i=2, j=2 -> (3)*1009 + (3))

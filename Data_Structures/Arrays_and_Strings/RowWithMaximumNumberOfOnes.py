# Row with maximum number of ones

# Problem Description
# Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.
# NOTE:
# If two rows have the maximum number of 1 then return the row which has a lower index.
# Rows are numbered from top to bottom and columns are numbered from left to right.
# Assume 0-based indexing.
# Assume each row to be sorted by values.

# Expected time complexity is O(rows + columns).

# Problem Constraints
# 1 <= N <= 1000
# 0 <= A[i] <= 1

# Input Format
# The only argument given is the integer matrix A.

# Output Format
# Return the row with the maximum number of 1.

# Example Input

# Input 1:
#  A = [   [0, 1, 1]
#          [0, 0, 1]
#          [0, 1, 1]   ]

# Input 2:
#  A = [   [0, 0, 0, 0]
#          [0, 0, 0, 1]
#          [0, 0, 1, 1]
#          [0, 1, 1, 1]    ]

# Example Output

# Output 1:
#  0
# Output 2:
#  3

# Example Explanation

# Explanation 1:
#  Row 0 has maximum number of 1s.
# Explanation 2:
#  Row 3 has maximum number of 1s.

class Solution:
    # @param A : list of list of integers
    # @return an integer denoting the row index with maximum number of 1s
    
    def solve(self, A):
        n = len(A)  # Get the number of rows (and columns, since the matrix is square)
        maxOnes = 0  # Variable to store the maximum number of 1s found so far
        i = 0  # Index for rows
        k = n - 1  # Start from the last column for each row
        row = 0  # Variable to store the row index with the maximum number of 1s
        
        # Iterate through each row
        while i < n:
            # If the current element in the row is 1, move left (decrease column index)
            if A[i][k] == 1:
                k -= 1
                # If we've moved beyond the first column (no more 1s in this row), return this row
                if k == -1:
                    return i
            # If the current element is 0, check if the remaining columns have more 1s
            elif A[i][k] == 0:
                # If the number of 1s in this row (n-k-1) is greater than the previously recorded maximum
                if n - k - 1 > maxOnes:
                    maxOnes = n - k - 1  # Update maxOnes
                    row = i  # Update the row with maximum 1s
                # Move to the next row and reset column index to the last column
                i += 1
                k = n - 1
                
        return row  # Return the row with the maximum number of 1s
    
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: A simple case with 3 rows and 3 columns
    A1 = [
        [0, 1, 1],
        [0, 0, 1],
        [0, 1, 1]
    ]
    # Explanation: Row 0 has the maximum number of 1s.
    print("Test Case 1 Output:", solution.solve(A1))  # Expected Output: 0

    # Test Case 2: A larger matrix where row 3 has the maximum number of 1s
    A2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 1, 1, 1]
    ]
    # Explanation: Row 3 has the maximum number of 1s (3 1s).
    print("Test Case 2 Output:", solution.solve(A2))  # Expected Output: 3

    # Test Case 3: A matrix with no 1s
    A3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Explanation: There are no 1s, so the first row with no 1s is returned.
    print("Test Case 3 Output:", solution.solve(A3))  # Expected Output: 0

    # Test Case 4: A matrix where all rows have the same number of 1s
    A4 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    # Explanation: All rows have the same number of 1s, so the first row (index 0) is returned.
    print("Test Case 4 Output:", solution.solve(A4))  # Expected Output: 0

    # Test Case 5: A matrix with increasing number of 1s in each row
    A5 = [
        [0, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    # Explanation: Row 2 has the maximum number of 1s (3 1s).
    print("Test Case 5 Output:", solution.solve(A5))  # Expected Output: 2

    # Test Case 6: Matrix with a single row and no 1s
    A6 = [
        [0, 0, 0]
    ]
    # Explanation: There are no 1s, so the row is 0.
    print("Test Case 6 Output:", solution.solve(A6))  # Expected Output: 0

    # Test Case 7: Matrix with only one row and one 1
    A7 = [
        [0, 1, 0]
    ]
    # Explanation: The first row has 1 one.
    print("Test Case 7 Output:", solution.solve(A7))  # Expected Output: 0

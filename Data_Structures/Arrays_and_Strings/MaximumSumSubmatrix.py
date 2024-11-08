# Maximum Sum Submatrix

# Problem Description
# Given a N * M 2D matrix A. Find the maximum sum sub-matrix from the matrix A. Return the Sum.

# Problem Constraints
# 1 <= N, M <= 300
# -104 <= A[i][j] <= 104

# Input Format
# The first argument is a 2D Integer array A.

# Output Format
# Return the sum of the maximum sum sub-matrix from matrix A.

# Example Input

# Input 1:-
#     -6 -6
#    -29 -8
# A =  3 -8
#    -15  2
#     25 25
#     20 -5

# Input 2:-
# A = -17 -2
#      20 10

# Example Output

# Output 1:-
# 65
# Output 2:-
# 30

# Example Explanation

# Explanation 1:-
# The submatrix 
# 25 25
# 20 -5
# has the highest submatrix sum 65.

# Explanation 2:-
# The submatrix 
# 20 10
# has the highest sub matrix sum 30.

class Solution:
    # Function to find the maximum sum of a submatrix in a 2D matrix A
    # @param A: List of List of integers (2D matrix)
    # @return: Integer (maximum sum of the submatrix)
    def solve(self, A):
        # Edge case: If the matrix is empty or the first row is empty, return 0
        if not A or not A[0]:
            return 0
        
        # Initialize the number of rows and columns
        rows, cols = len(A), len(A[0])
        
        # Initialize the max_sum to a very small number (negative infinity)
        max_sum = float('-inf')
        
        # Iterate over all pairs of columns (left and right)
        for left in range(cols):
            # Initialize an array to store row sums for the current column pair (left, right)
            row_sums = [0] * rows
            
            # Iterate over all columns from left to right
            for right in range(left, cols):
                # Update the row_sums array by adding the elements in the current column
                for i in range(rows):
                    row_sums[i] += A[i][right]
                
                # Use Kadane's algorithm to find the maximum subarray sum in row_sums
                max_sum = max(max_sum, self.kadane(row_sums))
        
        # Return the maximum sum found
        return max_sum

    # Helper function to find the maximum sum of a subarray using Kadane’s algorithm
    # @param arr: List of integers
    # @return: Integer (maximum sum of subarray)
    def kadane(self, arr):
        max_sum = float('-inf')  # Initialize the maximum sum to a very small number
        curr_sum = 0  # Initialize the current sum to 0
        
        # Iterate over the array to find the maximum subarray sum
        for num in arr:
            curr_sum += num  # Add the current element to the current sum
            max_sum = max(max_sum, curr_sum)  # Update the max_sum if the current sum is larger
            
            # If the current sum is negative, reset it to 0 (start new subarray)
            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum  # Return the maximum subarray sum

# Test function to run test cases
def run_tests():
    s = Solution()
    
    # Test Case 1: Basic case with positive numbers
    A1 = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]
    print(s.solve(A1))  # Expected output: 29 (submatrix with sum 29)

    # Test Case 2: Case where all numbers are negative
    A2 = [
        [-1, -2, -3],
        [-4, -5, -6],
        [-7, -8, -9]
    ]
    print(s.solve(A2))  # Expected output: -1 (maximum sum subarray is just the least negative number)

    # Test Case 3: Case with some positive and negative numbers
    A3 = [
        [1, -2, 3],
        [4, -1, 2],
        [-1, 5, -3]
    ]
    print(s.solve(A3))  # Expected output: 8 (submatrix [1, -2, 3], [4, -1, 2])

    # Test Case 4: Case with single row
    A4 = [
        [1, 2, 3]
    ]
    print(s.solve(A4))  # Expected output: 6 (the entire row is the submatrix with maximum sum)

    # Test Case 5: Case with single column
    A5 = [
        [1],
        [2],
        [3]
    ]
    print(s.solve(A5))  # Expected output: 6 (the entire column is the submatrix with maximum sum)

    # Test Case 6: Empty matrix
    A6 = []
    print(s.solve(A6))  # Expected output: 0 (matrix is empty)

    # Test Case 7: Matrix with one element
    A7 = [
        [5]
    ]
    print(s.solve(A7))  # Expected output: 5 (matrix has only one element)

# Run test cases
run_tests()

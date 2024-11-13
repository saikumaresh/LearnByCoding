# Rotate by 90 degree
# Difficulty: Medium

# https://www.geeksforgeeks.org/problems/rotate-by-90-degree0356/1

# Problem Statement
# Given a square mat[][]. The task is to rotate it by 90 degrees in clockwise direction without using any extra space.

# Examples:

# Input: mat[][] = [[1 2 3], [4 5 6], [7 8 9]]
# Output:
# 7 4 1 
# 8 5 2
# 9 6 3

# Input: mat[][] = [1 2], [3 4]
# Output:
# 3 1 
# 4 2

# Input: mat[][] = [[1]]
# Output:
# 1

# Constraints:
# 1 ≤ mat.size() ≤ 1000
# 1 <= mat[][] <= 100

# Expected Complexities
# Time Complexity: O(n^2)Auxiliary Space: O(1)

def rotate(mat): 
    """
    Rotates the given square matrix by 90 degrees clockwise.

    Parameters:
    mat (List[List[int]]): A 2D list representing the square matrix to be rotated.

    Returns:
    List[List[int]]: The rotated matrix.
    """
    n = len(mat)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    
    # Step 2: Reverse each row to achieve the 90-degree clockwise rotation
    for i in range(n):
        mat[i].reverse()
    
    return mat

# Test Cases
if __name__ == "__main__":
    # Test Case 1: 3x3 matrix
    mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Test Case 1:", rotate(mat1))  
    # Expected output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    
    # Test Case 2: 2x2 matrix
    mat2 = [
        [1, 2],
        [3, 4]
    ]
    print("Test Case 2:", rotate(mat2))  
    # Expected output: [[3, 1], [4, 2]]
    
    # Test Case 3: 4x4 matrix
    mat3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("Test Case 3:", rotate(mat3))  
    # Expected output: [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

    # Test Case 4: 5x5 matrix
    mat4 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    print("Test Case 4:", rotate(mat4))  
    # Expected output: [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]

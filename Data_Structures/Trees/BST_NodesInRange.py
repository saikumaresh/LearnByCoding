# BST nodes in a range

# Problem Description
# Given a binary search tree of integers. You are given a range B and C.
# Return the count of the number of nodes that lie in the given range.

# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= B < = C <= 109

# Input Format
# First argument is a root node of the binary tree, A.
# Second argument is an integer B.
# Third argument is an integer C.

# Output Format
# Return the count of the number of nodes that lies in the given range.

# Example Input

# Input 1:
#             15
#           /    \
#         12      20
#         / \    /  \
#        10  14  16  27
#       /
#      8
#      B = 12
#      C = 20

# Input 2:
#             8
#            / \
#           6  21
#          / \
#         1   7
#      B = 2
#      C = 20


# Example Output

# Output 1:
#  5
# Output 2:
#  3

# Example Explanation

# Explanation 1:
#  Nodes which are in range [12, 20] are : [12, 14, 15, 20, 16]
# Explanation 2:
#  Nodes which are in range [2, 20] are : [8, 6, 7]

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x  # Node value
        self.left = None  # Left child node
        self.right = None  # Right child node

class Solution:
    # Function to count the number of nodes with values between B and C (inclusive)
    # @param A : root node of the tree
    # @param B : integer (lower bound of the range)
    # @param C : integer (upper bound of the range)
    # @return an integer (count of nodes within the given range)
    def solve(self, A, B, C):
        # Base case: if the current node is None, return 0
        if not A:
            return 0

        # Initialize count to 0
        count = 0
        
        # If the current node's value is within the range [B, C], increment the count
        if B <= A.val <= C:
            count += 1
        
        # Recursively count nodes in the left and right subtrees
        count += self.solve(A.left, B, C)
        count += self.solve(A.right, B, C)
        
        # Return the total count of nodes within the range
        return count


# Test cases for the solve function
def test_solve():
    solution = Solution()

    # Test Case 1: Tree with multiple nodes
    # Tree structure:
    #       10
    #      /  \
    #     5    15
    #    / \     \
    #   3   7    20
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right.right = TreeNode(20)

    # Counting nodes in the range [5, 15]
    print("Test Case 1:", "Passed" if solution.solve(root1, 5, 15) == 4 else "Failed")
    # Expected result: 4 (nodes: 5, 7, 10, 15)

    # Test Case 2: Tree with no nodes in the range
    # Tree structure:
    #       8
    #      / \
    #     3   10
    root2 = TreeNode(8)
    root2.left = TreeNode(3)
    root2.right = TreeNode(10)

    # Counting nodes in the range [20, 30]
    print("Test Case 2:", "Passed" if solution.solve(root2, 20, 30) == 0 else "Failed")
    # Expected result: 0 (no nodes in the range)

    # Test Case 3: Single node tree
    # Tree structure:
    #       5
    root3 = TreeNode(5)

    # Counting nodes in the range [1, 10]
    print("Test Case 3:", "Passed" if solution.solve(root3, 1, 10) == 1 else "Failed")
    # Expected result: 1 (only node 5 is in the range)

    # Test Case 4: Empty tree
    root4 = None

    # Counting nodes in the range [1, 10]
    print("Test Case 4:", "Passed" if solution.solve(root4, 1, 10) == 0 else "Failed")
    # Expected result: 0 (tree is empty)

# Run the test cases
test_solve()

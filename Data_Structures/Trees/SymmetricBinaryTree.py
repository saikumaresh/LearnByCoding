# Symmetric Binary Tree

# Problem Description
# Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Problem Constraints
# 1 <= number of nodes <= 105

# Input Format
# First and only argument is the root node of the binary tree.

# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ).

# Example Input

# Input 1:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# Input 2:
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Example Output

# Output 1:
#  1
# Output 2:
#  0

# Example Explanation

# Explanation 1:
#  The above binary tree is symmetric. 
# Explanation 2:
# The above binary tree is not symmetric.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Helper function to check if two subtrees are mirrors of each other
    # @param left: left subtree of the current node
    # @param right: right subtree of the current node
    # @return an integer (1 if they are mirrors, 0 if they are not)
    def isMirror(self, left, right):
        # If both subtrees are None, they are mirrors of each other (base case)
        if left is None and right is None:
            return 1  # Both are empty subtrees, so they are symmetric

        # If one subtree is None and the other is not, they are not mirrors
        if left is None or right is None:
            return 0  # One subtree is missing, so they can't be symmetric

        # If the values of the current nodes are different, they are not mirrors
        if left.val != right.val:
            return 0  # Values are not equal, so they are not symmetric

        # Recursively check the following:
        # 1. The left subtree of the left node with the right subtree of the right node
        # 2. The right subtree of the left node with the left subtree of the right node
        return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    # Main function to check if the entire tree is symmetric
    # @param A : root node of the tree
    # @return an integer (1 if the tree is symmetric, 0 if it is not)
    def isSymmetric(self, A):
        # If the tree is empty, it is symmetric
        if not A:
            return 1  # An empty tree is considered symmetric

        # Check if the left and right subtrees of the root are mirrors of each other
        return self.isMirror(A.left, A.right)

# Test cases for the code

def test_isSymmetric():
    solution = Solution()

    # Test Case 1: Symmetric Tree
    # Tree structure:
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    print("Test Case 1 (Symmetric):", "Passed" if solution.isSymmetric(root1) == 1 else "Failed")

    # Test Case 2: Asymmetric Tree
    # Tree structure:
    #       1
    #      / \
    #     2   2
    #      \    \
    #       3    3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    print("Test Case 2 (Asymmetric):", "Passed" if solution.isSymmetric(root2) == 0 else "Failed")

    # Test Case 3: Single Node Tree
    # Tree structure:
    #       1
    root3 = TreeNode(1)

    print("Test Case 3 (Single Node):", "Passed" if solution.isSymmetric(root3) == 1 else "Failed")

    # Test Case 4: Empty Tree
    root4 = None

    print("Test Case 4 (Empty Tree):", "Passed" if solution.isSymmetric(root4) == 1 else "Failed")

# Run the test cases
test_isSymmetric()
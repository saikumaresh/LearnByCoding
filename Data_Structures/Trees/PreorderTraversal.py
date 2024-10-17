# Preorder Traversal

# Problem Description
# Given a binary tree, return the preorder traversal of its nodes values.

# Problem Constraints
# 1 <= number of nodes <= 105

# Input Format
# First and only argument is root node of the binary tree, A.

# Output Format
# Return an integer array denoting the preorder traversal of the given binary tree.

# Example Input

# Input 1:

#    1
#     \
#      2
#     /
#    3

# Input 2:
#    1
#   / \
#  6   2
#     /
#    3


# Example Output

# Output 1:
#  [1, 2, 3]
# Output 2:
#  [1, 6, 2, 3]

# Example Explanation

# Explanation 1:
#  The Preoder Traversal of the given tree is [1, 2, 3].
# Explanation 2:
#  The Preoder Traversal of the given tree is [1, 6, 2, 3].

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of the tree
    # @return a list of integers in preorder traversal order
    def preorderTraversal(self, A):
        result = []  # List to store the result
        if not A:
            return []  # If the current node is None, return an empty list
        
        # Append the current node's value
        result.append(A.val)
        
        # Recursively call on the left subtree and extend result with the output
        result.extend(self.preorderTraversal(A.left))
        
        # Recursively call on the right subtree and extend result with the output
        result.extend(self.preorderTraversal(A.right))
        
        return result  # Return the final preorder traversal result

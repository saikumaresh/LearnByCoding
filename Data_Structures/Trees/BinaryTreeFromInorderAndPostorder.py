# Binary Tree From Inorder And Postorder

# https://www.interviewbit.com/problems/binary-tree-from-inorder-and-postorder/

# Given inorder and postorder traversal of a tree, construct the binary tree.
# Note: You may assume that duplicates do not exist in the tree.

# Example :
# Input : 
#         Inorder : [2, 1, 3]
#         Postorder : [2, 3, 1]

# Return : 
#             1
#            / \
#           2   3

# Definition for a binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers (Inorder)
    # @param B : list of integers (Postorder)
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not A or not B:
            return None
        
        # The last element in postorder is the root of the current subtree
        root_val = B.pop()
        root = TreeNode(root_val)
        
        # Find the index of the root in the inorder traversal
        root_index = A.index(root_val)
        
        # Recursively build the right subtree and then the left subtree
        root.right = self.buildTree(A[root_index + 1:], B)
        root.left = self.buildTree(A[:root_index], B)
        
        return root

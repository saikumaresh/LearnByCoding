# Remove Half Nodes

# Problem Description
# Given a binary tree A with N nodes.
# You have to remove all the half nodes and return the final binary tree.
# NOTE:
# Half nodes are nodes which have only one child.
# Leaves should not be touched as they have both children as NULL.

# Problem Constraints
#  1 <= N <= 105

# Input Format
# First and only argument is an pointer to the root of binary tree A.

# Output Format
# Return a pointer to the root of the new binary tree.

# Example Input

# Input 1:
#            1
#          /   \
#         2     3
#        / 
#       4

# Input 2:
#             1
#           /   \
#          2     3
#         / \     \
#        4   5     6

# Example Output

# Output 1:
#            1
#          /   \
#         4     3

# Output 2:
#             1
#           /   \
#          2     6
#         / \
#        4   5

# Example Explanation

# Explanation 1:
#  The only half node present in the tree is 2 so we will remove this node.
# Explanation 2:
#  The only half node present in the tree is 3 so we will remove this node.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to remove half nodes from the binary tree
    def solve(self, A):
        # Base case: if the node is null, return null
        if A is None:
            return None
        
        # Recursively remove half nodes from left and right subtrees
        A.left = self.solve(A.left)
        A.right = self.solve(A.right)
        
        # If the current node is a half node with only a left child, return the left child
        if A.left and not A.right:
            return A.left
        
        # If the current node is a half node with only a right child, return the right child
        if A.right and not A.left:
            return A.right
        
        # If the node is not a half node, return the node itself
        return A

# Explanation:
# We define the base case where the node is None, meaning we have reached a leaf or end of the subtree.
# The function recursively processes the left and right subtrees using post-order traversal, making sure to remove half nodes in the subtrees first.
# For each node, if it has only one child (either left or right), we replace it with its only child, effectively removing the half node.
# If the node has both children or no children, we return the node as is.

# Time Complexity: The solution performs a post-order traversal of the tree, visiting each node exactly once, making the time complexity O(N), 
# where N is the number of nodes in the tree.
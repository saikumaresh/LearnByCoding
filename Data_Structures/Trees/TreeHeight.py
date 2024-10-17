# Tree Height

# Problem Description
# You are given the root node of a binary tree A. You have to find the height of the given tree.
# A binary tree's height is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Problem Constraints
# 1 <= Number of nodes in the tree <= 105
# 0 <= Value of each node <= 109

# Input Format
# The first and only argument is a tree node A.

# Output Format
# Return an integer denoting the height of the tree.

# Example Input

# Input 1:
#  Values =  1 
#           / \     
#          4   3       
                 
# Input 2:
#  Values =  1      
#           / \     
#          4   3                       
#         /         
#        2                                     


# Example Output

# Output 1:
#  2 
# Output 2:
#  3 

# Example Explanation

# Explanation 1:
#  Distance of node having value 1 from root node = 1
#  Distance of node having value 4 from root node = 2 (max)
#  Distance of node having value 3 from root node = 2 (max)

# Explanation 2:
#  Distance of node having value 1 from root node = 1
#  Distance of node having value 4 from root node = 2
#  Distance of node having value 3 from root node = 2
#  Distance of node having value 2 from root node = 3 (max)

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
sys.setrecursionlimit(10**6)  # Setting recursion limit to handle deep trees

class Solution:
    # @param A : root node of the tree
    # @return an integer representing the maximum depth of the tree
    def solve(self, A):
        if A is None: 
            return 0  # If the current node is None, the depth is 0
        
        else:
            # Recursively find the depth of the left subtree
            lDepth = self.solve(A.left) 
            
            # Recursively find the depth of the right subtree
            rDepth = self.solve(A.right)
            
            # The depth of the current node is the maximum of left and right depths plus 1
            return (max(lDepth, rDepth) + 1)

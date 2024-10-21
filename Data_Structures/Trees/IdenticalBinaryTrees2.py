# Identical Binary Trees

# Problem Description
# Given two binary trees, check if they are equal or not.
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Problem Constraints
# 1 <= number of nodes <= 105

# Input Format
# The first argument is a root node of the first tree, A.
# The second argument is a root node of the second tree, B.

# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

# Example Input

# Input 1:
#    1       1
#   / \     / \
#  2   3   2   3

# Input 2:
#    1       1
#   / \     / \
#  2   3   3   3

# Example Output

# Output 1:
#  1
# Output 2:
#  0

# Example Explanation

# Explanation 1:
#  Both trees are structurally identical and the nodes have the same value.
# Explanation 2:
#  Values of the left child of the root node of the trees are different.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of the first tree
    # @param B : root node of the second tree
    # @return an integer (1 if both trees are identical, 0 if not)
    
    def isSameTree(self, A, B):
        # If both nodes are None (i.e., both trees are empty), they are the same
        if (not A) and (not B):
            return 1  # Both trees are identical (base case)
        
        # If one node is None and the other is not, the trees are not identical
        elif ((not A) and B) or (A and (not B)):
            return 0  # The trees are not the same
        
        # Check if the current node values in both trees are equal
        if A.val == B.val:
            flag = 1  # The current nodes are the same
        else:
            flag = 0  # The current nodes are different
        
        # Recursively check the left and right subtrees for both trees
        # The result is the product of the current flag and the recursive results
        flag *= self.isSameTree(A.left, B.left)  # Check left subtrees
        flag *= self.isSameTree(A.right, B.right)  # Check right subtrees
        
        # Return the final result after checking all nodes
        return flag

# Create the nodes for Tree A
A = TreeNode(1)
A.left = TreeNode(2)
A.right = TreeNode(3)

# Create the nodes for Tree B
B = TreeNode(1)
B.left = TreeNode(2)
B.right = TreeNode(3)

# Create a solution object
sol = Solution()

# Call the function to check if the trees are identical
result = sol.isSameTree(A, B)

print(result)  # Output: 1 (since both trees are identical)
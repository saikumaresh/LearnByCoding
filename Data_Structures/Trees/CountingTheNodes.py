# Counting the Nodes

# Problem Description
# Given the root of a tree A with each node having a certain value, find the count of nodes with more value than all its ancestors.
# Ancestor means that every node that occurs before the current node in the path from root to the node.

# Problem Constraints
# 1 <= Number of Nodes <= 200000
# 1 <= Value of Nodes <= 2000000000

# Input Format
# The first and only argument of input is a tree node.

# Output Format
# Return a single integer denoting the count of nodes that have more value than all of its ancestors.

# Example Input

# Input 1:
#      3

# Input 2:
#     4
#    / \
#   5   2
#      / \
#     3   6

# Example Output

# Output 1:
#  1 
# Output 2:
#  3

# Example Explanation

# Explanation 1:
#  There's only one node in the tree that is the valid node.
# Explanation 2:
#  The valid nodes are 4, 5 and 6.

# Definition for a binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # Recursive helper function to count nodes greater than the current max value in the path
    # @param A : root node of the tree
    # @param maxval : maximum value seen so far along the path
    # @return an integer : count of nodes with value greater than maxval
    def nodes(self, A, maxval):
        # Base case: if the node is None, return 0
        if not A:
            return 0
        
        count = 0  # Initialize count to 0 for this node
        
        # If the current node's value is greater than maxval, increment count
        if A.val > maxval:
            count += 1  # Node is considered a "good" node
            maxval = A.val  # Update maxval to the current node's value
        
        # Recursively count "good" nodes in the left and right subtrees
        count += self.nodes(A.left, maxval)
        count += self.nodes(A.right, maxval)
        
        # Return the total count for this node and its subtrees
        return count

    # Main function to start the node counting process
    # @param A : root node of the binary tree
    # @return an integer : total count of "good" nodes
    def solve(self, A):
        maxval = 0  # Initialize maxval to 0 (assuming tree has positive values)
        
        # Start the recursive process from the root node and return the total count
        return self.nodes(A, maxval)

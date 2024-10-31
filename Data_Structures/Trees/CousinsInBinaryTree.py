# Cousins in Binary Tree

# https://www.interviewbit.com/problems/cousins-in-binary-tree/

# Problem Description
# Given a Binary Tree A consisting of N nodes.
# You need to find all the cousins of node B.
# NOTE:
# Siblings should not be considered as cousins.
# Try to do it in single traversal.
# You can assume that Node B is there in the tree A.
# Order doesn't matter in the output.

# Problem Constraints
#  1 <= N <= 105 
#  1 <= B <= N

# Input Format
# First Argument represents the root of binary tree A.
# Second Argument is an integer B denoting the node number.

# Output Format
# Return an integer array denoting the cousins of node B.
# NOTE: Order doesn't matter.

# Example Input

# Input 1:
#  A =
#            1
#          /   \
#         2     3
#        / \   / \
#       4   5 6   7 
# B = 5

# Input 2:
#  A = 
#             1
#           /   \
#          2     3
#         / \ .   \
#        4   5 .   6
# B = 1

# Example Output
# Output 1:
#  [6, 7]
# Output 2:
#  []

# Example Explanation

# Explanation 1:
#  Cousins of Node 5 are Node 6 and 7 so we will return [6, 7]
#  Remember Node 4 is sibling of Node 5 and do not need to return this.

# Explanation 2:
#  Since Node 1 is the root so it doesn't have any cousin so we will return an empty array.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Helper function to find cousins
    def cousinsTree(self, root, B):
        # Initialize queue with root node and its parent (-1 since root has no parent)
        queue = [[root, -1]]
        flag = False  # Flag to indicate if we have found node B
        
        while queue:
            level = []  # List to keep track of nodes at the current level
            
            # Process all nodes at the current level
            for i in range(len(queue)):
                curr, parent = queue.pop(0)  # Get the current node and its parent
                level.append([curr.val, parent])  # Add current node's value and parent to level list
                
                # Check if the current node is B, if yes, store its parent and set flag
                if curr.val == B:
                    flag = True
                    target_parent = parent
                
                # Add left and right children to the queue with the current node as parent
                if curr.left:
                    queue.append([curr.left, curr.val])
                if curr.right:
                    queue.append([curr.right, curr.val])
            
            # If we found node B in the current level, stop the search
            if flag:
                break

        # Collect cousins (nodes at the same level but different parent)
        result = [val for val, parent in level if parent != target_parent]
        return result

    # Main solve function
    def solve(self, A, B):
        return self.cousinsTree(A, B)

# Constructing the binary tree for testing
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

solution = Solution()

# Test case 1: Finding cousins of node 5, which should be [6]
print(solution.solve(root, 5))  # Expected output: [6]

# Test case 2: Finding cousins of node 4, which should be [6]
print(solution.solve(root, 4))  # Expected output: [6]

# Test case 3: Finding cousins of node 6, which should be [4, 5]
print(solution.solve(root, 6))  # Expected output: [4, 5]

# Test case 4: Root node has no cousins
print(solution.solve(root, 1))  # Expected output: []

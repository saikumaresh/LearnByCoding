# Vertical Order traversal of Binary Tree

# https://www.interviewbit.com/problems/vertical-order-traversal-of-binary-tree/

# Problem Description
# Given a binary tree A consisting of N nodes, return a 2-D array denoting the vertical order traversal of A.

# NOTE:
# If 2 or more Tree Nodes shares the same vertical level then the one with earlier occurence in the level-order traversal of tree comes first in the output.
# Row 1 of the output array will be the nodes on leftmost vertical line similarly last row of the output array will be the nodes on the rightmost vertical line.

# Problem Constraints
# 0 <= N <= 104

# Input Format
# First and only argument is an pointer to root of the binary tree A.

# Output Format
# Return a 2D array denoting the vertical order traversal of A.

# Example Input
# Input 1:

#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9
# Input 2:

#            1
#          /   \
#         2     3
#        / \
#       4   5


# Example Output
# Output 1:

#  [
#     [2],
#     [3],
#     [6, 5],
#     [7],
#     [9]
#  ]
# Output 2:

#  [
#     [4],
#     [2],
#     [1, 5],
#     [3]
#  ]


# Example Explanation

# Explanation 1:
#  Nodes on Vertical Line 1: 2
#  Nodes on Vertical Line 2: 3
#  Nodes on Vertical Line 3: 6, 5
#     As 6 and 5 are on the same vertical level but as 6 comes first in the level-order traversal of the tree so we will output 6 before 5.
#  Nodes on Vertical Line 4: 7
#  Nodes on Vertical Line 5: 9

# Explanation 2:
#  Nodes on Vertical Line 1: 4
#  Nodes on Vertical Line 2: 2
#  Nodes on Vertical Line 3: 1, 5
#  Nodes on Vertical Line 4: 3

# ================== Solution ================== 

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict, deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        if not A:
            return []

        # Dictionary to store nodes at each horizontal distance
        column_table = defaultdict(list)
        # Queue to perform level-order traversal (node, column)
        queue = deque([(A, 0)])

        while queue:
            node, column = queue.popleft()
            if node:
                column_table[column].append(node.val)
                # Add left child to the queue with column - 1
                if node.left:
                    queue.append((node.left, column - 1))
                # Add right child to the queue with column + 1
                if node.right:
                    queue.append((node.right, column + 1))

        # Sort the dictionary by column index and prepare the result
        sorted_columns = sorted(column_table.keys())
        result = [column_table[col] for col in sorted_columns]

        return result

# Example Usage
# Input Tree:
#       6
#     /   \
#    3     7
#   / \     \
#  2   5     9

A = TreeNode(6)
A.left = TreeNode(3)
A.right = TreeNode(7)
A.left.left = TreeNode(2)
A.left.right = TreeNode(5)
A.right.right = TreeNode(9)

solution = Solution()
result = solution.verticalOrderTraversal(A)
print(result)  # Output: [[2], [3], [6, 5], [7], [9]]

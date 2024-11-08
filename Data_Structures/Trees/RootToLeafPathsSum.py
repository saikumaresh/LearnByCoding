# Root to leaf paths sum

# Difficulty: Medium
# https://www.geeksforgeeks.org/problems/root-to-leaf-paths-sum/1

# Problem Statement
# Given a binary tree, where every node value is a number. 
# Find the sum of all the numbers that are formed from root to leaf paths. 
# The formation of the numbers would be like 10*parent + current (see the examples for more clarification).

# Examples:

# Input:      
# https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700454/Web/Other/blobid0_1730705508.png
# Output: 13997
# Explanation : There are 4 leaves, resulting in leaf path of 632, 6357, 6354, 654 sums to 13997.

# Input:    
# https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/700454/Web/Other/blobid1_1730705776.png
# Output: 2630
# Explanation: There are 3 leaves, resulting in leaf path of 1240, 1260, 130 sums to 2630.

# Input:    
#            1
#           /
#          2                    
# Output: 12
# Explanation: There is 1 leaf, resulting in leaf path of 12.

# Constraints:
# 1 ≤ number of nodes ≤ 31
# 1 ≤ node->data ≤ 100

# Company Tags
# Amazon, Microsoft, OYO Rooms, Google

# Topic Tags
# TreeData Structures

# Expected Complexities
# Time Complexity: O(n)Auxiliary Space: O(h)

# Helper class for binary tree node definition
class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    # Function to calculate the sum of all numbers formed from root-to-leaf paths
    # @param root: Root node of the binary tree
    # @param prefix: Accumulated value passed down from the parent nodes (default is 0)
    # @return: Integer sum of all numbers formed from root-to-leaf paths
    def treePathSum(self, root, prefix=0):
        # If the node is None, return 0 (base case for recursion)
        if not root:
            return 0
        
        # Calculate the current sum by appending the current node's value to the path sum so far
        currsum = 10 * prefix + root.data
        
        # If the current node is a leaf node, return the current path sum
        if not root.left and not root.right:
            return currsum

        # Recursively calculate the sum for left and right subtrees
        # Add up the results from both left and right paths
        return self.treePathSum(root.left, currsum) + self.treePathSum(root.right, currsum)

# Test function to run test cases
def run_tests():
    s = Solution()

    # Test Case 1: Simple tree with one root-to-leaf path
    # Tree structure:
    #       1
    #        \
    #         2
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    print(s.treePathSum(root1))  # Expected output: 12 (formed by the path 1 -> 2)

    # Test Case 2: Tree with multiple root-to-leaf paths
    # Tree structure:
    #       1
    #      / \
    #     2   3
    # Paths: 1->2 (12), 1->3 (13)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(s.treePathSum(root2))  # Expected output: 25 (12 + 13)

    # Test Case 3: Larger tree with more levels
    # Tree structure:
    #       4
    #      / \
    #     9   0
    #    / \
    #   5   1
    # Paths: 4->9->5 (495), 4->9->1 (491), 4->0 (40)
    root3 = TreeNode(4)
    root3.left = TreeNode(9)
    root3.right = TreeNode(0)
    root3.left.left = TreeNode(5)
    root3.left.right = TreeNode(1)
    print(s.treePathSum(root3))  # Expected output: 1026 (495 + 491 + 40)

    # Test Case 4: Tree with only root node
    # Tree structure:
    #       7
    root4 = TreeNode(7)
    print(s.treePathSum(root4))  # Expected output: 7 (only one path with root alone)

    # Test Case 5: Tree with negative values
    # Tree structure:
    #       -1
    #      /   \
    #    -2     3
    # Paths: -1->-2 (-12), -1->3 (-7)
    root5 = TreeNode(-1)
    root5.left = TreeNode(-2)
    root5.right = TreeNode(3)
    print(s.treePathSum(root5))  # Expected output: -19 (-12 + -7)

    # Test Case 6: Empty tree
    # Expected output: 0
    root6 = None
    print(s.treePathSum(root6))  # Expected output: 0

# Run test cases
run_tests()

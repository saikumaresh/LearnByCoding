# Invert the Binary Tree

# Problem Description
# Given a binary tree A, invert the binary tree and return it.
# Inverting refers to making the left child the right child and vice versa.

# Problem Constraints
# 1 <= size of tree <= 100000

# Input Format
# First and only argument is the head of the tree A.

# Output Format
# Return the head of the inverted tree.

# Example Input

# Input 1:
#      1
#    /   \
#   2     3

# Input 2:
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7

# Example Output

# Output 1:
#      1
#    /   \
#   3     2

# Output 2:
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4


# Example Explanation

# Explanation 1:
# Tree has been inverted.
# Explanation 2:
# Tree has been inverted.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x  # Node value
        self.left = None  # Left child node
        self.right = None  # Right child node

class Solution:
    # Function to invert the binary tree (mirror the tree)
    # @param A : root node of the tree
    # @return the root node of the inverted tree
    def invertTree(self, A):
        # Base case: if the current node is None, return None
        if not A:
            return None
        
        # Swap the left and right children of the current node
        A.right, A.left = A.left, A.right
        
        # Recursively invert the left subtree
        self.invertTree(A.left)
        
        # Recursively invert the right subtree
        self.invertTree(A.right)
        
        # Return the root node of the inverted tree
        return A

# Function to print the tree in level order for testing purposes
def printLevelOrder(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

# Test cases for the invertTree function
def test_invertTree():
    solution = Solution()

    # Test Case 1: Tree with multiple nodes
    # Original Tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)

    # Inverting the tree
    inverted_root1 = solution.invertTree(root1)

    # Expected inverted tree structure:
    #       1
    #      / \
    #     3   2
    #    /   / \
    #   6   5   4
    print("Test Case 1:", "Passed" if printLevelOrder(inverted_root1) == [1, 3, 2, 6, 5, 4] else "Failed")

    # Test Case 2: Single node tree
    # Original Tree:
    #       7
    root2 = TreeNode(7)

    # Inverting the tree (should remain the same)
    inverted_root2 = solution.invertTree(root2)

    # Expected inverted tree structure: [7]
    print("Test Case 2:", "Passed" if printLevelOrder(inverted_root2) == [7] else "Failed")

    # Test Case 3: Empty tree
    root3 = None

    # Inverting the empty tree (should return None)
    inverted_root3 = solution.invertTree(root3)

    # Expected result: empty list
    print("Test Case 3:", "Passed" if printLevelOrder(inverted_root3) == [] else "Failed")

    # Test Case 4: Tree with two nodes
    # Original Tree:
    #       9
    #        \
    #        10
    root4 = TreeNode(9)
    root4.right = TreeNode(10)

    # Inverting the tree
    inverted_root4 = solution.invertTree(root4)

    # Expected inverted tree structure:
    #       9
    #      /
    #     10
    print("Test Case 4:", "Passed" if printLevelOrder(inverted_root4) == [9, 10] else "Failed")

# Run the test cases
test_invertTree()

# Serialize Binary Tree Migrated

# https://www.interviewbit.com/problems/serialize-binary-tree-migrated/

# Problem Description
# Given the root node  of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.
# Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.
# NOTE:
# In the array, the NULL/None child is denoted by -1.
# For more clarification check the Example Input.

# Problem Constraints
#  1 <= number of nodes <= 105

# Input Format
# Only argument is a A denoting the root node of a Binary Tree.

# Output Format
# Return an integer array denoting the Level Order Traversal of the given Binary Tree.

# Example Input

# Input 1:
#            1
#          /   \
#         2     3
#        / \
#       4   5

# Input 2:
#             1
#           /   \
#          2     3
#         / \     \
#        4   5     6


# Example Output

# Output 1:
#  [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
# Output 2:
#  [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


# Example Explanation

# Explanation 1:
#  The Level Order Traversal of the given tree will be [1, 2, 3, 4, 5 , -1, -1, -1, -1, -1, -1].
#  Since 3, 4 and 5 each has both NULL child we had represented that using -1.

# Explanation 2:
#  The Level Order Traversal of the given tree will be [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1].
#  Since 3 has left child as NULL while 4 and 5 each has both NULL child.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # Function to return level-order traversal with placeholders for None nodes
    def solve(self, A):
        """
        Perform a level-order traversal on a binary tree. For each level,
        append node values to result list. If a node is missing (None),
        append -1 to maintain the structure.
        
        Parameters:
        A (TreeNode): Root node of the binary tree.
        
        Returns:
        List[int]: List of node values in level-order traversal,
                   with -1 as placeholders for missing nodes.
        """
        # Edge case: if tree is empty
        if not A:
            return []
        
        result = []  # Stores the final level-order traversal result
        queue = deque([A])  # Initialize a deque with root node
        # Using deque here improves efficiency compared to a regular list, as popleft() in a deque is O(1), while removing the first element of a list is O(n)

        while queue:
            # Dequeue a node
            node = queue.popleft()
            if node:
                result.append(node.val)  # Add node value to result
                # Add left and right children (or None) to the queue
                queue.append(node.left)
                queue.append(node.right)
            else:
                # Use -1 as placeholder for missing node
                result.append(-1)
        
        return result

# Helper function to build a binary tree for testing
def build_tree(values):
    """
    Build a binary tree from a list of values, where None represents a missing node.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Full binary tree
    root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(solution.solve(root1))  # Expected: [1, 2, 3, 4, 5, 6, 7]

    # Test Case 2: Binary tree with missing nodes
    root2 = build_tree([1, 2, None, 4, 5])
    print(solution.solve(root2))  # Expected: [1, 2, -1, 4, 5, -1, -1]

    # Test Case 3: Single node tree
    root3 = build_tree([1])
    print(solution.solve(root3))  # Expected: [1]

    # Test Case 4: Empty tree
    root4 = build_tree([])
    print(solution.solve(root4))  # Expected: []

    # Test Case 5: Binary tree with some leaf nodes missing
    root5 = build_tree([1, None, 2, None, 3])
    print(solution.solve(root5))  # Expected: [1, -1, 2, -1, 3, -1, -1]

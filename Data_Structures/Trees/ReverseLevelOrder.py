# Reverse Level Order

# Problem Description
# Given a binary tree, return the reverse level order traversal of its nodes values. (i.e, from left to right and from last level to starting level).

# Problem Constraints
# 1 <= number of nodes <= 5 * 105
# 1 <= node value <= 105

# Input Format
# First and only argument is a pointer to the root node of the Binary Tree, A.

# Output Format
# Return an integer array denoting the reverse level order traversal from left to right.

# Example Input

# Input 1:
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Input 2:
#    1
#   / \
#  6   2
#     /
#    3

# Example Output

# Output 1:
#  [15, 7, 9, 20, 3] 
# Output 2:
#  [3, 6, 2, 1]

# Example Explanation

# Explanation 1:
#  Nodes as level 3 : [15, 7]
#  Nodes at level 2: [9, 20]
#  Nodes at level 1: [3]
#  Reverse level order traversal will be: [15, 7, 9, 20, 3]

# Explanation 2:
#  Nodes as level 3 : [3]
#  Nodes at level 2: [6, 2]
#  Nodes at level 1: [1]
#  Reverse level order traversal will be: [3, 6, 2, 1]

class TreeNode:
    # A class to represent each node in the binary tree
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Method to perform a reverse level-order traversal on a binary tree
    # @param A : root node of the binary tree
    # @return a list of integers representing the reverse level-order traversal

    def solve(self, A):
        # If the tree is empty, return an empty list
        if not A:
            return []
        
        # Initialize the queue with the root node and levels list to store each level
        queue = [A]
        levels = []
        
        # Perform level-order traversal
        while queue:
            level = []
            
            # Iterate through all nodes at the current level
            for i in range(len(queue)):
                node = queue.pop(0)  # Get the node from the queue
                level.append(node.val)  # Append the node's value to the current level list
                
                # Add the left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add the current level to the levels list
            levels.append(level)
        
        # Prepare the final result in reverse level-order
        result = []
        for i in reversed(levels):
            result.extend(i)
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Helper function to build a binary tree from a list of values (None represents missing nodes)
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i, node in enumerate(nodes):
            if node:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    node.left = nodes[left_index]
                if right_index < len(nodes):
                    node.right = nodes[right_index]
        return nodes[0]
    
    # Test Case 1
    # Tree:       3
    #           /   \
    #          9     20
    #               /   \
    #              15    7
    # Expected Output: [15, 7, 9, 20, 3]
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(solution.solve(root))  # Output: [15, 7, 9, 20, 3]
    
    # Test Case 2
    # Tree:       1
    #           /   \
    #          2     3
    # Expected Output: [2, 3, 1]
    root = build_tree([1, 2, 3])
    print(solution.solve(root))  # Output: [2, 3, 1]
    
    # Test Case 3
    # Tree:       1
    # Expected Output: [1]
    root = build_tree([1])
    print(solution.solve(root))  # Output: [1]
    
    # Test Case 4
    # Empty tree
    # Expected Output: []
    root = build_tree([])
    print(solution.solve(root))  # Output: []
    
    # Test Case 5
    # Tree:       1
    #           / 
    #          2
    #         /
    #        3
    # Expected Output: [3, 2, 1]
    root = build_tree([1, 2, None, 3])
    print(solution.solve(root))  # Output: [3, 2, 1]

# Flatten Binary Tree to Linked List

# Problem Description
# Given a binary tree A, flatten it to a linked list in-place.
# The left child of all nodes should be NULL.

# Problem Constraints
# 1 <= size of tree <= 100000

# Input Format
# First and only argument is the head of tree A.

# Output Format
# Return the linked-list after flattening.

# Example Input

# Input 1:
#      1
#     / \
#    2   3

# Input 2:
#          1
#         / \
#        2   5
#       / \   \
#      3   4   6

# Example Output

# Output 1:
# 1
#  \
#   2
#    \
#     3

# Output 2:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Example Explanation

# Explanation 1:
#  Tree flattening looks like this.
# Explanation 2:
#  Tree flattening looks like this.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        # Initialize the node with a value x, and left and right pointers
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        This function flattens a binary tree into a 'linked list' in-place.
        After flattening, the left of each node should be NULL, and the right child
        should contain the next node in preorder traversal.
        
        Arguments:
        root -- the root node of the binary tree
        
        Returns:
        The root of the modified tree, which is now flattened.
        """
        if not root:
            return
        
        # Recursively flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # If the left subtree exists
        if root.left:
            # Store the right subtree temporarily
            temp = root.right
            # Move the left subtree to the right
            root.right = root.left
            # Set the left subtree to None
            root.left = None
            
            # Traverse to the rightmost node of the new right subtree
            current = root.right
            while current.right:
                current = current.right
            # Attach the original right subtree to the end of the new right subtree
            current.right = temp
        
        # Return the modified tree root
        return root

# Helper function to create a binary tree from a list of values
def create_binary_tree(values):
    """
    Creates a binary tree from a list of values using level-order insertion.
    
    Arguments:
    values -- list of integers representing tree node values
    
    Returns:
    The root of the created binary tree.
    """
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# Helper function to get the flattened tree as a list
def get_flattened_list(root):
    """
    Returns the values of a flattened binary tree as a list.
    
    Arguments:
    root -- the root node of the binary tree
    
    Returns:
    A list of values in the flattened tree.
    """
    result = []
    while root:
        result.append(root.val)
        root = root.right
    return result

# Test cases
def test_flatten():
    """
    Test cases for the flatten function.
    """
    solution = Solution()

    # Test Case 1: Tree with multiple levels
    # Tree structure:
    #      1
    #     / \
    #    2   5
    #   / \   \
    #  3   4   6
    # After flattening: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    root1 = create_binary_tree([1, 2, 5, 3, 4, None, 6])
    solution.flatten(root1)
    result1 = get_flattened_list(root1)
    print("Test Case 1:", result1)  # Expected output: [1, 2, 3, 4, 5, 6]

    # Test Case 2: Tree with single node
    # Tree structure:
    #   1
    # After flattening: 1
    root2 = create_binary_tree([1])
    solution.flatten(root2)
    result2 = get_flattened_list(root2)
    print("Test Case 2:", result2)  # Expected output: [1]

    # Test Case 3: Tree with only left children
    # Tree structure:
    #      1
    #     /
    #    2
    #   /
    #  3
    # After flattening: 1 -> 2 -> 3
    root3 = create_binary_tree([1, 2, None, 3])
    solution.flatten(root3)
    result3 = get_flattened_list(root3)
    print("Test Case 3:", result3)  # Expected output: [1, 2, 3]

    # Test Case 4: Empty tree
    # Tree structure: None
    root4 = create_binary_tree([])
    solution.flatten(root4)
    result4 = get_flattened_list(root4)
    print("Test Case 4:", result4)  # Expected output: []

    # Test Case 5: Tree with right children only
    # Tree structure:
    #  1
    #   \
    #    2
    #     \
    #      3
    # After flattening: 1 -> 2 -> 3
    root5 = create_binary_tree([1, None, 2, None, 3])
    solution.flatten(root5)
    result5 = get_flattened_list(root5)
    print("Test Case 5:", result5)  # Expected output: [1, 2, 3]

# Run test cases
test_flatten()

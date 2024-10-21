# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x  # Node value
        self.left = None  # Left child node
        self.right = None  # Right child node

class Solution:
    # @param A : root node of tree
    # @param B : integer (target value to find the path to)
    # @return a list of integers representing the path from root to node B

    def solve(self, A, B):
        # Helper function to find the path from the root to the target node
        # @param node : current node
        # @param target : target node value
        # @param path : list that stores the path from the root to the current node
        # @return : list of integers representing the path if found, otherwise an empty list
        def find_path(node, target, path):
            # If the current node is None, return an empty list
            if not node:
                return []

            # Add the current node value to the path
            path = path + [node.val]

            # If the current node's value matches the target, return the current path
            if node.val == target:
                return path

            # Recursively check in the left subtree
            left_path = find_path(node.left, target, path)
            if left_path:  # If a path is found in the left subtree, return it
                return left_path

            # Recursively check in the right subtree
            right_path = find_path(node.right, target, path)
            if right_path:  # If a path is found in the right subtree, return it
                return right_path

            # If the target is not found in either subtree, return an empty list
            return []

        # Call the helper function starting from the root node A
        return find_path(A, B, [])

# Test cases for the solve function
def test_solve():
    solution = Solution()

    # Test Case 1: Tree with multiple nodes, path to leaf node
    # Tree structure:
    #        5
    #       / \
    #      3   8
    #     / \   \
    #    1   4   9
    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(4)
    root1.right.right = TreeNode(9)

    # Finding the path to node with value 4
    result1 = solution.solve(root1, 4)
    # Expected path: [5, 3, 4]
    print("Test Case 1:", "Passed" if result1 == [5, 3, 4] else "Failed", "| Output:", result1)

    # Test Case 2: Tree with a single node (root only)
    # Tree structure:
    #        7
    root2 = TreeNode(7)

    # Finding the path to node with value 7 (root node)
    result2 = solution.solve(root2, 7)
    # Expected path: [7]
    print("Test Case 2:", "Passed" if result2 == [7] else "Failed", "| Output:", result2)

    # Test Case 3: Path to a node that doesn't exist
    # Tree structure:
    #        5
    #       / \
    #      3   8
    #     / \   \
    #    1   4   9
    root3 = root1

    # Finding the path to a node with value 10 (which doesn't exist)
    result3 = solution.solve(root3, 10)
    # Expected output: [] (no path found)
    print("Test Case 3:", "Passed" if result3 == [] else "Failed", "| Output:", result3)

    # Test Case 4: Path to root node
    # Finding the path to node with value 5 (root node)
    result4 = solution.solve(root1, 5)
    # Expected path: [5]
    print("Test Case 4:", "Passed" if result4 == [5] else "Failed", "| Output:", result4)

    # Test Case 5: Path to a right child
    # Finding the path to node with value 9
    result5 = solution.solve(root1, 9)
    # Expected path: [5, 8, 9]
    print("Test Case 5:", "Passed" if result5 == [5, 8, 9] else "Failed", "| Output:", result5)

# Run the test cases
test_solve()

# Valid BST from Preorder

# Problem Description
# You are given a preorder traversal A, of a Binary Search Tree.
# Find if it is a valid preorder traversal of a BST.
# Note: Binary Search Tree by definition has distinct keys and duplicates in binary search tree are not allowed.

# Problem Constraints
# 1 <= A[i] <= 106
# 1 <= |A| <= 105

# Input Format
# First and only argument is an integer array A denoting the pre-order traversal.

# Output Format
# Return an integer:
# 0 : Impossible preorder traversal of a BST
# 1 : Possible preorder traversal of a BST

# Example Input
# Input 1:
# A = [7, 7, 10, 10, 9, 5, 2, 8]

# Example Output
# Output 1:
#  0

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        stack = []
        lower_bound = float('-inf')
        
        for value in A:
            # If we find a node that is less than the lower_bound, return 0
            if value < lower_bound:
                return 0
            
            # Pop elements from the stack and update lower_bound
            # when we encounter a node greater than stack's top
            while stack and value > stack[-1]:
                lower_bound = stack.pop()
            
            # Check for duplicates
            if stack and stack[-1] == value:
                return 0
            
            # Push the current value onto the stack
            stack.append(value)
        
        # If all elements satisfy the BST properties, return 1
        return 1

# Example usage:
# solution = Solution()
# print(solution.solve([1, 1, 2, 3, 4]))  # Output should be 0

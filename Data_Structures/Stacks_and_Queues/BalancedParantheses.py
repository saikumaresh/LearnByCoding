# Balanced Parantheses!

# Problem Description
# Given a string A consisting only of '(' and ')'.
# You need to find whether parentheses in A are balanced or not, if it is balanced then return 1 else return 0.

# Problem Constraints
# 1 <= |A| <= 105

# Input Format
# First argument is an string A.

# Output Format
# Return 1 if parantheses in string are balanced else return 0.

# Example Input

# Input 1:
#  A = "(()())"
# Input 2:
#  A = "(()"

# Example Output

# Output 1:
#  1
# Output 2:
#  0

# Example Explanation

# Explanation 1:
#  Given string is balanced so we return 1.
# Explanation 2:
#  Given string is not balanced so we return 0.

class Solution:
    # Function to determine if a string of parentheses is balanced
    # @param A : string
    # @return an integer (1 if balanced, 0 otherwise)
    def solve(self, A):
        # Initialize an empty stack to keep track of open parentheses
        stack = []

        # Iterate through each character in the input string
        for i in A:
            # If the character is an opening parenthesis, push it onto the stack
            if i == '(':
                stack.append(i)
            # If the character is a closing parenthesis and the stack is not empty
            # (i.e., there's an unmatched opening parenthesis), pop the stack
            elif len(stack) > 0 and i == ')':
                stack.pop()
            # If a closing parenthesis is encountered and the stack is empty,
            # it means there's no matching opening parenthesis, so return 0 (unbalanced)
            else:
                return 0

        # After processing the entire string, if the stack is empty, it means all
        # parentheses were matched correctly, so return 1 (balanced)
        if len(stack) == 0:
            return 1
        # If the stack is not empty, there are unmatched opening parentheses, so return 0 (unbalanced)
        else:
            return 0

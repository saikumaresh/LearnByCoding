# Balanced Paranthesis

# Problem Description
# Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.
# Refer to the examples for more clarity.

# Problem Constraints
# 1 <= |A| <= 100

# Input Format
# The first and the only argument of input contains the string A having the parenthesis sequence.

# Output Format
# Return 0 if the parenthesis sequence is not balanced.
# Return 1 if the parenthesis sequence is balanced.

# Example Input

# Input 1:
#  A = {([])}
# Input 2:
#  A = (){
# Input 3:
#  A = ()[] 

# Example Output

# Output 1:
#  1 
# Output 2:
#  0 
# Output 3:
#  1 

class Solution:
    # Function to determine if a string of brackets is balanced
    # @param A : string
    # @return an integer (1 if balanced, 0 otherwise)
    def solve(self, A):
        # Initialize an empty stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the input string
        for i in A:
            # If the character is an opening bracket, push it onto the stack
            if i in ["{", "(", "["]:
                stack.append(i)
            else:
                # If a closing bracket is encountered and the stack is empty,
                # it means there's no matching opening bracket, so return 0 (unbalanced)
                if len(stack) == 0:
                    return 0
                
                # Get the top element of the stack (the last opening bracket)
                top_value = stack[-1]

                # If the top of the stack is not an opening bracket, return 0 (unbalanced)
                if top_value not in ["{", "(", "["]:
                    return 0
                
                # Check if the top of the stack matches the current closing bracket
                if (top_value == "{" and i == "}") or \
                   (top_value == "(" and i == ")") or \
                   (top_value == "[" and i == "]"):
                    # If it matches, pop the opening bracket from the stack
                    stack.pop()
        
        # After processing the entire string, if the stack is empty,
        # it means all brackets were matched correctly, so return 1 (balanced)
        if len(stack) == 0:
            return 1
        # If the stack is not empty, there are unmatched opening brackets, so return 0 (unbalanced)
        else:
            return 0

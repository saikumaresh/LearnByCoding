# 20. Valid Parentheses

# Problem Statement
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if a string of brackets is valid.
        A string is valid if:
        1. Every opening bracket has a corresponding closing bracket.
        2. Brackets are closed in the correct order.
        
        :param s: A string containing '(', ')', '{', '}', '[' or ']'.
        :return: True if the string is valid, False otherwise.
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped element matches the expected opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack


# Testing the function
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = {
        "()"        : True,
        "()[]{}"    : True,
        "(]"        : False,
        "([)]"      : False,
        "{[]}"      : True,
        ""          : True,  # Empty string is valid
        "("         : False, # Unmatched opening bracket
        ")"         : False, # Unmatched closing bracket
        "(((([]))))": True,  # Nested brackets
        "{[()]}{}"  : True,  # Multiple sets of brackets
        "[{]}"      : False, # Incorrect closing order
    }
    
    # Running test cases
    for test_input, expected_output in test_cases.items():
        result = solution.isValid(test_input)
        print(f"Input: '{test_input}' | Expected: {expected_output} | Output: {result}")

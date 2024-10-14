# Min Stack

# Problem Description
# Design a stack that supports push, pop, top, and retrieve the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# NOTE:
# All the operations have to be constant time operations.
# getMin() should return -1 if the stack is empty.
# pop() should return nothing if the stack is empty.
# top() should return -1 if the stack is empty.

# Problem Constraints
# 1 <= Number of Function calls <= 107

# Input Format
# Functions will be called by the checker code automatically.

# Output Format
# Each function should return the values as defined by the problem statement.

# Example Input

# Input 1:
# push(1)
# push(2)
# push(-2)
# getMin()
# pop()
# getMin()
# top()

# Input 2:
# getMin()
# pop()
# top()

# Example Output
# Output 1:
#  -2 1 2
# Output 2:
#  -1 -1

# Example Explanation

# Explanation 1:
# Let the initial stack be : []
# 1) push(1) : [1]
# 2) push(2) : [1, 2]
# 3) push(-2) : [1, 2, -2]
# 4) getMin() : Returns -2 as the minimum element in the stack is -2.
# 5) pop() : Return -2 as -2 is the topmost element in the stack.
# 6) getMin() : Returns 1 as the minimum element in stack is 1.
# 7) top() : Return 2 as 2 is the topmost element in the stack.

# Explanation 2:
# Let the initial stack be : []
# 1) getMin() : Returns -1 as the stack is empty.
# 2) pop() :  Returns nothing as the stack is empty.
# 3) top() : Returns -1 as the stack is empty.
# Expected Output
# Enter your input as per the following guideline:
# There are 1 lines in the input

import sys

class MinStack:
    
    # Initializes the MinStack with two lists:
    # - stack: to store all elements pushed
    # - minstack: to keep track of the minimum elements
    def __init__(self):
        self.stack = []  # Stack to store all elements
        self.minstack = [sys.maxsize]  # Initialize with a very large value to handle the minimum comparisons
    
    # Pushes an element onto the stack
    # @param x, an integer
    # @return nothing
    def push(self, x):
        # If the pushed element is smaller than or equal to the current minimum, push it to the minstack as well
        if x <= self.minstack[-1]:
            self.minstack.append(x)
        # Push the element onto the main stack
        self.stack.append(x)

    # Removes the top element from the stack
    # @return the popped element or None if the stack is empty
    def pop(self):
        if len(self.stack) > 0:
            temp = self.stack[-1]  # Get the top element
            # If the top element is the current minimum, pop it from the minstack as well
            if temp == self.minstack[-1]:
                self.minstack.pop()
            # Pop the element from the main stack
            self.stack.pop()
            return temp
        return None  # If the stack is empty, return None

    # Retrieves the top element without removing it
    # @return the top element or -1 if the stack is empty
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]  # Return the top element
        return -1  # If the stack is empty, return -1

    # Retrieves the minimum element in the stack
    # @return the minimum element or -1 if the stack is empty
    def getMin(self):
        if len(self.stack) > 0:
            return self.minstack[-1]  # Return the minimum element from the minstack
        return -1  # If the stack is empty, return -1

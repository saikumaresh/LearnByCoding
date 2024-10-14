# Flatten Nested List Iterator
# Solved
# feature icon
# Using hints except Complete Solution is Penalty free now
# Use Hint
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
# Constraints:
# The sum of integers in all cases does not exceed 1e5.
# The values of the integers in the nested list are in the range [-1e6, 1e6].

# # This is the interface that allows for creating nested lists.
# # You should not implement it, or speculate about its implementation
# class NestedInteger:
#     def __init__(self, x):
        
#     # Return true if this NestedInteger holds a single integer, rather than a nested list.
#     def isInteger(self):
        
#     # Return the single integer that this NestedInteger holds, if it holds a single integer
#     # The result is 1e9 if this NestedInteger holds a nested list
#     def getInteger(self):
        
#     # Return the nested list that this NestedInteger holds, if it holds a nested list
#     # The result is an empty list if this NestedInteger holds a single integer
#     def getList(self):
        
class NestedIterator:
    def __init__(self, nestedList):
        """
        Initialize the NestedIterator with a list of NestedInteger objects.
        The stack is initialized in reverse order to allow us to process the nested
        list in a LIFO (Last-In, First-Out) manner, mimicking the recursive flattening of the list.
        
        Args:
        nestedList (List[NestedInteger]): A list containing integers or nested lists.
        """
        # Stack will hold the elements of the nested list, reversed to process correctly
        self.stack = nestedList[::-1]

    def next(self):
        """
        Return the next integer in the flattened list.
        Assumes that hasNext has already been called and the top of the stack is an integer.

        Returns:
        int: The next integer in the flattened list.
        """
        # Pop the top integer from the stack and return it
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        Return True if there are more integers to be returned from the nested list, otherwise False.
        This method also flattens the nested list on the fly by processing nested lists
        as it goes and pushing their contents onto the stack.

        Returns:
        bool: True if there is a next integer, False otherwise.
        """
        # Loop while there are elements in the stack
        while self.stack:
            # Get the top element from the stack (without popping)
            top = self.stack[-1]
            
            # If the top element is an integer, return True (next() can now retrieve it)
            if top.isInteger():
                return True
            
            # If it's a list, pop it and flatten it by pushing its contents to the stack
            self.stack.pop()  # Remove the list from the stack
            # Get the list inside this NestedInteger, reverse it, and push to the stack
            self.stack.extend(top.getList()[::-1])
        
        # If we exit the loop, there are no more integers in the stack
        return False

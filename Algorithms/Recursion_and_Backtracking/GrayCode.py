# Gray Code

# Problem Description
# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.

# Problem Constraints
# 1 <= A <= 16

# Input Format
# The first argument is an integer A.

# Output Format
# Return an array of integers representing the gray code sequence.

# Example Input
# Input 1:
# A = 2
# Input 1:
# A = 1

# Example Output
# output 1:
# [0, 1, 3, 2]
# output 2:
# [0, 1]

# Example Explanation

# Explanation 1:
# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].

# Explanation 1:
# for A = 1 the gray code sequence is:
#     00 - 0
#     01 - 1
# So, return [0, 1].

class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        # Base case: If A is 1, return the gray code sequence for 1 bit
        if A == 1:
            return [0, 1]
        
        # Recursive case: Get the gray code sequence for A-1 bits
        prev_gray = self.grayCode(A - 1)
        
        # Mirror the gray code sequence and append the new numbers for A bits
        mirrored_gray = []
        add_bit = 1 << (A - 1)  # Equivalent to 2^(A-1)
        
        # Generate the new list by reversing the previous gray code and adding the bit
        for num in reversed(prev_gray):
            mirrored_gray.append(num + add_bit)
        
        # Return the original gray code for A-1 bits followed by the mirrored and modified gray code
        return prev_gray + mirrored_gray
sol = Solution()

# Test case 1
A = 2
print("Gray Code for A =", A, ":", sol.grayCode(A))
# Output: [0, 1, 3, 2]

# Test case 2
A = 1
print("Gray Code for A =", A, ":", sol.grayCode(A))
# Output: [0, 1]

# Test case 3
A = 3
print("Gray Code for A =", A, ":", sol.grayCode(A))
# Output: [0, 1, 3, 2, 6, 7, 5, 4]


# Recursive Breakdown for A = 3

# We will use the recursive function grayCode(A) and break it down step by step for A = 3:

# Step 1: Base Case for A = 1

# Input: A = 1
# Action:
# In the function, if A == 1, return [0, 1] since this is the base case.
# Output: The Gray Code for A = 1 is [0, 1].
# A = 1: Gray Code Sequence = [0, 1]

# Step 2: Recursive Call for A = 2

# Input: A = 2
# Action:
# Call grayCode(A - 1) which is grayCode(1) to get the Gray Code for A = 1.
# Previous Gray Code for A = 1: [0, 1]
# Reverse this Gray Code: [1, 0].
# Add 1 << (A - 1) to each element of the reversed list, i.e., add 1 << 1 = 2:
# [1 + 2, 0 + 2] = [3, 2].
# Concatenate the original list [0, 1] with the modified list [3, 2] to get [0, 1, 3, 2].

# A = 2: 
# Previous Gray Code for A = 1: [0, 1]
# Reversed Gray Code: [1, 0]
# Modified Gray Code (add 2): [3, 2]
# Final Gray Code Sequence: [0, 1, 3, 2]

# Step 3: Recursive Call for A = 3

# Input: A = 3
# Action:
# Call grayCode(A - 1) which is grayCode(2) to get the Gray Code for A = 2.
# Previous Gray Code for A = 2: [0, 1, 3, 2]
# Reverse this Gray Code: [2, 3, 1, 0].
# Add 1 << (A - 1) to each element of the reversed list, i.e., add 1 << 2 = 4:
# [2 + 4, 3 + 4, 1 + 4, 0 + 4] = [6, 7, 5, 4].
# Concatenate the original list [0, 1, 3, 2] with the modified list [6, 7, 5, 4] to get the final result: [0, 1, 3, 2, 6, 7, 5, 4].

# A = 3: 
# Previous Gray Code for A = 2: [0, 1, 3, 2]
# Reversed Gray Code: [2, 3, 1, 0]
# Modified Gray Code (add 4): [6, 7, 5, 4]
# Final Gray Code Sequence: [0, 1, 3, 2, 6, 7, 5, 4]

# Iterations Summary:

# Here is the iteration breakdown for each A:
# For A = 1:
# Gray Code Sequence: [0, 1]
# For A = 2:
# Start with the sequence for A = 1: [0, 1].
# Reverse it: [1, 0].
# Add 2 to each number in the reversed list: [3, 2].
# Concatenate: [0, 1] + [3, 2] = [0, 1, 3, 2].
# For A = 3:
# Start with the sequence for A = 2: [0, 1, 3, 2].
# Reverse it: [2, 3, 1, 0].
# Add 4 to each number in the reversed list: [6, 7, 5, 4].
# Concatenate: [0, 1, 3, 2] + [6, 7, 5, 4] = [0, 1, 3, 2, 6, 7, 5, 4].
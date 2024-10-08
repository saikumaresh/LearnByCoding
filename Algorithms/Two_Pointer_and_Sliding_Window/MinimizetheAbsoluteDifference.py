# Minimize the absolute difference

# https://www.interviewbit.com/problems/minimize-the-absolute-difference/

# Medium

# Problem Statement
# Given three sorted arrays A, B  and Cof not necessarily same sizes.
# Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively.
# i.e. minimize | max(a,b,c) - min(a,b,c) |.

# Example :

# Input:
# A : [ 1, 4, 5, 8, 10 ]
# B : [ 6, 9, 15 ]
# C : [ 2, 3, 6, 6 ]

# Output:
# 1

# Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i, j, k = 0, 0, 0  # Initialize three pointers
        min_diff = float('inf')  # Set initial minimum difference to infinity

        # Traverse until one of the arrays is exhausted
        while i < len(A) and j < len(B) and k < len(C):
            # Get the current values from A, B, C
            a, b, c = A[i], B[j], C[k]
            
            # Find the current maximum and minimum of the triplet
            current_max = max(a, b, c)
            current_min = min(a, b, c)
            
            # Update the minimum difference
            min_diff = min(min_diff, current_max - current_min)
            
            # Move the pointer that points to the minimum value
            if current_min == a:
                i += 1
            elif current_min == b:
                j += 1
            else:
                k += 1
        
        return min_diff

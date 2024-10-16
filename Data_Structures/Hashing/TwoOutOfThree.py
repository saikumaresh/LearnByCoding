# Two out of Three

# https://www.interviewbit.com/problems/two-out-of-three/

# Problem Description
# Given are Three arrays A, B and C.
# Return the sorted list of numbers that are present in atleast 2 out of the 3 arrays.

# Problem Constraints
# 1 <= |A|, |B|, |C| <= 100000
# 1 <= A[i], B[i], C[i] <= 100000
# A, B, C may or may not have pairwise distinct elements.

# Input Format
# First argument is the array A.
# First argument is the array B.
# First argument is the array C.

# Output Format
# Return a sorted array of numbers.

# Example Input

# Input 1:
# A = [1, 1, 2]
# B = [2, 3]
# C = [3]

# Input 2:
# A = [1, 2]
# B = [1, 3]
# C = [2, 3]


# Example Output

# Output 1:
# [2, 3]
# Output 2:
# [1, 2, 3]


# Example Explanation

# Explanation 1:
# 1 is only present in A. 2 is present in A and B. 3 is present in B and C.
# Explanation 2:
# All numbers are present in atleast 2 out of 3 lists.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        # Combine unique elements from A, B, and C
        temp = list(set(A)) + list(set(B)) + list(set(C))
        
        # Create a hashmap to count occurrences of each number
        hashmap = {}
        result = []
        
        # Count occurrences of each number across all three arrays
        for i in temp:
            if i in hashmap:
                hashmap[i] += 1  # Increment count if number is already in hashmap
            else:
                hashmap[i] = 1    # Initialize count to 1 if it's the first occurrence
                
        # Collect numbers that appear in at least two of the arrays
        for i in hashmap:
            if hashmap[i] >= 2:   # Check if count is 2 or more
                result.append(i)   # Add to the result list
                
        # Sort the result list before returning
        return sorted(result)

# Example usage
A = [1, 1, 2]
B = [2, 3]
C = [3]
solution = Solution()
print(solution.solve(A, B, C))  # Expected Output: [2, 3]

A2 = [1, 2]
B2 = [1, 3]
C2 = [2, 3]
print(solution.solve(A2, B2, C2))  # Expected Output: [1, 2, 3]
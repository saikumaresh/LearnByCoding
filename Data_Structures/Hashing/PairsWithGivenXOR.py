# Pairs With Given Xor

# Problem Description
# Given an integer array A containing N distinct integers.
# Find the number of unique pairs of integers in the array whose XOR is equal to B.
# NOTE:
# Pair (a, b) and (b, a) is considered to be the same and should be counted once.

# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i], B <= 107

# Input Format

# The first argument is an integer array A.
# The second argument is an integer B.

# Output Format
# Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.

# Example Input

# Input 1:
#  A = [5, 4, 10, 15, 7, 6]
#  B = 5
# Input 2:
#  A = [3, 6, 8, 10, 15, 50]
#  B = 5

# Example Output

# Output 1:
#  1
# Output 2:
#  2


# Example Explanation

# Explanation 1:
#  (10 ^ 15) = 5
# Explanation 2:
#  (3 ^ 6) = 5 and (10 ^ 15) = 5 

class Solution:
    # @param A : list of integers
    # @param B : integer (target XOR value)
    # @return an integer (count of unique pairs)
    def solve(self, A, B):
        unique_pairs = 0  # Initialize counter for unique pairs
        xor_map = {}  # Dictionary to store XOR results and their indices

        # First loop: Populate the xor_map with the XOR of each element in A with B
        for i in range(len(A)):
            xor_map[A[i] ^ B] = i  # Store the XOR result as the key and the index as the value
        
        # Second loop: Check if the current element in A exists in the xor_map
        for i in range(len(A)):
            if A[i] in xor_map and xor_map[A[i]] != i:
                # If A[i] exists in xor_map and is from a different index, count the pair
                unique_pairs += 1
        
        # Since each pair is counted twice (once for each element in the pair), divide by 2
        return unique_pairs // 2
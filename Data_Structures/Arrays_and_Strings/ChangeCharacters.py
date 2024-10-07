# Change character

# Problem Description

# You are given a string A of size N consisting of lowercase alphabets.
# You can change at most B characters in the given string to any other lowercase alphabet such that the number of distinct characters in the string is minimized.
# Find the minimum number of distinct characters in the resulting string.

# Problem Constraints
# 1 <= N <= 100000
# 0 <= B <= N

# Input Format
# The first argument is a string A.
# The second argument is an integer B.

# Output Format
# Return an integer denoting the minimum number of distinct characters in the string.

# Example Input
# A = "abcabbccd"
# B = 3

# Example Output
# 2

# Example Explanation

# We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
# So the minimum number of distinct character will be 2.

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B >= len(A):
            return 1
        array = [0] * 26
        for i in range(len(A)):
            temp = ord(A[i]) - ord('a')
            array[temp] += 1
        total = 0
        for i in array:
            if i != 0:
                total += 1
        array.sort()
        changes = 0
        for i in range(26):
            if array[i] != 0 and (B - array[i]) >= 0:
                B -= array[i]
                changes += 1
        return total - changes
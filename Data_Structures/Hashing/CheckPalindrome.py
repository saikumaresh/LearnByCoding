# Check Palindrome - II

# Problem Description
# Given a string A consisting of lowercase characters.
# Check if characters of the given string can be rearranged to form a palindrome.
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

# Problem Constraints
# 1 <= |A| <= 105
# A consists only of lower-case characters.

# Input Format
# First argument is an string A.

# Output Format
# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.

# Example Input

# Input 1:
#  A = "abcde"
# Input 2:
#  A = "abbaee"

# Example Output
# Output 1:
#  0
# Output 2:
#  1

# Example Explanation

# Explanation 1:
#  No possible rearrangement to make the string palindrome.
# Explanation 2:
#  Given string "abbaee" can be rearranged to "aebbea" to form a palindrome.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_hashmap = {}
        for i in A:
            if i in count_hashmap:
                count_hashmap[i] += 1
            else:
                count_hashmap[i] = 1
        counts = list(count_hashmap.values())
        even = odd = 0
        for i in counts:
            if i % 2 == 0:
                even += 1
            else: 
                odd += 1
        if odd <= 1:
            return 1
        return 0
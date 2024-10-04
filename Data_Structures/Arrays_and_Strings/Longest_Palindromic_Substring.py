# Q7. Longest Palindromic Substring

# Problem Description

# Given a string A of size N, find and return the longest palindromic substring in A.
# Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
# Incase of conflict, return the substring which occurs first ( with the least starting index).

# Problem Constraints
# 1 <= N <= 6000

# Input Format
# First and only argument is a string A.

# Output Format
# Return a string denoting the longest palindromic substring of string A.

# Example Input

# Input 1:
# A = "aaaabaaa"
# Input 2:
# A = "abba

# Example Output

# Output 1:
# "aaabaaa"
# Output 2:
# "abba"


# Example Explanation

# Explanation 1:
# We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".
# Explanation 2:
# We can see that longest palindromic substring is of length 4 and the string is "abba".

# Code Solution
class Solution:
    def longestPalindrome(self, A):
        if len(A) == 0 or A == A[::-1]:
            return A
        def expand(A,p1,p2):
            while p1 >= 0 and p2 <= len(A)-1 and A[p1] == A[p2]:
                p1 -= 1
                p2 += 1
            return [p2-p1-1,p1+1,p2-1]
        length = 0
        result = []
        for i in range(len(A)):
            temp = expand(A, i, i)
            if temp[0] > length:
                result = temp[1:]
                length = temp[0] # odd cases
        for i in range(len(A)-1):
            temp = expand(A, i, i+1)
            if temp[0] > length:
                result = temp[1:]
                length = temp[0] #even cases
        if len(result) == 0:
            return ""
        return A[result[0]:result[1]+1]
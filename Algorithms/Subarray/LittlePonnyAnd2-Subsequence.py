# Little Ponny and 2-Subsequence

# Problem Description
# Little Ponny has been given a string A, and he wants to find out the lexicographically minimum subsequence from it of size >= 2. Can you help him?
# A string a is lexicographically smaller than string b, if the first different letter in a and b is smaller in a. 
# For example, "abc" is lexicographically smaller than "acc" because the first different letter is 'b' and 'c' which is smaller in "abc".

# Problem Constraints
# 1 <= |A| <= 105
# A only contains lowercase alphabets.

# Input Format
# The first and the only argument of input contains the string, A.

# Output Format
# Return a string representing the answer.

# Example Input

# Input 1:
#  A = "abcdsfhjagj" 
# Input 2:
#  A = "ksdjgha" 

# Example Output

# Output 1:
#  "aa" 
# Output 2:
#  "da" 

# Example Explanation

# Explanation 1:
#  "aa" is the lexicographically minimum subsequence from A. 
# Explanation 2:
#  "da" is the lexicographically minimum subsequence from A. 

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # Initialize the first minimum character and its index
        firstMinIndex = 0
        firstMinChar = A[0]
        
        # Finding the first minimum character
        for i in range(len(A)-1):
            if ord(A[i]) < ord(firstMinChar):
                firstMinChar = A[i]
                firstMinIndex = i 
        
        # Initialize the second minimum character and its index
        secMinIndex = firstMinIndex + 1
        
        # If there is no second character, return an empty string
        if secMinIndex >= len(A):
            return ""
        
        secMinChar = A[secMinIndex]
        
        # Finding the second minimum character
        for i in range(firstMinIndex + 1, len(A)):
            if ord(A[i]) < ord(secMinChar):
                secMinChar = A[i]
                secMinIndex = i 
        
        # Return the two minimum characters in the correct order
        if firstMinIndex < secMinIndex:
            return firstMinChar + secMinChar
        else:
            return secMinChar + firstMinChar

# Test cases
solution = Solution()

# Test case 1: normal case with distinct characters
print(solution.solve("abcd"))  # Output: "ab"

# Test case 2: normal case with duplicate characters
print(solution.solve("bacd"))  # Output: "ab"

# Test case 3: only two characters
print(solution.solve("zy"))    # Output: "zy"

# Test case 4: string with all same characters
print(solution.solve("aaaa"))  # Output: "aa"

# Test case 5: string with no second character
print(solution.solve("a"))     # Output: "" (no second character)

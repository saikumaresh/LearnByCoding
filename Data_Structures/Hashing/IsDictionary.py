# Is Dictionary?

# Problem Description
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order. 
# The order of the alphabet is some permutation of lowercase letters.
# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string B of size 26, 
# return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.


# Problem Constraints
# 1 <= N, length of each word <= 105
# Sum of the length of all words <= 2 * 106

# Input Format
# The first argument is a string array A of size N.
# The second argument is a string B of size 26, denoting the order.

# Output Format
# Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

# Example Input

# Input 1:
#  A = ["hello", "scaler", "interviewbit"]
#  B = "adhbcfegskjlponmirqtxwuvzy"

# Input 2:
#  A = ["fine", "none", "bush"]
#  B = "qwertyuiopasdfghjklzxcvbnm"


# Example Output

# Output 1:
#  1
# Output 2:
#  0


# Example Explanation

# Explanation 1:

#  The order shown in string B is: h < s < i (adhbcfegskjlponmirqtxwuvzy) for the given words. 
#  So, Return 1.

# Explanation 2:
#  "none" should be present after "bush", Since b < n (qwertyuiopasdfghjklzxcvbnm). 
#  So, Return 0.

class Solution:
    # @param A : list of strings (list of words to check order)
    # @param B : string (custom alphabet order)
    # @return an integer (1 if words in A are sorted according to B, otherwise 0)
    def solve(self, A, B):
        # Create a dictionary 'order' to store the position of each character in B
        # B defines a custom order of characters
        order = {}
        B = list(B.strip())  # Remove any leading/trailing whitespace from B and convert to list of characters
        
        # Map each character in B to its index (i.e., custom order)
        for i in range(len(B)):
            order[B[i]] = i  # Store character positions (e.g., order['a'] = 0 if 'a' is first in B)
        
        # Loop through adjacent words in A to check if they follow the order in B
        for i in range(1, len(A)):
            # Compare the first character of the two adjacent words
            order1 = order[A[i-1][0]]  # Get the order of the first character in the (i-1)-th word
            order2 = order[A[i][0]]    # Get the order of the first character in the i-th word
            
            if order2 > order1:
                # If the first character of the current word comes after the previous word's character, continue
                continue
            elif order2 < order1:
                # If the current word's first character comes before the previous word's first character, return 0
                return 0
            elif order1 == order2:
                # If the first characters are equal, check subsequent characters
                char = 1  # Start comparing from the second character of the words
                flag = True  # To control the inner loop
                while flag and order1 == order2:
                    # Check if we've reached the end of one of the words
                    if char == min(len(A[i-1]), len(A[i])):
                        # If the previous word is longer than the current word, return 0 (invalid order)
                        if len(A[i-1]) <= len(A[i]):
                            flag = False  # Words are in correct order if previous word is shorter or equal in length
                        else:
                            return 0  # Invalid order if previous word is longer
                    else:
                        # Compare the next characters in both words
                        order1 = order[A[i-1][char]]  # Get the order of the next character in the (i-1)-th word
                        order2 = order[A[i][char]]    # Get the order of the next character in the i-th word
                        
                        if order2 < order1:
                            return 0  # If current word's character is smaller, return 0
                        else:
                            char += 1  # Move to the next character
        
        # If all words follow the order in B, return 1
        return 1
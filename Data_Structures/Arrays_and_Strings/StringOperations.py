# String operations

# Problem Description
# Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:

# Concatenate the string with itself.
# Delete all the uppercase letters.
# Replace each vowel with '#'.
# You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.

# NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.


# Problem Constraints
# 1<=N<=100000

# Input Format
# First argument is a string A of size N.

# Output Format
# Return the resultant string.

# Example Input
# Input 1:
# A="aeiOUz"
# Input 2:
# A="AbcaZeoB"

# Example Output
# Output 1:
# "###z###z"
# Output 2:
# "bc###bc###"


# Example Explanation

# Explanation 1:
# First concatenate the string with itself so string A becomes "aeiOUzaeiOUz".
# Delete all the uppercase letters so string A becomes "aeizaeiz".
# Now replace vowel with '#', A becomes "###z###z".
# Explanation 2:
# First concatenate the string with itself so string A becomes "AbcaZeoBAbcaZeoB".
# Delete all the uppercase letters so string A becomes "bcaeobcaeo".
# Now replace vowel with '#', A becomes "bc###bc###".

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = list(A)
        temp = A
        A.extend(temp)
        vowels = ['a','e','i','o','u']
        result = []
        for i in range(len(A)):
            if ord(str(A[i])) >= ord('A') and ord(str(A[i])) <= ord('Z'):
                continue
            else:
                result.append(A[i])
        for i in range(len(result)):
            if result[i] in vowels:
                result[i] = '#'
        return "".join(result)
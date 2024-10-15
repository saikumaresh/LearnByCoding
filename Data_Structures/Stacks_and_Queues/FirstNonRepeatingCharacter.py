# First non-repeating character in a stream of characters

# Problem Description
# Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
# B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. 
# If no non-repeating character is found then append '#' at the end of B.

# Problem Constraints
# 1 <= length of the string <= 100000

# Input Format
# The only argument given is string A.

# Output Format
# Return a string B after processing the stream of lowercase alphabets A.

# Example Input
# Input 1:
#  A = "abadbc"
# Input 2:
#  A = "abcabc"

# Example Output
# Output 1:
#  "aabbdd"
# Output 2:
#  "aaabc#"


# Example Explanation

# Explanation 1:
#     "a"      -   first non repeating character 'a'
#     "ab"     -   first non repeating character 'a'
#     "aba"    -   first non repeating character 'b'
#     "abad"   -   first non repeating character 'b'
#     "abadb"  -   first non repeating character 'd'
#     "abadbc" -   first non repeating character 'd'

# Explanation 2:
#     "a"      -   first non repeating character 'a'
#     "ab"     -   first non repeating character 'a'
#     "abc"    -   first non repeating character 'a'
#     "abca"   -   first non repeating character 'b'
#     "abcab"  -   first non repeating character 'c'
#     "abcabc" -   no non repeating character so '#'

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        # List to simulate the queue
        queue = []
        # Array to store the frequency of each character
        char_count = [0] * 26
        
        # Resultant string
        result = []
        
        for char in A:
            # Convert character to index
            index = ord(char) - ord('a')
            # Increment the count of the current character
            char_count[index] += 1
            # Add the character to the queue
            queue.append(char)
            
            # Remove characters from the queue that have frequency > 1
            while queue and char_count[ord(queue[0]) - ord('a')] > 1:
                queue.pop(0)  # Remove from the front of the list (simulating a queue)
            
            # Append the first non-repeating character or '#' if no such character exists
            if queue:
                result.append(queue[0])
            else:
                result.append('#')
        
        # Join the result list into a string
        return ''.join(result)

# Prakash in IZOCXUL

# https://unstop.com/code/challenge-assessment/250758?moduleId=428

# Problem Statement
# Prakash had a dream about a planet named IZOCXUL, where only lowercase letters exist. 
# He gave you a string S from that planet, and your task is to find how many substrings of length 2 to K consist of unique characters only.

# Input Format
# The first line contains a string S, representing the string from this planet.
# The Second line consists of an integer K.

# Output Format
# Print K-1 lines where each line denotes the count of substring of size, from 2 to K.

# Constraints
# |S| <= 10^3
# 2<=K<= |S|,
# NOTE : |S| denotes the length of the string.

# Sample Testcase 0

# Testcase Input
# aabce
# 4

# Testcase Output
# 3
# 2
# 1

# Explanation
# Given K = 4 and string - 'aabce
# Substrgin of length 2 with unique characters are (ab), (bc) and (ce), Count - 3
# Substrgin of length 3 with unique characters are (abc) and (bce), Count - 2
# Substrgin of length 4 with unique characters are (abce), Count - 1


# Sample Testcase 1

# Testcase Input
# abc
# 3

# Testcase Output
# 2
# 1

# Explanation
# Given K = 3 and string - 'abc'
# Substrgin of length 2 with unique characters are (ab) and (bc), Count - 2
# Substrgin of length 3 with unique characters are (abc), Count - 1

def count_unique_substrings(S, K):
    # For each length from 2 to K
    for length in range(2, K+1):
        count = 0
        # Slide through the string to extract all substrings of current length
        for i in range(len(S) - length + 1):
            substring = S[i:i+length]
            # Check if all characters are unique
            if len(set(substring)) == length:
                count += 1
        # Print the result for current length
        print(count)

# Input
S = input().strip()  # The string from the planet
K = int(input())  # The maximum length to consider for substrings

# Process and output the counts
count_unique_substrings(S, K)

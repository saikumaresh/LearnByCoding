# The Largest Pack

# https://unstop.com/code/challenge-assessment/250913?moduleId=422

# Problem Statement
# A toy manufacturing factory produced n marbles in a day.
# According to the factory rules, the number of marbles in a pack must be a power of 2.
# Find the size of the largest pack of marbles that can be produced using N or fewer marbles.

# Input Format
# The input consists of a single integer N – the number of marbles produced in a day.

# Output Format
# Print a single integer – the number of marbles in the largest pack that can be produced.

# Constraints
# 1 <= N <= 231 - 1

# Sample Testcase 0
# Testcase Input
# 5
# Testcase Output
# 4
# Explanation
# The largest number less than 5 that is a power of 2 is 4.

# Sample Testcase 1
# Testcase Input
# 16
# Testcase Output
# 16
# Explanation
# We can produce a pack using all 16 marbles as 2^4 = 16.

class Solution:
    def largestPowerOf2(self, N):
        # Find the largest power of 2 less than or equal to N
        return 1 << (N.bit_length() - 1)

# Example Usage:
sol = Solution()

# Testcase 0
print(sol.largestPowerOf2(5))  # Output: 4

# Testcase 1
print(sol.largestPowerOf2(16))  # Output: 16

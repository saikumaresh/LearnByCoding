# Next Similar Number

# Problem Description
# Given a number A in a form of string.
# You have to find the smallest number that has same set of digits as A and is greater than A.
# If A is the greatest possible number with its set of digits, then return -1.

# Problem Constraints
#  1 <= A <= 10100000
#  A doesn't contain leading zeroes.

# Input Format
# First and only argument is an numeric string denoting the number A.

# Output Format
# Return a string denoting the smallest number greater than A with same set of digits , if A is the largest possible then return -1.

# Example Input
# Input 1:
#  A = "218765"
# Input 2:
#  A = "4321"

# Example Output
# Output 1:
#  "251678"
# Output 2:
#  "-1"


# Example Explanation
# Explanation 1:
#  The smallest number greater then 218765 with same set of digits is 251678.
# Explanation 2:
#  The given number is the largest possible number with given set of digits so we will return -1.

class Solution:
    # @param A : string
    # @return a string
    def solve(self, A):
        n = len(A)
        A = list(A)

        # Step 1: Find the first decreasing digit from the right
        i = n - 2
        while i >= 0 and A[i] >= A[i + 1]:
            i -= 1

        # If no such index is found, it means A is the largest permutation
        if i == -1:
            return "-1"

        # Step 2: Find the smallest digit greater than A[i] to the right
        j = n - 1
        while A[j] <= A[i]:
            j -= 1

        # Step 3: Swap A[i] and A[j]
        A[i], A[j] = A[j], A[i]

        # Step 4: Sort the digits after index i
        A = A[:i + 1] + sorted(A[i + 1:])

        return ''.join(A)

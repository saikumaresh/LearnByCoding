# Longest Common Subsequence

# Problem Description
# Given two strings A and B. Find the longest common sequence ( A sequence which does not need to be contiguous), which is common in both the strings.
# You need to return the length of such longest common subsequence.

# Problem Constraints
# 1 <= |A|, |B| <= 1005

# Input Format
# First argument is an string A.
# Second argument is an string B.

# Output Format
# Return the length of such longest common subsequence between string A and string B.

# Example Input
# Input 1:
#  A = "abbcdgf"
#  B = "bbadcgf"

# Example Output
# Output 1:
#  5

# Example Explanation
# Explanation 1:
#  The longest common subsequence is "bbcgf", which has a length of 5

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def longest_subseq(self, a, b):
        """
        Finds the length of the longest common subsequence (LCS) between two strings.
        
        :param a: First string
        :param b: Second string
        :return: Length of the LCS
        """
        # Initialize a 2D DP table with dimensions (len(a)+1) x (len(b)+1)
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

        # Fill the DP table
        for i in range(1, len(a) + 1):  # Iterate over characters in `a`
            for j in range(1, len(b) + 1):  # Iterate over characters in `b`
                if a[i - 1] == b[j - 1]:
                    # If characters match, take diagonal value + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise, take the maximum of top or left cell
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The bottom-right corner of the table contains the LCS length
        return dp[-1][-1]

    def solve(self, A, B):
        """
        Wrapper function to find the LCS length between two strings.
        """
        return self.longest_subseq(A, B)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("abcde", "ace"),  # Common subsequence: "ace" → Length = 3
        ("abc", "def"),    # No common subsequence → Length = 0
        ("aaaa", "aa"),    # Common subsequence: "aa" → Length = 2
        ("abcdef", "acf"), # Common subsequence: "acf" → Length = 3
        ("xyz", "xyz"),    # Common subsequence: "xyz" → Length = 3
        ("", ""),          # Both strings are empty → Length = 0
        ("abcd", ""),      # One string is empty → Length = 0
        ("abc", "cba"),    # Common subsequence: "a" or "b" or "c" → Length = 1
    ]

    for a, b in test_cases:
        result = solution.solve(a, b)
        print(f"LCS length between '{a}' and '{b}': {result}")

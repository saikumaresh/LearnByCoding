# Flip

# Problem Description
# You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. 
# In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. 
# By flipping, we mean changing character 0 to 1 and vice-versa.
# Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
# If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. 
# If there are multiple solutions, return the lexicographically smallest pair of L and R.
# NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

# Problem Constraints
# 1 <= size of string <= 100000

# Input Format
# First and only argument is a string A.

# Output Format
# Return an array of integers denoting the answer.

# Example Input

# Input 1:
# A = "010"
# Input 2:
# A = "111"

# Example Output

# Output 1:
# [1, 1]
# Output 2:
# []


# Example Explanation

# Explanation 1:
# A = "010"
# Pair of [L, R] | Final string
# _______________|_____________
# [1 1]          | "110"
# [1 2]          | "100"
# [1 3]          | "101"
# [2 2]          | "000"
# [2 3]          | "001"
# We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].

# Explanation 2:
# No operation can give us more than three 1s in final string. So, we return empty array [].

class Solution:
    # @param A : string
    # @return a list of integers representing the left and right indices of the subarray to flip
    def flip(self, A):
        # Initialize variables
        l = r = 0  # Start and end indices of the current subarray
        currsum = maxsum = 0  # Current and maximum sums to track the best flip range
        ans = [0, 0]  # Stores the result indices (1-based)

        for i in range(len(A)):
            if A[i] == '0':
                # Treat '0' as +1 for flipping
                currsum += 1
            else:
                # Treat '1' as -1 for flipping
                currsum -= 1

            # Update maxsum and best range if we found a new maximum sum
            if currsum > maxsum:
                maxsum = currsum
                ans[0] = l + 1  # Convert 0-based to 1-based index
                ans[1] = r + 1  # Convert 0-based to 1-based index

            # If current sum drops below 0, reset the window
            if currsum < 0:
                currsum = 0
                l = r = i + 1  # Move left and right pointers to the next index
            else:
                r += 1  # Expand the right end of the current subarray

        # If maxsum is still 0, no beneficial flip was found, return empty list
        if maxsum == 0:
            return []

        # Return the indices of the best flip range
        return ans

# Test cases
solution = Solution()

# Test case 1: Basic case with alternating '0's and '1's
print(solution.flip("010"))  # Expected output: [1, 1] (flipping the first '0' maximizes 1's)

# Test case 2: All '1's - no beneficial flip
print(solution.flip("111"))  # Expected output: [] (flipping can't increase number of '1's)

# Test case 3: All '0's - best flip is the whole array
print(solution.flip("000"))  # Expected output: [1, 3] (flipping all results in all '1's)

# Test case 4: Mix of '0's and '1's
print(solution.flip("1101010001"))  # Expected output: [4, 8] (best flip range maximizes 1's)

# Test case 5: Edge case with single element
print(solution.flip("1"))  # Expected output: [] (no benefit from flipping)
print(solution.flip("0"))  # Expected output: [1, 1] (flipping the only '0' results in a single '1')

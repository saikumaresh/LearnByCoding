# Majority Vote

# https://www.geeksforgeeks.org/problems/majority-vote/1

# Difficulty: Medium
# Accuracy: 48.1%

# You are given an array of integer nums[] where each number represents a vote to a candidate. 
# Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return -1. 

# Note: The answer should be returned in an increasing format.

# Examples:

# Input: nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
# Output: [5, 6]
# Explanation: 5 and 6 occur more n/3 times.

# Input: nums = [1, 2, 3, 4, 5]
# Output: [-1]
# Explanation: no candidate occur more than n/3 times.

# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)

# Constraint:
# 1 <= nums.size() <= 106
# 0 <= nums[i] <= 109

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        n = len(nums)
        one = None
        two = None
        count_1 = 0
        count_2 = 0
        output = []

        # Step 1: Find potential candidates using Boyer-Moore Voting algorithm
        for i in range(n):
            if one == nums[i]:
                count_1 += 1
            elif two == nums[i]:
                count_2 += 1
            elif count_1 == 0:
                one = nums[i]
                count_1 = 1
            elif count_2 == 0:
                two = nums[i]
                count_2 = 1
            else:
                count_1 -= 1
                count_2 -= 1

        # Step 2: Verify the candidates
        count_1 = 0
        count_2 = 0
        for num in nums:
            if num == one:
                count_1 += 1
            elif num == two:
                count_2 += 1

        if count_1 > n // 3:
            output.append(one)
        if count_2 > n // 3:
            output.append(two)

        if len(output) == 0:
            output = [-1]

        return sorted(output)
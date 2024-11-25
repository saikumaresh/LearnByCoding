# 1. Two Sum

# Problem Statement 
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the list that add up to the target and return their indices.

        Parameters:
        nums (List[int]): List of integers.
        target (int): Target sum.

        Returns:
        List[int]: Indices of the two numbers in the list that add up to the target.
        """
        # Dictionary to store numbers and their indices
        hashmap = {}

        # Traverse the list
        for i, num in enumerate(nums):
            # Calculate the complement that would complete the pair
            complement = target - num
            
            # Check if the complement is already in the hashmap
            if complement in hashmap:
                # If found, return the indices of the current number and its complement
                return [hashmap[complement], i]
            
            # Otherwise, store the current number and its index in the hashmap
            hashmap[num] = i

        # If no solution is found (although the problem guarantees a solution), return an empty list
        return []

# Test cases
def test_twoSum():
    solution = Solution()

    # Test Case 1
    nums1, target1 = [2, 7, 11, 15], 9
    print("Test Case 1:", solution.twoSum(nums1, target1))  # Expected Output: [0, 1]

    # Test Case 2
    nums2, target2 = [3, 2, 4], 6
    print("Test Case 2:", solution.twoSum(nums2, target2))  # Expected Output: [1, 2]

    # Test Case 3
    nums3, target3 = [3, 3], 6
    print("Test Case 3:", solution.twoSum(nums3, target3))  # Expected Output: [0, 1]

    # Test Case 4
    nums4, target4 = [1, 2, 3, 4, 5], 9
    print("Test Case 4:", solution.twoSum(nums4, target4))  # Expected Output: [3, 4]

    # Test Case 5
    nums5, target5 = [0, 4, 3, 0], 0
    print("Test Case 5:", solution.twoSum(nums5, target5))  # Expected Output: [0, 3]

test_twoSum()

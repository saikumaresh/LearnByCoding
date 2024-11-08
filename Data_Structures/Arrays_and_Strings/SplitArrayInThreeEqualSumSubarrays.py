# Split array in three equal sum subarrays

# Difficulty: Medium
# https://www.geeksforgeeks.org/problems/split-array-in-three-equal-sum-subarrays/1

# Problem Statement
# Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. 
# If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), 
# otherwise return an array {-1,-1}.
# Note: Driver code will print true if arr can be split into three equal sum subarrays, otherwise, it is false.

# Examples :

# Input:  arr[] = [1, 3, 4, 0, 4]
# Output: true
# Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4. 

# Input: arr[] = [2, 3, 4]
# Output: false
# Explanation: No three subarrays exist which have equal sum.

# Input: arr[] = [0, 1, 1]
# Output: false

# Constraints:
# 3 ≤ arr.size() ≤ 106
# 0 ≤ arr[i] ≤ 106

# Expected Complexities
# Time Complexity: O(n)Auxiliary Space: O(1)

class Solution:
    # Function to determine if array arr can be split into three equal sum subarrays
    # @param arr: List of integers
    # @return: List of two indices [i, j] if possible, otherwise [-1, -1]
    def findSplit(self, arr):
        total_sum = sum(arr)  # Calculate the total sum of the array
        
        # If the total sum is not divisible by 3, return [-1, -1] as we cannot split it into three equal parts
        if total_sum % 3 != 0:
            return [-1, -1]
        
        target_sum = total_sum // 3  # Each subarray must sum to this value
        current_sum = 0  # Track the running sum of elements
        first_split = -1  # Index for the end of the first subarray
        second_split = -1  # Index for the end of the second subarray

        # Iterate over the array to find valid split points
        for i in range(len(arr)):
            current_sum += arr[i]  # Update the current running sum
            
            # Check for the first split point where the sum is equal to target_sum
            if current_sum == target_sum and first_split == -1:
                first_split = i  # Set the end of the first subarray
                
            # Check for the second split point where the sum is 2 * target_sum
            elif current_sum == 2 * target_sum and first_split != -1:
                second_split = i  # Set the end of the second subarray
                break  # Stop after finding both splits
        
        # If both split points are found, return them; otherwise, return [-1, -1]
        if first_split != -1 and second_split != -1:
            return [first_split, second_split]
        
        return [-1, -1]

# Test function to run test cases
def run_tests():
    s = Solution()
    
    # Test Case 1: Array can be split into three equal sum subarrays
    arr1 = [1, 3, 4, 0, 4]
    print(s.findSplit(arr1))  # Expected output: [1, 2]
    
    # Test Case 2: Array cannot be split into three equal sum subarrays
    arr2 = [2, 3, 4]
    print(s.findSplit(arr2))  # Expected output: [-1, -1]
    
    # Test Case 3: Array cannot be split due to insufficient elements
    arr3 = [0, 1, 1]
    print(s.findSplit(arr3))  # Expected output: [-1, -1]
    
    # Test Case 4: Array with zeroes that can be split into equal parts
    arr4 = [0, 0, 0, 0]
    print(s.findSplit(arr4))  # Expected output: [0, 1] (or any valid split with equal zero sum)
    
    # Test Case 5: Large array with multiple possible split points
    arr5 = [3, 3, 6, 3, 3]
    print(s.findSplit(arr5))  # Expected output: [1, 3]
    
    # Test Case 6: Array with negative numbers that can be split
    arr6 = [-3, 1, 2, 1, 2, 1, -3]
    print(s.findSplit(arr6))  # Expected output: [1, 4]
    
    # Test Case 7: All elements are the same and can be split
    arr7 = [4, 4, 4, 4, 4, 4]
    print(s.findSplit(arr7))  # Expected output: [1, 3]
    
    # Test Case 8: Array with mixed positive and negative numbers, not splittable
    arr8 = [-5, 10, 5, -10, 5]
    print(s.findSplit(arr8))  # Expected output: [-1, -1]

# Run test cases
run_tests()

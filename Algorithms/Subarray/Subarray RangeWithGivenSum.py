# Subarray range with given sum

# https://www.geeksforgeeks.org/problems/subarray-range-with-given-sum0128/1

# Problem Statement
# Given an unsorted array of integers arr[], and a target tar, determine the number of subarrays whose elements sum up to the target value.

# Examples:

# Input: arr[] = [10, 2, -2, -20, 10] , tar = -10
# Output: 3
# Explanation: Subarrays with sum -10 are: [10, 2, -2, -20], [2, -2, -20, 10] and [-20, 10].

# Input: arr[] = [1, 4, 20, 3, 10, 5] , tar = 33
# Output: 1
# Explanation: Subarray with sum 33 is: [20,3,10].

# Expected Time Complexity: O(n)
# Expected Auxilary Space: O(n)

# Constraints:
# 1 <= arr.size() <= 106
# -105 <= arr[i] <= 105
# -105 <= tar <= 105

class Solution:
    
    # Complete this function
    # Function to count the number of subarrays which add to the given sum.
    def subArraySum(self, arr, tar):
        # Initialize current sum and hashmap for prefix sum
        currsum = 0
        hashmap = {}
        count = 0
        
        # Traverse through the array
        for i in arr:
            currsum += i
            
            # If current sum equals the target, increment count
            if currsum == tar:
                count += 1
                
            # Check if (currsum - tar) exists in hashmap
            if (currsum - tar) in hashmap:
                count += hashmap[currsum - tar]
                
            # Add or update the current sum's frequency in hashmap
            if currsum in hashmap:
                hashmap[currsum] += 1
            else:
                hashmap[currsum] = 1
        
        return count

sol = Solution()
arr = [10, 2, -2, -20, 10]
tar = -10
print(sol.subArraySum(arr, tar))  # Output: 3

arr2 = [1, 4, 20, 3, 10, 5]
tar2 = 33
print(sol.subArraySum(arr2, tar2))  # Output: 1

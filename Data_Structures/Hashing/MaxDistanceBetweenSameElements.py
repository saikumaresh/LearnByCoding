# Max distance between same elements
# Difficulty: Easy

# https://www.geeksforgeeks.org/problems/max-distance-between-same-elements/1

# Problem Statement
# Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

# Note: You may assume that every input array has repetitions.

# Examples:

# Input: arr = [1, 1, 2, 2, 2, 1]
# Output: 5
# Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

# Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
# Output: 10
# Explanation: maximum distance for 2 is 11-1 = 10, 
# maximum distance for 1 is 4-2 = 2 ,
# maximum distance for 4 is 10-5 = 5, 
# So max distance is 10.

# Expected Time Complexity :  O(n)
# Expected Auxilliary Space : O(n)

# Constraints:
# 1 <= arr.size() <= 10^6
# 1 <= arr[i] <= 10^9

class Solution:
    def maxDistance(self, arr):
        # Code here
        hashmap = {}
        for i in range(len(arr)):
            if arr[i] in hashmap:
                hashmap[arr[i]].append(i)
            else:
                hashmap[arr[i]] = [i]
        max_distance = 0
        for i in hashmap:
            temp = abs(hashmap[i][0] - hashmap[i][-1])
            max_distance = max(temp, max_distance)
        return max_distance
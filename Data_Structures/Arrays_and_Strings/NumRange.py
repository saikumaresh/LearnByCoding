# NUMRANGE

# https://www.interviewbit.com/problems/numrange/

# Given an array of non negative integers A, and a range (B, C), 

# find the number of continuous subsequences in the array which have sum S in the range [B, C] or B <= S <= C

# Continuous subsequence is defined as all the numbers A[i], A[i + 1], .... A[j]

# where 0 <= i <= j < size(A)

# Example :

# A : [10, 5, 1, 0, 2]
# (B, C) : (6, 8)
# ans = 3 

# as [5, 1], [5, 1, 0], [5, 1, 0, 2] are the only 3 continuous subsequence with their sum in the range [6, 8]

# NOTE : The answer is guranteed to fit in a 32 bit signed integer.

# Solution approach: We can use a sliding window technique to count the number of continuous subarrays with sums within the specified range. 
# We first count subarrays with sums less than or equal to C and then subtract the count of those with sums less than B.

class Solution:
    def numRange(self, A, B, C):
        def countSubarraysWithMaxSum(max_sum):
            if max_sum < 0:
                return 0
            n = len(A)
            current_sum = 0
            left = 0
            count = 0
            for right in range(n):
                current_sum += A[right]
                while current_sum > max_sum:
                    current_sum -= A[left]
                    left += 1
                count += (right - left + 1)
            return count
        return countSubarraysWithMaxSum(C) - countSubarraysWithMaxSum(B - 1)
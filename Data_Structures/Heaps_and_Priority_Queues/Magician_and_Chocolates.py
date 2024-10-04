# Title: Magician and Chocolates

# https://www.interviewbit.com/problems/magician-and-chocolates/

# Problem Description
# Given N bags, each bag contains Bi chocolates. There is a kid and a magician. 
# In one unit of time, kid chooses a random bag i, eats Bi chocolates, 
# then the magician fills the ith bag with floor(Bi/2) chocolates.
#
# Find the maximum number of chocolates that kid can eat in A units of time.
#
# NOTE: 
# floor() function returns the largest integer less than or equal to a given number.
# Return your answer modulo 10^9+7
#
# Problem Constraints
# 1 <= A <= 10^5
# 1 <= |B| <= 10^5
# 1 <= Bi <= INT_MAX
#
# Input Format
# First argument is an integer A.
# Second argument is an integer array B of size N.
#
# Output Format
# Return an integer denoting the maximum number of chocolates that kid can eat in A units of time.

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def maxChocolates(self, A, B):
        import heapq
        
        # Create a max heap (using negative values for the heapq)
        max_heap = [-b for b in B]
        heapq.heapify(max_heap)
        
        total_chocolates = 0
        MOD = 10**9 + 7
        
        for _ in range(A):
            # Get the bag with the maximum chocolates
            max_chocolates = -heapq.heappop(max_heap)
            total_chocolates = (total_chocolates + max_chocolates) % MOD
            
            # Refill the bag with floor(max_chocolates / 2)
            heapq.heappush(max_heap, -(max_chocolates // 2))
        
        return total_chocolates

# Example Usage:
# solution = Solution()
# result = solution.maxChocolates(3, [6, 5])
# print(result)  # Output: 14
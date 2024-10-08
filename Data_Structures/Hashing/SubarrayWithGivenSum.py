# Subarray with given sum

# Problem Description

# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
# If the answer does not exist return an array with a single integer "-1".
# First sub-array means the sub-array for which starting index in minimum.

# Problem Constraints

# 1 <= length of the array <= 100000
# 1 <= A[i] <= 109
# 1 <= B <= 109


# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.

# Output Format
# Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single integer "-1".

# Example Input

# Input 1:
#  A = [1, 2, 3, 4, 5]
#  B = 5
# Input 2:
#  A = [5, 10, 20, 100, 105]
#  B = 110

# Example Output

# Output 1:
#  [2, 3]
# Output 2:
#  [-1]

# Example Explanation

# Explanation 1:
#  [2, 3] sums up to 5.
# Explanation 2:
#  No subarray sums up to required number.

class Solution:
    # @param A : list of integers (input array)
    # @param B : integer (target sum to find in subarray)
    # @return a list of integers (the subarray with sum equal to B)
    def solve(self, A, B):
        # Get the length of the input array
        n = len(A)
        
        # Variables to track the start and end of the subarray with sum B
        start = n  # Initially, start is set beyond the array (invalid start)
        end = -1   # Initially, end is set to an invalid index
        
        # Dictionary to store prefix sums and their corresponding indices
        pf_hashmap = {}
        
        # Variable to keep track of the current cumulative sum (prefix sum)
        currsum = 0 
        
        # Iterate through the array to calculate prefix sums
        for i in range(n):
            currsum += A[i]  # Add current element to the cumulative sum
            
            # Store the current cumulative sum and its index in the hashmap
            pf_hashmap[currsum] = i
            
            # Check if there's a prefix sum that makes the current subarray sum to B
            if (currsum - B) in pf_hashmap:
                # If (currsum - B) exists, it means the subarray sum equals B
                index = pf_hashmap[currsum - B]  # Get the index of the previous sum
                
                # If the subarray start index is smaller, update the start and end
                if index < start:
                    start = index  # Update the start index
                    end = i        # Update the end index
                    # Return the subarray from the next index after 'start' to 'end'
                    return A[start + 1:end + 1]
            
            # If the cumulative sum itself equals B, the subarray is from the start
            if currsum == B:
                # Return the subarray from the beginning to the current index
                return A[:i + 1]
        
        # If no such subarray is found, return [-1] to indicate failure
        return [-1]
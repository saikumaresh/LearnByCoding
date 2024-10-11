# 2 Sum

# Problem Description
# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers 
# (both index1 and index2 ) are not zero-based. Put both these numbers in order in an array and return the array from your function 
# ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.
# If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

# Input: [2, 7, 11, 15], target=9

# Output: index1 = 1, index2 = 2

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        # HashMap to store the difference (target - current number) and its index
        difference_hash = {}

        # Variables to track the minimum index1 and index2
        index1 = len(A) + 1  # Set to len(A) + 1 to indicate uninitialized state
        index2 = len(A) + 1

        # Iterate through the array
        for i in range(len(A)):
            current_value = A[i]
            
            # Check if the complement (B - A[i]) exists in the hashmap
            if (B - current_value) in difference_hash:
                # Get the index of the complement
                temp_idx1 = difference_hash[B - current_value] + 1  # 1-based index of complement
                temp_idx2 = i + 1  # 1-based index of the current element
                
                # Ensure idx1 is the smaller index and idx2 is the larger index
                idx1 = min(temp_idx1, temp_idx2)
                idx2 = max(temp_idx1, temp_idx2)

                # Update index1 and index2 only if the new pair is lexicographically smaller
                if (idx2 < index2) or (idx2 == index2 and idx1 < index1):
                    index1 = idx1
                    index2 = idx2
            
            # If current number is not in the hashmap, store its index for future lookups
            if current_value not in difference_hash:
                difference_hash[current_value] = i  # Store 0-based index

        # If index1 and index2 remain uninitialized, return an empty list (no pair found)
        if index1 == len(A) + 1:
            return []
        
        # Return the 1-based indices of the two numbers
        return [index1, index2]

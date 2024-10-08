# Largest Continuous Sequence Zero Sum

# Problem Description
# Given an array A of N integers.
# Find the largest continuous sequence in a array which sums to zero.

# Problem Constraints
# 1 <= N <= 106
# -107 <= A[i] <= 107

# Input Format
# Single argument which is an integer array A.

# Output Format
# Return an array denoting the longest continuous sequence with total sum of zero.
# NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.

# Example Input
# A = [1,2,-2,4,-4]

# Example Output
# [2,-2,4,-4]

# Example Explanation
# [2,-2,4,-4] is the longest sequence with total sum of zero.

def largest_zero_sum_subarray(A):
    # Dictionary to store the first occurrence of each cumulative sum
    sum_index_map = {}
    max_len = 0
    start_index = -1
    end_index = -1
    
    # Initialize sum and add a starting point for cumulative sum 0
    curr_sum = 0
    sum_index_map[0] = -1
    
    for i in range(len(A)):
        # Update the running sum (cumulative sum)
        curr_sum += A[i]
        
        # Check if this cumulative sum has been seen before
        if curr_sum in sum_index_map:
            # Calculate the length of the subarray with sum 0
            prev_index = sum_index_map[curr_sum]
            subarray_len = i - prev_index
            
            # Check if it's the longest found so far
            if subarray_len > max_len:
                max_len = subarray_len
                start_index = prev_index + 1
                end_index = i
        else:
            # If not seen, store the current sum with the current index
            sum_index_map[curr_sum] = i
    
    # If no subarray found, return an empty list
    if start_index == -1:
        return []
    
    # Return the longest subarray with sum 0
    return A[start_index:end_index + 1]

# Example input
A = [1, 2, -2, 4, -4]

# Find the largest continuous subarray with zero sum
result = largest_zero_sum_subarray(A)
print(result)

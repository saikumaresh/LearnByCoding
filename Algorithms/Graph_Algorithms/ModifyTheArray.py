# Modify the Array

# https://www.geeksforgeeks.org/problems/ease-the-array0633/1

# Problem Statement
# Given an array arr. Return the modified array in such a way that if the current and next numbers 
# are valid numbers and are equal then double the current number value and replace the next number with 0. 
# After the modification, rearrange the array such that all 0's are shifted to the end.
# Note:
# Assume ‘0’ as the invalid number and all others as a valid number.
# The sequence of the valid numbers is present in the same order.

# Example:

# Input: arr[] = [2, 2, 0, 4, 0, 8] 
# Output: [4, 4, 8, 0, 0, 0] 
# Explanation: At index 0 and 1 both the elements are the same. 
# So, we will change the element at index 0 to 4 and the element at index 1 is 0 then we will shift all the zeros to the end of the array. 
# So, the array will become [4, 4, 8, 0, 0, 0].

# Input: arr[] = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8] 
# Output: [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
# Explanation: At index 5 and 6 both the elements are the same. 
# So, we will change the element at index 5 to 12 and the element at index 6 is 0. 
# We will change the element at index 1 to 4 and the element at index 2 is 0. 
# Then we shift all the zeros to the end of the array. So, array will become [4, 2, 12, 8, 0, 0, 0, 0, 0, 0].

# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 106

class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)  # Get the length of the array
        
        # Traverse the array up to the second last element
        for i in range(n - 1):
            # Check if the current element and the next element are the same and not zero
            if arr[i] == arr[i + 1] and arr[i] != 0:
                arr[i] = arr[i] * 2  # Double the current element
                arr[i + 1] = 0  # Set the next element to zero
        
        # Collect all non-zero elements from the array
        result = [x for x in arr if x != 0]
        # Calculate the number of zeros to append
        zeros = [0] * (n - len(result))  # Append required number of zeros
        result.extend(zeros)  # Combine non-zero elements with zeros
        
        return result  # Return the modified array


# Test cases to validate the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    arr1 = [2, 2, 0, 4, 0, 8]
    print(solution.modifyAndRearrangeArr(arr1))  # Expected Output: [4, 4, 8, 0, 0, 0]
    
    # Test case 2
    arr2 = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
    print(solution.modifyAndRearrangeArr(arr2))  # Expected Output: [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
    
    # Test case 3
    arr3 = [0, 0, 0, 0]
    print(solution.modifyAndRearrangeArr(arr3))  # Expected Output: [0, 0, 0, 0]
    
    # Test case 4
    arr4 = [1, 1, 1, 1, 1]
    print(solution.modifyAndRearrangeArr(arr4))  # Expected Output: [2, 2, 0, 0, 0]
    
    # Test case 5
    arr5 = [2, 0, 2, 2, 2, 0]
    print(solution.modifyAndRearrangeArr(arr5))  # Expected Output: [4, 2, 0, 0, 0, 0]
    
    # Test case 6
    arr6 = [5, 5, 0, 5, 0, 5]
    print(solution.modifyAndRearrangeArr(arr6))  # Expected Output: [10, 5, 5, 0, 0, 0]

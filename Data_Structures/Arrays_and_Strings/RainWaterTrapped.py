# Rain Water Trapped

# Problem Description
# Imagine a histogram where the bars' heights are given by the array A. 
# Each bar is of uniform width, which is 1 unit. 
# When it rains, water will accumulate in the valleys between the bars.
# Your task is to calculate the total amount of water that can be trapped in these valleys.

# Problem Constraints
# 1 <= |A| <= 105
# 0 <= A[i] <= 105

# Input Format
# First and only argument is the Integer Array, A.

# Output Format
# Return an Integer, denoting the total amount of water that can be trapped in these valleys

# Example Input

# Input 1:
#  A = [0, 1, 0, 2]
# Input 2:
# A = [1, 2]

# Example Output

# Output 1:
# 1
# Output 2:
# 0

# Example Explanation

# Explanation 1:
# 1 unit is trapped on top of the 3rd element.
# Rain Water Histogram

# Explanation 2:
# No water is trapped.

class Solution:
    # Method to calculate trapped water between buildings represented by heights in array A
    # @param A : tuple of integers representing heights
    # @return an integer representing total trapped water

    def trap(self, A):
        # Edge case: If there are less than 3 buildings, no water can be trapped
        n = len(A)
        if n < 3:
            return 0
        
        # Arrays to store the maximum heights from the left and right for each index
        left_max = []
        right_max = []
        
        # Variable to accumulate the total water trapped
        water_trapped = 0
        
        # Calculate left_max for each index
        curr = 0
        for i in range(n):
            curr = max(curr, A[i])
            left_max.append(curr)
        
        # Calculate right_max for each index
        curr = 0
        for i in range(n - 1, -1, -1):
            curr = max(curr, A[i])
            right_max.append(curr)
        
        # Reverse right_max to align it with left_max
        right_max = right_max[::-1]
        
        # Calculate the water trapped at each position
        for i in range(1, n - 1):  # Ignore first and last positions
            # Minimum of left_max and right_max defines the max water level
            temp = min(left_max[i - 1], right_max[i + 1])
            
            # If the water level is higher than current height, water is trapped
            if temp > A[i]:
                water_trapped += temp - A[i]
        
        return water_trapped

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Heights: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # Expected Output: 6
    print(solution.trap((0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1)))  # Output: 6
    
    # Test Case 2
    # Heights: [3, 0, 2, 0, 4]
    # Expected Output: 7
    print(solution.trap((3, 0, 2, 0, 4)))  # Output: 7
    
    # Test Case 3
    # Heights: [0, 0, 0, 0]
    # Expected Output: 0
    print(solution.trap((0, 0, 0, 0)))  # Output: 0
    
    # Test Case 4
    # Heights: [1, 1, 1, 1]
    # Expected Output: 0
    print(solution.trap((1, 1, 1, 1)))  # Output: 0
    
    # Test Case 5
    # Heights: [4, 2, 0, 3, 2, 5]
    # Expected Output: 9
    print(solution.trap((4, 2, 0, 3, 2, 5)))  # Output: 9

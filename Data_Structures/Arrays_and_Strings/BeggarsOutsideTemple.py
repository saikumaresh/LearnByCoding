# Continuous Sum Query

# Problem Description
# There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, 
# they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.
# Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, 
# find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
# For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 2D array B

# Problem Constraints
# 1 <= A <= 2 * 105
# 1 <= L <= R <= A
# 1 <= P <= 103
# 0 <= len(B) <= 105

# Input Format
# The first argument is a single integer A.
# The second argument is a 2D integer array B.

# Output Format
# Return an array(0 based indexing) that stores the total number of coins in each beggars pot.

# Example Input
# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

# Example Output
# 10 55 45 25 25

# Example Explanation
# First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
# Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
# Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]

class Solution:
    # Method to process range update queries on an array
    # @param A : integer (size of the array)
    # @param B : list of list of integers (queries in the format [start, end, value])
    # @return a list of integers representing the final state of the array after all queries

    def solve(self, A, B):
        # Number of queries to be processed
        queries = len(B)
        
        # Initialize a prefix array with zero values
        pf = [0] * A
        
        # Process each query
        for i in range(queries):
            start = B[i][0] - 1  # Convert to zero-based index for start
            end = B[i][1] - 1    # Convert to zero-based index for end
            value = B[i][2]      # Value to be added in the range
            
            # Apply the value at the start index
            pf[start] += value
            
            # Apply the negative value at end+1 if within bounds
            if end + 1 < A:
                pf[end + 1] -= value

        # Calculate prefix sum to get final values
        for i in range(1, A):
            pf[i] += pf[i - 1]

        return pf

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    # Array size: 5, Queries: [[1, 3, 10], [2, 5, 5]]
    # Expected Output: [10, 15, 15, 5, 5]
    print(solution.solve(5, [[1, 3, 10], [2, 5, 5]]))  # Output: [10, 15, 15, 5, 5]
    
    # Test Case 2
    # Array size: 4, Queries: [[1, 2, 4], [3, 4, 3]]
    # Expected Output: [4, 4, 3, 3]
    print(solution.solve(4, [[1, 2, 4], [3, 4, 3]]))  # Output: [4, 4, 3, 3]
    
    # Test Case 3
    # Array size: 6, Queries: [[1, 6, 2]]
    # Expected Output: [2, 2, 2, 2, 2, 2]
    print(solution.solve(6, [[1, 6, 2]]))  # Output: [2, 2, 2, 2, 2, 2]
    
    # Test Case 4
    # Array size: 3, Queries: []
    # Expected Output: [0, 0, 0]
    print(solution.solve(3, []))  # Output: [0, 0, 0]

# First Missing Integer

# Problem Description
# Given an unsorted integer array, A of size N. Find the first missing positive integer.
# Note: Your algorithm should run in O(n) time and use constant space.

# Problem Constraints
# 1 <= N <= 1000000
# -109 <= A[i] <= 109

# Input Format
# First argument is an integer array A.

# Output Format
# Return an integer denoting the first missing positive integer.

# Example Input

# Input 1:
# [1, 2, 0]

# Input 2:
# [3, 4, -1, 1]

# Input 3:
# [-8, -7, -6]

# Example Output

# Output 1:
# 3
# Output 2:
# 2
# Output 3:
# 1

# Example Explanation

# Explanation 1:
# A = [1, 2, 0]
# First positive integer missing from the array is 3.

# Explanation 2:
# A = [3, 4, -1, 1]
# First positive integer missing from the array is 2.

# Explanation 3:
# A = [-8, -7, -6]
# First positive integer missing from the array is 1.

class Solution:
    # @param A : list of integers
    # @return an integer denoting the first missing positive integer
    
    def firstMissingPositive(self, A):
        n = len(A)  # Get the size of the array
        i = 0  # Start index for iteration

        # Step 1: Place each number in its correct position if possible (indexing from 1 to n)
        while i < n:
            # Only process numbers that are within the range [1, n]
            if 1 <= A[i] <= n:
                correct_index = A[i] - 1  # Correct index for the number A[i]
                
                # If the number is not already in the correct position
                if A[i] != A[correct_index]:
                    # Swap numbers to place A[i] at its correct position
                    A[i], A[correct_index] = A[correct_index], A[i]
                else:
                    # If the number is already in the correct position, move to the next index
                    i += 1
            else:
                # If A[i] is outside the range [1, n], move to the next index
                i += 1
        
        # Step 2: Find the first missing positive integer
        for i in range(n):
            if A[i] != i + 1:
                return i + 1  # The first missing positive integer is the one that is out of place
        
        # Step 3: If all positions from 1 to n are filled correctly, the missing number is n + 1
        return n + 1

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Missing positive integer is greater than the size of the array
    A1 = [1, 2, 0]
    # Explanation: The first missing positive integer is 3, because 1 and 2 are present.
    print("Test Case 1 Output:", solution.firstMissingPositive(A1))  # Expected Output: 3

    # Test Case 2: Missing positive integer is 2
    A2 = [3, 4, -1, 1]
    # Explanation: The first missing positive integer is 2, because 1 is present but 2 is missing.
    print("Test Case 2 Output:", solution.firstMissingPositive(A2))  # Expected Output: 2

    # Test Case 3: All elements are negative, so the first missing positive integer is 1
    A3 = [-8, -7, -6]
    # Explanation: The first missing positive integer is 1 because all numbers are negative.
    print("Test Case 3 Output:", solution.firstMissingPositive(A3))  # Expected Output: 1

    # Test Case 4: The array contains all numbers from 1 to n
    A4 = [1, 2, 3]
    # Explanation: The first missing positive integer is 4.
    print("Test Case 4 Output:", solution.firstMissingPositive(A4))  # Expected Output: 4

    # Test Case 5: The array contains only one element, which is negative
    A5 = [-1]
    # Explanation: The first missing positive integer is 1 because there are no positive numbers.
    print("Test Case 5 Output:", solution.firstMissingPositive(A5))  # Expected Output: 1

    # Test Case 6: The array is already in correct order with no missing positive integer
    A6 = [1, 2, 3, 4, 5]
    # Explanation: The first missing positive integer is 6 because all integers from 1 to 5 are present.
    print("Test Case 6 Output:", solution.firstMissingPositive(A6))  # Expected Output: 6

    # Test Case 7: The array has a large size with mixed elements
    A7 = [3, 1, 5, 4, 2, 7, 6]
    # Explanation: The first missing positive integer is 8.
    print("Test Case 7 Output:", solution.firstMissingPositive(A7))  # Expected Output: 8

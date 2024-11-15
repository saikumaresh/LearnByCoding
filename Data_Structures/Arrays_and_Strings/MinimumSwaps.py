# Minimum Swaps

# Problem Description
# Given an array of integers A and an integer B, find and return the minimum number of swaps required 
# to bring all the numbers less than or equal to B together.
# Note: It is possible to swap any two elements, not necessarily consecutive.

# Problem Constraints
# 1 <= length of the array <= 100000
# -109 <= A[i], B <= 109

# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.

# Output Format
# Return the minimum number of swaps.

# Example Input

# Input 1:
#  A = [1, 12, 10, 3, 14, 10, 5]
#  B = 8
# Input 2:
#  A = [5, 17, 100, 11]
#  B = 20

# Example Output

# Output 1:
#  2
# Output 2:
#  1

# Example Explanation

# Explanation 1:
#  A = [1, 12, 10, 3, 14, 10, 5]
#  After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
#  After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
#  Now, all elements less than or equal to 8 are together.

# Explanation 2:
#  A = [5, 17, 100, 11]
#  After swapping 100 and 11, A => [5, 17, 11, 100].
#  Now, all elements less than or equal to 20 are together.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        Finds the minimum number of swaps required to bring all elements <= B together in an array.

        Parameters:
        A (List[int]): The array of integers.
        B (int): The threshold value.

        Returns:
        int: Minimum number of swaps needed.
        """
        count = 0  # Counts the number of elements <= B
        for i in A:
            if i <= B:
                count += 1

        # If all elements are <= B, no swaps needed
        if count == len(A):
            return 0

        # Initialize the count of <= B elements in the first window of size `count`
        count_in_window = []
        temp = 0
        for i in range(count):  # First window
            if A[i] <= B:
                temp += 1
        count_in_window.append(temp)

        # Slide the window across the array
        for i in range(1, len(A) - count + 1):  # Subsequent windows
            if A[i - 1] <= B:  # Remove the effect of the element going out of the window
                temp -= 1
            if A[i + count - 1] <= B:  # Add the effect of the new element entering the window
                temp += 1
            count_in_window.append(temp)

        # Maximum count of <= B elements in any window
        max_count_in_window = max(count_in_window)
        
        # Result is the difference between total required count and the maximum found in any window
        return count - max_count_in_window

# Test cases
solution = Solution()

# Test Case 1: Standard case with mixed values
print("Test Case 1:", solution.solve([1, 3, 5, 2, 8, 6, 4], 5))
# Expected Output: 1 (Moving `5` or `2` next to the group of values <= 5)

# Test Case 2: All values are <= B
print("Test Case 2:", solution.solve([2, 1, 3, 4], 5))
# Expected Output: 0 (All elements are already <= B)

# Test Case 3: All values are > B
print("Test Case 3:", solution.solve([6, 7, 8, 9], 5))
# Expected Output: 0 (No elements <= B, so no swaps needed)

# Test Case 4: Array with values both greater and smaller than B
print("Test Case 4:", solution.solve([2, 7, 9, 5, 8, 7, 4], 6))
# Expected Output: 2 (Requires two swaps to bring 2 and 5 close to each other)

# Test Case 5: Single element array
print("Test Case 5:", solution.solve([5], 5))
# Expected Output: 0 (Single element, no swaps needed)

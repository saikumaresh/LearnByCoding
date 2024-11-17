# Add Binary Strings

# Problem Description
# Given two binary strings A and B. Return their sum (also a binary string).

# Problem Constraints
# 1 <= length of A <= 105
# 1 <= length of B <= 105
# A and B are binary strings

# Input Format
# The two argument A and B are binary strings.

# Output Format
# Return a binary string denoting the sum of A and B

# Example Input

# Input 1:
# A = "100"
# B = "11"
# Input 2:
# A = "110"
# B = "10"

# Example Output

# Output 1:
# "111"
# Output 2:
# "1000"

# Example Explanation

# For Input 1:
# The sum of 100 and 11 is 111.
# For Input 2: 
# The sum of 110 and 10 is 1000.

class Solution:
    # @param A : string (binary number as a string)
    # @param B : string (binary number as a string)
    # @return a string (binary sum as a string)
    def addBinary(self, A, B):
        """
        Adds two binary numbers represented as strings and returns their sum as a binary string.

        Parameters:
        A (str): The first binary number as a string.
        B (str): The second binary number as a string.

        Returns:
        str: The binary sum of A and B as a string.
        """
        # Convert binary strings to integers, add them, then convert the result back to a binary string
        return bin(int(A, 2) + int(B, 2)).replace("0b", "")

# Test cases
def test_addBinary():
    solution = Solution()
    
    # Test Case 1
    A1, B1 = "101", "11"
    print("Test Case 1:", solution.addBinary(A1, B1))  # Expected Output: "1000"

    # Test Case 2
    A2, B2 = "110", "110"
    print("Test Case 2:", solution.addBinary(A2, B2))  # Expected Output: "1100"

    # Test Case 3
    A3, B3 = "0", "0"
    print("Test Case 3:", solution.addBinary(A3, B3))  # Expected Output: "0"

    # Test Case 4
    A4, B4 = "1", "111"
    print("Test Case 4:", solution.addBinary(A4, B4))  # Expected Output: "1000"

    # Test Case 5
    A5, B5 = "101010", "1111"
    print("Test Case 5:", solution.addBinary(A5, B5))  # Expected Output: "110001"

test_addBinary()

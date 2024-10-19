# Nearest multiple of 10

# https://www.geeksforgeeks.org/problems/nearest-multiple-of-102437/1

# Problem statement
# A string str is given to represent a positive number. The task is to round str to the nearest multiple of 10.  
# If you have two multiples equally apart from str, choose the smallest element among them.

# Examples:

# Input: str = 29 
# Output: 30
# Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 

# Input: str = 15
# Output: 10
# Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.

# Expected Time Complexity: O(n).
# Expected Auxiliary Space: O(1).

# Constraints:
# 1 <= str.size()<= 105

class Solution:
    def roundToNearest(self, string):
        # Get the last digit of the string (this represents the unit place)
        last_digit = int(string[-1])
        
        # Check if the last digit is less than or equal to 5
        # If so, round down by replacing the last digit with '0'
        if last_digit <= 5:
            return string[:-1] + str(0)
        
        # If the last digit is greater than 5, we need to round up
        else:
            # Get the second-to-last digit (tens place) and increment it if possible
            prev_digit = int(string[-2])
            
            # Check if the tens place digit is not 9, so we can simply increment it
            if prev_digit is not 9:
                # Increment the tens digit and set the last digit to '0'
                return string[:-2] + str(prev_digit + 1) + str(0)
            
            # If the tens digit is 9, we need to handle the carry-over case
            else:
                temp = "0"  # We store the current result here (starting with '0')
                i = -2      # Pointer to keep track of the current digit, starting from the second last one
                
                # Loop until we find a digit that is not 9
                while prev_digit is 9:
                    temp = "0" + temp  # Add '0' to the result for each 9 encountered
                    i -= 1             # Move the pointer to the next digit to the left
                    
                    # Check if we have reached the beginning of the string
                    if (i * -1) > len(string):
                        # If all digits are 9 (e.g., 999, 9999), return "1000", "10000" etc.
                        return "1" + str("0" * len(string))
                        break
                    else:
                        # Move to the next left digit
                        prev_digit = int(string[i])
                
                # Increment the left-most non-9 digit and append the required number of '0's
                return string[:i] + str(prev_digit + 1) + temp

sol = Solution()
print(sol.roundToNearest("12345"))
print(sol.roundToNearest("989"))
print(sol.roundToNearest("99"))
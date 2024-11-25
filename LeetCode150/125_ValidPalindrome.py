# 125. Valid Palindrome

# Problem Statement
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome considering only alphanumeric characters
        and ignoring cases.

        :param s: A string to check.
        :return: True if the string is a palindrome, False otherwise.
        """
        # Step 1: Filter out non-alphanumeric characters and convert to lowercase
        s = "".join(filter(str.isalnum, s.lower()))
        
        # Step 2: Check if the processed string is the same when reversed
        return s == s[::-1]


# Testing the function
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = {
        "A man, a plan, a canal: Panama": True,  # Classic palindrome ignoring spaces and punctuation
        "race a car": False,  # Not a palindrome
        " ": True,  # Empty or whitespace-only strings are palindromes
        "abba": True,  # Simple even-length palindrome
        "abcba": True,  # Simple odd-length palindrome
        "abcd": False,  # Not a palindrome
        "No lemon, no melon": True,  # Palindrome ignoring case and spaces
        "12321": True,  # Numeric palindrome
        "12345": False,  # Not a palindrome
        "Was it a car or a cat I saw?": True,  # Palindrome ignoring case and punctuation
        "": True,  # Empty string is a palindrome
        "a.": True,  # Single character with punctuation is a palindrome
    }
    
    # Running test cases
    for test_input, expected_output in test_cases.items():
        result = solution.isPalindrome(test_input)
        print(f"Input: '{test_input}' | Expected: {expected_output} | Output: {result}")

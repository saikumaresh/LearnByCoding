def is_palindrome(s):
    if len(s) < 2:  # Base case: if the string has less than 2 characters, it's a palindrome
        return True
    if s[0] != s[-1]:  # If the first and last characters don't match, it's not a palindrome
        return False
    # Recursive step: check the substring that excludes the first and last characters
    return is_palindrome(s[1:-1])

words = ["Tamil", "Malayalam", "English", "eye", "aabbcc"]  # List of words to check

# Iterate over each word and check if it's a palindrome
for word in words:
    if is_palindrome(word.lower()):  # Convert to lowercase for case-insensitive comparison
        print(word + " is a palindrome")
    else:
        print(word + " is not a palindrome")
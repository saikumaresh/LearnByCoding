def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

words = ["Tamil", "Malayalam", "English", "eye", "aabbcc"]

for word in words:
    if is_palindrome(word.lower()):  # Using lower() to handle case sensitivity
        print(word + " is a palindrome")
    else:
        print(word + " is not a palindrome")

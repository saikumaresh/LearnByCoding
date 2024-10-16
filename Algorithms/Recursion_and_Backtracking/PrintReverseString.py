# Print reverse string

# Problem Description
# Write a recursive function that takes a string, S, as input and prints the characters of S in reverse order.

# Problem Constraints
# 1 <= |s| <= 1000

# Input Format
# First line of input contains a string S.

# Output Format
# Print the character of the string S in reverse order.

# Example Input

# Input 1:
#  scaleracademy
# Input 2:
#  cool

# Example Output

# Output 1:
#  ymedacarelacs
# Output 2:
#  looc

import sys
sys.setrecursionlimit(1000000)
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    s = list(input())
    def reverse(s,n):
        if n == 0:
            print(s[n], end="")
            return
        print(s[n], end="")
        return reverse(s,n-1)
    reverse(s,len(s)-1)
    return 0

if __name__ == '__main__':
    main()
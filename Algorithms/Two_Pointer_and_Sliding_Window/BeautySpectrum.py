# Beauty Spectrum

# https://unstop.com/code/challenge-assessment/307102?moduleId=467

# Problem Statement

# Imagine you are running a small restaurant, and you want to evaluate the beauty of each group of customers who dine together at your restaurant.
# Each group of customers can be represented as an array of integers, where each integer represents the amount of money each customer spent on their meal. 
# The size of the array represents the number of customers in the group.
# The beauty of a group can be defined as the Xth smallest amount of money spent by a customer in the group if it is negative. 
# If there are fewer than X negative amounts, the beauty is 0.

# For example, if a group of four customers spent $10, $-5, $20, and $-8, respectively, and we want to find the beauty of the subarray of size 3, 
# we would first consider all subarrays of size 3 within this group:
# $10, $-5, $20: the smallest negative value is $-5, so the beauty is $-5.
# $-5, $20, $-8: the smallest negative value is $-8, so the beauty is $-8.
# Therefore, the beauty of this group for subarrays of size 3 would be [$-5, $-8].


# Input Format
# The input should consist of:
# The first line contains the value of k, which is an integer representing the size of the subarrays to consider.
# The second line contains the value of X.
# The third line contains the value of N, which is an integer representing the number of customers.
# The fourth line contains a vector of N integers nums, representing the amount of money each customer spent on their meal.

# Output Format
# Print a numeric array of N - k + 1 numbers that represent the beauty of the subarrays in the array.

# Constraints
# N == nums.length 
# 1 <= N <= 10^5
# 1 <= k <= N
# 1 <= x <= k 
# -50 <= nums[i] <= 50 


# Sample Testcase 0

# Testcase Input
# 2
# 2
# 5
# -1 -2 -3 -4 -5

# Testcase Output
# -1 -2 -3 -4

# Explanation
# With k = 2, there are 4 subarrays.
# The second smallest negative number for [-1, -2] is -1.
# The second smallest negative number for [-2, -3] is -2.
# The second smallest negative number for [-3, -4] is -3.
# The second smallest negative number for [-4, -5] is -4. 

# Sample Testcase 1

# Testcase Input
# 2
# 1
# 6
# -3 1 2 -3 0 -3

# Testcase Output
# -3 0 -3 -3 -3

# Explanation
# 5 subarrays of size k = 2 are present.
# The first smallest negative number for the range [-3, 1] is 3.
# There is no negative integer for [1, 2]; hence the beauty is 0.
# The first smallest negative number for [2, -3] is -3.
# The first smallest negative integer for [-3, 0] is -3.
# The first smallest negative integer for the range [0, -3] is -3.

import sys

input = sys.stdin.read  # To read all inputs at once
data = input().split()  # Split the input into parts

k = int(data[0])
x = int(data[1])
n = int(data[2])
a = list(map(int, data[3:]))

result = []

for i in range(n - k + 1):
    temp = a[i:i + k]
    # Get the negative elements, sorted
    negative_elements = sorted([num for num in temp if num < 0])
    
    # Check if there are at least 'x' negative elements
    if len(negative_elements) >= x:
        result.append(negative_elements[x - 1])  # Append the x-th smallest negative
    else:
        result.append(0)  # Append 0 if there are fewer than x negative elements

# Print the result as a space-separated string
print(" ".join(map(str, result)))

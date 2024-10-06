# XOR Queries of a Subarray

# Problem Statement

# You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].
# For each query i compute the XOR of elements from left to right (that is, arr[left] XOR arr[left + 1] XOR ... XOR arr[right] ).
# Display an array answer where answer[i] is the answer to the ith query.

# Input Format
# The first line contains the number of elements in the array, n.
# The second line contains n space-seprated integers representing the array
# The third line contains the number of queries, q
# The fourth line contains the number of columns in queries matrxi which is always 2.
# The next q lines contains the queries where there are two space-seprated integers represnting left and right.

# Output Format
# Display a single line containing q space-seprated integers representing the answer to each query.

# Constraints
# 1 <= arr.length, queries.length<= 3 ^ 104
# 1 <= arr[i] <= 109
# queries[i].length == 2
# 0 <= lefti<= righti <arr.length

# Sample Testcase 0
# Testcase Input
# 4
# 4 8 2 10
# 4
# 2
# 2 3
# 1 3
# 0 0
# 0 3
# Testcase Output
# 8
# 0
# 4

# Explanation
# The answer to the queries:
# For 1st query: 2^10 = 8
# For 2nd query:8^2^10 = 0
# For 3rd query:4 = 4
# For 4th query: 4^8^2^10 = 4

def compute_xor(arr, queries):
    n = len(arr)
    
    # Create the prefix XOR array
    prefix_xor = [0] * n
    prefix_xor[0] = arr[0]
    
    for i in range(1, n):
        prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]
    
    # Process each query
    answers = []
    for left, right in queries:
        if left > 0:
            answer = prefix_xor[right] ^ prefix_xor[left - 1]
        else:
            answer = prefix_xor[right]
        answers.append(answer)
    
    return answers

# Input reading for Python 2
n = int(input())
arr = list(map(int, input().strip().split()))
q = int(input())
query_size = int(input())  # This will always be 2, but we read it anyway.
queries = [list(map(int, input().strip().split())) for _ in range(q)]

# Compute answers for queries
results = compute_xor(arr, queries)

# Output results
for i in results:
  print(i)

# Practice Problems: Subarrays, Subsequences, and Subsets

## 1. Maximum Subarray Sum (Kadane's Algorithm)
# Problem: Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum.
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

def max_subarray_sum(nums):
    max_so_far = nums[0]
    current_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(max_so_far, current_max)

    return max_so_far

# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(nums))  # Output: 6


## 2. Find All Subarrays of an Array
# Problem: Print all possible subarrays of the given array.
# Input: nums = [1, 2, 3]
# Output: [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]

def print_all_subarrays(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            print(nums[i:j+1])

# Example usage:
nums = [1, 2, 3]
print_all_subarrays(nums)


## 3. Subarray Product Less Than K
# Problem: Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all elements in the subarray is strictly less than `k`.
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The subarrays are [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6].

def num_subarrays_with_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    prod = 1
    result = 0
    left = 0

    for right in range(len(nums)):
        prod *= nums[right]
        while prod >= k:
            prod //= nums[left]
            left += 1
        result += right - left + 1

    return result

# Example usage:
nums = [10, 5, 2, 6]
k = 100
print(num_subarrays_with_product_less_than_k(nums, k))  # Output: 8


## 4. Longest Increasing Subsequence (LIS)
# Problem: Given an integer array `nums`, return the length of the longest increasing subsequence.
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2, 3, 7, 101].

def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4


## 5. Count All Subsequences of a String
# Problem: Given a string `s`, print all possible subsequences of the string.
# Input: s = "abc"
# Output: a, b, c, ab, ac, bc, abc

def print_all_subsequences(s):
    n = len(s)
    for i in range(1, 1 << n):
        subseq = ""
        for j in range(n):
            if i & (1 << j):
                subseq += s[j]
        print(subseq)

# Example usage:
s = "abc"
print_all_subsequences(s)


## 6. Longest Common Subsequence (LCS)
# Problem: Given two strings `text1` and `text2`, return the length of their longest common subsequence.
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace".

def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage:
text1 = "abcde"
text2 = "ace"
print(longest_common_subsequence(text1, text2))  # Output: 3


## 7. Generate All Subsets (Power Set)
# Problem: Given an array of distinct integers, return all possible subsets.
# Input: nums = [1, 2, 3]
# Output: [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]

def subsets(nums):
    result = []
    n = len(nums)
    
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)
    
    return result

# Example usage:
nums = [1, 2, 3]
print(subsets(nums))


## 8. Subset Sum Problem
# Problem: Given an array `arr[]` and a sum `sum`, determine if there is a subset of the given set with a sum equal to `sum`.
# Input: arr = [3, 34, 4, 12, 5, 2], sum = 9
# Output: True

def subset_sum(arr, sum):
    n = len(arr)
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][sum]

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
sum = 9
print(subset_sum(arr, sum))  # Output: True


## 9. Count Subsets with a Given Sum
# Problem: Given an array `arr[]` and a sum, count the number of subsets of the given array with a sum equal to the given sum.
# Input: arr = [2, 3, 5, 6, 8, 10], sum = 10
# Output: 3
# Explanation: The subsets are {10}, {2, 8}, {3, 5}.

def count_subsets_with_sum(arr, sum):
    n = len(arr)
    dp = [[0] * (sum + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][sum]

# Example usage:
arr = [2, 3, 5, 6, 8, 10]
sum = 10
print(count_subsets_with_sum(arr, sum))  # Output: 3


## 10. Partition Equal Subset Sum
# Problem: Given a non-empty array `nums`, determine if it can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Input: nums = [1, 5, 11, 5]
# Output: True

def canPartition(nums):
    # Step 1: Calculate the total sum of the array
    total_sum = 0
    for i in nums:
        total_sum += i
    
    # Step 2: If the sum is odd, it's impossible to partition into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    # Step 3: Set the target sum to be half of the total sum
    target = total_sum // 2
    
    # Step 4: Initialize a boolean DP array where dp[i] means we can achieve sum i
    dp = [False] * (target + 1)
    dp[0] = True  # We can always achieve sum 0 with an empty subset
    
    # Step 5: Process each number in nums
    for num in nums:
        # Update the DP array from right to left
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    # Step 6: The answer is whether we can achieve the target sum
    return dp[target]

# Example usage
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True

def print_subarrays(arr):
    print("Subarrays:")
    n = len(arr)
    for i in range(n):  # Starting point of subarray
        for j in range(i, n):  # Ending point of subarray
            subarray = []
            for k in range(i, j+1):
                subarray.append(arr[k])
            print(subarray)


def print_subsequences(arr):
    print("\nSubsequences:")
    subsequences = []
    
    # Recursive helper function to generate subsequences
    def generate_subsequences(index, subsequence):
        if index == len(arr):
            subsequences.append(subsequence)
            return
        # Exclude the current element
        generate_subsequences(index + 1, subsequence)
        # Include the current element
        generate_subsequences(index + 1, subsequence + [arr[index]])

    generate_subsequences(0, [])
    for subseq in subsequences:
        print(subseq)


def print_subsets(arr):
    print("\nSubsets:")
    n = len(arr)
    subsets = []
    
    # Recursive helper function to generate subsets
    def generate_subsets(index, subset):
        if index == n:
            subsets.append(subset)
            return
        # Exclude the current element
        generate_subsets(index + 1, subset)
        # Include the current element
        generate_subsets(index + 1, subset + [arr[index]])

    generate_subsets(0, [])
    for subset in subsets:
        print(subset)


# Example usage
arr = [1, 2, 3]

print_subarrays(arr)    # Subarrays must be contiguous
print_subsequences(arr) # Subsequences are non-contiguous but in the same order
print_subsets(arr)      # Subsets are combinations without order constraint

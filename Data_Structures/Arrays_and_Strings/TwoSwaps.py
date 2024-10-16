# Two Swaps

# https://www.geeksforgeeks.org/problems/two-swaps--155623/1

# Problem Statement
# Given a permutation of some of the first natural numbers in an array arr[], determine if the array can be sorted in exactly two swaps. 
# A swap can involve the same pair of indices twice.
# Return true if it is possible to sort the array with exactly two swaps, otherwise return false.

# Examples:

# Input: arr = [4, 3, 2, 1]
# Output: true
# Explanation: First, swap arr[0] and arr[3]. The array becomes [1, 3, 2, 4]. Then, swap arr[1] and arr[2]. The array becomes [1, 2, 3, 4], which is sorted.

# Input: arr = [4, 3, 1, 2]
# Output: false
# Explanation: It is not possible to sort the array with exactly two swaps.

# Constraints:
# 1 ≤ arr.size() ≤ 106
# 1 ≤ arr[i] ≤ arr.size()

class Solution:
    def swap_element(self, arr, idx):
        """
        Swap the element at index 'idx' with the element in the array that 
        should have been at that position.
        
        Parameters:
        arr: List of integers to be checked and swapped if necessary.
        idx: The current index where the element is misplaced.
        """
        val = idx + 1  # The correct value that should be at index 'idx'.
        target = arr.index(val)  # Find the index of the correct value in the array.
        # Swap the misplaced element with the correct one.
        arr[idx], arr[target] = arr[target], arr[idx]

    def checkSorted(self, arr):
        """
        Check if the array can be sorted by at most one or two swaps.
        
        Parameters:
        arr: List of integers to be checked.
        
        Returns:
        True if the array can be sorted with 0 or 2 swaps, False otherwise.
        """
        misplaced = 0  # Counter to track how many elements are out of place.

        # Loop through the array and check if each element is in its correct position.
        for idx, val in enumerate(arr):
            if val != idx + 1:  # If the element is not in the correct position.
                misplaced += 1  # Increment the misplaced count.
                self.swap_element(arr, idx)  # Try to correct the misplaced element.
            
            # If more than 2 elements are misplaced, return False (can't be fixed with 2 swaps).
            if misplaced > 2:
                return False
        
        # If 0 or 2 elements were misplaced, the array can be sorted with 0 or 2 swaps.
        if misplaced in (0, 2):
            return True
        
        return False  # Otherwise, return False.
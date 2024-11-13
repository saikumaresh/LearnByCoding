# Meeting Rooms
# Difficulty: Easy

# https://www.geeksforgeeks.org/problems/attend-all-meetings/1

# Problem Statement
# Given an array arr[][] such that arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting, 
# the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.
# Note: A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.

# Examples:

# Input: arr[][] = [[1, 4], [10, 15], [7, 10]]
# Output: true
# Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings.

# Input: arr[][] = [[2, 4], [9, 12], [6, 10]]
# Output: false
# Explanation: It is not possible to attend the second and third meetings simultaneously.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 2*106

# Expected Complexities
# Time Complexity: O(n log n)Auxiliary Space: O(n)

class Solution:
    def canAttend(self, arr):
        """
        Determines if a person can attend all meetings without any overlap.
        
        Parameters:
        arr (List of Tuples): A list where each tuple represents a meeting interval (start, end).
        
        Returns:
        bool: True if the person can attend all meetings without any conflicts, False otherwise.
        """
        # If there's only one meeting, it can always be attended without conflict
        if len(arr) == 1:
            return True
        
        # Step 1: Sort the meetings by their start time.
        # This allows us to check consecutive meetings for overlaps.
        arr.sort()
        
        # Step 2: Track the end time of the current meeting
        # Set the current_end to the end time of the first meeting
        current_end = arr[0][1]
        
        # Step 3: Iterate over the remaining meetings to check for overlaps
        for i in range(1, len(arr)):
            # If the start time of the current meeting is less than the end time of the previous meeting
            # there's an overlap, so the person cannot attend all meetings
            if arr[i][0] < current_end:
                return False
            # Update the current_end to the end time of the current meeting
            current_end = arr[i][1]
        
        # If no overlaps are found, return True
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Overlapping meetings
    arr1 = [(1, 3), (2, 4), (5, 7)]
    # Explanation: The meetings (1, 3) and (2, 4) overlap.
    print("Test Case 1:", solution.canAttend(arr1))  # Expected output: False

    # Test Case 2: Non-overlapping meetings
    arr2 = [(1, 2), (3, 4), (5, 6)]
    # Explanation: All meetings are separated with no overlap.
    print("Test Case 2:", solution.canAttend(arr2))  # Expected output: True

    # Test Case 3: Single meeting
    arr3 = [(1, 5)]
    # Explanation: Only one meeting, so no overlap is possible.
    print("Test Case 3:", solution.canAttend(arr3))  # Expected output: True

    # Test Case 4: Edge case with overlapping at boundaries
    arr4 = [(1, 5), (5, 10)]
    # Explanation: Meetings end and start at the same time, no overlap.
    print("Test Case 4:", solution.canAttend(arr4))  # Expected output: True

    # Test Case 5: Large gap between meetings
    arr5 = [(1, 2), (10, 20)]
    # Explanation: Large gap between meetings, so no overlap.
    print("Test Case 5:", solution.canAttend(arr5))  # Expected output: True

    # Test Case 6: Multiple overlapping meetings
    arr6 = [(1, 5), (4, 8), (8, 10)]
    # Explanation: Meetings (1,5) and (4,8) overlap.
    print("Test Case 6:", solution.canAttend(arr6))  # Expected output: False

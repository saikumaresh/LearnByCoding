# Merge Overlapping Intervals

# Problem Description
# Given a collection of intervals, merge all overlapping intervals.

# Problem Constraints
# 1 <= Total number of intervals <= 100000.

# Input Format
# First argument is a list of intervals.

# Output Format
# Return the sorted list of intervals after merging all the overlapping intervals.

# Example Input
# Input 1:
# [1,3],[2,6],[8,10],[15,18]

# Example Output
# Output 1:
# [1,6],[8,10],[15,18]

# Example Explanation

# Explanation 1:
# Merge intervals [1,3] and [2,6] -> [1,6].
# so, the required answer after merging is [1,6],[8,10],[15,18].
# No more overlapping intervals present.

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Intervals
    def merge(self, intervals):
        """
        Merges overlapping intervals from the given list.

        Parameters:
        intervals (List[Interval]): A list of Interval objects.

        Returns:
        List[Interval]: A list of merged Interval objects.
        """
        n = len(intervals)
        if n <= 1:  # If there are 0 or 1 intervals, return as is
            return intervals
        
        # Sort intervals by their start times
        intervals.sort(key=lambda x: x.start)
        
        i = 0
        while i < n - 1:
            first = intervals[i]
            second = intervals[i + 1]
            
            # Check if intervals overlap
            if second.start <= first.end:
                # Merge the intervals
                second.start = min(first.start, second.start)
                second.end = max(first.end, second.end)
                intervals.pop(i)  # Remove the merged interval
                n -= 1
            else:
                i += 1  # Move to the next interval
        
        return intervals

# Helper function to create intervals from a list of tuples and print results
def test_merge(interval_tuples):
    intervals = [Interval(s, e) for s, e in interval_tuples]
    solution = Solution()
    merged_intervals = solution.merge(intervals)
    return [(interval.start, interval.end) for interval in merged_intervals]

# Test cases
print("Test Case 1:", test_merge([(1, 3), (2, 6), (8, 10), (15, 18)]))
# Expected Output: [(1, 6), (8, 10), (15, 18)]

print("Test Case 2:", test_merge([(1, 4), (4, 5)]))
# Expected Output: [(1, 5)]

print("Test Case 3:", test_merge([(6, 8), (1, 9), (2, 4), (4, 7)]))
# Expected Output: [(1, 9)]

print("Test Case 4:", test_merge([(1, 3)]))
# Expected Output: [(1, 3)] (Only one interval, no merging needed)

print("Test Case 5:", test_merge([]))
# Expected Output: [] (No intervals)

print("Test Case 6:", test_merge([(1, 3), (2, 4), (5, 7), (6, 8)]))
# Expected Output: [(1, 4), (5, 8)]
# Merge Intervals

# Problem Description
# You have a set of non-overlapping intervals. You are given a new interval [start, end], 
# insert this new interval into the set of intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Problem Constraints
# 0 <= |intervals| <= 105

# Input Format
# First argument is the vector of intervals
# second argument is the new interval to be merged

# Output Format
# Return the vector of intervals after merging

# Example Input

# Input 1:
# Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
# Input 2:
# Given intervals [1, 3], [6, 9] insert and merge [2, 6] .

# Example Output

# Output 1:

#  [ [1, 5], [6, 9] ]
# Output 2:
#  [ [1, 9] ]

# Example Explanation

# Explanation 1:
# (2,5) does not completely merge the given intervals
# Explanation 2:
# (2,6) completely merges the given intervals

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals: List of Intervals (each Interval has start and end)
    # @param newInterval: A single new Interval that we need to insert
    # @return: A list of intervals after inserting the new interval and merging if necessary
    
    def insert(self, intervals, newInterval):
        # Step 1: Handle the case where the new interval start is greater than the end
        # Ensure that the new interval is in the correct order
        if newInterval.start > newInterval.end:
            newInterval.start, newInterval.end = newInterval.end, newInterval.start 
        
        n = len(intervals)  # Get the number of intervals in the input list
        updatedIntervals = []  # Initialize an empty list to store the result
        
        # Step 2: Iterate through the intervals
        for i in range(n):
            current_interval = intervals[i]
            
            # Step 2.1: If the new interval is completely to the right of the current interval
            if newInterval.start > current_interval.end:
                updatedIntervals.append(current_interval)  # No overlap, just append the current interval
                
            # Step 2.2: If the new interval is completely to the left of the current interval
            elif newInterval.end < current_interval.start:
                updatedIntervals.append(newInterval)  # No overlap, insert new interval and continue with the rest
                updatedIntervals.extend(intervals[i:])  # Add the remaining intervals
                return updatedIntervals  # Return the updated intervals list
                
            # Step 2.3: If the new interval overlaps with the current interval
            else:
                # Merge the new interval with the current interval
                newInterval.start = min(current_interval.start, newInterval.start)  # Take the earliest start
                newInterval.end = max(current_interval.end, newInterval.end)  # Take the latest end
        
        # Step 3: Add the merged or new interval to the list after processing all intervals
        updatedIntervals.append(newInterval)
        
        # Step 4: Return the final list of intervals
        return updatedIntervals


# Test cases to validate the solution
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: New interval doesn't overlap with any existing interval
    intervals1 = [Interval(1, 3), Interval(6, 9)]
    newInterval1 = Interval(2, 5)
    # Expected output: [Interval(1, 5), Interval(6, 9)]
    print("Test Case 1 Output:", [f"({i.start}, {i.end})" for i in solution.insert(intervals1, newInterval1)])

    # Test Case 2: New interval completely overlaps with an existing interval
    intervals2 = [Interval(1, 3), Interval(6, 9)]
    newInterval2 = Interval(2, 5)
    # Expected output: [Interval(1, 5), Interval(6, 9)]
    print("Test Case 2 Output:", [f"({i.start}, {i.end})" for i in solution.insert(intervals2, newInterval2)])

    # Test Case 3: New interval is to the left of existing intervals
    intervals3 = [Interval(1, 3), Interval(6, 9)]
    newInterval3 = Interval(0, 0)
    # Expected output: [Interval(0, 0), Interval(1, 3), Interval(6, 9)]
    print("Test Case 3 Output:", [f"({i.start}, {i.end})" for i in solution.insert(intervals3, newInterval3)])

    # Test Case 4: New interval is to the right of existing intervals
    intervals4 = [Interval(1, 3), Interval(6, 9)]
    newInterval4 = Interval(10, 12)
    # Expected output: [Interval(1, 3), Interval(6, 9), Interval(10, 12)]
    print("Test Case 4 Output:", [f"({i.start}, {i.end})" for i in solution.insert(intervals4, newInterval4)])

    # Test Case 5: New interval fully overlaps multiple existing intervals
    intervals5 = [Interval(1, 3), Interval(6, 9)]
    newInterval5 = Interval(2, 6)
    # Expected output: [Interval(1, 9)]
    print("Test Case 5 Output:", [f"({i.start}, {i.end})" for i in solution.insert(intervals5, newInterval5)])

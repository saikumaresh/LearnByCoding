# Meeting Point

# https://www.interviewbit.com/problems/meeting-point/

# Problem Description
# You and your friend decided to meet at one of the N locations in the town. The ith location is located at (A[i][0], A[i][1]) on an infinite 2D grid.
# You want to meet at the location with minimum x-coordinate. If there are multiple such locations, choose the one with the minimum y-coordinate.
# If there are still multiple such locations, you can choose any of them.
# Your friend wants to meet at the location with minimum y-coordinate. If there are multiple such locations, choose the one with the minimum x-coordinate. 
# If there are still multiple such locations, you can choose any of them.   
# Now, you need to find the distance between these two locations. The distance between (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2| where |a| is the absolute value of a.


# Problem Constraints
# 2 <= N <= 2 x 105 
# 1 <= A[i][0], A[i][1] <= 109
# There maybe multiple locations with the same coordinates.

# Input Format
# The first and only argument contains an integer array A of size N x 2.

# Output Format
# Return a single integer, the answer to the problem.

# Example Input

#   Input 1:
#   A : 
#   [
#     [10, 10]
#     [2, 9]
#     [4, 6]
#   ]

# Input 2:
#   A : 
#   [
#     [1, 3]
#     [7, 5]
#   ]

# Example Output
#   Output 1:
#   5
# Output 2:
#   0


# Example Explanation

#   Explanation 1:
#   You will meet at (2, 9). Friend wants to meet at (4, 6). Distance between them is |2 - 4| + |9 - 6| = 5.
# Explanation 2:
#   (1, 3) has both minimum x and y coordinate.


class Solution:
    # @param A : list of lists of integers
    # @return an integer
    def solve(self, A):
        # Step 1: Find the location with minimum x-coordinate (and minimum y-coordinate in case of a tie)
        min_x = min(A, key=lambda loc: (loc[0], loc[1]))

        # Step 2: Find the location with minimum y-coordinate (and minimum x-coordinate in case of a tie)
        min_y = min(A, key=lambda loc: (loc[1], loc[0]))

        # Step 3: Calculate Manhattan distance between the two locations
        return abs(min_x[0] - min_y[0]) + abs(min_x[1] - min_y[1])

# Example run
sol = Solution()
locations = [[10, 10], [2, 9], [4, 6]]
result = sol.solve(locations)
print(f"The distance between the meeting locations is {result}")
# Output: The distance between the meeting locations is 5

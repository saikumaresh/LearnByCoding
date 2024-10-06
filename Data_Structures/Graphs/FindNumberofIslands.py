# Find the number of islands

# https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1

# Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of '0's (Water) and '1's(Land). Find the number of islands.
# Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., 
# in all 8 directions.

# Examples:

# Input: grid = [[0,1],[1,0],[1,1],[1,0]]
# Output: 1
# Explanation:
# The grid is-
# All lands are connected.

# Input: grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
# Output: 2
# Expanation:
# The grid is-
# There are two islands :- one is colored in "blue" and other in "red".

# Expected Time Complexity: O(n*m)
# Expected Space Complexity: O(n*m)

# Constraints:
# 1 ≤ n, m ≤ 500
# grid[i][j] = {'0', '1'}

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
    
        # Dimensions of the grid
        n, m = len(grid), len(grid[0])
    
        # Directions for 8 possible movements (right, left, up, down, and 4 diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
        # Stack-based DFS function to explore the connected lands
        def dfs_iterative(x, y):
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if cx < 0 or cx >= n or cy < 0 or cy >= m or grid[cx][cy] == 0:
                    continue
    
                # Mark the current cell as visited by setting it to 0 (visited)
                grid[cx][cy] = 0
    
                # Explore all 8 directions
                for dx, dy in directions:
                    stack.append((cx + dx, cy + dy))
    
        # Main logic to count islands
        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # Found an unvisited land
                    island_count += 1  # New island
                    dfs_iterative(i, j)  # Explore the entire island
    
        return island_count

### Code Breakdown:

# 1. Check for Empty Grid:  
#    If the input `grid` is empty, there are no islands, so we return `0`.

# 2. Grid Dimensions:  
#    `n` is the number of rows, and `m` is the number of columns in the grid.

# 3. Define Directions:  
#    To explore all possible adjacent cells, we define 8 directions for movement:  
#    - Up, Down, Left, Right: `(-1, 0)`, `(1, 0)`, `(0, -1)`, `(0, 1)`
#    - 4 Diagonals: `(-1, -1)`, `(-1, 1)`, `(1, -1)`, `(1, 1)`

# 4. DFS Function:  
#    The `dfs_iterative` function explores all the connected land cells from a starting point `(x, y)`:
#    - Stack Initialization: It uses a stack, starting with the given cell `(x, y)`.
#    - While Loop: As long as the stack is not empty, the loop continues.
#    - Boundary Check: If the current cell `(cx, cy)` is out of bounds or already visited (`grid[cx][cy] == 0`), we skip to the next cell.

# 5. Mark as Visited:  
#    If the cell is within bounds and is land (`1`), we mark it as visited by setting `grid[cx][cy]` to `0`.

# 6. Explore All Directions:  
#    For each direction, we add the neighboring cell `(cx + dx, cy + dy)` to the stack for further exploration.

# 7. Counting Islands:
#    - Traverse the Grid: We iterate through each cell in the grid.
#    - Found New Island: If the cell is land (`1`), we increase the `island_count` by `1`, as we have found a new island.
#    - Explore the Island: We call `dfs_iterative(i, j)` to mark all connected land cells as visited.

# 8. Return Result:  
#    Finally, we return the total count of islands found.

# This approach ensures that we visit each cell at most once, achieving the desired time complexity of `O(n*m)`.
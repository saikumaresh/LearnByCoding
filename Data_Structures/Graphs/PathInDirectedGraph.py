# Path in Directed Graph

# Problem Description
# Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that there is a edge directed from node
# B[i][0] to node B[i][1].
# Find whether a path exists from node 1 to node A.
# Return 1 if path exists else return 0.
# NOTE:
# There are no self-loops in the graph.
# There are no multiple edges between two nodes.
# The graph may or may not be connected.
# Nodes are numbered from 1 to A.
# Your solution will run on multiple test cases. If you are using global variables make sure to clear them.

# Problem Constraints
# 2 <= A <= 105
# 1 <= M <= min(200000,A*(A-1))
# 1 <= B[i][0], B[i][1] <= A

# Input Format
# The first argument given is an integer A representing the number of nodes in the graph.
# The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

# Output Format
# Return 1 if path exists between node 1 to node A else return 0.

# Example Input
# Input 1:
#  A = 5
#  B = [  [1, 2] 
#         [4, 1] 
#         [2, 4] 
#         [3, 4] 
#         [5, 2] 
#         [1, 3] ]

# Input 2:
#  A = 5
#  B = [  [1, 2]
#         [2, 3] 
#         [3, 4] 
#         [4, 5] ]

# Example Output
# Output 1:
#  0
# Output 2:
#  1

# Example Explanation
# Explanation 1:
#  The given doens't contain any path from node 1 to node 5 so we will return 0.
# Explanation 2:
#  Path from node1 to node 5 is ( 1 -> 2 -> 3 -> 4 -> 5 ) so we will return 1.

class Graph:
    def __init__(self, edges):
        """
        Initializes a directed graph from the given list of edges.

        :param edges: List of pairs representing directed edges in the graph.
        """
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            # Populate the adjacency list
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]


class Solution:
    # @param A : integer (target node)
    # @param B : list of list of integers (edges)
    # @return an integer (1 if target is reachable, 0 otherwise)
    def solve(self, A, B):
        """
        Determines if there exists a path from node 1 to node A in a directed graph.

        :param A: The target node.
        :param B: List of directed edges.
        :return: 1 if there's a path from node 1 to A, otherwise 0.
        """
        # Step 1: Create the graph using the provided edges
        graph = Graph(B)
        
        # Step 2: Initialize BFS
        queue = [1]  # Start from node 1
        visited = set()  # To keep track of visited nodes
        
        while queue:
            current = queue.pop(0)  # Dequeue the next node
            
            # Check if we reached the target node
            if current == A:
                return 1  # Path found
            
            visited.add(current)  # Mark the current node as visited
            
            # Add neighbors to the queue
            if current in graph.graph_dict: 
                for neighbor in graph.graph_dict[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return 0  # Path not found


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (4, [[1, 2], [2, 3], [3, 4]]),  # Simple path: 1 → 2 → 3 → 4
        (4, [[1, 2], [2, 3]]),  # No path to 4
        (3, [[1, 2], [2, 3], [1, 3]]),  # Multiple paths to 3
        (1, []),  # Single node with no edges (self-reachable)
        (5, [[1, 2], [2, 3], [3, 4], [4, 5]]),  # Long path: 1 → 2 → 3 → 4 → 5
        (5, [[1, 2], [3, 4], [4, 5]]),  # Disconnected graph, no path to 5
        (6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]),  # Path exists to 6
        (6, [[1, 3], [3, 5], [5, 6]]),  # Skips intermediate nodes, still connected
        (6, [[1, 2], [2, 3], [4, 5], [5, 6]]),  # Disconnected graph
    ]

    for target, edges in test_cases:
        result = solution.solve(target, edges)
        print(f"Target: {target}, Edges: {edges} → Path Exists? {result}")

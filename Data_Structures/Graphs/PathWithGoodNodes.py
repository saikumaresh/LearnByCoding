# Path with good nodes!

# Problem Description
# Given a tree with N nodes labelled from 1 to N.
# Each node is either good or bad denoted by binary array A of size N where if A[i] is 1 then ithnode is good else if A[i] is 
# 0 then ith node is bad.
# Also the given tree is rooted at node 1 and you need to tell the number of root to leaf paths in the tree that contain not more than C good nodes.
# NOTE:
# Each edge in the tree is bi-directional.

# Problem Constraints
# 2 <= N <= 105
# A[i] = 0 or A[i] = 1
# 0 <= C <= N

# Input Format
# First argument is an binary integer array A of size N.
# Second argument is a 2-D array B of size (N-1) x 2 denoting the edge of the tree.
# Third argument is an integer C.

# Output Format
# Return an integer denoting the number of root to leaf paths in the tree that contain not more than C good nodes.

# Example Input

# Input 1:
#  A = [0, 1, 0, 1, 1, 1]
#  B = [  [1, 2]
#         [1, 5]
#         [1, 6]
#         [2, 3]
#         [2, 4]
#      ]
#  C = 1

# Example Output
# Output 1:
#  3

# Example Explanation
# Explanation 1:
#  Path (1 - 2 - 3) and (1 - 5) and (1 - 6) are the paths which contain atmost C nodes.

def dfs(graph, A, visited, C, curr, good_count, ans):
    """
    Depth First Search to traverse the graph and count valid leaf nodes.

    :param graph: Adjacency list representation of the tree.
    :param A: List indicating if a node is "good" (1) or not (0).
    :param visited: List to track visited nodes.
    :param C: Maximum allowed "good" nodes in a path.
    :param curr: Current node being visited.
    :param good_count: Remaining count of "good" nodes allowed on the path.
    :param ans: List to store the count of valid leaf nodes.
    """
    if visited[curr]:
        return  # If the node is already visited, stop further exploration.

    visited[curr] = True

    # If the current node is "good", decrement the remaining good node count.
    if A[curr] == 1:
        good_count -= 1  

    # If the remaining good node count becomes negative, terminate the path.
    if good_count < 0:
        return

    is_leaf = True  # Assume the current node is a leaf.

    # Explore all neighbors of the current node.
    for neighbor in graph[curr]:
        if not visited[neighbor]:
            is_leaf = False  # If there are unvisited neighbors, it's not a leaf.
            dfs(graph, A, visited, C, neighbor, good_count, ans)

    # If it's a leaf node, increment the valid leaf count.
    if is_leaf:
        ans[0] += 1


class Solution:
    def solve(self, A, B, C):
        """
        Solves the problem of counting valid leaf nodes in a tree.

        :param A: List of integers (1 for "good", 0 for "not good").
        :param B: List of edges in the tree (1-indexed).
        :param C: Maximum allowed "good" nodes in a path.
        :return: Number of valid leaf nodes.
        """
        n = len(A)
        
        # Build the adjacency list for the graph (convert 1-indexed edges to 0-indexed).
        graph = [[] for _ in range(n)]
        for u, v in B:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        visited = [False] * n  # To track visited nodes.
        ans = [0]  # To count valid leaf nodes.

        # Start DFS from the root node (0-indexed).
        dfs(graph, A, visited, C, 0, C, ans)

        return ans[0]


# Testing the function
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    A = [0, 1, 0, 1, 1]
    B = [(1, 2), (1, 3), (3, 4), (3, 5)]
    C = 1
    print("Test Case 1 Output:", solution.solve(A, B, C))  # Expected Output: 2

    # Test case 2
    A = [1, 0, 1, 0, 1, 0]
    B = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    C = 1
    print("Test Case 2 Output:", solution.solve(A, B, C))  # Expected Output: 3

    # Test case 3
    A = [1, 1, 1, 0, 0]
    B = [(1, 2), (2, 3), (3, 4), (3, 5)]
    C = 2
    print("Test Case 3 Output:", solution.solve(A, B, C))  # Expected Output: 1

    # Test case 4
    A = [0, 0, 0, 1, 0, 1, 0]
    B = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    C = 2
    print("Test Case 4 Output:", solution.solve(A, B, C))  # Expected Output: 4

    # Test case 5
    A = [1]
    B = []
    C = 0
    print("Test Case 5 Output:", solution.solve(A, B, C))  # Expected Output: 0

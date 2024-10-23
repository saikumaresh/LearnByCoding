# Find the Sum of Last N nodes of the Linked List

# https://www.geeksforgeeks.org/problems/find-the-sum-of-last-n-nodes-of-the-linked-list/1

# Problem Statement
# Given a single linked list, calculate the sum of the last n nodes.
# Note: It is guaranteed that n <= number of nodes.

# Examples:

# Input: Linked List: 5->9->6->3->4->10, n = 3
# Output: 17
# Explanation: The sum of the last three nodes in the linked list is 3 + 4 + 10 = 17.

# Input: Linked List: 1->2, n = 2
# Output: 3
# Explanation: The sum of the last two nodes in the linked list is 2 + 1 = 3.

# Constraints:
# 1 <= number of nodes, n <= 105
# 1 <= node->data <= 103

# Node Class to define each node in the linked list
class Node:
    def __init__(self, data):
        # Initialize node with given data and next pointer as None
        self.data = data
        self.next = None

class Solution:
    def sumOfLastN_Nodes(self, head, n):
        """
        This function returns the sum of the last 'n' nodes in a linked list.
        
        Arguments:
        head -- the head node of the linked list
        n    -- the number of last nodes to sum
        
        Returns:
        The sum of the last 'n' nodes.
        """
        # List to store the last 'n' nodes
        result = []
        
        # Traverse the linked list
        while head:
            # If the length of the result list exceeds 'n', remove the first element
            if len(result) >= n:
                result.pop(0)
            # Add the current node's data to the result list
            result.append(head.data)
            # Move to the next node
            head = head.next
        
        # Return the sum of the last 'n' nodes
        return sum(result)

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    """
    Creates a linked list from a list of values and returns the head of the list.
    
    Arguments:
    values -- list of integers to be used as node values
    
    Returns:
    The head of the created linked list.
    """
    if not values:
        return None
    head = Node(values[0])  # Create the head node
    current = head  # Keep track of the current node
    # Iterate over the remaining values and create nodes
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Test cases
def test_sumOfLastN_Nodes():
    """
    Test cases for the sumOfLastN_Nodes function.
    """
    solution = Solution()

    # Test Case 1: Linked list with multiple elements, last 3 nodes
    # Linked list: 1 -> 2 -> 3 -> 4 -> 5
    # n = 3 (sum of 3, 4, and 5)
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.sumOfLastN_Nodes(head1, 3)
    print("[1, 2, 3, 4, 5]", "3", result1)  # Expected output: 12

    # Test Case 2: Linked list with only one element
    # Linked list: 10
    # n = 1 (sum of the only node 10)
    head2 = create_linked_list([10])
    result2 = solution.sumOfLastN_Nodes(head2, 1)
    print("[10]", "1", result2)  # Expected output: 10

    # Test Case 3: Linked list with all identical values, last 4 nodes
    # Linked list: 5 -> 5 -> 5 -> 5 -> 5
    # n = 4 (sum of last four nodes: 5 + 5 + 5 + 5)
    head3 = create_linked_list([5, 5, 5, 5, 5])
    result3 = solution.sumOfLastN_Nodes(head3, 4)
    print("[5, 5, 5, 5, 5]", "4", result3)  # Expected output: 20

    # Test Case 4: Linked list with more elements, sum of all nodes
    # Linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
    # n = 7 (sum of all nodes: 1 + 2 + 3 + 4 + 5 + 6 + 7)
    head4 = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    result4 = solution.sumOfLastN_Nodes(head4, 7)
    print("[1, 2, 3, 4, 5, 6, 7]", "7", result4)  # Expected output: 28

    # Test Case 5: Linked list with mixed values, last 2 nodes
    # Linked list: 100 -> 200 -> 300 -> 400
    # n = 2 (sum of last two nodes: 300 + 400)
    head5 = create_linked_list([100, 200, 300, 400])
    result5 = solution.sumOfLastN_Nodes(head5, 2)
    print("[100, 200, 300, 400]", "2", result5)  # Expected output: 700

# Run test cases
test_sumOfLastN_Nodes()

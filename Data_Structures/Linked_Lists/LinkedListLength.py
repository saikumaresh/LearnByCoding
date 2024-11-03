# Is Linked List Length Even?
# Difficulty: BasicAccuracy: 71.58%Submissions: 76K+Points: 1
# Given a linked list, your task is to complete the function isLengthEven() which contains the head of the linked list, and check whether the length of the linked list is even or not. Return true if it is even, otherwise false.

# Examples:

# Input: Linked list: 12->52->10->47->95->0

# Output: true
# Explanation: The length of the linked list is 6 which is even, hence returned true.
# Input: Linked list: 9->4->3

# Output: false
# Explanation: The length of the linked list is 3 which is odd, hence returned false.
# Expected Time Complexity: O(n)
# Expected Auxillary Space: O(1)

# Constraints:
# 1 <= number of nodes <= 105
# 1 <= elements of the linked list <= 105

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Function to check if the linked list length is odd
    def isLengthEven(self, head):
        """
        This function checks the length of a linked list.
        Returns False if the length is even, and True if the length is odd.
        """
        count = 0  # Initialize the count of nodes
        # Traverse through the linked list and count nodes
        while head:
            head = head.next
            count += 1
        # Check if the count is odd or even
        return count % 2 != 0

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Even number of nodes
    head1 = create_linked_list([1, 2, 3, 4])
    print(solution.isLengthEven(head1))  # Output: False, as length is even

    # Test Case 2: Odd number of nodes
    head2 = create_linked_list([1, 2, 3])
    print(solution.isLengthEven(head2))  # Output: True, as length is odd

    # Test Case 3: Single node (odd length)
    head3 = create_linked_list([1])
    print(solution.isLengthEven(head3))  # Output: True, as length is odd

    # Test Case 4: Empty list (even length)
    head4 = create_linked_list([])
    print(solution.isLengthEven(head4))  # Output: False, as length is zero which is even

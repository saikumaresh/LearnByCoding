# Intersection Point in Y Shaped Linked Lists
# Difficulty: Medium

# https://www.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1

# Problem Statement
# Given two singly linked lists, return the point where two linked lists intersect.
# Note: If the linked lists do not merge at any point, return -1.

# Examples:
# Input: Linked list 1: 4->4->4->4->4, Linked list 2: 4->4->4
# Output: 4
# Explanation: From the above image, it is clearly seen that the common part is 4->4 whose starting point is 4.

# Input: Linked list 1: 4->1->8->4->5, Linked List 2: 5->6->1->8->4->5
# Output: 8
# Explanation: From the above image, it is clearly seen that the common part is 8->4->5 whose starting point is 8.

# Input: Linked list 1: 1->2->3, Linked list 2: 4->5->6
# Output: -1
# Explanation: There is no common part, so there is no interaction point.

# Constraints:
# 2 ≤ size of first linkedist + size of second linkedlist ≤ 2*105
# -1000 ≤ data of nodes ≤ 1000

# Expected Complexities
# Time Complexity: O(n + m)Auxiliary Space: O(1)

# Definition for a singly linked list node
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the intersection point in Y-shaped linked lists
def intersetPoint(head1, head2):
    # Initialize pointers for both linked lists
    curr1, curr2 = head1, head2
    
    # Step 1: Count the lengths of both linked lists
    count1, count2 = 0, 0
    while curr1:
        count1 += 1
        curr1 = curr1.next
    while curr2:
        count2 += 1
        curr2 = curr2.next
    
    # Reset pointers to the head of each list to start again
    curr1, curr2 = head1, head2
    
    # Step 2: Align the starting points of the two lists
    # Advance the pointer of the longer list by the length difference
    if count1 > count2:
        for _ in range(count1 - count2):
            curr1 = curr1.next
    else:
        for _ in range(count2 - count1):
            curr2 = curr2.next

    # Step 3: Traverse both lists together to find the intersection
    while curr1 and curr2:
        # If the nodes are the same, we've found the intersection
        if curr1 == curr2:
            return curr1.data
        curr1 = curr1.next
        curr2 = curr2.next
    
    # If no intersection is found, return -1
    return -1

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to attach one list to a node in another list
def attach_lists(head1, head2, intersection_value):
    # Find the intersection node in head1
    curr = head1
    while curr and curr.data != intersection_value:
        curr = curr.next
    
    # Attach head2 to this intersection node
    tail = head2
    while tail.next:
        tail = tail.next
    tail.next = curr

# Create two lists with an intersection
# List 1: 3 -> 6 -> 9 -> 15 -> 30
# List 2: 10 -> 15 -> 30
head1 = create_linked_list([3, 6, 9, 15, 30])
head2 = create_linked_list([10])

# Attach lists to have intersection at node with value 15
attach_lists(head1, head2, 15)

# Test the function
print("Intersection point data:", intersetPoint(head1, head2))  # Expected output: 15

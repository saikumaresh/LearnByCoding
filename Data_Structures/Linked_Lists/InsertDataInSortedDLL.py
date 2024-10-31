# Insert in Sorted way in a Sorted DLL

# https://www.geeksforgeeks.org/problems/insert-in-sorted-way-in-a-sorted-dll/1

# Problem Statement
# Given a sorted doubly linked list and an element x, you need to insert the element x into the correct position in the sorted Doubly linked list(DLL).

# Note: The DLL is sorted in ascending order

# Example:

# Input: LinkedList: 3->5->8->10->12 , x = 9
# Output: 3->5->8->9->10->12
# Explanation: Here node 9 is inserted in the Doubly Linked-List.

# Input: LinkedList: 1->4->10->11 , x = 15
# Output: 1->4->10->11->15

# Constraints:
# 1 <= number of nodes <= 103
# 1 <= node -> data , x <= 104

# Node class for a doubly linked list
class Node:
    def __init__(self, data):
        self.data = data        # The data value of the node
        self.prev = None        # Pointer to the previous node in the list
        self.next = None        # Pointer to the next node in the list

class Solution:
    # Function to insert a node with value x in a sorted doubly linked list
    def sortedInsert(self, head, x):    
        new_node = Node(x)  # Create a new node with the given value

        # Case 1: Insert at the beginning if list is empty or x is less than or equal to head data
        if head is None or head.data >= x:
            new_node.next = head  # Point new node's next to the current head
            if head:  # If list is not empty, set head's previous to new_node
                head.prev = new_node
            return new_node  # New node becomes the new head of the list
        
        # Case 2: Traverse the list to find the correct insertion position
        current = head
        while current.next and current.next.data < x:
            current = current.next  # Move forward in the list

        # Insert new_node after the 'current' node
        new_node.next = current.next  # Connect new_node's next to current's next
        if current.next:  # If new_node is not inserted at the end, set the previous link
            current.next.prev = new_node
        new_node.prev = current  # Set new_node's previous link to current
        current.next = new_node  # Set current's next to new_node

        return head  # Return the head of the updated list

# Helper function to print the doubly linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Helper function to create a doubly linked list from a list of values
def create_doubly_linked_list(values):
    head = None
    for value in values:
        new_node = Node(value)
        if head is None:
            head = new_node
        else:
            tail.next = new_node
            new_node.prev = tail
        tail = new_node
    return head

# Test Case 1: Insert into an empty list
head = None
solution = Solution()
head = solution.sortedInsert(head, 5)
print("Expected: 5")
print("Output:", end=" ")
print_list(head)

# Test Case 2: Insert at the beginning of the list
head = create_doubly_linked_list([10, 20, 30])
head = solution.sortedInsert(head, 5)
print("Expected: 5 10 20 30")
print("Output:", end=" ")
print_list(head)

# Test Case 3: Insert in the middle of the list
head = create_doubly_linked_list([10, 20, 30])
head = solution.sortedInsert(head, 25)
print("Expected: 10 20 25 30")
print("Output:", end=" ")
print_list(head)

# Test Case 4: Insert at the end of the list
head = create_doubly_linked_list([10, 20, 30])
head = solution.sortedInsert(head, 35)
print("Expected: 10 20 30 35")
print("Output:", end=" ")
print_list(head)

# Test Case 5: Insert duplicate value in the list
head = create_doubly_linked_list([10, 20, 30])
head = solution.sortedInsert(head, 20)
print("Expected: 10 20 20 30")
print("Output:", end=" ")
print_list(head)

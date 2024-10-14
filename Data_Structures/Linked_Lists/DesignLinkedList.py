# Design Linked list


# Problem Description
# Given a matrix A of size Nx3 representing operations. Your task is to design the linked list based on these operations.
# There are four types of operations:
# 0 x -1: Add a node of value x before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# 1 x -1: Append a node of value x to the last element of the linked list.
# 2 x index: Add a node of value x before the indexth node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# 3 index -1: Delete the indexth node in the linked list, if the index is valid.
# A[i][0] represents the type of operation.
# A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.
# Note: Indexing is 0 based.

# Problem Constraints
# 1 <= Number of operations <= 1000
# 1 <= All node values <= 109

# Input Format
# The only argument given is matrix A.

# Output Format
# Return the pointer to the starting of the linked list.

# Example Input
# Input 1:
#     A = [   [0, 1, -1]
#             [1, 2, -1]
#             [2, 3, 1]   ]
# Input 2:
#     A = [   [0, 1, -1]
#             [1, 2, -1]
#             [2, 3, 1]
#             [0, 4, -1]
#             [3, 1, -1]
#             [3, 2, -1]  ]


# Example Output
# Output 1:
#     1->3->2->NULL
# Output 2:
#     4->3->NULL

class Node:
    def __init__(self, value):
        """
        Initialize a new node with a value and a pointer to the next node.
        
        :param value: The integer value stored in the node
        """
        self.val = value  # Store the value
        self.next = None  # Initialize the next pointer as None

class Solution:
    def __init__(self):
        """
        Initialize the Solution class with the head of the linked list set to None.
        """
        self.head = None  # The head of the linked list

    def insert_node(self, position, value):
        """
        Insert a new node with the given value at the specified position.
        
        :param position: The position where the node should be inserted. 
                         If position == 1, insert at the head.
                         If position == -1, append the node at the end.
        :param value: The integer value to be inserted into the new node
        """
        new_node = Node(value)  # Create a new node with the given value
        
        if position == 1:
            # Insert at the head of the linked list
            new_node.next = self.head
            self.head = new_node
        elif position == -1:
            # Append the node at the end of the list
            if self.head is None:
                # If the list is empty, set the head to the new node
                self.head = new_node
            else:
                # Traverse to the end of the list
                current = self.head
                while current.next:
                    current = current.next
                # Append the new node
                current.next = new_node
        else:
            # Insert at the specified position
            if self.head is None:
                # If the list is empty, return (do nothing)
                return
            current = self.head
            # Traverse the list to find the node just before the insertion point
            for _ in range(position - 2):
                if current.next is None:
                    return  # If the position is out of bounds, do nothing
                current = current.next
            # Insert the new node in the correct position
            new_node.next = current.next
            current.next = new_node

    def delete_node(self, position):
        """
        Delete the node at the specified position.
        
        :param position: The position of the node to delete (1-based index)
        """
        if self.head is None:
            # If the list is empty, there's nothing to delete
            return
        
        if position == 1:
            # If the position is the head, update the head to the next node
            self.head = self.head.next
        else:
            # Traverse the list to find the node just before the one to be deleted
            current = self.head
            for _ in range(position - 2):
                if current is None or current.next is None:
                    return  # If the position is out of bounds, do nothing
                current = current.next
            if current.next:
                # If the next node exists, bypass the node to be deleted
                current.next = current.next.next

    def solve(self, A):
        """
        Process a list of operations on the linked list.
        
        :param A: A list of operations where each operation is represented as:
                  - [0, value]: Insert value at the head (position 1).
                  - [1, value]: Insert value at the end.
                  - [2, value, index]: Insert value at index (0-based).
                  - [3, index]: Delete the node at index (0-based).
        :return: The head of the linked list after all operations are performed
        """
        for operation in A:
            if operation[0] in [0, 1, 2]:
                value = operation[1]
                if operation[0] == 0:
                    # Insert at the head (position 1)
                    position = 1
                elif operation[0] == 1:
                    # Append at the end (position -1)
                    position = -1
                else:
                    # Insert at a specific index (convert 0-based index to 1-based)
                    position = operation[2] + 1
                self.insert_node(position, value)
            else:
                # Delete operation (convert 0-based index to 1-based)
                self.delete_node(operation[1] + 1)
        return self.head

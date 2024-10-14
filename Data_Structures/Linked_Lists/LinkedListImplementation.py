# Linked-List Implementation

# Problem Description
# Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes - an integer value and a pointer to the next node.
# It should support the following operations:
# insert_node(position, value) - To insert the input value at the given position in the linked list.
# delete_node(position) - Delete the value at the given position from the linked list.
# print_ll() - Print the entire linked list, such that each element is followed by a single space (no trailing spaces).

# Note:
# If an input position does not satisfy the constraint, no action is required.
# Each print query has to be executed in a new line.


# Problem Constraints
# 1 <= value <= 105
# 1 <= position <= n where, n is the size of the linked-list.



# Input Format
# First line contains an integer denoting number of cases, let's say t. Next t line denotes the cases.


# Output Format

# When there is a case of print_ll(), Print the entire linked list, such that each element is followed by a single space.
# There should not be any trailing space.
# NOTE: You don't need to return anything.


# Example Input

# Input 1:
# 5
# i 1 23
# i 2 24
# p
# d 1
# p

# Input 2:
# 3
# i 1 54
# d 10
# p


# Example Output

# Output 1:
# 23 24
# 24

# Output 2:
# 54


# Example Explanation

# Explanation 1:
# After first two cases linked list contains two elements 23 and 24.
# At third case print: 23 24.
# At fourth case delete value at first position, only one element left 24.
# At fifth case print: 24.

# Explanation 2:
# After the first case,  linked list contains: 54
# At second case delete value at 10th position,  
# Since the position is higher than the length of the linkedlist. 
# It does not satisfy the constraint, So no action is required.
# At third case print: 54.


# Define the head pointer globally
head = None

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

def insert_node(position, value):
    global head
    new_node = Node(value)
    
    # Case 1: Insertion at the head (position 1)
    if position == 1:
        new_node.next = head
        head = new_node
        return
    
    # Case 2: Insertion at any other position
    current = head
    for i in range(1, position - 1):
        if current is None:
            return  # If position is out of bounds, do nothing
        current = current.next
    
    if current is None:
        return  # If we reach a None before reaching the required position, do nothing
    
    new_node.next = current.next
    current.next = new_node

def delete_node(position):
    global head
    
    # Case 1: Deletion at the head (position 1)
    if position == 1:
        if head is not None:
            head = head.next
        return
    
    # Case 2: Deletion at any other position
    current = head
    for i in range(1, position - 1):
        if current is None or current.next is None:
            return  # If position is out of bounds, do nothing
        current = current.next
    
    if current is None or current.next is None:
        return  # If position is out of bounds, do nothing
    
    current.next = current.next.next

def print_ll():
    global head
    current = head
    output = []
    
    while current is not None:
        output.append(str(current.data))
        current = current.next
    
    print(" ".join(output))

# Driver code to handle multiple test cases
t = int(input())  # Number of operations

for _ in range(t):
    query = input().split()
    
    if query[0] == 'i':  # Insert operation
        position = int(query[1])
        value = int(query[2])
        insert_node(position, value)
    
    elif query[0] == 'd':  # Delete operation
        position = int(query[1])
        delete_node(position)
    
    elif query[0] == 'p':  # Print operation
        print_ll()
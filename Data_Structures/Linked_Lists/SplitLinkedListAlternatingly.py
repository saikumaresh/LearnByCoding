# Split Linked List Alternatingly

# https://www.geeksforgeeks.org/problems/split-singly-linked-list-alternatingly/1

# Given a singly linked list's head. Your task is to complete the function alternatingSplitList() that splits the given linked list into two smaller lists. 
# The sublists should be made from alternating elements from the original list.
# Note: 
# The sublist should be in the order with respect to the original list.
# Your have to return an array containing the both sub-linked lists.

# Examples:
# Input: LinkedList = 0->1->0->1->0->1
# Output: 0->0->0 , 1->1->1
# Explanation: After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.

# Input: LinkedList = 2->5->8->9->6
# Output: 2->8->6 , 5->9
# Explanation: After forming two sublists of the given list as required, we have two lists as: 2->8->6 and 5->9.

# Input: LinkedList: 7 
# Output: 7 , <empty linked list>

# Constraints:
# 1 <= number of nodes <= 100
# 1 <= node -> data <= 104

# Class definition for a Node in the linked list
class Node:
    # Constructor to initialize the node's data and the next pointer
    def __init__(self, data):
        self.data = data  # Assign data to the node
        self.next = None  # Initialize next as None

# Solution class to perform the alternating split of the linked list
class Solution:
    def alternatingSplitList(self, head):
        # Initialize pointers for two resulting lists: h1 and h2
        h1 = head  # h1 will point to the first node
        h2 = head.next  # h2 will point to the second node
        ptr1 = h1  # Pointer to traverse the first list (h1)
        ptr2 = h2  # Pointer to traverse the second list (h2)
        
        # Initialize result list containing heads of the two new lists
        res = [h1, h2]

        # Loop through the linked list, alternating between the two lists
        while(ptr2 != None and ptr2.next != None):
            # Move ptr1 to the next alternate node
            ptr1.next = ptr2.next
            ptr1 = ptr1.next
            
            # Move ptr2 to the next alternate node
            ptr2.next = ptr1.next
            ptr2 = ptr2.next

        # Terminate the first list (h1) by setting the last node's next to None
        ptr1.next = None

        # Return the heads of the two split lists (h1 and h2)
        return res
    
# Creating a linked list 1 -> 2 -> 3 -> 4 -> 5 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Creating a solution object
sol = Solution()

# Splitting the linked list
result = sol.alternatingSplitList(head)

# result[0] contains the first split list: 1 -> 3 -> 5 -> None
# result[1] contains the second split list: 2 -> 4 -> None

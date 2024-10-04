# Deletion and Reverse in Circular Linked List

# https://www.geeksforgeeks.org/problems/deletion-and-reverse-in-linked-list/1

# Difficulty: Medium

# Given a Circular Linked List. The task is to delete the given node, key in the circular linked list, and reverse the circular linked list.

# Note:
# You don't have to print anything, just return the head of the modified list in each function.
# Nodes may consist of Duplicate values.
# The key may or may not be present.

# Expected Time Complexity: O(n)
# Expected Auxillary Space: O(1)

# Constraints:
# 2 <= number of nodes, key  <= 105
# 1 <= node -> data <= 105

# Examples:

# Input: Linked List: 2->5->7->8->10, key = 8
# Output: 10->7->5->2 
# Explanation: After deleting 8 from the given circular linked list, it has elements as 2, 5, 7, 10. Now, reversing this list will result in 10, 7, 5, 2, the resultant list is also circular.

# Input: Linked List: 1->7->8->10, key = 8
# Output: 10->7->1
# Explanation: After deleting 8 from the given circular linked list, it has elements as 1, 7,10. Now, reversing this list will result in 10, 7, 1, the resultant list is also circular.

# Input: Linked List: 3->6->4->10, key = 9
# Output: 10->4->6->3
# Explanation: As there no key present in the list, so simply reverse the list, the resultant list is also circular.


class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        # easy way
        arr = [head.data]
        temp = head.next
        while temp!=head:
            arr.append(temp.data)
            temp = temp.next
        temp = head
        for element in arr[::-1]:
            temp.data = element
            temp = temp.next
        return head
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        prev = head
        temp = head.next
        
        # Find tail
        tail = head
        while temp != head:
            temp = temp.next
            tail = tail.next
            
        # If head is key, set tail to the element next of head
        if head.data == key:
            tail.next = head.next
            head = head.next
            return head
            
        # If head is not key
        temp = head.next
        while temp != head:
            if temp.data == key:
                prev.next = temp.next
                temp = temp.next
                break
            prev = prev.next
            temp = temp.next
        return head
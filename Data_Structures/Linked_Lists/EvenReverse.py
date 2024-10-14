# Even Reverse

# https://www.interviewbit.com/problems/even-reverse/

# Problem Description
# Given a linked list A , reverse the order of all nodes at even positions.

# Problem Constraints
# 1 <= Size of linked list <= 100000

# Input Format
# First and only argument is the head of the Linked-List A.

# Output Format
# Return the head of the new linked list.

# Example Input

# Input 1:
# A = 1 -> 2 -> 3 -> 4
# Input 2:
# A = 1 -> 2 -> 3


# Example Output

# Output 1:
#  1 -> 4 -> 3 -> 2
# Output 2:
#  1 -> 2 -> 3

# Example Explanation

# Explanation 1:
# Nodes are positions 2 and 4 have been swapped.
# Explanation 2:
# No swapping neccassary here.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of the linked list
    # @return the head node of the new linked list
    def solve(self, A):
        if not A or not A.next:
            return A
        
        # Step 1: Collect all nodes at even positions
        even_nodes = []
        odd = A
        even = A.next
        while even:
            even_nodes.append(even.val)
            if not even.next:
                break
            odd = even.next
            even = odd.next
        
        # Step 2: Reverse the list of even nodes
        even_nodes.reverse()
        
        # Step 3: Reinsert the reversed even nodes
        index = 0
        even = A.next
        while even:
            even.val = even_nodes[index]
            index += 1
            if not even.next:
                break
            odd = even.next
            even = odd.next
        
        return A

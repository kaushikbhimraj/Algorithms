"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # Trick here is to have two pointers. 
        # 2nd pointer will be displaced (n) from 1st pointer. 
        curr   = head
        first  = curr
        second = None
        
        # Set 2nd pointer in position. 
        for i in range(n):
            curr = curr.next
        second = curr
        
        # Increment and traverse until 2nd pointer reaches end. 
        while second.next:
            first = first.next
            second = second.next
        
        # Pointer 1st pointer node to next.next of its position, skipping the node 
        # we needs to be deleted.
        first.next = first.next.next
        return head
"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

	# Singly list so need to remember the previous node while traversing. 
	# After the swap, the return value is not starting from the new swapped value as heap. 
    def swapPairs(self, head: ListNode) -> ListNode:
    	node = head
    	while head:
    		if not head.next:
    			break
    		temp = head.next.val
    		head.next.val = head.val
    		head.val = temp
    		head = head.next.next
    	return head


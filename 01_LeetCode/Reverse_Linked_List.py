"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def reverseList(self, head):

		# Edge case
		# Write your code here.
	    if not head:
			return head
		
		# Three pointer algorithm. 
		# Pointer #1: Current Node
		# Pointer #2: Next Node
		# Pointer #3: Next Next Node
		
		# Initializing the first two pointers. 
		# Setting head.next to None.
		p_1 = head
		p_2 = p_1.next
		p_1.next = None
		
		while p_2:
			# Saving the next value if pointer #2 before setting it previous node.
			p_3 = p_2.next
			p_2.next = p_1
			
			# Moving pointers to the next node. 
			p_1 = p_2
			p_2 = p_3
			
		# Once the end node is reach, all the nodes before it have been set to point
		# to their previous nodes. So the list is reversed at this point. 
		return p_1
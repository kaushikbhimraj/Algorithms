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
		if not head:
			return head

		# Algorithm has three pointers. 
		# Initialize first and second pointer and 
		# point #1 should be pointing to a None. 
		p_1 = head
		p_2 = p_1.next
		p_1.next = None

		while p_2:
			# In order to reverse a linked list, conside 3 pointers. 
			# The main pointer in this scenario is pointer #2 and need 
			# to save the next pointer its is pointing to before we 
			# point to the previous value in pointer #1.  
			p_3 = p_2.next
			p_2.next = p_1

			# After switching, move all pointers to the right. 
			p_1 = p_2
			p_2 = p_3

		return p_1
"""
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseBetween(self, head, m, n):

		if not head:
			return None

		# Two pointer 
		# prev : pointer to one before the current node. 
		# curr : pointer to current node. 
		prev, curr = None, head
		while m > 1:
			prev = curr
			curr = curr.next
			m, n = m-1, n-1

		# Store the prev value and current value to set it the start and ends of the reversed linked list. 
		front_connection = prev
		tail_connection  = curr

		# Reverse the linked list here.
		while n:
			p_3 = curr.next
			curr.next = prev
			prev = curr
			curr = p_3
			n -= 1

		# Stitch the reversed linked list back with the main linked list. 
		if front_connection:
			front_connection.next = prev
		else:
			head = prev
		tail_connection.next = curr

		return head
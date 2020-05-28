"""
Date: 05/27/2020
ADD TWO NUMBERS:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored 
in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as 
a linked list. 

ISSUE:
	Three things you missed.
		- need to make the NEW LINKED LIST is create the next node in the l3.next
		- need to make sure you are not created extra nodes at the end of the iteration
		- the last if condition should always create a new node and have the carry in it. 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		l3    = ListNode(None)
		start = l3
		ones, tens = 0, 0

		# "l1 or l2" route would work better for this scenario. 
		# And a method to check ones and tens would be great. (Stack might slow down the efficiency)
		while l1 and l2:
			ones = l1.val + l2.val + tens
			tens = 0

			if ones//10 > 0:
				tens = ones//10
				ones = ones%10
			
			l3.val = ones

			if l1.next or l2.next:
				l3.next = ListNode(None)
				l3 = l3.next

			l1 = l1.next
			l2 = l2.next

		while l1:
			ones = l1.val + tens
			tens = 0
			if ones//10 > 0:
				tens = ones//10
				ones = ones%10
			l3.val = ones

			if l1.next:
				l3.next = ListNode(None)
				l3 = l3.next
			l1 = l1.next

		while l2:
			ones = l2.val + tens
			tens = 0
			if ones//10 > 0:
				tens = ones//10
				ones = ones%10
			l3.val = ones

			if l2.next:
				l3.next = ListNode(None)
				l3 = l3.next
			l2 = l2.next

		if tens > 0:
			l3.next = ListNode(tens)

		return start
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
	def mergeKLists(self, lists):
		sortedList = []

		# Each element is a head node in the linked list.
		for node in lists:

			# Push each val, node onto the list. 
			while node:
				heappush(sortedList, node.val)
				node = node.next

		node = ListNode(None)
		head = node
		while sortedList:
			head.next = ListNode(heappop(sortedList))
			head = head.next

		return node.next
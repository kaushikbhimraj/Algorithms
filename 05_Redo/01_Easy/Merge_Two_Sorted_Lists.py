"""
MERGE TWO SORTED LISTS
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#      def __init__(self, val=0, nxt=None):
#          self.val = val
#          self.next = nxt

class Solution:

	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""
		Load the head into a new temp variable that can be used to build the LL. 
		"""
		head_node = ListNode()
		current_node = head_node

		while True:
			if l1 is None and l2 is None:
				break

			if l1 is None:
				current_node.next = l2
				break

			elif l2 is None:
				current_node.next = l1
				break

			else:
				min_value = 0
				if l1.val < l2.val:
					min_value = l1.val
					l1 = l1.next

				else:
					min_value = l2.val
					l2 = l2.next

			new_node = ListNode(min_value)
			current_node.next = new_node
			current_node = current_node.next

		return head_node.next

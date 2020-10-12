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
        # Create a new list and keep adding values to it. 
        head = ListNode(-1)
        curr = head
        
        # Simple merge list here. 
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
                
            curr = curr.next
        
        # Attach the remaining part of l1 or l2. 
        curr.next = l1 if l1 else l2
        
        # Skip the starting value.
        return head.next

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
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        return self.helper(head)
    
    def helper(self, curr, prev=None):
        if not curr:
            return prev
        
        temp = curr.next
        curr.next = prev
        prev = curr
        return self.helper(temp, prev)
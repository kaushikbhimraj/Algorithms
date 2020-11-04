# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        curr = head
        self.helper(curr)
        return curr
    
    def helper(self, node):
        if not node or not node.next:
            return
        
        temp = node.next.val
        node.next.val = node.val
        node.val = temp
        self.helper(node.next.next)
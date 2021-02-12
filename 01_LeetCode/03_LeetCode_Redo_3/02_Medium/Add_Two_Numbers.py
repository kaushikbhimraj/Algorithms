"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored 
in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        amt = 0
        head = ListNode()
        curr = head
        
        # Traverse both linked lists until any one or both run out. 
        while (l1 and l2):
            amt += l1.val + l2.val
            
            curr.next = ListNode(amt % 10)
            curr = curr.next
            
            amt = amt // 10
            l1 = l1.next
            l2 = l2.next
        
        # Check if one in two are still active. 
        # If so use the same logic as above to calculate the sum. 
        if (l1):
            while (l1):
                amt += l1.val
                curr.next = ListNode(amt % 10)
                curr = curr.next
                amt = amt // 10
                l1 = l1.next
            
        if (l2):
            while (l2):
                amt += l2.val
                curr.next = ListNode(amt % 10)
                curr = curr.next
                amt = amt // 10
                l2 = l2.next
        
        # One last check to see if the carry still have a value. 
        # If so, add as the last node. 
        if (amt):
            curr.next = ListNode(amt)
            
        return head.next

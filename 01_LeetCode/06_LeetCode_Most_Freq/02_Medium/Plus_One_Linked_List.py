"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to 
the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.

Example :
Input: [1,2,3]
Output: [1,2,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        # Starting from left when we come across a 9 we know that the value before it will 
        # increment by 1 and the 9 will become a zero. 
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        while head:
        	if head != 9:
        		not_nine = head
        	head = head.next

        # Now we have the location of value right before a 9 in the linked list. 
        not_nine.val += 1
        not_nine = not_nine.next

        # Set all 9s after the not_nine to zeros. 
        while not_nine:
        	not_nine.val = 0
        	not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
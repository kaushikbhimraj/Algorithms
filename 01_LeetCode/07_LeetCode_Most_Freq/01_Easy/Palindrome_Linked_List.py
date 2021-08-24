"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time:  O(n)
# Space: O(n)

class Solution:

    # Method 1: Copy the matrix into array and check if it is palindrome. 
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        # Copy into new array.
        first = head
        out = []
        while first:
            out.append(first.val)
            first = first.next

        # Check if palindrome. 
        left = 0
        right = len(out) - 1
        while left <= right:
            if out[left] != out[right]:
                return False
            left += 1
            right -= 1
        return True

# Time:  O(n)
# Space: O(1)

    # Method 2: Check list in place. 
    #   - Using slow and fast pointers find the mid of list. 
    #   - Reverse list from after mid node. 
    #   - Check if values match. 
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        start = head
        mid = self.findHalf(head)
        end = self.reverse(mid.next)
        
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True
    
    def findHalf(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
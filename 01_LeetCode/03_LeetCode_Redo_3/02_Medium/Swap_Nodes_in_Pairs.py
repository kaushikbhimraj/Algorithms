"""
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
 
Follow up: Can you solve the problem without modifying the values in the list's nodes? 
(i.e., Only nodes themselves may be changed.)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Following method will not swap nodes, just values. 
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        node = head
        while (node.next):
            
            temp = node.next.val
            node.next.val = node.val
            node.val = temp            
            node = node.next
            if node.next:
                node = node.next

        return head

    # Check if head and its next nodes exist. 
    # Store the first node in first
    # Store the second node in second
    # Then use the recursion fucntion to store the second.next in first.next
    # After the recursion stack in on the return second.next = first
    # The last step is essential. 
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if (not head or not head.next):
            return head
        
        first = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second
"""
LC: 328 Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) 
time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

T: O(n); S: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

    	odd = head
    	even = head.next
    	evenHead = head.next

    	while (even and even.next):
    		
    		# Update odd next value
    		# Move odd pointer to next value of odd.
    		odd.next = even.next
    		odd = odd.next

    		# Update even next value
    		# Move even pointer to next value of even. 
    		even.next = odd.next
    		even = even.next

    	# Odd pointer will be at the last value of odd. 
    	# Even list is created, just need to link the first node of the even list to the end 
    	# odd list. 
    	odd.next = evenHead
    	return head
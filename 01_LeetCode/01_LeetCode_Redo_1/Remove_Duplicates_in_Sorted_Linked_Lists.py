"""
Remove Duplicate from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
input:  1->1->2
output: 1->2

input:  1->1->2->3->3
output: 1->2->3
"""

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class prob_83:
    def __init__(self):
        self.memo = {}
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        if not node:
            return
        self.memo[node.val] = node.val
        
        while node and node.next:
            if node.next.val in self.memo.keys():
                node.next = node.next.next
                continue
            else:
                self.memo[node.next.val] = node.next.val
            node = node.next
        return head

"""
The logic has to handle linked list start and end nodes. 
Then it needs to see two steps in advanced to check if there are any nodes that it can swap out, if a repeat is found.
"""
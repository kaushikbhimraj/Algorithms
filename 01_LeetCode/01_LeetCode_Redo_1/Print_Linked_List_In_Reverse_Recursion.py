
"""
Date:     03.29.2020
Desc:     Create an algorithm that prints a linked list in reverse order. 
"""

# Basic Linked List DS Model. 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node('+')
    
    def insert(self, val):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(val)

# Following uses the stack to print values in the reverse order. 
class reversestack:
    def reverseLL(self, node):
        if not node:
            return
        self.reverseLL(node.next)
        print(node.val)
    
# Driver Code
arr = [9, 2, 3, 1, 4, 10, 23, 11]
a = LinkedList()
for val in arr:
    a.insert(val)

reversestack().reverseLL(a.head)
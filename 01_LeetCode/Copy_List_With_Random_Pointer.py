"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        copyDictionary = {}
        node = head
        
        # Create a copy of each node in a dictionary without its next or random node. 
        while node:
            copyDictionary[node] = Node(node.val)
            node = node.next
        
        # Iterate through the same list to upadte nodes in dictionary with 
        # next/random values from original. 
        node = head
        while node:
            
            if node.next:
                copyDictionary[node].next = copyDictionary[node.next]
                
            if node.random:
                copyDictionary[node].random = copyDictionary[node.random]
            
            node = node.next
        
        return copyDictionary[head]
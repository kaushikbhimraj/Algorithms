
"""
Doubly Linked List
"""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, val):
        if (not self.head.val):
            self.head.val = val
        else:
            if (not self.tail.val):
                self.tail.val = val
            else:
                newNode = Node(val)
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

    def print_all(self):
        curr = self.head
        while (curr):
            print(curr.val)
            curr = curr.next

            

x = LinkedList()
y = [4,3,5,1,13]

for val in y:
    x.insert(val)

x.print_all()
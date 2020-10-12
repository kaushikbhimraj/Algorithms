"""
Doubly linked lists
"""

class Node:
	def __init__(self, value):
		self.data = value
		self.prev = None
		self.next = None

class DoubleLinkedLists:
	def __init__(self, value):
		self.head = Node(value)

	def insertback(self, value):
		currentnode = self.head
		while currentnode.next:
			currentnode = currentnode.next
		currentnode.next = Node(value)

	def insertfront(self, value):
		currentnode = self.head
		while currentnode.prev:
			currentnode = currentnode.prev
		currentnode.prev = Node(value)

	def printallfront(self):
		currentnode = self.head
		while currentnode and currentnode.data:
			print(currentnode.data)
			currentnode = currentnode.prev

	def printallback(self):
		currentnode = self.head
		while currentnode and currentnode.data:
			print(currentnode.data)
			currentnode = currentnode.next

# Run
a = [2, 34, 32, 1212, "Kaushik", 892, 87]
A = DoubleLinkedLists(a[3])

# before head node
print("Print head and all values before it.")
A.insertfront(a[2])
A.insertfront(a[1])
A.insertfront(a[0])
A.printallfront()
print("\n")
print("Print head and all values after it.")
# after head node
A.insertback(a[4])
A.insertback(a[5])
A.printallback()

# How to delete nodes in the linked list?
# Linked Lists:
# -------------------------------
# Best & Worst: 
# Access - O(n)
# Search - O(n)
# Insertion - O(1)
# Deletion - O(1)

# Singly linked lists.
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self,first):
		self.head = Node(first)

	def insert(self, item):
		cursor = self.head
		while cursor.next != None:
			cursor = cursor.next
		cursor.next = Node(item)

	def search(self, item):
		cursor = self.head
		while cursor.next or cursor.data != item:
			cursor = cursor.next
		return cursor.data

	def delete(self, item):								# Further study.
		if self.head == item:
			self.head = self.head.next
			return True
		cursor = self.head
		while cursor.next or cursor.data != item:
			prev = cursor.data
			cursor.data = cursor.next

# Doubly linked lists.
class Node2:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

# Output Test
A = LinkedList(2)
A.insert(4)
A.insert(5)
A.insert(6)
A.insert("Kaushik")

print(A.search("Kaushik"))
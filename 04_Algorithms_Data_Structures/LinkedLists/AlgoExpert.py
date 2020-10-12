"""
Following explores creating, inserting and deleting nodes in a doubly linked list.
"""

class Node:
	def __init__(self, value):
		self.data = value
		self.next = None
		self.prev = None

class Doublylinkedlist:
	def __init__(self):
		self.head = Node(None)
		self.tail = Node(None)

	def setHead(self, node):
		if self.head is None:
			self.head = node
			self.tail = node
			return 
		self.insertBefore(self.head, node)

	def setTail(self, node):
		if self.tail is None:
			self.tail = node
			return
		self.insertAfter(self.tail, node)

	def insertBefore(self, node, nodeToInsert):
		# Check if linked list exists. 
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return

		# Set prev and next parameters for the current node.
		self.remove(nodeToInsert) 
		nodeToInsert.prev = node.prev
		nodeToInsert.next = node

		# If not head, point previous node to nodeToInsert
		if node.prev is None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

	# Similar to insertBefore
	def insertAfter(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return

		self.remove(nodeToInsert)
		nodeToInsert.prev = node
		nodeToInsert.next = node.next

		if node.next is None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

	def insertAtPosition(self, position, nodeToInsert):

	def removeNodesWithValue(self, value):
		# Search for the nodes with the given value and then remove them. 
		node = self.head
		while node is not None:
			TrackOrder = node
			if node.value == value:
				self.remove(node)
			node = TrackOrder.next

	def remove(self, node):
		# Remove head
		if node == self.head:
			self.head = self.head.next
		# Remove tail
		if node == self.tail:
			self.tail = self.tail.prev
		# Remove node
		self.removeNodeBindings(node)

	def removeNodeBindings(self, node):
		if node.prev is not None:
			node.prev.next = node.next
		if node.next is not None:
			node.next.prev = node.prev
		node.next = None
		node.prev = None

	def containsNodeWithValue(self, value):
		node = self.head
		while node is not None and node.value != value:
			node = node.next
		return node is not None

https://www.bing.com/images/search?q=hot+saree+instagram&form=HDRSC2&first=1&cw=1604&ch=1603


01-12-1953
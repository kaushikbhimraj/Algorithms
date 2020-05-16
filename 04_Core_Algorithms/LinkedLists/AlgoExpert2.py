
class Node:
	def __init__(self, value):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self):
		self.head = Node(None)
		self.tail = Node(None)

	# Traverse once.
	def InsertAtEnd(self, value):
		if self.tail == None:
			self.tail.data = value

		else:
			temp = self.tail
			self.tail = Node(value)
			temp.next = self.tail
			self.tail.prev = temp

	# Take a node from anywhere in the linked list and make it the head.
	def SetNodetoHead(self, value):
			NodeCursor = self.head

		while NodeCursor.next != None:

			# This condition does not take head or tail into account.
			if NodeCursor.data == value:

				# Replacing the head with the node information.
				self.head.data = NodeCursor.data

				# Connecting the prev node with the next node.
				NodeCursor.next.prev = NodeCursor.prev
				NodeCursor.prev.next = NodeCursor.next

				# Deleting the node at its current location.
				NodeCursor.prev = None
				NodeCursor.next = None
				NodeCursor.data = None

				return True

			NodeCursor = NodeCursor.next

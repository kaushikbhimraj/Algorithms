"""
Binary Search Tree
"""

class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None


class BinarySearchTree:
	def insert(self, node, value:int) -> bool:
		if not node.data:
			node.data == Node(value)
			return True
		if node.data == value:
			return False
		else:
			if node.data > value:
				if not node.left:
					node.left = Node(value)
					return True
				else:
					self.insert(node.left, value)
			elif node.data < value:
				if not node.right:
					node.right = Node(value)
					return True
				else:
					self.insert(node.right, value)

	def print_this(self, node):
		if not node:
			return
		self.print_this(self, node.left)
		print(node.data)
		self.print_this(self, node.right)


# Build Tree



"""
	def search(self, node, value:int) -> bool:
		if node.data > value:
			if not node.left:
				return False
			else:
				BinarySearchTree.search(node.left, value)
		elif node.data < value:
			if not node.right:
				return False
			else:
				BinarySearchTree.search(node.right, value)
		elif node.data == value:
			return True
"""




"""
Create a Tree Node and write methods to insert and search nodes in the tree. 
A node can have n number of children. 
"""


class Node:
	""" 
	This object will store the children in an array. 
	Each element will its own Node object. 
	"""
	def __init__(self, value):
		self.val = value
		self.children = []



class Tree:
	"""
	Currently has three methods, 
		- self.root:  is the root node that is created with a const "root" string as name.
		              (replaces the "root" value with a string value when insert is run)
		- findNode:   finds the target node
		- insertNode: finds the parent node and create a new child node with the given value
		- dir:     	  prints all the values in the tree. 

	"""
	def __init__(self):
		self.root = Node("root")


	def findNode(self, startNode, targetNode:str):
		""" findNode(startNode: root, targetNode: string) -> object"""
		if not startNode:
			return 
		if startNode.val == targetNode:
			return startNode
		for child in startNode.children:
			return self.findNode(child, targetNode)

	""" insertNode(startNode: root, targetNodeName: string, insertValue: string)"""
	def insertNode(self, startNode, targetNodeName:str, insertValue:str):
		if not startNode:
			return
		if startNode.val == "root":
			startNode.val = insertValue
			return
		elif startNode.val == targetNodeName:
			startNode.children.append(Node(insertValue))
			return
		else:
			for child in startNode.children:
				return self.insertNode(child, insertValue)

	""" dir(startNode: root)"""
	def dir(self, startNode):
		if not startNode:
			return
		print(startNode.val)
		for child in startNode.children:
			self.dir(child)



# Application
x = Tree()
x.insertNode(x.root, "", "CEO")
x.insertNode(x.root, "CEO", "Director")
x.dir(x.root)


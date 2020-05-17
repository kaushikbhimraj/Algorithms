

"""
Date: 02/14/2020
Consolidated view of all the node object structures for various data structures. 
"""

class linkedlists_node:
	def __init__(self, value):
		self.val 		= value
		self.next 		= None

class tree_node:
	def __init__(self, value):
		self.val 		= value
		self.left 		= None
		self.right 		= None

class graph_node:
	def __init__(self, value):
		self.val 		= value
		self.visit 		= False
		self.neighbor 	= {}

	def insert(self, node_value):
		node_value = graph_node(node_value)
		try:
			self.neighbor[node_value.val]
		except KeyError:
			self.neighbor[node_value.val] = node_value


"""
Linked list will always point to the next node or if it is the last node it will point to None. 
Tree node will have point to two nodes and not greater than that. 
Lastly, graph can point to multiple nodes at the same time. 
"""
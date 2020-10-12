 
"""
Create AVL BST tree.

Have to look up how to delete a node in the tree. 
"""

class node:
	def __init__(self, value=None):
		self.value 			= value
		self.left_child 	= None
		self.right_child 	= None
		self.parent 		= None	# Pointer to the parent node in tree. 
		self.heigth 		= 1

class AVLTree:
	
	def _insert(self, value, cur_node):

		# Same logic from the BST tree construction
		if value < cur_node.value:
			if cur_node.left_child == None:
				cur_node.left_child = node(value)

				# Update the parent node for that node
				# Call the AVl function to inspect the node is unbalanced. 
				cur_node.left_child.parent = cur_node
				self._inspect_insertion(cur_node.left_child)

			else:
				self._insert(value, cur_node.left_child)

		# Same logic from the BST tree construction
		elif value > cur_node.value:
			if cur_node.right_child == None:
				cur_node.right_child = node(value)

				# Update the parent node for the current node. 
				# Call the AVL function to inspect the node is unbalanced. 
				cur_node.right_child.parent = cur_node
				self._inspect_insertion(cur_node.right_child)

			else:
				self._insert(value, cur_node.right_child)

		# To avoid duplicates.
		else:
			print("Value is already in tree")

	# Print all the nodes in the tree. 
	def _print_tree(self, cur_node):
		if cur_node != None:
			self._print_tree(cur_node.left_child)
			print('%s, h=%d'%(str(cur_node.value), cur_node.height))
			self._print_tree(cur_node.right_child)

	# Insert inspection function 
	def _inspect_insertion(self, cur_node, path=[]):
		if cur_node.parent==None: 
			return 
		path = [cur_node] + path

		left_height = self.get_height(cur_node.parent.left_child)
		right_height = self.get_height(cur_node.parent.right_child)

		if abs(left_height - right_height) > 1:
			path = [cur_node.parent] + path
			self._rebalance_node(path[0], path[1], path[2])
			return 

		new_height = 1 + cur_node.height
		if new_height > cur_node.parent.height:
			cur_node.parent.height= new_height
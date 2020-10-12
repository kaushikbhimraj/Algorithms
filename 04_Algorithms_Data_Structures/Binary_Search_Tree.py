"""
Date: 02.14.2020
Create a binary search tree using an insert algorithm. After the nodes are sucessfully inserted into the tree, print the nodes in order, pre-order and post-order fashion. Then write an algorithm to delete a given node. Make sure to capture all important edge cases when you design the tree. 
"""

# Node object has left and right. 
class Node:
	def __init__(self, vall):
		self.val 	= vall
		self.left 	= None
		self.right 	= None

# Insert value in Binary Tree. Avoid repeats
def insert(root, node):
	if root.val == node.val:
		return 
	if node.val < root.val:
		if not root.left:
			root.left = node
		else:
			insert(root.left, node)
	else:
		if not root.right:
			root.right = node
		else:
			insert(root.right, node)

# Print all nodes in a tree in a pre-ordered fashion.
def printTree(root):
	if root is None:
		return
	print(root.val)
	printTree(root.left)
	printTree(root.right)

# To delete a node in the tree, there are three cases that needs to be checked. 
# First check if the node is a leaf node. 
# Second check if the node has one child. If so replace the matching node with its child. 
# Finally check if node has two children. If so set the current node value to None. 

# When the node that is being deleted has two node children you will have to rearrange everything from that point to the leaf nodes. (Tricky!)
def delete(root, node):
	if not root:
		
		return

	if root.val == node:
		# Check whether the root has no children.
		if not root.left and not root.right:
			root = None



		# Check if root has atlreast one child.
		elif root.left and not root.right:
			root = root.left
			print(root.val)
		elif root.right and not root.left:
			root = root.right



		# Check if root has two children.
		elif root.left and root.left:
			print("This is the value that matches and has two children")
			print(root.val)
			root.val = None



	# If none of the above conditions are met, simply traverse the tree.
	else:
		if node < root.val:
			if root.left:
				delete(root.left, node)
		else:
			if root.right:
				delete(root.right, node)


# Build Tree
tree 					= Node(25)
tree.left 				= Node(15)
tree.right 				= Node(27)

# Insert Tree
insert(tree, Node(1))
insert(tree, Node(4056))
insert(tree, Node(43))
insert(tree, Node(54))
insert(tree, Node(13))

# Print Tree
print("\n")
printTree2(tree)

# Delete
print("\n")
delete(tree, 4056)
printTree2(tree)

"""
Unit test deleting the node from tree structure. 
"""
"""
Write a function that takes in a Binary Tree and inverts it. In other words, the fucntion
should swap every left node in the tree for its corresponding right node. 

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None/null.
"""

def invertBinaryTree(tree):
	if not tree:
		return 
	switchLeftandRight(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

def switchLeftandRight(tree):
	tree.left, tree.right = tree.right, tree.left
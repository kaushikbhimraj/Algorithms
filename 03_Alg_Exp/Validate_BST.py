"""
Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean repesenting
whether the BST is valid. 

Each BST node has an integer value, a left child node, and a right child node. A node is said to be valid BST
node if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right; and its children nodes are either 
valid BST nodes themselves or None/null. 

A BST is valid if and only if all of the nodes are valid BST nodes. 

INPUT 

			10
		   /  \
		  5   15
		 / \  / \
		2  5 13  22
	   /      \
      1        14

Notes:
We can use recursion for this. 
"""

class BST:
	def __init__(self, value):
		self.value = value
		self.left  = None
		self.right = None

def validateBST(tree):
	return helper_validateBST(tree, float("-inf"), float("inf"))

def helper_validateBST(tree, minValue, maxValue):
	if not tree:
		return True

	if tree.value < minValue or tree.value >= maxValue:
		return False		

	# You will uypda
	return helper_validateBST(tree.left, minValue, tree.value) and helper_validateBST(tree.right, tree.value, maxValue)
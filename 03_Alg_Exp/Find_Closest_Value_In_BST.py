"""
Write a function that takes in a Binary Search Tree (BST) and a target integer value and returns the closest
value to the target value contained in the BST. 

You can assume that there will only be one closest value. 

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST
node if and only if its satisfies the BST properly: its value is strictly greater than the values of every node 
to its left; its value is less than or equal to the values of every node to its right; and its children nodes 
are either valid BST nodes themselves or None/null.

"""

def findClosestValueInBst(tree, target):
	# Write your code here.
	return helper(tree, target, float("inf"))

def helper(tree, target, min_diff, closestValue=None):
	if not tree:
		return closestValue

	if min_diff > abs(tree.value-target):
		min_diff = abs(tree.value-target)
		closestValue = tree.value

	if target >= tree.value:
		return helper(tree.right, target, min_diff, closestValue)
	else:
		return helper(tree.left, target, min_diff, closestValue)
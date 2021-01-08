"""
Write a function that takes in a Binary Tree and returns a list of its branch sums 
ordered from left-most branch sum to rightmost branch sum. 

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch
is a path of nodes in a tree that starts at the root node and ends at any leaf node. 

Each Binary Tree node has an integer value, a left child node, and a right child node. 
Children nodes can either be Binary Tree nodes themselves or None/null.

INPUT:
tree =  		1
               / \
              2   3
             / \ / \
            4  5 6  7
           / \ 
          8   9

OUPTUT:
[15, 16, 18, 10, 11]
"""

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left  = None
		self.right = None

def branchSums(root):
	sums = []
	branchSums_height(root, 0, sums)
	return sums


def branchSums_height(root, branch_sum, sums):
	if not root:
		return

	branch_sum += root.value
	if not root.left and not root.right:
		sums.append(branch_sums)
		return

	branchSums_height(root.left, branch_sums, sums)
	branchSums_height(root.right, branch_sums, sums)

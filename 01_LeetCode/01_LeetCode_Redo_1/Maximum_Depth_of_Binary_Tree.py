"""
Maximum Derpth of Binary Tree

Given a binary tree, find its maximum depth. 
The maximum depth is the number ofnodes along the longest path from the root node down to the farthest lead node. 

Given binary tree [3, 9, null, null, 15, 7]

return its depth = 3
"""

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# Questions: Why are we starting with a count 1?
"""
			2
	34				6
N 		19 		N 		N
	8		N
"""

class prob_104:

	def __init__(self):
		self.memo = 0
		self.cont = 1

	# The counter is need to count and to be counted back at the end of stack. 
	# The memo records only the max value of the count value before reset. 
	def maxDepth(self, root:TreeNode) -> int:
		if root is None or not root.val:
			if self.memo < self.cont:
				self.memo = self.cont
			self.cont -= 1
			return 
		self.cont += 1
		self.maxDepth(root.left)
		self.maxDepth(root.right)
		return self.memo
		
a = TreeNode(2)
a.left = TreeNode(34)
a.left.right = TreeNode(19)
a.left.right.left = TreeNode(8)
a.right = TreeNode(6)

# Unit test
print(prob_104().maxDepth(a))
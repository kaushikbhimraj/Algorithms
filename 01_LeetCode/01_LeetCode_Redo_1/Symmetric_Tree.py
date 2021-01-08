"""
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (i.e. symmetric around its center)
For example, this binary tree [1,2,2,3,4,4,3] is symmetric.

Step 1: Use breadth first search to traverse through the tree.
Step 2: In each level compare the value for symmetry. 
Step 3: End points for the logic will be true if the traversal makes it to the end the leaf nodes. 	
		Return false if there is a assymmetry.


Here you are not only traversing the tree but you will have to handle None values in the nodes. 
This make the code a little lengthy than usual. 
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class prob_101:
	def __init__(self):
		self.memo = []

	def isSymmetric(self, root:TreeNode) -> bool:
		if not root:
			return True

		if len(self.memo) > 0:
			for i in range(len(self.memo)):
				x = self.memo.pop(0)
				if x is not None:
					self.memo.append(x.left)
					self.memo.append(x.right)

			i, j = 0, len(self.memo) - 1
			while i < j:
				if self.memo[i] is None and self.memo[j] is None:
					i += 1
					j -= 1
				elif (self.memo[i] is None and self.memo[j] is not None) or (self.memo[i] is not None and self.memo[j] is None):
					return False
				elif self.memo[i].val == self.memo[j].val:
					i += 1
					j -= 1
				else:
					return False
		else:
			self.memo.append(root)

		if not self.memo:
			return True
		else:
			return self.isSymmetric(self.memo[0])

# Unit test

c = TreeNode(9)
c.left = TreeNode(-42)
c.right = TreeNode(-42)
c.left.left = TreeNode(None)
c.left.right = TreeNode(76)
c.right.left = TreeNode(76)
c.right.right = TreeNode(None)
c.left.left.left = TreeNode(None)
c.left.left.right = TreeNode(13)
c.left.right.left = TreeNode(None)
c.left.right.right = TreeNode(13)

print(prob_101().isSymmetric(c))

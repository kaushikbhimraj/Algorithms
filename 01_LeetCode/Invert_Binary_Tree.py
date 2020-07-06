"""
Invert a Binary Tree

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# If this solution would be asked to be implemented iteratively, you will have to use the BFS algorithm. 
class Solution:

	# Using the depth first solution is the easiest way to implement this soluiton. 
	def invertTree(self, root):
		if not root:
			return 
		self.swapleftandright(root)
		self.invertTree(root.left)
		self.invertTree(root.right)
		return root

	def swapleftandright(self, root):
		root.left, root.right = root.right, root.left
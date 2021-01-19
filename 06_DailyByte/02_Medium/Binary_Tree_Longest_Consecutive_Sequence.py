"""
LC: 298 - Binary Tree Longest Consecutive Sequence
Give the reference to a binary tree, return the length of the longest path in the tree
that contains consecutive values. 

Note: The path must move downward in the tree. 
Ex: Given the following binary tree...
1
 \
  2
   \
    3
return 3.

Ex: Given the following binary tree…

       1
      / \
     2   2
    / \ / \
   4  3 5  8
     /
    4
return 4.


T: O(n); S: O(n) where n is the number of nodes in tree. 
"""

class Solution:
	def longestConsecutive(self, root: TreeNode) -> int:
		# Create an array to hold the max consecutive count. 
		res = [0]
		self.helper(root, 0, 0, res)
		return res[0]

	# Regular DFS to count and update max count at every step in traversal. 
	def helper(self, curr, prev, count, res):
		if (not curr):
			return
		elif (curr.val = prev + 1):
			count += 1
		else:
			count = 1

		res[0] = max(res[0], count)
		self.helper(curr.left, curr.val, count, res)
		self.helper(curr.right, curr.val, count, res)

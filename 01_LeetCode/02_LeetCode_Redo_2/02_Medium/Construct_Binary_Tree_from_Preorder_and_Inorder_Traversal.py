"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Eg.
# Pre-order => 1, 2, 4, 8, 9, 10, 11, 5, 3, 6, 7
# In-order  => 8, 4, 10, 9, 11, 2, 5, 1, 6, 3, 7

# New tree will be populated using recursion. 
# Creating a new helper funciton for this. 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	return self.helper(0, 0, len(preorder)-1, preorder, inorder)

	# Given pre-order and in-order traversal arrays of a binary tree. 
	# Re-create binary tree from the given information. 

	# Key characteristics of preorder and inorder. 
	# preorder -> root, root.left, root.right
	# inorder  -> root.left, root, root.right

	# So root of tree will always be the first element in preorder. 
	# We start from there. 

	def helper(self, preStart, inStart, inEnd, preorder, inorder):
		if (preStart > len(preorder)-1 or inStart > inEnd):
			return 

		# Create a root node for new binary tree. 
		# And find root.val in in-order array. Store position in new variable. 
		root = TreeNode(preorder[preStart])
		inIndex = 0
		for i in range(inStart, inEnd + 1):
			if root.val == inorder[i]:
				inIndex = i

		# Since we have location of the root node in in-order, 
		# we can now get its children by look at -1 and +1 of current position.
		# Using recursion this same process can be repeated for the sub-roots and children.  

		# KEY NOTE ==> preStart + (inIndex - inStart) + 1 ignores left section of the preorder array.
		# This formula finds the position of the next sub-root node in preorder array.  
		root.left  = self.helper(preStart + 1, inStart, inIndex-1, preorder, inorder)
		root.right = self.helper(preStart + (inIndex-inStart) + 1, inIndex + 1, inEnd, preorder, inorder)

		# After tree is create, return its root. 
		return root

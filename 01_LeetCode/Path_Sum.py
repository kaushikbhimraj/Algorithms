"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf such that adding up
all the values along the path equals the given sum. 

Note: A leaf is a node with no children. 

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
    	return self.hasPathSum_Helper(root, 0, sum)

    def hasPathSum_Helper(self, root, totol, targetSum):
    	if not root:
    		return False

    	total += root.val
    	if not root.left and not root.right and total == targetSum:
    		return True

    	# Ability to return something after traversing a stack is extremely vital when executing recursion. 
    	return self.hasPathSum_Helper(root.left, total, targetSum) or self.hasPathSum_Helper(root.right, total, targetSum)
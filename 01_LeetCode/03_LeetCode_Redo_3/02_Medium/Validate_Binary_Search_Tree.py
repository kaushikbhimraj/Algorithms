"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

T: O(n); S: O(1) where n is number of nodes in tree. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This is a simple recursion, where you would have to pass the parent value and check if the current node
# is greater or lesser than the limit. For left node, the node should not be greater than the parent value
# and for the right node, the value should not be lower than the parent value. 
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            
            if (node.val <= low or node.val >= high):
                return False
            
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root)
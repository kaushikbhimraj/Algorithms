"""
Given the reference to the root of a binary search tree and a target value, 
return whether or not two individual values within the tree can sum to the 
target. 

Ex: Given the following tree and target…

   1
  / \
 2   3, target = 4, return true.
Ex: Given the following tree and target…

   1
  / \
 2   3, target = 7, return false.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T: O(n); S: O(n) where n is number of nodes in BST.
class Solution:        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        mem = set()
        return self.helper(root, mem, k)
    
    def helper(self, root, mem, k):
        if (not root):
            return False
        if ((k - root.val) in mem):
            return True
        mem.add(root.val)
        return self.helper(root.left, mem, k) or self.helper(root.right, mem, k)
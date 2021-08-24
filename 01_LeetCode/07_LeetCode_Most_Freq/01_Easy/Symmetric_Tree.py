"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Follow up: Solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T: O(n); S: O(n) where n is the total number of nodes. 
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool: 
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        if left.val == right.val:
            l = self.helper(left.left, right.right)
            r = self.helper(left.right, right.left)
            return l == r
        else:
            return False
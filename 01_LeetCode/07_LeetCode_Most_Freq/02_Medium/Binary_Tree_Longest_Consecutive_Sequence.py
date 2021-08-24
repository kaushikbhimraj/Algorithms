"""
Given a binary tree, find the length of the longest consecutive sequence path.
The path refers to any sequence of nodes from some starting node to any node in the 
tree along the parent-child connections. The longest consecutive path need to be from 
parent to child (cannot be the reverse).

Example 1:
Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Example 2:
Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxval = 0
        
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return self.maxval
        self.helper(root)
        return self.maxval
    
    def helper(self, root):
        if not root:
            return 0
        
        cnt = 1
        if root.left:
            left = self.helper(root.left)
            if root.val == root.left.val - 1:
                cnt = left + 1
        if root.right:
            right = self.helper(root.right)
            if root.val == root.right.val - 1:
                cnt = max(cnt, right + 1)
        self.maxval = max(self.maxval, cnt)
        return cnt
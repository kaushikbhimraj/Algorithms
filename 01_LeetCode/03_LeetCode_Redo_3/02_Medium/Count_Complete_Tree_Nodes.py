# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T: O(n); S: O(d) where d is tree depth and n is number of nodes. 
class Solution:
    
    # LINEAR TIME
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_count = 1
        l = root.left
        while l:
            l = l.left
            left_count += 1
        
        right_count = 1
        r = root.right
        while r:
            r = r.right
            right_count += 1
        
        if (left_count == right_count):
            return (2**left_count) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
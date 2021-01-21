"""
LC. 230 - Kth Smallest Element in a BST
While traversing BST, put values into heap and return the (k+1)th value from the heap. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# T: O(n); S: O(n) where n is number of elements in BST. 
from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        heap = []
        self.helper(root, heap)
        
        res = 0
        while ( k > 0 ):
            res = heappop(heap)
            k -= 1
        
        return res
    
    def helper(self, root, heap):
        if ( not root ):
            return 
        heappush(heap, root.val)
        self.helper(root.left, heap)
        self.helper(root.right, heap)
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from 
left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        
        # Using BST 
        res = []
        queue = [root]
        reverse = False
        
        # Make sure to pop all values in queue for that level into the temporary array. 
        # Then use that ot 
        while queue:
            n = len(queue)
            currLevel = []
            for _ in range(n):
                curr = queue.pop(0)
                currLevel.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if reverse:
                res.append(self.rev(currLevel))
                reverse = False
            else:
                res.append(currLevel)
                reverse = True
        return res
    
    def rev(self, arr):
        l, r = 0, len(arr)-1
        while l < r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
        return arr
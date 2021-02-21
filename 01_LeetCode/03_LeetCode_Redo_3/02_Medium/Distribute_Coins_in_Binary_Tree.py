"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val 
coins and there are n coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another. (A 
move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:
Input: root = [3,0,0]
Output: 2

Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
"""
# T: O(n); S: O(k) where n is number of coins, k is maximum depth of tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        self.dfs(root)
        return self.moves
    
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        self.moves += abs(left) + abs(right)
        return root.val + left + right - 1
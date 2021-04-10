"""
We are given a binary tree (with root node root), a target node, and an integer value K.
Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # The solution to this problem contains three steps. 
    # First: create a hash map of node:parent
    # Secon: starting from target node, traverse to parent, left and right. 
    # Third: keep track of visited nodes while traversing the tree. 
    def __init__(self):
        self.p = {}
        self.seen = set()
        self.ans = []
        
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if (not root):
            return
        
        self.makeParent(root)
        self.checkDistance(target, K)
        return self.ans
    
    def makeParent(self, root):
        if (not root):
            return
        
        if (root.left):
            self.p[root.left] = root
            self.makeParent(root.left)
        
        if (root.right):
            self.p[root.right] = root
            self.makeParent(root.right)
    
    def checkDistance(self, root, k):
        if (not root):
            return
        
        if (root.val in self.seen):
            return
        
        self.seen.add(root.val)
        
        if (k == 0):
            self.ans.append(root.val)
            return
        
        if (root.left):
            self.checkDistance(root.left, k-1)
        
        if (root.right):
            self.checkDistance(root.right, k-1)
        
        if (root in self.p):
            self.checkDistance(self.p[root], k-1)
        
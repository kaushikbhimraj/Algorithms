
"""
Given a binary tree, return the vertical order traversal of its nodes' values. 
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:
[
  [9],
  [3,15],
  [20],
  [7]
]

Examples 2:
Input: [3,9,8,4,0,1,7]

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

Output:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Examples 3:
Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

Output:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        m = defaultdict(list)
        mx = [0,0]
        self.helper(root, 0, 0, m, mx)
        
        out = []
        for i in range(mx[0], mx[1]+1):
            m[i].sort(key=lambda x:x[0])
            out.append(val for _, val in m[i])
        return out
    
    def helper(self, root, col, row, m, mx):
        if (not root):
            return
        
        m[col].append((row, root.val))
        mx[0] = min(mx[0], col)
        mx[1] = max(mx[1], col)
        
        self.helper(root.left, col - 1, row + 1, m, mx)
        self.helper(root.right, col + 1, row + 1,  m, mx)
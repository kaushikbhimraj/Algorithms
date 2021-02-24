"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and 
all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:
Input: root = []
Output: 0

Example 3:
Input: root = [1]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
 
Follow up: Traversing the tree to count the number of nodes in the tree is an easy solution but with O(n) complexity. 
Could you find a faster algorithm?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# T: O(n); S: O(d) where d is tree depth and n is number of nodes. -> brute force
# T: O(log^2 n); S: O(d) where d is tree depth and n is number of nodes. -> brute force

class Solution:
    def countNodes_bruteForce(self, root):
        if (not root):
            return 0

        return 1 + self.countNodes_bruteForce(root.left) + self.countNodes_bruteForce(root.right)

    def countNodes(self, root: TreeNode) -> int:
        if (not root):
            return 0
        
        # Count the number of nodes on the left arm from root node. 
        leftCount = 0
        left = root
        while (left):
            leftCount += 1
            left = left.left
        
        # Count the number of nodes on the right arm from root node. 
        rightCount = 0
        right = root
        while (right):
            rightCount += 1
            right = right.right
        
        # If both sides are equal we have a perfect binary tree. 
        # So number of nodes are 2^N - 1
        if (leftCount == rightCount):
            return (2**leftCount) - 1
        
        # Use recursion to go a level deeper if the counts are not equal. 
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
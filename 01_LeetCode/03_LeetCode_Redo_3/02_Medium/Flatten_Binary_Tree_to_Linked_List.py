"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer 
points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Key to the problem is a post order traversal. 
# Make sure you keep track of the start and end of the left side of tree. 
# Then take the tail end of the left side of tree and connect the right side of tree to it. 
# Make the start of left of side tree the right side. 
# Set the left side to null. 

# T: O(n); S: O(n) where n is number of nodes in the tree. 

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Post-order operations in recursion. 
        if root.left:
            left_start = root.left
            left_tail = root.left
            while left_tail.right:
                left_tail = left_tail.right
            
            root.left = None
            temp = root.right
            root.right = left_start
            left_tail.right = temp
"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
	# T: O(n); S: O(n) where n is number of nodes in the tree. 
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        
        # BFS
        while queue:
            n = len(queue)
            for i in range(n):
                # Once the node is popped from the queue, add the next value in queue to node.next
                curr = queue.pop(0)
                
                if curr and curr.left:
                    queue.append(curr.left)
                if curr and curr.right:
                    queue.append(curr.right)
                
                # Needs to be at the end of iteration as the right child will have to be update 
                # with next node as well. 
                if queue and i < n-1:
                    curr.next = queue[0]
                
        return root


"""
Given a node in a binary search tree, find the in-order successor of that node in the BST.
If that node has no in-order successor, return null.
The successor of a node is the node with the smallest key greater than node.val.
You will have direct access to the node but not to the root of the tree. Each node will 
have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

Follow up:
Could you solve it without looking up any of the node's values?

Example 1:
Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.

Example 2:
Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

Example 3:
Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17

Example 4:
Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15

Example 5:
Input: tree = [0], node = 0
Output: null

Constraints:
-10^5 <= Node.val <= 10^5
1 <= Number of Nodes <= 10^4
All Nodes will have unique values.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# In-order is left -> root -> right
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
    	# Case 1:
    	# Check if node.right exists. 
    	# If so, the traverse to the left most node in the right branch. 
    	# The will be the successor to the current node. 
    	if node.right:
    		node = node.right
    		while node.left:
    			node = node.left
    		return node

    	# Case 2:
    	# Since the right node for the current node does not exists, 
    	# The sucessor will be somewhere above the current node. 
    	# So using the parent, traverse to the top until the node is the left node to its parent. 
    	# This will be the sucessor (next value to the current node)
    	while node.parent and node == node.parent.right:
    		node = node.parent
    	return node
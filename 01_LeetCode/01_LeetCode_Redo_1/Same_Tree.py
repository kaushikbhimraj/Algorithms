"""
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class prob_100:
	def isSameTree(self, p, q) -> bool:

		if (p and not q) or (not p and q):
			return False

		if not p and not q:
			return True

		if p.val == q.val:
			return bool(self.isSameTree(p.left, q.left) * self.isSameTree(p.right, q.right))
		else:
			return False


# Unit Test
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
b.left.left = TreeNode(4)
b.left.right = TreeNode(5)
b.right.left = TreeNode(6)
b.right.right = TreeNode(7)

print(prob_100().isSameTree(a,b))

# Is this an optimal solution?
# What is the runtime on this algorithm and can you improve this in any way?
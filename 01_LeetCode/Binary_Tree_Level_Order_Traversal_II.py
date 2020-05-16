"""
Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes values (ie, from left to right, level by level from leaf to root)

For example:
Given binary tree [3,9, 20, null, null, 15, 7]
return its bottom-up level order traversal as:

Notes:
Below logc is not tested not Null nodes in the tree. 

"""

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class prob_107:
	def __init__(self):
		# Array for a breadth first queue
		# Array for outputting values from the tree in the reverse level order.
		self.memo = []
		self.retn = []

	def levelOrderBottom(self, root: TreeNode):
		if root is None:
			return

		# Using the breadth-first concept to traverse the binary tree.
		# Adding the elements from each level of the tree to an array.
		# Append the entire array to the main array after every iteration. 
		if not self.memo:
			self.retn.append([root.val])
			self.memo.append(root)
		else:
			temp_len = len(self.memo)
			temp_arr = []
			for i in range(temp_len):
				frst_elm = self.memo.pop(0)
				if frst_elm.left:
					self.memo.append(frst_elm.left)
					temp_arr.append(frst_elm.left.val)
				if frst_elm.right:
					self.memo.append(frst_elm.right)
					temp_arr.append(frst_elm.right.val)

			if temp_arr:
				self.retn.append(temp_arr)

		# Check elements in queue.
		# Return array if nothing in queue
		# Else add to the stack
		if not self.memo[0]:
			i, j = 0, len(self.retn)-1

			# Reversing the array
			while i < j:
				temp = self.retn[i]
				self.retn[i] = self.retn[j]
				self.retn[j] = temp
				i += 1
				j -= 1

			return self.retn
		else:
			return self.levelOrderBottom(self.memo[0])


# Unit testing the process
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

print(prob_107().levelOrderBottom(a))

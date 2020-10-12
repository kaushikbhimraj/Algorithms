"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can 
only move in two directions, right and down, but certain cells are "off limits" such that the robot
cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom
right. 

Time Complexity:  O(mn)
Space Complexity: O(mn)
"""

class Solution:
	def __init__(self):
		self.memo = None

	def uniquePaths(self, m: int, n: int):

		# Create a 2-D array to store all paths. 
		self.memo = [[0]*n for _ in range(m)]
		return self.helper(m-1, n-1)

	def helper(self, row, col):
		# Bounding condition.
		if row < 0 or col < 0:
			return 0

		# Check if path is already visited. 
		if self.memo[row][col] > 0:
			return self.memo[row][col]

		# If traversal reaches origin then you found a new path.
		if row == 0 or col == 0:
			return 1

		# Main recursion. 
		self.memo[row][col] = self.helper(row-1, col) + self.helper(row, col-1)

		return self.memo[row][col]

row, col = 7,3
x = Solution()
print(x.uniquePaths(row, col))
print(x.memo)
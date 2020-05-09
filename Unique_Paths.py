
"""
Name: Unique Paths
Ques: 62
Desc: A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below.)
	  The robot can only move either down or right at any point in time. The robot is trying to reach the 
	  bottom-right corner of the grid (marked 'Finish' in the diagram below)

How many possible unique paths are there?
"""

class Unique:
	def __init__(self):
		self.routes = 0

	def uniquePaths(self, row, col):
		if row == 1 and col == 1:
			return 1
		return self.Paths(0, 0, row-1, col-1)

	# The method does not use memoization. This is key to get the count right. 
	# If we use memoization and store computed values from a previous stack, the method will not explore other paths.
	# It will simply cut the recursion at that point and go back the the previous call on stack (This will lead to not 
	# counting all the routes available for the robot.) 
	def Paths(self, nrow, ncol, row, col):

		if nrow > row or ncol > col:
			return 

		if nrow == row and ncol == col:
			self.routes += 1
			return 

		# Depth first algorithm 
		self.Paths(nrow+1, ncol, row, col)
		self.Paths(nrow, ncol+1, row, col)

		return self.routes



# Driver Code 
# This code is exceeding the time limit. 
m, n = 7, 3
print(Unique().uniquePaths(m, n))
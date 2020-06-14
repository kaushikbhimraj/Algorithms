
"""
In a given grid, each cell can have one of three values:
	- value 0: empty cell
	- value 1: fresh orange
	- value 2: rotten orange

Every minute, any fresh orange that is adjacent (4-direcitonally) to a rotten orange becomes 
rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1 instead. 


Notes:
	This problem is very similar to the number of islands problem. 
"""

class Solution:

	def __init__(self):
		self.count = 0

	def orangeRotting(self, grid) -> int:
		for i in range(len(grid)):
			for j in range(len(grid[0])):

				if grid[i][j] == 2:
					self.dfs(grid, i, j)

	def bst(self, grid, row, col):
		if row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col]!= 0:
			

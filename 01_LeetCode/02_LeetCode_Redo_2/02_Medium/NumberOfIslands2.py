"""
Given a 2d grid map of '1's (land) and '0's (water), num_of_islands the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""

class Solution:
	def __init__(self):
		self.num_of_islands = None
		self.grid = None

	def numIslands(self, grid: List[List[str]]) -> int:
		self.num_of_islands = 0
		self.grid  = grid

		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "1":
					self.num_of_islands += self.dfs(i, j)
		return self.num_of_islands


	def dfs(self, row, col):

		if row < 0 or row > len(self.grid)-1 or col < 0 or col > len(self.grid[0])-1 or self.grid[row][col]=="0":
			return 0

		# Sink the entire island 
		self.grid[row][col] = "0"
		
		# DFS
		self.dfs(row-1, col)
		self.dfs(row+1, col)
		self.dfs(row, col-1)
		self.dfs(row, col+1)
		return 1
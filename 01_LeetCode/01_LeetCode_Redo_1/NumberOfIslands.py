"""
Date: 05/27/2020
NUMBER OF ISLANDS:
Given a 2d grid map of '1' s(land) and '0's (water), self.count the number of islands. An island is 
surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
may assume all four edges of the grid are all surrounded by water. 

Input:
	11110
	11010
	11000
	00000

Output:	1

Input:
	11000
	11000
	00100
	00011

Output: 3

Notes:
	Do not use recursion where loops are much simpler. 
	Use recursion to serve its purpose. (DFS only when necessary).
"""

class Solution:
	def __init__(self):
		self.grid  = None

	def numIslands(self, grid):
		if not grid or len(grid) == 0:
			return 0
		self.grid = grid
		row = len(self.grid)
		col = len(self.grid[0])
		numOfIslands = 0

		# 2D array iteration for every value. 
		for i in range(row):
			for j in range(col):
				if self.grid[i][j] == "1":
					numOfIslands += self.dfs(row, col, i, j)
		return numOfIslands

	# Helper recursive function that will iterate the island and sink it. 
	def dfs(self, row, col, i, j):
		if i < 0 or i > row-1 or j < 0 or j > col-1 or self.grid[i][j] == "0":
			return 0

		self.grid[i][j] = "0"
		self.dfs(row, col, i+1, j)
		self.dfs(row, col, i-1, j)
		self.dfs(row, col, i, j+1)
		self.dfs(row, col, i, j-1)
		return 1



# Test Cases
a = [["1", "0"], ["0", "1"], ["1", "1"]]
b = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
c = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
d = [["0", "1", "0"], ["1", "0", "1"], ["0", "1", "0"]]

x = Solution()
print(x.numIslands(a))
print(x.numIslands(b))
print(x.numIslands(c))
print(x.numIslands(d))
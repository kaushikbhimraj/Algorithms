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
	Tree recursion to traverse the array and self.count the number of islands

input:
	x = [
		 ["1", "1", "0", "0", "0"], 
		 ["1", "1", "0", "0", "0"], 
		 ["0", "0", "1", "0", "0"], 
		 ["0", "0", "0", "1", "1"]
		]

	d = [
		 ["0", "1", "0"], 
		 ["1", "0", "1"], 
		 ["0", "1", "0"]
		]
"""

class Solution:
	def __init__(self):
		self.grid  = None
		self.cache = {}
		self.count = 0

	def numIslands(self, grid):
		self.grid  = grid
		self.cache = {}
		self.count = 0
		self._helper(0, 0, "0")
		return self.count

	def _helper(self, i, j, prev):
		if i > len(self.grid)-1 or j > len(self.grid[0])-1:
			prev = "0"
			return

		curr = self.grid[i][j]
		key  = str(i)+str(j)

		if key in self.cache.keys():
			return

		print(key, "prev ->", prev, "curr ->", curr, "count ->", self.count)
		"""
		if i+1 < len(self.grid) and j-1 >= 0:
			if self.grid[i][j] == "1" and self.grid[i+1][j-1] == "1":
				return
		"""

		if prev == "0" and curr == "1":
			self.count += 1
		if curr == "1" and self.count == 0:
			self.count += 1

		self.cache[key] = key
		self._helper(i+1, j, curr)
		self._helper(i, j+1, curr)


a = [["1", "0"], ["0", "1"], ["1", "1"]]
b = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
c = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
d = [["0", "1", "0"], ["1", "1", "1"], ["0", "1", "0"]]

x = Solution()

"""
x.numIslands(a)
print(x.count)

x.numIslands(b)
print(x.count)

x.numIslands(c)
print(x.count)
"""
x.numIslands(d)
print(x.count)
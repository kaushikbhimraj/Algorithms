
"""
In a given self.grid, each cell can have one of three values:
	- value 0: empty cell
	- value 1: fresh orange
	- value 2: rotten orange

Every minute, any fresh orange that is adjacent (4-direcitonally) to a rotten orange becomes 
rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1 instead. 


Notes:
	This problem is very similar to the number of islands problem. 
	Not checking if all the cells 1 can get spoit

"""

class Solution:
	def __init__(self):
		self.grid = None

	def orangesRotting(self, grid):
		self.grid = grid
		num_of_mins = 0

		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):

				if self.grid[i][j] == 2:
					self.grid[i][j] = 0
					temp = self.bfs(self.grid, i, j)
					if temp > 0:
						num_of_mins = temp

		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):

				if self.grid[i][j] == 1:
					num_of_mins = -1
					break

		return num_of_mins

	# Will have to use a variant of BFS. 
	def bfs(self, grid, row, col):
		
		num_of_mins = -1
		queue = []
		queue.append([row, col])

		row_length = len(self.grid)
		col_length = len(self.grid[0])

		while queue:
			
			for i in range(len(queue)):
				row, col = queue.pop(0)

				if row-1 >= 0 and self.grid[row-1][col] == 1:
					self.grid[row-1][col] = 0
					queue.append([row-1, col])

				if row+1 < row_length and self.grid[row+1][col] == 1:
					self.grid[row+1][col] = 0
					queue.append([row+1, col])

				if col-1 >= 0 and self.grid[row][col-1] == 1:
					self.grid[row][col-1] = 0
					queue.append([row, col-1])

				if col+1 < col_length and self.grid[row][col+1] == 1:
					self.grid[row][col+1] = 0
					queue.append([row, col+1])
			num_of_mins += 1

			print(num_of_mins, queue)
		return num_of_mins 


a = [[2,1,1],[1,1,0],[0,1,1]]
b = [[2,1,1],[0,1,1],[1,0,1]]
c = [[0,2]]
d = [[0]]
e = [[1],[2],[2]]
f = [[2],[1],[1],[1],[2],[1],[1]]
g = [[2,2],[1,1],[0,0],[2,0]]

x = Solution()
"""
print(x.orangesRotting(a))
print("\n")
print(x.orangesRotting(b))
print("\n")
print(x.orangesRotting(c))
print("\n")
print(x.orangesRotting(d))
print("\n")
print(x.orangesRotting(e))
print("\n")
print(x.orangesRotting(f))
print("\n") 
"""
print(g)
print(x.orangesRotting(g))
print("\n") 

"""
[
	[2,1,1],
	[0,1,1],
	[1,0,1]
]
"""
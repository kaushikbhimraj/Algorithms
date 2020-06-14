
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
	But the change in logic that we are finding all the neighbors around the rotten oranges and then proceeding
	to the next level. 

	Use BST. 
	But here rather than using a queue to keep track of all the values, you will have to traverse through the
	grid to cache coordinates of all rotting oranges and oranges that are fresh. 

	Use the arrays with the rotting oranges to find its immediate neighbors and them to the rotting array. 
	Then take 
"""

class Solution:

	# Declaring global parameters to improve space comp. 
	def __init__(self):
		self.count   = None
		self.grid    = None
		self.fresh   = None

	def orangesRotting(self, grid) -> int:

		# Since sequence is important for the BST, the rotten will be cache in an array. 
		# Fresh oranges will be cached in a hashmap to check only for remaining stranglers. 
		self.grid    = grid
		self.fresh   = {}
		rotting      = []
		count        = 0
		
		# Seperating fresh and rotten oranges and caching their coordinates. 
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):

				if self.grid[i][j] == 2:
					rotting.append([i,j])

				elif self.grid[i][j] == 1:
					self.fresh[str(i)+str(j)] = str(i)+str(j)

		# The first batch of rotten oranges will go to BST. 
		# The BST will return the neighbors of these. 
		# Feeding the children back into BST for its children. 
		# Each cycle will be counted. 
		while rotting:
			rotting = self.bst(rotting)
			print(rotting)

			if len(rotting) == 0:
				break
			count += 1

		# Check for any remaining fresh oranges. 
		if self.fresh:
			return -1

		return count 

	# Internal queue will be used to reset return only the children. 
	# Deleting coordinates from the fresh cache once they are rotting. 
	def bst(self, rotting):
		queue = []
		for row,col in rotting:
			if row-1 >= 0 and self.grid[row-1][col] == 1:
				self.grid[row-1][col] = 2
				del self.fresh[str(row-1)+str(col)]
				queue.append([row-1, col])

			if row+1 < len(self.grid) and self.grid[row+1][col] == 1:
				self.grid[row+1][col] = 2
				del self.fresh[str(row+1)+str(col)]
				queue.append([row+1, col])

			if col-1 >= 0 and self.grid[row][col-1] == 1:
				self.grid[row][col-1] = 2
				del self.fresh[str(row)+str(col-1)]
				queue.append([row, col-1])

			if col+1 < len(self.grid[0]) and self.grid[row][col+1] == 1:
				self.grid[row][col+1] = 2
				del self.fresh[str(row)+str(col+1)]
				queue.append([row, col+1])
		return queue



# Unit Tests
a = [[2,1,1],[0,1,1],[1,0,1]]
b = [[2,1,1],[1,1,0],[0,1,1]]

x = Solution()
print(x.orangesRotting(a))
print("\n")
print(x.orangesRotting(b))

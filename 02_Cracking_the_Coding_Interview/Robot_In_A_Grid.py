
"""
RECURSIVE AND DYNAMIC PROGRAMMING

Question 8.2
Imagine a robot sitting on the upper left conrner of grid with r rows and c columns. The robot can only move in 
two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design
an algorithm to find the path for the robot from the top left to the bottom right.
"""

class RobotInGrid:
	def __init__(self):
		self.cache = {}
		self.path  = ""
		self.grid  = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
					  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
					 ]

	def findPath(self, row, col):

		if row > len(self.grid)-1 or col > len(self.grid[0])-1:
			return

		coordinates = "(" + str(row) + ", " + str(col) + ")"
		if coordinates in self.cache:
			return

		if row == len(self.grid)-1 and col == len(self.grid[0])-1:
			print(self.path + coordinates)

		self.findPath(row+1, col)
		self.findPath(row, col+1)

		self.path += coordinates + ", "
		print(self.path)
		self.cache[coordinates] = coordinates


# Driver Code
print(RobotInGrid().findPath(0,0))


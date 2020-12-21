"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a 
knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares 
in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is 
guaranteed the answer exists.

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
"""

# Time: log()
# Space: 

class Solution:
	# This problem can be solved using breadth first search. 
	# Need a queue to append each layer from position. 
	# Also need to keep track of all positions that have been visited.
	def minKnightMoves(self, x:int, y:int) -> int:

		que = collections.queue()
		visited = set()

		# The starting position is always from the origin. 
		# Third value in que counts the layers until reaching target. 
		que.append((0,0,0))
		visited.add((0,0))

		# Iterating through queue. 
		while que:
			a, b, steps = que.popleft()

			if (a == x and b == y):
				return steps

			# All the next positions from current location is loaded into queue. 
			for i,j in [(-2,-1),(-1,-2),(-2,1),(1,-2),(-1,2),(2,-1),(1,2),(2,1)]:

				if (a+i,b+j) in visited:
					continue

				que.append(a+i, b+j, steps+1)
				visited.add(a+i, b+j)

	# Due to there being 4 quadarants we're having to search 8 times for each position. 
	# But all four quadrants are projections of one and the position will be same everywhere if 
	# we don't consider the signs. 
	def minKnightMoves2(self, x:int, y:int) -> int:

		x, y = abs(x), abs(y)

		# Handle exceptions when position is either origin or (1,1)
		if x + y == 0:
			return 0

		if x + y == 2:
			return 2

		# Starting from x, y we can go the reverse order until we hit the origin. 
		que = collections.queue()
		visited = set()

		# Add destination to queue and set. 
		que.append((x, y, 0))
		visited.add((x, y))

		while que:
			a, b, steps = que.popleft()

			if (a == 0 and b == 0):
				return steps

			for i, j in [(-2,-1),(-1,-2)]:
				ii, jj = abs(a + i), abs(b + j)
			
				if (ii, jj) in visited:
					continue

				que.append((ii, jj, steps + 1))
				visited.add((ii, jj))
"""
Spiral Traverse
Write a function that takes in an nxm two dimensional array (that can be square-shaped
when n==m) and returns a one dimensional array of all the array's elements in a spiral 
order. 

Spiral order starts at the top left corner of the two-dimensional array, goes to the 
right, and proceeds in a spiral pattern all the way until every element has been 
visited. 

INPUT:
array = [
		 [01, 02, 03, 04],
		 [12, 13, 14, 05],
		 [11, 16, 15, 06],
		 [10, 09, 08, 07]
		]

OUTPUT:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


NOTE TO SELF:
	Make sure you get the start and stop for the FOR loops inside the main loop. 
	MOST IMPORTANT 
"""

class Solution:
	def spiralTraverse(self, array):
		spiral = []

		# Shrink the perimeter inwards every iteration. 
		# Have loop to traverse each side of the perimeter before moving inwards.
		row_start = 0
		row_end   = len(array) - 1

		col_start = 0
		col_end   = len(array[0]) - 1

		# row_start and row_end should overlap and loop shall be broken at line 50 and 55. 
		# We need this to break out when there is only one value left. 
		while row_start <= row_end and col_start <= col_end:

			for i in range(col_start, col_end+1):
				spiral.append(array[row_start][i])

			for i in range(row_start+1, row_end+1):
				spiral.append(array[i][col_end])

			for i in reversed(range(col_start, col_end)):
				if row_start == row_end:
					break
				spiral.append(array[row_end][i])

			for i in reversed(range(row_start+1, row_end)):
				if col_start == col_end:
					break
				spiral.append(array[i][col_start])


			row_start += 1
			row_end -= 1

			col_start += 1
			col_end	-= 1

		return spiral


a = [[1, 2, 3, 4],[12, 13, 14, 5],[11, 16, 15, 6],[10, 9, 8, 7]]
x = Solution()
print(x.spiralTraverse(a))





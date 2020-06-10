"""
Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n==m) and returns 
a one dimensional array of all the array's elements in spiral order. 

Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a 
spiral parttern all the way until every element has been visited.

INPUT
array = [
	[1, 2, 3, 4],
	[12, 13, 14, 5],
	[11, 16, 15, 6],
	[10, 9, 8, 7],
] 

OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

class Solution:
	def spiralTraverseLoop(self, array):
		results = []
		rowS, rowE = 0, len(array)-1
		colS, colE = 0, len(array[0]) - 1

		while rowS <= rowE and colS <= colE:

			for i in range(colS, colE+1):
				results.append(array[rowS][i])

			for i in range(rowS+1, rowE+1):
				results.append(array[i][colE])

			for i in reversed(range(colS, colE)):
				if rowS == rowE:
					break
				results.append(array[rowE][i])

			for i in reversed(range(rowS+1, rowE)):
				if colS == colE:
					break
				results.append(array[i][colS])

			rowS += 1
			rowE -= 1
			colS += 1
			colE -= 1

		return results

	def spiralTraverseRecursive(self, array):
		pass


a = [
		[1, 2, 3, 4],
		[12, 13, 14, 5],
		[11, 16, 15, 6],
		[10, 9, 8, 7]
	]
x = Solution()
print(x.spiralTraverseLoop(a))
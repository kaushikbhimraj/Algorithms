"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix
in spiral order. 

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

class Solution():
	def spiralOrder(self, matrix):

		# Capturing the edge-cases
		if not matrix:
			return matrix

		# Initializing start position of rows and columns
		# Initializing array to store the values reached by iteration. 
		straighten_out = []
		row_start = 0
		row_end   = len(matrix)-1
		col_start = 0
		col_end   = len(matrix[0])-1

		# Traversing each perimeter before going inwards. 
		while row_start <= row_end and col_start <= col_end:

			for i in range(col_start, col_end+1):
				straighten_out.append(matrix[row_start][i])

			for i in range(row_start+1, row_end+1):
				straighten_out.append(matrix[i][col_end])

			for i in reversed(range(col_start, col_end)):
				if row_start == row_end:
					break
				straighten_out.append(matrix[row_end][i])

			for i in reversed(range(row_start+1, row_end)):
				if col_start == col_end:
					break
				straighten_out.append(matrix[i][col_start])

			row_start += 1
			row_end   -= 1

			col_start += 1
			col_end   -= 1

		return straighten_out


# Test cases
a = [[1, 2, 3, 4],[12, 13, 14, 5],[11, 16, 15, 6],[10, 9, 8, 7]]
b = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]

x = Solution()
print(x.spiralOrder(a))
print(x.spiralOrder(b))


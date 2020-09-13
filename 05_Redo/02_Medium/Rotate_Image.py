class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    	# Matrix can be rotates 90 degrees by simply taking the transpose and reversing each row. 

    	# Transpose of matrix
    	for i in range(len(matrix)):
    		for j in range(i, len(matrix[0])):
    			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    	# Reversing each row. 
    	for i in range(len(matrix)):
    		matrix[i] = reversed(matrix[i])
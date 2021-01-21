

"""
LC: 48 Rotate Image
Given an image represented as a 2D array of pixels, return the image rotation ninety degrees.

Ex: Given the following image…

image = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
], return the image such that it's been modified as follows...
[
    [16,13,10],
    [17,14,11],
    [18,15,12]
]

Step 1: Switch each element in row with element in column around diagonal.
Step 2: Reverse each row in matrix. 
Step 3: Return matrix. 

T: O(mn), S: O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse all rows in matrix. 
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i])-1
            while (l < r):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
        return matrix
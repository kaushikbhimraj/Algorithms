"""
LC. 867 - Transpose Matrix
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column 
indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 
Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000

Solution:
There are two cases for solving this. 
    Case 1: When matrix is square. 
            Switch row and col around diagonal. 
    Case 2: When matrxi is a rectange. 
            Have to create a new matrix and add element in each columns into 
            the row of new matrix    

T: O(mn); S: O(mn)
"""

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row, col = len(A), len(A[0])
        
        # Case 1:
        if ( row == col ):
            for i in range(row):
                for j in range(i, col):
                    A[i][j], A[j][i] = A[j][i], A[i][j]
            return A
        
        # Case 2:
        res = []
        for i in range(col):
            new = []
            for j in range(row):
                new.append(A[j][i])
            res.append(new)
        return res
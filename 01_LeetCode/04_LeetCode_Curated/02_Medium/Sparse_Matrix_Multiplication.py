"""
Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 
Constraints:
1 <= A.length, B.length <= 100
1 <= A[i].length, B[i].length <= 100
-100 <= A[i][j], B[i][j] <= 100
"""

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        # Helper function to multiply row with column. 
        def multiply(x, y):
            temp = 0
            for i in range(len(x)):
                temp += x[i] * y[i]
            return temp 
        
        # Get dimensions of A and B. 
        a_row, a_col = len(A), len(A[0])
        b_row, b_col = len(B), len(B[0])
        
        # Create an output matrix the size of [a_row x b_col]
        res = [[0] * b_col for _ in range(a_row)]
        
        # Iterate through each row of A and then each column of B.
        # Create an array out of value at column in each row in B.
        # Using helper function to multiply values in the row and col.
        for i in range(a_row):
            for j in range(b_col):
                res[i][j] = multiply(A[i], [B[r][j] for r in range(b_row)])
        
        return res

	# Line 84: Multiply each value in A with each row in B and sum up those value in res array.  
    def multiply2(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        a_row, a_col = len(A), len(A[0])
        b_row, b_col = len(B), len(B[0])
        
        res = [[0] * b_col for _ in range(a_row)]
        for i in range(a_row):
            for j in range(a_col):
                if A[i][j] != 0:

                    for k in range(b_col):
                        if B[j][k] != 0:
                            res[i][k] += A[i][j] * B[j][k]
        return res
                            
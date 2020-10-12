"""
Given a matrix of m x n elements (m rows, n columns), return all elements 
of the matrix in spiral order.

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

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Output array to store values.
        results = []
        
        # Edge case
        if not matrix or len(matrix) == 0:
            return results
        
        # One external loop to decrement each layer of the matrix. 
        # Four internal loops for each side of the matrix. 
        
        row_top = 0
        row_bot = len(matrix) - 1
        
        col_left = 0
        col_right = len(matrix[0]) - 1
        
        while row_top <= row_bot and col_left <= col_right:
            
            # Traverse top
            for i in range(col_left, col_right+1):
                results.append(matrix[row_top][i])
            
            # Traverse right
            for i in range(row_top+1, row_bot+1):
                results.append(matrix[i][col_right])
            
            # Traverse bot (right to left)
            for i in reversed(range(col_left, col_right)):
                if row_top == row_bot:
                    break
                results.append(matrix[row_bot][i])
            
            # Traverse left
            for i in reversed(range(row_top+1, row_bot)):
                if col_left == col_right:
                    break
                results.append(matrix[i][col_left])
                
            row_top += 1
            row_bot -= 1
            col_left += 1
            col_right -= 1
        
        return results
            
                
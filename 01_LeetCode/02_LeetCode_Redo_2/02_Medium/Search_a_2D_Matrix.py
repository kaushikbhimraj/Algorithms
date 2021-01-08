"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix 
has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Using two sub-functions. 
        
        # First to find the row within which the element is bound. 
        # Binary search is modified and the condition for check whether
        # the first value is less than or equal to target and the last element is 
        # row is greater than or equal to target. (To confirm whether the value is in row)
        def findRow():
            left = 0
            right = len(matrix)-1
            
            while left <= right:
                mid = left + right
                
                if target >= matrix[mid][0] and matrix[mid][-1] >= target:
                    return mid
                
                if target > matrix[mid][0]:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        # Second to find the target element in that row. 
        # Straight forward binary search. Gotta remember the while condition to be left <= right. 
        # The two pointers should overlap to find the element here. 
        def findElement():
            left = 0
            right = len(matrix[0])-1
            
            while left <= right:
                mid = left + right
                
                if target == matrix[row][mid]:
                    return True
                
                elif target < matrix[row][mid]:
                    right = mid - 1
                
                else:
                    left = mid + 1
            return False
        
        # START OF PROGRAM. 
        # Make sure matrix is not empty of contains subarray with single '0'
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        row =  findRow()
        if row == -1:
            return False
        return findElement()

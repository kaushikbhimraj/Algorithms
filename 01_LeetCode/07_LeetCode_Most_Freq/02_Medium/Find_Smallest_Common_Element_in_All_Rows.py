"""
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest 
common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.
"""

# T: O(m*n*log(n)) where m is number of rows and n is number of cols in matrix. 
# S: O(1)
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # Find max value in the first row. 
        rowval = 0
        maxval = 0
        for i in range(len(mat)):
            if maxval < mat[i][0]:
                maxval = mat[i][0]
                rowval = i

        for j in range(len(mat[rowval])):
            state = True
            for k in range(len(mat)):
                if k == rowval:
                    continue
                state = state and self.binarySearch(mat[k], mat[rowval][j])
            
            if state:
                return mat[rowval][j]
        return -1        
    
    # Helper for binary search. 
    def binarySearch(self, row, target) -> bool:
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
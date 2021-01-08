"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to
 adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total 
number of rows in the triangle.
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from bottom, n-1 row, then traverse each element in row, 
        # and replace it with sum of min between element at [row+1][col], [row+1][col+1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j+1], triangle[i+1][j])
        
        # The top most value is bound to return the least sum in the triangle. 
        return triangle[0][0]
        
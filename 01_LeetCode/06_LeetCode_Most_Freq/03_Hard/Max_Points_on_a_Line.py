"""
Given n points on a 2D plane, find the maximum number of points that lie on the same 
straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code 
definition to get new method signature.
"""

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        def factor(x, y):
            d = gcd(x, y)
            return (x//d, y//d)
        
        # Iterate through each point and then iterate through all other points. 
        n = len(points)
        count = 0
        
        # Store slopes in the dictionary. 
        # Reset the horizontal lines and dictionary for the nested loop. 
        for i in range(n):
            same = 0
            lines = {'i': 1}
            
            for j in range(i+1, n):
                nx, ny = points[j][0], points[j][1]
                mx = points[i][0] - nx
                my = points[i][1] - ny
                
                # If same ordered set. 
                if mx == 0 and my == 0:
                    same += 1
                    continue
                    
                # If line is horizontal                
                if my == 0:
                    slope = "i"
                else:
                    slope = factor(mx, my)
                    
                # Check if slope is already present. 
                if slope not in lines:
                    lines[slope] = 1
                lines[slope] += 1
                
            # Update the main count in the outer loop. 
            count = max(count, max(lines.values()) + same)
        return count
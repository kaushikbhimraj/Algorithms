"""
LC: 994 Rotting Oranges

Step 1: Traverse grid and keep track of 
            rotten in array
            fresh in set
Step 2: Traverse rotten array and implement BFS

Step 3: Count += 1 for each level of BFS and return the count. 

Note: Return count only if there is no fresh oranges left.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Create a dictionary to hold locations for all fresh oranges. 
        # Hold locations of all rotten oranges in an array. 
        fresh = set()
        rotten = []
        
        # Add the positions of rotten and fresh oranges into data structures.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if (grid[i][j] == 2):
                    rotten.append((i, j))
                
                elif (grid[i][j] == 1):
                    fresh.add((i, j))
        
        # With count as zero. 
        # Initialize the BFS starting with the positions of rotten oranges.
        # At any point if there are no rotten oranges left in basket, break out of loop. 
        count = 0
        while (rotten):
            row = len(grid)
            col = len(grid[0])
            
            for i in range(len(rotten)):
                x, y = rotten.pop(0)
                
                if ( x-1 >= 0 and grid[x-1][y] == 1 ):
                    grid[x-1][y] = 2
                    fresh.discard((x-1, y))
                    rotten.append((x-1, y))
                    
                if ( x+1 < row and grid[x+1][y] == 1 ):
                    grid[x+1][y] = 2
                    fresh.discard((x+1, y))
                    rotten.append((x+1, y))
                
                if ( y-1 >= 0 and grid[x][y-1] == 1 ):
                    grid[x][y-1] = 2
                    fresh.discard((x, y-1))
                    rotten.append((x, y-1))
                
                if ( y+1 < col and grid[x][y+1] == 1):
                    grid[x][y+1] = 2
                    fresh.discard((x, y+1))
                    rotten.append((x, y+1))
            
            # Check rotten basket to break. 
            if not rotten:
                break
            count += 1
        
        # Lastly check if there are anymore fresh oranges left. 
        return -1 if (fresh) else count
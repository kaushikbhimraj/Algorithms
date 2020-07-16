class Solution:
    def __init__(self):
        self.grid = None
        self.freshOranges = None
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        self.grid = grid
        
        # Store the index of 2s and 1s in arrays.
        self.freshOranges = {}
        rottenOranges = []
                 
        # Traverse through the grid until you come across a rotten mango.
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 2:
                    rottenOranges.append([i,j])
                elif self.grid[i][j] == 1:
                    self.freshOranges[str(i) + str(j)] = str(i) + str(j)
                    
        
        # Once all oranges have been grouped, use the rotten oranges as starts for BST. 
        while rottenOranges:
            rottenOranges = self.orangeRottingHelper(rottenOranges)
            if not rottenOranges:
                break
            count += 1
        
        if self.freshOranges:
            return -1
        
        return count
        
    # Helper function to implement BST. 
    def orangeRottingHelper(self, rottenOranges):
        temp_queue = []
        
        # Go through all rotten oranges in list and add only fresh oranges around them in a new queue.
        for row, col in rottenOranges:
            
            if row-1 >= 0 and self.grid[row-1][col] == 1:
                self.grid[row-1][col] = 2
                del self.freshOranges[str(row-1)+str(col)]
                temp_queue.append([row-1, col])
            
            if row+1 < len(self.grid) and self.grid[row+1][col] == 1:
                self.grid[row+1][col] = 2
                del self.freshOranges[str(row+1)+str(col)]
                temp_queue.append([row+1, col])
            
            if col-1 >= 0 and self.grid[row][col-1] == 1:
                self.grid[row][col-1] = 2
                del self.freshOranges[str(row)+str(col-1)]
                temp_queue.append([row, col-1])
            
            if col+1 < len(self.grid[0]) and self.grid[row][col+1] == 1:
                self.grid[row][col+1] = 2
                del self.freshOranges[str(row)+str(col+1)]
                temp_queue.append([row, col+1])
            
        return temp_queue

#include <iostream>
#include <vector>

class Solution {
    private:
    void helper(std::vector<std::vector<char>>& grid, int i, int j){
        int row = grid.size();
        int col = grid[0].size();
        
        grid[i][j] = '0';
        if (i + 1 < row && grid[i+1][j] == '1') helper(grid, i+1, j);
        if (i - 1 >= 0  && grid[i-1][j] == '1') helper(grid, i-1, j);
        if (j + 1 < col && grid[i][j+1] == '1') helper(grid, i, j+1);
        if (i - 1 >= 0  && grid[i][j-1] == '1') helper(grid, i, j-1);
    }

    public:
    int numIslands(std::vector<std::vector<char>>& grid) {
        int count = 0;
        for (int i=0; i<grid.size(); i++){
            for (int j=0; j<grid[0].size(); i++){
                if (grid[i][j] == '1'){
                    ++count;
                    helper(grid, i, j);
                }
            }
        }
        return count;
    }
};

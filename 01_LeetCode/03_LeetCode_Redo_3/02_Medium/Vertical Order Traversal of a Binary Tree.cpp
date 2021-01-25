#include <iostream>
#include <vector>
#include <map>
#include <set>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    public:
    std::vector<std::vector<int>> verticalTraversal(TreeNode* root) {

        // Create a 2-d map that has a set inside the second map as the second. 
        // DFS search tree and populate the order map with all its values. 
        std::map<int, std::map<int, std::set<int>>> order;
        helperDFS(root, 0, 0, order);

        // Main part of this problem is to output the values in the proper format. 
        std::vector<std::vector<int>> res;
        for (auto col : order){
            
            std::vector<int> colArr;
            for (auto row : col.second){
                colArr.insert(colArr.end(), row.second.begin(), row.second.end());
            }
            res.push_back(colArr);
        }
        return res;
    }

private:
    void helperDFS(TreeNode* root, int col, int row, std::map<int, std::map<int, std::set<int>>>& order){
        if (!root) return;
        order[col][row].insert(root -> val);
        helperDFS(root -> left, col - 1, row + 1, order);
        helperDFS(root -> right, col + 1, row + 1, order);
    }

};


int main(){
    Solution x;
    // Unit test
}
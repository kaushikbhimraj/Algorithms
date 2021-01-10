#include <iostream>
#include <vector>
#include <queue>

struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
};

class Solution{
public:
    std::vector<int> rightSideView(TreeNode* root){
        if (!root){
            return {};
        }
        //Store the right most node from the tree at each level in another array. 
        std::vector<int> rightSide;

        //Queue for BST
        std::queue<TreeNode*> todo;
        todo.push(root);

        // Pop all elements in queue that are from a certain level. 
        // Add only the last element to the output array . 
        while (!todo.empty()){
            int n = todo.size();

            for (int i=0; i<n; i++){
                TreeNode* node = todo.front();
                todo.pop();

                if (i == n-1){
                    rightSide.push_back(node->val);
                }
                if (node->left){
                    todo.push(node->left);
                }
                if (node->right){
                    todo.push(node->right);
                }
            }
        }
        return rightSide;
    }
};

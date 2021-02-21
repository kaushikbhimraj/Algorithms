/**
You are given the root of a binary tree with n nodes where each node in the tree has node.val 
coins and there are n coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another. (A 
move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:
Input: root = [3,0,0]
Output: 2

Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };

 * T: O(n); S: O(k) where n is number of coins, k is maximum depth of tree.
 */
#include <iostream>

class Solution {
public:
    int moves = 0;
    int distributeCoins(TreeNode* root) {
        dfs(root);
        return moves;
    }
    
    int dfs(TreeNode* root) {
        if (!root) return 0;
        int left = dfs(root->left);
        int right = dfs(root->right);
        moves = moves + std::abs(left) + std::abs(right);
        return root->val + left + right - 1;
    }
};
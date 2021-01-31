class Solution {
public:
    // Create a DP array size [coins.size(), amount]
    vector<vector<int>> dp;
    
    int coinChangeHelper(vector<int>& coins, int n, int amount){
        if (n == 0) return 0;
        
        if (amount == 0) return 1;
        
        if (dp[n][amount] != -1) return dp[n][amount];
        
        if (coins[n-1] > amount){
            dp[n][amount] = coinChangeHelper(coins, n-1, amount);
            return dp[n][amount];
        }
        
        dp[n][amount] = coinChangeHelper(coins, n, amount - coins[n - 1]) + coinChangeHelper(coins, n - 1, amount);
        return dp[n][amount];
    }
        
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        
        if (n == 0) return 0;
        if (amount == 1) return 1;
        
        dp.resize(n+2,vector<int>(amount+2, -1));
        dp[n][amount] = coinChangeHelper(coins, n, amount);
        
        return dp[n][amount];
    }
};
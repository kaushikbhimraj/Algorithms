/*
You are given coins of different denominations and a total amount of money. Write a function to 
compute the number of combinations that make up that amount. You may assume that you have infinite 
number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10] 
Output: 1

Note:
You can assume that
0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
*/

#include <iostream>
#include <vector>

class Solution {
    public:

    // T: O(2^N); S: O(1) where N is depth of recursion stack.
    // Following code uses recursion to find all the possible combinations. 
    // When amount is zero we have a combination. 
    // WHen the pointer n (goes from right to left in the coins array) is zero then we have reached the end of array (not necessaryly 
    // found a combination, so we return a 0)
    int coinChangeRecur(std::vector<int>& coins, int amount){
        int n = coins.size();
        if (n == 0) return 0;
        if (amount == 0) return 1;
        return coinChangeRecurHelper(coins, n, amount);
    }

    // T: O(n * amount); S: O(n * amount)
    // Recursion would also follow the same edge case rules as above.
    // Check if element at n-1 is greater than amount, if so pointer to left and go a level deeper in recursion stack. 
    // There are two problems to solve in this 
    //      1. check if coin at n-1 can be used repeatedly to decrement amount. 
    //      2. check the next coin in the coins by decrementing the pointer n.
    int coinChangeRecurHelper(std::vector<int>& coins, int n, int amount){
        if (n == 0) return 0;
        if (amount == 0) return 1;
        if (coins[n-1] > amount) return coinChangeRecurHelper(coins, n - 1, amount);
        return coinChangeRecurHelper(coins, n, amount - coins[n-1]) + coinChangeRecurHelper(coins, n - 1, amount);
    }

    // METHOD 2: 
    // Create a 2-D array that would hold the values where rows -> 0 to coins.size() and columns -> 0 to amount. 
    // We could use this to check if value already exists, if (dp[n][amount] != -1) return dp[n][amount];
    std::vector<std::vector<int>> dp;
    int changeMemo(int amount, std::vector<int>& coins) {
        int n = coins.size();
        if (amount == 0) return 1;
        if (n == 0) return 0;
        
        dp.resize(n+2, std::vector<int>(amount + 2, -1));
        dp[n][amount] = changeMemoHelper(coins, n, amount);
        return dp[n][amount];
    }
    
    int changeMemoHelper(std::vector<int>& coins, int n, int amount){
        if (amount == 0) return 1;
        if (n == 0) return 0;
        if (dp[n][amount] != -1) return dp[n][amount];

        // Similar to line 28, but rather than simply returning the output, update the dp array 
        // and then return the element at n, amount.
        if (coins[n-1] > amount){
            dp[n][amount] = changeMemoHelper(coins, n-1, amount);
            return dp[n][amount];
        }
        
        dp[n][amount] = changeMemoHelper(coins, n, amount - coins[n - 1]) + changeMemoHelper(coins, n - 1, amount);
        return dp[n][amount];
    }
};
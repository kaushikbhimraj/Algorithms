"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

# Time:  O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Basically thought of storing the value in a dp array. 
        # Then optimized it to store value in a min variable. 
        minValue = prices[0]
        profit = 0
        maxProfit = 0
        
        # Min value is only update when prices[i] - minValue < 0. 
        # Every iteration max profit is updated. 
        for i in range(1, len(prices)):
            
            profit = prices[i] - minValue
            if profit < 0:
                minValue = prices[i]
            else:
                maxProfit = max(profit, maxProfit)
            
        return maxProfit if maxProfit > 0 else 0
            
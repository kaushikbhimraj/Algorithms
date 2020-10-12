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

class Solution:

	# Brite force - > Time: O(n**2) Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = float("-inf")
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])
        return maxProfit if maxProfit > 0 else 0

    # Find the global minimum in price first 
    # Make sure every time value of minimum is updated in loop, reset max price to zero
    def maxProfit(self, prices: List[int]) -> int:
        maxNet = 0
        
        minPrice = float("inf")
        maxPrice = float("-inf")
        
        for i in range(len(prices)):
            
            # Reset max prices when new  minimum is found.
            if minPrice > prices[i]:
                maxPrice = 0
                minPrice = prices[i]
            
            # Update maximum profit every iteration.
            maxPrice = max(maxPrice, prices[i])
            maxNet = max(maxNet, maxPrice-minPrice)
        
        return maxNet
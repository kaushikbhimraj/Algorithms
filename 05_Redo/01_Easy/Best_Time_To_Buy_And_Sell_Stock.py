"""
		[7 	1 	5 	3 	6	4]

		[0	0	4	2	5	3]

		state[i] = max(state[i-1] + prices[i] - prices[i-1], 0)
"""

class Solution:
    def maxProfit(self, prices):
        
        # Track minimum and difference of min and current price
        # for every iteration
        minprice = float("inf")
        maxprofit = 0
        
        for i in range(len(prices)):
            
            # Update min and max profit
            minprice = min(minprice, prices[i])
            maxprofit = max(maxprofit, prices[i] - minprice)
        
        # MaxProfit will return the maximum profit. 
        return maxprofit

    def maxProfitDP(self, prices):

    	# Store all max differences in one array. 
    	dp = [0]*len(prices)

    	# Store max of previous state and current difference in current state. 
    	for i in range(1, len(prices)):
    		dp[i] = max(dp[i-1] + prices[i] - prices[i-1], 0)

    	# Return maxprofit
    	return max(dp)




a = [7,1,5,3,6,4]

x = Solution()
print(x.maxProfit(a))
print(x.maxProfitDP(a))
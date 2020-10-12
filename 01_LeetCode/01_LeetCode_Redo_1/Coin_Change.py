"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that 
amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.

"""
class Solution:
	def coinChange(self, coins, amount):
		
		# Create a 1-D dp with the size of the amount, to store coin change for each value of the amount. 
		dp = [0] + [float("inf")] * amount

		# Iterate through each coin
		# Then iterate through coin to amount and store all substractions between i - coin. 
		for coin in coins:
			print("\n")
			for i in range(coin, amount+1):
				print(coin, i)
				dp[i] = min(dp[i], 1 + dp[i - coin])


		# Return the last value in the dp table
		# The value is float("inf") then there wasn't any change for the amount. 
		return dp[-1] if dp[-1] != float("inf") else -1


a = [1,2,5]
b = 11

x = Solution()
print(x.coinChange(a, b))
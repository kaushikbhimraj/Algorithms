"""
You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.
"""

class CoinChangeRecursion:
	def change(self, amount, coins):
		if (amount == 0):
			return 1

		if (len(coins) == 0):
			return 0

		return self.change_helper(amount, coins, len(coins))

	def change_helper(self, amount, coins, idx):
		if (idx == 0):
			return 0;

		if (amount == 0):
			return 1

		if (coins[idx] > amount):
			return self.change_helper(amount, coins, idx-1);

		return self.change_helper(amount-coins[idx], coins, idx) + self.change_helper(amount, coins, idx-1)

class CoinChangeMemoization:
	def change(self, amount, coins):
		return

	def change_helper(self, amount, coins, idx, book):
		return


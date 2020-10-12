"""
Climbing stairs

You are climbing a stair case, it takes n steps to reach to the top. 
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Give n will be a positive integer. 

Example: 

input:  2
output: 2

Explanation:
there are two ways to climb to the top
1 + 1
2

input:  3
output: 3
there are three ways to climb to the top
1 + 1 + 1
1 + 2
2 + 1

The logic is very similar to a fibonnaci logic wherein the numbers are broken down
using a recursive method. The computation stack can get pretty big so we manage that using
memoization. 
"""

class prob_70:
	def __init__(self):
		self.memo = {}
	def climbStairs(self, n: int) -> int:
		try:
			return self.memo[n]
		except KeyError:
			if n < 2:
				return 1
			self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
		return self.memo[n]

print(prob_70().climbStairs(23))

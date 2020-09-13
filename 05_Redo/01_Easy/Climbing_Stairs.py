"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution:
    # Use memoization to store results from recursion tree. 
    def __init__(self):
        self.cache = {}
        
    def climbStairs(self, n: int) -> int:
        
        # Base case -> if no steps you found a way!
        if (n == 0):
            return 1
        
        # If steps are negative, it is no longer valid. 
        if (n < 0):
            return 0
        
        # Every recursive stack, check if value in cache.
        if n in self.cache:
            return self.cache[n]
        
        # Recursion with n-1 and n-2 
        self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # Return nth key from cache. 
        return self.cache[n]
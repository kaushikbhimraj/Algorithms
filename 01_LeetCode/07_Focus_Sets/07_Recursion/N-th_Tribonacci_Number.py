"""
# 1137 - 
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        self.memo = {}
        return self.helper(n)
    
    def helper(self, n):
        if (n == 0):
            return 0
        
        if (n <= 2):
            return 1
        
        if (n in self.memo):
            return self.memo[n]
        
        self.memo[n] = self.helper(n-1) + self.helper(n-2) + self.helper(n-3)
        return self.memo[n]
        
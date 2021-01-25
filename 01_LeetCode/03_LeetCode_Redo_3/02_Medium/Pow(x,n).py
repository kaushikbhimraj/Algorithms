"""
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 
Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

T: O(log n)l S: O(1)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (n < 0):
            y = self.helper(x, -n)
            return 1/y
        else:
            return self.helper(x, n)
        
        
    def helper(self, x, n):
        # There are three cases to cover here. 
        # n = 0, n is EVEN & n is ODD. 
        
        if (n == 0):
            return 1
        
        if (n % 2 == 0):
            y = self.helper(x, n/2)
            return y * y
        
        else:
            return x * self.helper(x, n-1)
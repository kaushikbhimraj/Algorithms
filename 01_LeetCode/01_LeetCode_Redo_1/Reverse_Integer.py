"""
Given a 32-bit singed integer, reverse digits of an integer. 

input:   123
output:  321

input:  -123
output: -321

input:   120
output:   21

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Solution:
1    2    3 
100  10   0

300
 20
+ 1
---
321
"""
class Solution:
    def reverse(self, x: int) -> int:
    	exp = 0
    	temp = 0
    	if x < 0:
    		x = -(x)
    		temp = 1

    	y = x
    	while y > 0:
    		y //= 10
    		exp += 1

    	if temp:
    		return -(self._helper(exp, x))
    	return self._helper(exp, x)

    def _helper(self, exp, x):
    	total = 0
    	while x > 0:
    		total += (x % 10) * (10 ** (exp-1))
    		exp -= 1
    		x //= 10

    	if total > (2**31 -1):
    		return 0
    	return total

num = [123, -123, 120000000, 900000, 10, 1534236469]
expected = [321, -321, 21, 9, 1, 0]

for i,n in enumerate(num):
	print(n, expected[i], Solution().reverse(n))


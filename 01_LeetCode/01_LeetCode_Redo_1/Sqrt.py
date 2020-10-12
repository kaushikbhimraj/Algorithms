"""
Implement int sqrt(int x)

Compute and return the sqaure root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
input:  4
output: 2

input:  8
output: 2

Explanation: The square root of 8 is 2.82, and since the decimal part is truncated, 2 is returned. 
"""
class prob_69:
	def mySqrt(self, x: int) -> int:
		return int((x**(0.5))//1)

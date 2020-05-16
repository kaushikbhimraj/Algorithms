
"""
FIBONACCI SERIES
Print the nth fibonacci number in the series.
Solve the problem using recursion and iteration.  
"""

class Fibonacci:
	def __init__(self):
		self.memo = {}

	def recursive(self, n):
		if n in self.memo:
			return self.memo[n]
		if n == 0:
			return 1
		if n == 1:
			return 1
		value =  self.recursive(n-1) + self.recursive(n-2)
		return value

x = Fibonacci()
print(x.recursive(10))



"""
Fibonacci sequence can be quite tasking during computation. The best solution for this sequence is log n runtime which is highly unlikely to be asked during an interview. 
"""


class Fibonacci:

	def __init__(self):
		self.memo = {}

	# brute force (recursive)
	# runtime O(2^n)
	def fib_1(self, n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		return self.fib_1(n-1) + self.fib_1(n-2)

	# memoization (recursive)
	# runtime O(n)
	def fib_2(self, n):
		if n in self.memo.keys():
			return self.memo[n]
		if n == 0:
			return 0
		if n== 1:
			return 1
		f = self.fib_2(n-1) + self.fib_2(n-2)
		self.memo[n] = f
		return f

	# lean and mean (iterative)
	# runtime O(n)
	def fib_3(self, n):
		if n == 0:
			return 0 
		if n == 1:
			return 1
		a = 0
		b = 1
		for i in range(n-1):
			m = a + b
			a = b
			b = m
		return m

	# same logic in a bottom up method
	def fib_4(self, n):
		fib = {}
		for i in range(1, n+1):
			if i <= 2:
				f = 1
			else:
				f = fib[i-1] + fib[i-2]
			fib[i] = f
		return fib[n]

# Unit Test
x = 10
print(Fibonacci().fib_4(x))
print(Fibonacci().fib_3(x))
print(Fibonacci().fib_2(x))
print(Fibonacci().fib_1(x))
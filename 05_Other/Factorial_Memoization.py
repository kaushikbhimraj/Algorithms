
"""
Calculate the factorial of a number using memoization.
"""

class factMem:
	def __init__(self):
		self.cache = {}

	def calc(self, num):
		try:
			return self.cache[num]
		except KeyError:
			if num <= 1:
				return 1
			temp = num * self.calc(num-1)
			self.cache[num] = temp
			return temp

"""
print(factMem().calc(50))
"""
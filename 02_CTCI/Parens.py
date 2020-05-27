"""
PARENS:
Implement an algorithm to print all valid (i.e, properly opened and closed) combinations of n pairs of parentheses.
Input:  3
Output: ((())), (()()), (())(), ()(()), ()()()

Time Complexity:  O(2^n)
Space Complexity: O(n*(2^n))

Notes:
	Current code fails to implement the complete solution. Missing (()()) combo.
"""

class parens:
	def __init__(self):
		self.cache  = {}
		self.outstr = []


	# Build initial string.
	def build(self, pairs):
		parensStr = ""
		if pairs <= 0 or type(pairs) != int:
			return pairs
		for i in range(pairs):
			parensStr = "("+ parensStr +")"
		self.combo(pairs-1, pairs-1, pairs, parensStr)


	# Append all possible permutations to self.outstr.
	def combo(self, depth, i, j, string):
		if depth < 0:
			return
		if string in self.cache.keys():
			return
		
		self.cache[string] = string
		self.outstr.append(string)

		temp = string[i] + string[j] + string[:i] + string[j+1:]
		self.combo(depth-1, i+1, j+1, temp)
		
		string = string[:i] + string[j+1:] + string[i] + string[j]
		self.combo(depth-1, i-1, j-1, string)



x = parens()
x.build(4)
print(x.outstr)
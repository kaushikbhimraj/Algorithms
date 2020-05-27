"""
PERMUTATIONS WITHOUT DUPS
Write a method to computer all permutations of a string of unique characters. 

Notes:
	You are given a string 
	a = "kau"

	Your output would be 
	ka
	ku
	ak
	au
	uk
	ua

Time Complexity: O(n!) where n is the length of the input string.
"""

# Rather than passing the entire string on each in call in stack, 
# the string can be declared once in the constructor of the object and used 
# on every call without taking up extra space. 

class prm:
	def __init__(self, string):
		self.s      = list(string)
		self.length = len(string)

	def prmstr(self, i):
		if i == len(self.s)-1:
			print("".join(self.s))
			return
		else:
			for j in range(i, self.length):
				self.s[i], self.s[j] = self.s[j], self.s[i]
				self.prmstr(i+1)
				self.s[i], self.s[j] = self.s[j], self.s[i]


a = "abc"
prm(a).prmstr(0)
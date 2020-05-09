"""
Given two binary strings, return their sum (also a binary string). 
The input strings are both non-empty and contains only characters 1 or 0.

Example1: 
input: 	a = '11', b = '1'
output: '100'

input:  a =  '1010', b = '1011'
output: '10101'
"""

class prob_67:
	def addBinary(self, a:str, b: str) -> str:
		# Edge case
		if a == ' ' or b == '  ':
			return None

		# Logic will add from the end
		# Using a dictionary the system will compare all possible states of binary addition
		add = ''
		count = 1
		x = y = ''
		carry = '0'
		book = {
				"000":["0","0"],
				"001":["0","1"],
				"010":["0","1"],
				"011":["1","0"],
				"100":["0","1"], 
				"101":["1","0"], 
				"110":["1","0"], 
				"111":["1","1"]
				}
		length = max(len(a), len(b))

		while count <= length:

			if count > len(a):
				x = '0'
			else:
				x = a[-count]

			if count > len(b):
				y = '0'
			else:
				y = b[-count]

			carry, out = book[x+y+carry]
			add = out + add
			count += 1

		if carry == "1":
			carry,out = book[x+y+carry]
			return carry + add
		return add

c = "11"
v = "11"
print(prob_67().addBinary(c, v))


"""
Notes: Takes O(n) runtime where n is length of the longest of the two strings. 
	   Takes O(n) space. 
"""
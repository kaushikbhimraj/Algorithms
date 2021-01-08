"""
ZigZag Conversion
Question: 6

The string "PAYPALISHIRING" is written in zigzag pattern on a given number of rows like this: (you 
may want to display the pattern in a fixed font for better legibility)


Input: "PAYPALISHIRING", 3
Output: 

P   A   H   N
A P L S I I G
Y   I   R

this arrangement when written in an array can look like this 

PAHNAPLSIIGYIR

If n=4

P     I     N
A   L S   I G
Y A   H R
P     I

PINALSIGYAHRPI

"""

class ZigZag:
	def conversion(self, s: str, numRows: int):
		j = 0
		output = ""

		for j in range(numRows):
			i = k = 0

			while k < len(s):
				k = (2 * (numRows - 1) * i)
				before = k - j
				after  = k + j

				if before < 0:
					before = after

				if after > len(s) - 1:
					after = before

				if after < len(s):
					if before == after:
						output += s[after]
					else:
						if j == numRows - 1:
							output += s[after]
						else:
							output += s[before]
							output += s[after]

				i += 1
		return output[:-1]


# Driver Function
x = "PAYPALISHIRING"
print(ZigZag().conversion(x, 3))
print(ZigZag().conversion(x, 4))
print(ZigZag().conversion(x, 5))
print(ZigZag().conversion(x, 6))


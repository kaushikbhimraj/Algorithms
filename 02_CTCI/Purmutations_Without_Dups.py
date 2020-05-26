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
"""

def permuteString(i, string):
	if i == len(string)-1:
		print("".join(string))
		return
	else:
		for j in range(i, len(string)):
			string[i], string[j] = string[j], string[i]
			print(i, j, string)
			permuteString(i+1, string)
			string[i], string[j] = string[j], string[i]


a = "abc"
permuteString(0, list(a))
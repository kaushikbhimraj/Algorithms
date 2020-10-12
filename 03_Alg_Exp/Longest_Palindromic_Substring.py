"""
Write a function that, given a string, returns its longest palindromic substring. 
A palindrome is defined as a string that's written the same forward and backward. 
Note that single-character strings are palindromes. 

You can assume that there will only be one longest palindromic substring. 

INPUT:
string = "adaxyzzyxf"

OUTPUT:
xyzzyx
"""

def longestPalindrome(s:str)->str:
	s = s
	max_length = [0,1]

	# Look both ways (left and right) from the middle to check if values are the same. 
	# There are two kinds of palindromes, ODD and EVEN. 
	# Odd palidrome has a mid and even does not. 
	for i in range(1, len(s)):
		oddPalindrome = self.getPalindromicSize(s, i-1, i+1)
		evenPalindrome = self.getPalindromicSize(s, i-1, i)

		# Pick the maximum value from using a lambda, the key is a max *args. 
		maxOddEven = max(oddPalindrome, evenPalindrome, key=lambda x:x[1]-x[0])
		max_length = max(max_length, maxOddEven, key=lambda x:x[1]-x[0])

	# Slicing and returning the maximum palindrome from the string. 
	return s[max_length[0]:max_length[1]]

# When there is a break in the while loop, the indexs are going to be off by one. 
def getPalindromicSize(s, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(s):
		if s[leftIdx] != s[rightIdx]:
			break
		leftIdx  -= 1
		rightIdx += 1
	return [leftIdx+1, rightIdx]

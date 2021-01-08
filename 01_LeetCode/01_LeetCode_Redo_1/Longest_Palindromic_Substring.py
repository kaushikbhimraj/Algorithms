"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Time Complexity:  O(n^2)
Space Complexity: O(1)
"""

class Solution:
	def __init__(self):
		self.s = None

	def longestPalindrome(self, s:str)->str:
		self.s = s
		max_length = [0,1]

		# Look both ways (left and right) from the middle to check if values are the same. 
		# There are two kinds of palindromes, ODD and EVEN. 
		# Odd palidrome has a mid and even does not. 
		for i in range(1, len(self.s)):
			oddPalindrome = self.getPalindromicSize(i-1, i+1)
			evenPalindrome = self.getPalindromicSize(i-1, i)

			# Pick the maximum value from using a lambda, the key is a max *args. 
			maxOddEven = max(oddPalindrome, evenPalindrome, key=lambda x:x[1]-x[0])
			max_length = max(max_length, maxOddEven, key=lambda x:x[1]-x[0])

		# Slicing and returning the maximum palindrome from the string. 
		return self.s[max_length[0]:max_length[1]]

	# When there is a break in the while loop, the indexs are going to be off by one. 
	def getPalindromicSize(self, leftIdx, rightIdx):
		while leftIdx >= 0 and rightIdx < len(self.s):
			if self.s[leftIdx] != self.s[rightIdx]:
				break
			leftIdx  -= 1
			rightIdx += 1
		return [leftIdx+1, rightIdx]


# Test Cases
a = "babad"
b = "cdds"
c = "bb"
d = "aaaa"
e = "aabbccddd"

x = Solution()
print(x.longestPalindrome(a))
print(x.longestPalindrome(b))
print(x.longestPalindrome(c))
print(x.longestPalindrome(d))
print(x.longestPalindrome(e))
"""
Implement strStr()
Return the index of the first occurence of needle in heystack or -1 if needle is not part of haystack. 

Example 1:
input:  haystack = "hello", needle "ll"
output: 2

Exmaple 2:
input:  haystack = "aaaaa", needle = "bbe"
otuput: -1 

Example 3:
input:  akdlksdilsdksdfddsik
output: ik

"""

class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		# Gotta capture the sigle alphbet strings to skip all the bullshit. 
		if not needle:
			return 0
		if haystack == needle:
			return 0

		for i in range(len(haystack)-len(needle)+1):
			if haystack[i:i+(len(needle))] == needle:
				return i
		return -1

"""
The above logic is going to run in O(n) where n is the number of alphabets in haystack
These words are not sorted so we will have to run through all the alphabets. 
Each iteration, I am comparing a set of strings that are the length of the needle.
"""

haystack = "jawwork"
needle = "work"
print(Solution().strStr(haystack, needle))

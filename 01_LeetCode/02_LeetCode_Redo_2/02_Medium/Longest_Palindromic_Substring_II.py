"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
	def longestPalindrome(self, s):
		locations = [0,1]

		for i in range(1, len(s)):
			odd  = self.expandFromMid(s, locations, i-1, i+1)
			even = self.expandFromMid(s, locations, i-1, i)

			maxOddEven = max(odd, even, key=lambda x: x[1]-x[0])
			locations  = max(locations, maxOddEven, key=lambda x:x[1] - x[0])

		return s[locations[0]:locations[1]]


	def expandFromMid(self, s, locs, left, right):
		
		while left >= 0 and right < len(s):
			if s[left] != s[right]:
				break
			left -= 1
			right += 1

		return [left+1, right]
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

	# Break the problem into smaller chunks. 
	# Part 1: Check if the string is of even or odd length. 
	# 		  Check if every palindrome is the max length. 
	
	# Part 2: Check if the string contains palindrome.
	def longestPalindrome(self, s):
		max_length = [0, 1]

		for i in range(1, len(s)):
			# There are two types of palindromes,
			# 	Ezample 1: 	odd length
			# 	Example 2:  even length

			odd  = self.findPalindrome(i-1, i+1, s)
			even = self.findPalindrome(i-1, i, s)

			# Get the max of the two in each iteration.
			maxPalindrome = max(odd, even, key=lambda x: x[1]-x[0])

			# Update the maximum if it is a new maximum. 
			max_length = max(maxPalindrome, max_length, key=lambda x:x[1]-x[0])

		return s[max_length[0]:max_length[1]]


	# Program that would check if substring is a palindrome. . 
	def findPalindrome(self, leftIdx, rightIdx, string):

		while leftIdx > 0 and rightIdx < len(string):
			if string[leftIdx] != string[rightIdx]:
				break
			
			leftIdx += 1
			rightIdx -= 1
		return [leftIdx, rightIdx]

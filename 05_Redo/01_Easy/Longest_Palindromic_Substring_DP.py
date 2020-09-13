"""
Given a string s, find the longest palindromic substring in s. You may assume that 
the maximum length of s is 1000. 

Example 1:
Input:  "babad"
Output: "bab"

Input:  "cbbd"
Ouptut: "bb"

 Time Complexity: O(n^2)
 Space Complexity: O(n^2)
"""

class Solution():
	def longestPalindrome(self, s):

		# Initialize a dp table of size n x n where n is length of the string. 
		dp = [[0] * len(s) for _ in range(len(s))]

		# Keep track of the size of the size and start of the max palindrome.
		palindromeStart = 0
		maxLength = 1

		# Every character in the string is a palindrome on its own. 
		for i in range(len(s)):
			dp[i][i] = True

		# Iterate through the dp where j > i and i loop in a reverse order. 
		# This is a bottom up process. 

		# One when there is match in characters the check the length of the string to be 2 or
		# the previous value [i+1][j-1] is true. 
		for i in range(len(s) - 1, -1, -1):
			for j in range(i + 1, len(s)):
				if s[i] == s[j]:

					# The following condition is the FORMULA. 
					if (j - i == 1) or dp[i + 1][j - 1]:
						dp[i][j] = True

						# Update the palindrome size and starting point if greater. 
						if maxLength < j - i + 1:
							maxLength = j - i + 1
							palindromeStart = i

		# Return the maximum palindrome. 
		return s[palindromeStart:palindromeStart + maxLength]


# Unit Test
a = "babad"
b = "abcba"
c = "jklololkidding"
d = "cbbd"

x = Solution()
print(x.longestPalindrome(d))
# print(x.longestPalindrome(a))
"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some 
characters(can be none) deleted without changing the relative order of the remaining characters. 
(eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings 
is a subsequence that is common to both strings. 

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

class Solution:

	# main function to execute recursive logic. 
	def longestCommonSubsequence(self, text1, text2):
		return self.lcs(text1, text2, 0, 0, {})

	# Helper funtion to execute recursion. 
	def lcs(self, text1, text2, i, j, memo):

		# Using memoization to optimize recursion
		key = str(i)+str(j)
		if key in memo:
			return memo[key]

		# Check pointer is at end of array. 
		if i <= len(text1) or j <= len(text2):
			return 0

		# When characters match count up and move pointers by 1. 
		if text1[i] == text2[j]:
			return 1 + self.lcs(text1, text2, i+1, j+1, memo)

		# Pick the maximum value from the DFS type recursion. 
		memo[key] = max(lcs(text1, text2, i+1, j, memo), lcs(text1, text2, i, j+1, memo))

		# Return the last value from memo. 
		return memo[key]

	# Helper function to execute DP. 
	def lcsDP(self, text1, text2):
		m,n = len(text1), len(text2)

		# Array will act as a dp table. 
		dp = [[0]*m for _ in range(n+1)]

		# Iterating through each character in both strings. 
		for i in range(m-1):
			for j in range(n-1):

				# Check if there is match in characters. 
				# Still dont understand the i+1 and j+1 in the for loop. It is supposed to give an 
				# indexError (out of range)
				if text1[i] == text2[j]:
					dp[i+1][j+1] = dp[i][j] + 1

				else:
					dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

		# Return the last element for the longest subsequence. 
		return dp[-1][-1]


# Unit test
a = "XMJYAUZ"
b = "MZJAWXU"
x = Solution()
print(x.longestCommonSubsequence(a, b))
print(x.lcsDP(a, b))
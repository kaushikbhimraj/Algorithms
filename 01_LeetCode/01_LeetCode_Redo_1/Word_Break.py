"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""
class Solution:
	def wordBreak(self, s, words):

		# 1-D dp array. 
		d = [False] * len(s)

		# Iterate through each character in string. 
		# You want to check if the word in the dictionary is in the string and also that the string does have any negative # values in the previous iteration. 
		for currPos in range(len(s)):
			for word in words:

				if word == s[currPos - len(word)+1: currPos+1] and (d[currPos - len(word)] or currPos - len(word) == -1):
					d[currPos] = True

		# The end value will have the final check. 
		return d[-1]

# Unit Test
a = "leetcode"
b = ["leet","code"]

x = Solution()
print(x.wordBreak(a, b))
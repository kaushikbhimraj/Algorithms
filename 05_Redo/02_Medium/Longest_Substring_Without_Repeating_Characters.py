
"""
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
Given a string, find the length of the longest substring without repeating characters. 

Example 1:
	Input:  "abcabcbb"
	Output:  3
	Exp: 	This answer is "abc"

Example 2:
	Input:	"bbbbb"
	Output: 1
	Exp: 	The answer is "b", with the length of 1. 

Example 3:
	Input: 	"pwwkew"
	Output: 3
	Exp: 	The answer is "wke", with the lenght of 3. 
			Note that the answer must be a substring, "pwke" is a subsequence and not a substring. 
"""

class Solution:
	def lengthOfLongestSubstring(self, s:str) -> int:

		cache = {}
		maxcount = count = 0

		for i in range(len(s)):
			
			if count > maxcount:
				maxcount = count
			try:
				cache[s[i]]
				count = 0
			except KeyError:
				cache[s[i]] = i
				count += 1

		return maxcount



x = "pwwkew"
print(Solution().lengthOfLongestSubstring(x))
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not asubstring
"""


class Solution:

	def lengthOfLongestSubstring(self, s: str) -> int:
		"""
		Iterate through the list using a pointer.
		Store all indexes of values in dictionary.
		Value is already in dictionary, 
			- update pointer with that index. 
			- reset dictionary to empty.
			- reset counter to zero.

		Keep incrementing counter when value not in dictionary.
		"""
		cache = {}
		maxc = c = i = 0

		while i < len(s):

			try:
				i = cache[s[i]]
				cache = {}
				c = 0

			except KeyError:
				cache[s[i]] = i
				c += 1

			if maxc < c:
				maxc = c

			i += 1
		return maxc


	"""
	Method below is a lot more efficient than the above. 
	"""
	def lengthOfLongestSubstring_1(self, s: str) -> int:
		if not s:
			return 0

		maxc = 1
		index_1 = 0
		index_2 = 0 

		while index_2 < len(s):

			if s[index_2] not in s[index_1: index_2]:
				index_2 += 1
			else:
				index_1 += 1

			# Update the max length after the indexes are readjusted. 
			if len(s[index_1: index_2]) > maxc:
				maxc = len(s[index_1: index_2])

		return maxc


x = Solution()

a = "abcabcbb"
b = "pwwkew"  
c = "bbbbbb"
d = "aab"
e = "dvdf"
f = ""

print(x.lengthOfLongestSubstring(a))
print(x.lengthOfLongestSubstring(b))
print(x.lengthOfLongestSubstring(c))
print(x.lengthOfLongestSubstring(d))
print(x.lengthOfLongestSubstring(e))
print(x.lengthOfLongestSubstring(f))

print("\n")
print(x.lengthOfLongestSubstring_1(a))
print(x.lengthOfLongestSubstring_1(b))
print(x.lengthOfLongestSubstring_1(c))
print(x.lengthOfLongestSubstring_1(d))
print(x.lengthOfLongestSubstring_1(e))
print(x.lengthOfLongestSubstring_1(f))


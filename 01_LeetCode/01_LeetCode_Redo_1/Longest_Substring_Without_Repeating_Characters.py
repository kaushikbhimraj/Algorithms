"""
Question:
	ID:   3
	Name: Longest Substring Without Repeating Characters
	Desc:
	Given a string find the length of the longest substring without repeating characters. 

	Input: 			"abcabcbb"
	Output: 		3
	Explanation:	The answer is "abc", with the length of 3. 

	Input: 			"bbbbb"
	Output:			1
	Explanation: 	The answer is "b", with the length of 1. 

	Input: 			"pwwkew"
	Output: 		3
	Explanation: 	The answer is "wke", with the length of 3. 
					Note that the answer must be a substring, "pwke" is a subsequence and not a substring

Tho whole point of this program is be able to check and see if you have a value already present in the 
string. For this a dictionary would be the best strategy. Next issue to address is to count up whenever
the dictionary does not have values and reset the counter to 1 if there a value present in the consecutive 
sequence. So we need one more variable to keep the max count. 
"""


class LongSubstring:
	
	def __init__(self):
		self.memo = {}

	# Main method
	def lengthOfLongestSubstring(self, s):
		maxcount = 1
		count = 1
		# Run through the string once
		for val in s:
			if count > maxcount:
				maxcount = count

			if not self.check(val):
				self.memo[val] = val
				count += 1
			else:
				count = 1
		return maxcount

	# Helper method to check if the value is present in the dictionary.
	def check(self, val):
		try:
			self.memo[val]
			return True
		except KeyError:
			return False

# Driver Code
s = "pwwkew"
print(LongSubstring().lengthOfLongestSubstring(s))
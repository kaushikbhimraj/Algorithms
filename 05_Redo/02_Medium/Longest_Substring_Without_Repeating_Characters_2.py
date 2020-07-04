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
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Time Complexity:  O(n)
Space Complexity: O(min(s, previousValue)) 
"""

class Solution:
	def lengthOfLongestSubstring(self, s:str) -> int:

		# Need a way to track if the char in the string is a repeat. Using dictionary for that. 
		# Record the maximum distance in an array. 
		# Need another pointer in the array that would act as a start index. 
		previousValue = {}
		locations = [0, 1]
		startIdx  = 0

		for index, char in enumerate(s):

			# startIdx will have be updated if the value is already in the previousValue dictionary. 
			# startIdx will be the one index after the index found in dictionary and max of startIdx & previousValue.
			if char in previousValue:
				startIdx = max(startIdx, previousValue[char] + 1)

			# Update locations if the substring length is greater than what is already present. 
			if locations[1] - locations[0] < index+1 - startIdx:
				locations = [startIdx, index+1]

			# Every iteration update dictionary. 
			previousValue[char] = index

		# Here you have choice to return the entire string or just its length. 
		return locations[1]-locations[0]

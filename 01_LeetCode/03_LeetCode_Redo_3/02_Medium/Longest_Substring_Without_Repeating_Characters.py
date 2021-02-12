"""
Given a string s, find the length of the longest substring without repeating characters. 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0
"""
# T: O(n); S: O(n) where n is length of given string. 
class Solution:

	# Have two pointers. 
	# Every iteration add current value and its location into a dictionary
	# If character at right pointer exists in the dictionary, move the left pointer to the dictionary position + 1
	# Note: Make sure left pointer is always moving from left to right (if i <= dictionary[right pointer])
	# Every iteration update max for length between left and right pointer. 
	# return teh max length. 
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        locations = {}
        i, j = 0, 0
        size = 0
        while (j < len(s)):
            if (s[j] in locations and i <= locations[s[j]]):
                i = locations[s[j]] + 1
            
            locations[s[j]] = j
            size = max(size, j - i + 1)
            j += 1
        return size
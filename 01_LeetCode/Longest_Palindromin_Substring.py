"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

Example 3:
input:  "xxacvcbabcxcbaxx"
input:  "xxasdafassdfasdmadamlkjalkjdsaf"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

    	# Variables
        length_of_string = len(s)
        center = right = 0

        # Check for edge-cases
        if length_of_string > 1000 or not s:
        	return None

        # Convert length from even to odd
        if length_of_string%2:
        	s = "#".join(s)
        	temp = 1

        # Create an array of same size as string.
        pally_length = [0] * length_of_string
        pally_length[0] = 1

        # Iterating through each character.

        for num in range(length_of_string):
        	
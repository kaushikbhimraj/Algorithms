"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one 
letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, 
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
 

Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""

class Solution:
	def longesetStrChain(self, words):

		dp = dict()
		maxvalue = 0

		# Fill all the value stored in the dictionary to 1. 
		for word in words:
			dp[word] = 1

		# It is essential for the words array to be sorted based on the length of words in it. 
		for word in sorted(words, key=len):
			for i in range(len(word)):

				# Remove a single character from the word
				new_word = word[i:] + word[i+1:]

				# Check if the new_word is in dictionary
				if new_word in dp:

					# This is the core logic
					dp[word] = max(dp[word], 1 + dp[new_word])
			
			# Update the longest values with the maxvalue after trying all combinations of the word. 
			longest = max(dp[word], longest)

		return longest



"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

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
    def longestStrChain(self, words: List[str]) -> int:
        
        # Create a dictionary to hold chain length
        # dictionary -> word: chain length
        dp = dict()
        for word in words:
            dp[word] = 1
        
        # Keep track of the longest string chain
        # Sort words based on length, as you want to look at the previous chain length and build on it.
        longest = 0
        for word in sorted(words, key=len):
            for i in range(len(word)):
                
                # Skipping a specific alphabet each iteration. 
                prevWord = word[:i] + word[i+1:]
                
                # Check if the prevWord exists in the dictionary
                # If exists, take max of value for the current word or 1 + value for the previous word in dictionary.
                if prevWord in dp:
                    dp[word] = max(dp[word], dp[prevWord]+1)
            
            # Update longest variable.
            longest = max(longest, dp[word])
        return longest
"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        # basic assumption is that word1 and word2 are not same.
        # declaring distance to keep tracking of min distance b/w words.
        distance = float("inf")        
        word1_idx, word2_idx = -1, -1
        distance = float("inf")
        
        # traverse through nums, when word matches record location
        for i in range(len(words)):
            
            if word1 == words[i]:
                word1_idx = i
                
            if word2 == words[i]:
                word2_idx = i
            
            # check if location of word1 - location of word2 < previous
            if word1_idx != -1 and word2_idx != -1:
                distance = min(distance, abs(word1_idx - word2_idx))
        
        return distance
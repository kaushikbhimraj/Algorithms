"""
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
 
Example 1:
Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).

Example 2:
Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.

Example 3:
Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3

Example 4:
Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0
 
Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
"""

# Iterate the string using a set window size. For the window size the lowest one as maxSize doesn't have to be used. 
# Each iterate check if the word is in dictionary and increment count if substring is already present. 
# Based on the rule in the question, add to dictionary only if the distinct characters in substring don't exceed maxLetter. 

# Make sure to return 0 if the counts dictionary is unpopulated.
# Else simply return the max count from the dictionary values. 

# T: O(n); S: O(n) where n is length of string. 

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = {}
        
        for i in range(len(s)-minSize+1):
            word = s[i:i + minSize]
            
            if word in counts:
                counts[word] += 1
            else:
                if len(set(word)) <= maxLetters:
                    counts[word] = 1
            
        return max(counts.values()) if len(counts) != 0 else 0
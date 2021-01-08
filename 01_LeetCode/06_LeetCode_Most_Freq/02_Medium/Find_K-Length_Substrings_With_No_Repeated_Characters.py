"""
Given a string S, return the number of substrings of length K with no 
repeated characters.

Example 1:
Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

Example 2:
Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to 
find any substring.
"""

class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if K > len(S):
            return 0
        
        count = 0
        for i in range(len(S)-K+1):
            if len(set(S[i:i+K])) == K:
                count += 1
        return count
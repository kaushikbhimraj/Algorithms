"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
 
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        start = 0
        length = 1
        
        for i in range(len(s)):
            dp[i][i] = True
        
        # If s[i] and s[j] are the same, then check the substring length is atleast 
        # length of 2 or the previous value (diagonal value) is True. 
        # If one of the above conditions are satisfied, update max length.
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if (s[i] == s[j]):
                    if (j-i == 1 or dp[i+1][j-1]):
                        dp[i][j] = True
                        
                        if (j-i+1 > length):
                            start = i
                            length = j-i+1
        return s[start:start+length]
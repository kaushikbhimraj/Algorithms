"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different 
substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Note:
The input string length won't exceed 1000.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            dp[i][i] = 1
            ans += 1
        
        # Populate the DP array by checking the conditions on the input array. 
        # Key for using a DP array is to check for previous value and not doing repetitive work. 
        # Here we are going from left to right column and traversing each column top to bottom. 
        for j in range(len(dp[0])):
            for i in range(0, j):
                if (j-i == 1 and s[i] == s[j]):
                    dp[i][j] = 1
                    ans += 1
                elif (i+1 < len(s) and dp[i+1][j-1] == 1 and s[i] == s[j]):
                    dp[i][j] = 1
                    ans += 1
        return ans
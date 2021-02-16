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
        dp = [[0]*len(s) for _ in range(len(s))]
        ans = 0
        for i in range(len(s)):
            dp[i][i] = 1
            ans += 1
        
        for col in range(len(dp[0])):
            for row in range(0, col):
                if (col-row==1 and s[row] == s[col]):
                    dp[row][col] = 1
                    ans += 1
                elif (row+1 < len(dp) and dp[row+1][col-1] == 1 and s[row] == s[col]):
                    dp[row][col] = 1
                    ans += 1
        return ans
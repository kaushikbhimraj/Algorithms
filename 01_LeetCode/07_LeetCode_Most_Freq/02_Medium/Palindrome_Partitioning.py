"""
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

# T: O(N.2^N) where N is length of string. 
# S: O(N)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
    
    # Helper function to run DFS
    def dfs(self, s, curr, res):
        if not s:
            res.append(curr[:])
            return 
        
        # if we start from 0, recursion stack will exceed memory 
        # as pointer will always stay at zero. 
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], curr+[s[:i]], res)
    
    # Standard check for palindrome
    def isPalindrome(self, s):
        low, high = 0, len(s)-1
        while low < high:
            if (s[low] != s[high]):
                return False
            low += 1
            high -= 1
        return True
"""
LC: 3 Longest Substring Without Repeating Characters

Given a string s, return the length of the longest substring that contains only unique
characters. 

Ex: Given the following string s...
s = "ababbc", return 2. 

Ex: Given the follwing string s...
s = "abcdssa", return 5.

T: O(n)
S: O(n)
where n is length of string.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (not s):
            return 0
        
        # Two Pointers i & j
        # Hash Map
        mem = {}
        i, res = 0, 0
        
        # Iterate string and check if value is in hash map, 
        # 	Not in hash map -> update consecutive count +1 and check max count. 
        # 	In hash map     -> check position where character was last occuring in string 
        #                      and move i to i+1 
        for j in range(len(s)):
            char = s[j]
            if (char in mem):
                i = max(mem[char]+1, i)
            
            res = max(res, j - i + 1)
            mem[char] = j
        return res
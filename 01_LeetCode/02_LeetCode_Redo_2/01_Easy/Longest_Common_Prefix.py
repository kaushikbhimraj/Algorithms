"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Lame edge-case
        if not strs:
            return ""
        
        prefix = strs[0]
        # Key trick here: check if the prefix is at position '0'. Should know how to use find. 
        # If not keep reducing the string by one. 
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
        
        return prefix
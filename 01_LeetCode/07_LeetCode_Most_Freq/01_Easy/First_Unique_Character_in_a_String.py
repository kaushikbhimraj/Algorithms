"""
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

Note: You may assume the string contains only lowercase English letters.
"""

# T: O(n); S: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count alphabet repetitions in string. 
        alp = [0] * 26
        for i in range(len(s)):
            alp[ord(s[i])-97] += 1
        
        # Unicode representation of the letters in the string. 
        counts = [ord(s[x])-97 for x in range(len(s))]
        
        for i in range(len(counts)):
            if alp[counts[i]] == 1:
                return i
        return -1
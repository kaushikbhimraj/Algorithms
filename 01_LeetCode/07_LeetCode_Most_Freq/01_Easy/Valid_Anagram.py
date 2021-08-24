"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Not an anagram if string size is different.
        if len(s) != len(t):
            return False
        
        # Count characters in string and store count in dictionary.
        cache = {}
        for val in s:
            if val in cache:
                cache[val] += 1
            else:
                cache[val] = 1
                
        # Iterate through t and decrement count in dictionary if string exists. 
        for i in range(len(t)):
            if t[i] not in cache or not cache[t[i]]:
                return False
            else:
                cache[t[i]] -= 1
        return True

# Solve Next
# 49. Group Anagram
# 438. Find All Anagrams in a String
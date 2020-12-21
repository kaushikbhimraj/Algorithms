"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # E.g: for "abbccc" we can store {(1,2,3,0,0,0,0,...0): [abbccc, bbaccc,cacbcb]}
        combinations = {}
        
        # Iterate through each string in strs. 
        for string in strs:
            
            # There are 26 alphabets. 
            count = [0] * 26
            # Iterate through each alphabet in string. 
            for s in string:
                count[ord(s) - ord('a')] += 1
            
            # Add the combination to dictionary if it doesn't already exist. 
            if tuple(count) in combinations:
                combinations[tuple(count)].append(string)
            else:
                combinations[tuple(count)] = [string]
        
        return combinations.values()

# Similar
# Group Shifted Strings

"""
Given a string, we can "shift" each of its letter to its successive letter, 
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group 
all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Each string sequence will have a fixed length. Based on string length, 
        # string can be stored in a dictionary and values can be returned. 
        results = {}
        for string in strings:
            
            # The trick in solution is to create the key. 
            # Create the key using the distance between characters in string. 
            # If the distances are consistent, then we can store in value array. 
            # This conviniently solves our string size problem as well. 
            key = ()
            for i in range(len(string) - 1):
                dist = ord(string[i+1]) - ord(string[i])
                key += (dist % 26,)
            if key in results:
                results[key].append(string)
            else:
                results[key] = [string]
            
        return results.values()


# Similar:
# Simplify Path
# Max Points on a Line
# Prison Cells After N Days

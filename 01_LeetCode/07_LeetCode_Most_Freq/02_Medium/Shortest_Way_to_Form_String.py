"""
From any string, we can form a subsequence of that string by deleting some number of characters 
(possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that 
their concatenation equals target. If the task is impossible, return -1.

Example 1:
Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source 
"abc".

Example 2:
Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due 
to the character "d" in target string.

Example 3:
Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".

Constraints:
Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
"""

# Two pointers: 1 for source and 1 for target
# For each character in target, check if it exists in source. 
# If so, increment both pointers to check if the next characters match as well. 
# If it doesn't, match increment only the source pointer. 
# In the end, if the character in target doesn't match anything in source return -1.
# Use a flag to understand if we have a match. 
# Each iteration update the counter. 

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        tar = 0 
        num = 0
        while (tar < len(target)):
            src = 0
            flag = False
            while (src < len(source) and tar < len(target)):
                if source[src] == target[tar]:
                    src += 1
                    tar += 1
                    flag = True
                else:
                    src += 1
            
            if flag:
                num += 1
            else:
                return -1
        return num
"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the 
number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not 
map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

input: 
"23"

output:
['ad']
['ad', 'ae']
['ad', 'ae', 'af']
['ad', 'ae', 'af', 'bd']
['ad', 'ae', 'af', 'bd', 'be']
['ad', 'ae', 'af', 'bd', 'be', 'bf']
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd']
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce']
['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""

class Solution:
    def __init__(self):
        self.strs = ["0","1","abc","def","ghi","jkl","mno", "pqrs","tuv", "wxyz"]
        
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        self.helper(res, digits, "", 0)
        return res
    
    def helper(self, res, digits, curr, idx):
        if idx == len(digits):
            res.append(curr[:])
            return 
        
        letters = self.strs[ord(digits[idx]) - ord("0")]
        for i in range(len(letters)):
            self.helper(res, digits, curr + letters[i], idx+1)
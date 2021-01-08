"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and 
ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a set containing all alphabets in English. 
        # Convert all characters in 's' to lower case for ease. 
        alpha = set("abcdefghijklmnopqrstuvwxyz0123456789")
        s = s.lower()
        
        # Start from both ends of the string and check character at position in set. 
        # If not in set, increment/decrement pointer. 
        # If character in set check value at both pointers. 
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l] not in alpha:
                    l += 1
                elif s[r] not in alpha:
                    r -= 1
                else:
                    return False
        return True
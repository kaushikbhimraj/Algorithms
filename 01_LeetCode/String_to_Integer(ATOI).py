
"""
Date:       03.29.2020
LeetCode:   #8
Question:   
Implement ASCII to Integer(atoi) which converts a string to an integer. 

The function first discards as many whitespace characters as necessary until the first non-whiespace
character is found. Then, starting from this character, takes an optional initial plus or minus sign followed
by as many numerical digits as possible, and inteprets them as a numerical value. 

The string can contain additional characters after those that form the integral number, which are ignored and
have no effect on the behaviour of the function. 

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence
exists because either str is empty or it contains only whitespace characters, no conversion is performed. 

If no valid conversion could be performed, a zero value is returned. 

Note:
    Only the space character ' ' is considered as whitespace character. 
    Assume we are dealing with an environment which could only store integers within the 32-bit signed 
    integer range of [2^-31, 2^31 - 1]. If the numerical value is out of the range of representable value, 
    INT_MAX (2^31-1) or INT_MIN(-2^31) is returned. 
    
    

EXAMPLE:
    Input:  "42"
    Output:  42
    
    Input:  "-42"
    output: -42
    
    Input:  "4193 with words"
    Output: 4193
    
    Input:  "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. 
    
"""

class Solution:
    def __init__(self):
        self.num = {'-':'-', 
                    '.':'.', 
                    '0':'0', 
                    '1':'1', 
                    '2':'2', 
                    '3':'3', 
                    '4':'4', 
                    '5':'5', 
                    '6':'6', 
                    '7':'7', 
                    '8':'8', 
                    '9':'9'}
        
    def myAtoi(self, s:str) -> int:
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                try:
                    self.num[s[i]]
                except KeyError:
                    break
                i += 1
            
        if i <= 1:
            return 0
        try:
            return self.num_range(int(s[:i]))
        except:
            return self.num_range(float(s[:i]))
        
    def num_range(self, num):
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        else:
            return num
            
x = "     -42.2812"
y = Solution().myAtoi(x)
print(y)
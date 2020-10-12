
"""
Date:     04.01.2020
Question: 12
Roman numerals are represented by seven different symbols I, V, X, L, C, D and M. 

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        
For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is sharply X + II. The number twenty seven is written as XXVII, which is 
XX + V + II. 

Roman numerals are usually written largest to smallest from left to right. However, the numercal for four 
is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it
making four. The same principle applies to number nine, which is written as IX. There are six instances 
where subtraction is used:

    - I can be placed before V (5) and X (10) to make 4 and 9. 
    - X can be placed before L (50) and C (100) to make 40 and 90
    - C can be placed before D (500) and M (1000) to make 400 and 900. 
    
Given an integer, convert it to a roman numeral, input is guaranteed to be within the range from 1 to 3999. 

EXAMPLE:
    Input:  3
    Output: "III"
    
    Input:  4
    Output: "IV"
    
    Input:  9
    Output: "IX"
    
    Inptut: 58
    Output:  "LVIII"
    
    Input:  1994
    Output: "MCMXCIV"

Notes:
    Since there is a limit given which is 3999, the numbers will not exceed 1000, so we start with 1000. 
    Each digit starting from the left, is ran through conditions. 
    If the condition is 4 the you will have to multiple 5*dictionary[times] + dictioanary[times]
    and this way each condition is analyzed. The roman is concatenated from the end since the 
    number is considered from left to right.
"""
class Roman:
    def __init__(self):
        self.romans = {1:"I", 
                       5:"V", 
                       10:"X", 
                       50:"L", 
                       100:"C", 
                       500:"D", 
                       1000:"M"}
    
    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:
            return 
        
        times = 1000
        romannum = ""
        while times >= 1:
            digit = num//times
            if digit < 4:
                romannum += digit*self.romans[times]
            elif digit == 4:
                romannum += self.romans[times] + self.romans[5*times]
            elif digit == 5:
                romannum += self.romans[times*digit]
            elif 5 < digit < 9:
                romannum += self.romans[5*times*] + (digit-5)*self.romans[times]
            elif digit == 9:
                romannum += self.romans[times] + self.romans[10*times]
            
            num = num%times
            times = int(times/10)
        return romannum

# Driver Code
print(Roman().intToRoman(3))
print(Roman().intToRoman(4))
print(Roman().intToRoman(9))
print(Roman().intToRoman(58))
print(Roman().intToRoman(1994))
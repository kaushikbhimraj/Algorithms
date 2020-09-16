"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Choose the bigger string off the two given strings. 
        # The following unpacks into max string, max length, min string, min lenght respectively. 
        b, bl, s, sl = (a, len(a)-1, b, len(b)-1) if len(a) >= len(b) else (b, len(b)-1, a, len(a)-1)
        
        # Initializing variables to store output string and running carry. 
        carry = "0"
        result = ""
        
        # Loop through the range of min length and perform binary addition on each bit. 
        while (sl >= 0):
            # List conditions. 
            if carry == "1":
                if (b[bl] == "0" and s[sl] == "1") or (b[bl] == "1" and s[sl] == "0"):
                    result = "0" + result
                    carry = "1"
                
                elif (b[bl] == "1" and s[sl] == "1"):
                    result = "1" + result
                    carry = "1"
                    
                else:
                    result = carry + result
                    carry = "0"
            else:
                if (b[bl] == "0" and s[sl] == "1") or (b[bl] == "1" and s[sl] == "0"):
                    result = "1" + result                    
                    carry = "0"
                
                elif (b[bl] == "1" and s[sl] == "1"):
                    result = "0" + result
                    carry = "1"
                
                else:
                    result = "0" + result
            bl -= 1
            sl -= 1
        
        # Add the carry to the remain bits in the max length string. 
        while (bl >= 0):
            if carry == "0":
                return b[:bl+1] + result
            else:
                if b[bl] == "1":
                    result = "0" + result
                    carry = "1"
                else:
                    result = "1" + result
                    carry = "0"
            bl -= 1
        
        # Finally check carry is not holding a value, return appropriately. 
        return result if carry != "1" else carry + result
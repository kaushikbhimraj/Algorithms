"""
Given a string s containing only digits, return all possible valid IP addresses 
that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 
and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" 
and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and 
"192.168@1.1" are invalid IP addresses. 

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
Constraints:
0 <= s.length <= 3000
"""

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # Check if given string is between size 4 and 12. 
        if not (4 <= len(s) <= 12):
            return []
        
        # Helper function is used to backtrack. 
        # Params: pointer(idx), running array(curr)
        # Terminal condition:
        #         a. Check if length the running array is 4. 
        #              a-1. Check if pointer is at end of string s. (If so, add the current array to result)
        # Recursive condition:
        #         a. Try with substring of length 1, 2 & 3 (based on pointer: pointer+1,... pointer+3)
        #         b. If a substring is starting with '0' and its length is greater than 1, skip!
        #         c. Only when substring is between integer value 0 and 255, continue recursion
        #               Append the current substring to current array
        #               Use the loop index+1 as pointer in recursion.
        #               Note: Make sure to pop off the value after the recursion stack is popped.
        # Return the result array. 
        
        def helper(idx, curr):
            # Terminal condition
            if (len(curr) == 4):
                nonlocal res
                if (idx == len(s)):
                    res.append(".".join(curr))
                return
            
            # Recursion condition
            num = ''
            for i in range(idx, min(idx + 3, len(s))):
                num += s[i]
                
                if (num[0] =='0' and len(num) > 1):
                    break
                
                if (0 <= int(num) <= 255):
                    curr.append(num)
                    helper(i+1, curr)
                    curr.pop()
        
        res = []
        helper(0, [])
        return res
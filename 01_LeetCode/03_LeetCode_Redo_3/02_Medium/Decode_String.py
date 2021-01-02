class Solution:
    def decodeString(self, s: str) -> str:
        if (len(s) == 1):
            return s
        # If string contains nested brackets, best to use stacks. 
        stack = []
        res = ""
        
        # T: O(n); S: O(n)
        for i in range(len(s)):
            if (s[i] == "]" or s[i] == "["):
                continue
            else:
                stack.append(s[i])
                
        # T: O(n);
        i = len(stack)
        val = stack.pop()
        while stack:
            num = ""
            in_string = ""
            
            while (stack and not val.isdigit()):
                in_string = val + in_string
                val = stack.pop()
            
            while (stack and val.isdigit()):
                num = val + num
                val = stack.pop()
                
            if num:
                in_string = in_string * int(num)
                res = in_string + res
            else:
                continue
        
        # Messy!
        if (val.isdigit()):
            in_string = in_string * int(val)
        else:
            in_string = val + in_string
        res = in_string + res
        
        return res

"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] == "]":
                val = stack.pop()
                inString = ""
                
                while (stack and val != "["):
                    inString = inString + val
                    val = stack.pop()
                
                print(inString)
            else:
                stack.append(s[i])
"""
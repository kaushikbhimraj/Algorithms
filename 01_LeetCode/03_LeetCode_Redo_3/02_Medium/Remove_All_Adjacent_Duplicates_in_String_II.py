class Solution:

    # T: O(n^2/k); S: O(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # Convert string to array. 
        # Use pointer to traverse array and remove adj characters that match count k.
        # Make user to move pointer back after remove an element until it reaches count == 1. 
        def helper(string):
            strArray = list(string)
            n = len(strArray)
            i, count = 1, 1
            
            while (i < n):
                
                if (strArray[i] != strArray[i-1]):
                    count = 1
                else:
                    count += 1
                
                # Most important step. 
                # This part has to always come after the counter is update based on adjacent match.
                if (count == k):
                    while (count > 0):
                        strArray.pop(i)
                        i -= 1
                        count -= 1
                
                # Update array length after every iteration. 
                i += 1
                n = len(strArray)
            
            return "".join(strArray)
        
        # Nested function to make sure there are no duplications of length k. 
        prev = ""
        while (prev != s):
            prev = s
            s = helper(s)
        return s

    # Using the stack, we load the character in string, if the next string is the same simply count up
    # Else add the value with count to string. 
    # When the count is == k, then pop the top value in array. 
    # Returnt the stack and then use the left over characters and their counts to be concatenated to the 
    # new string and return it. 
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[s[0], 1]]
        
        for i in range(1, len(s)):
            if (not stack or s[i] != stack[-1][0]):
                stack.append([s[i], 1])
            else:
                stack[-1][1] += 1
                if (stack[-1][1] == k):
                    stack.pop()
        
        res = ""
        for char, count in stack:
            res += (char * count)
        return res
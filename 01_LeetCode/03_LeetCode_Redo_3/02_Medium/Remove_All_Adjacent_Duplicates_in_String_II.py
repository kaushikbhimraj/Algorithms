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
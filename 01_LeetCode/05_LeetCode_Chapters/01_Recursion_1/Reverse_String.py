class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(0, len(s)-1, s)
        return s
    
    def helper(self, l, r, s):
        if (l >= r):
            return 

        self.helper(l+1, r-1, s)
        s[l], s[r] = s[r], s[l]
        

x = Solution()
print(x.reverseString(["H","a","n","n","a","h"]))
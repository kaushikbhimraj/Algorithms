"""
A message containing letters from `A-Z` can be **encoded** into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To **decode** an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping 
above (there may be multiple ways). For example, `"11106"` can be mapped into:

- `"AAJF"` with the grouping `(1 1 10 6)`
- `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return *the **number** of ways to **decode** it*.

The answer is guaranteed to fit in a **32-bit** integer.
"""
# Simple recursion: Brute Force
class Solution:
    def numDecodings(self, s: str) -> int:
        if (not s):
            return 0
        return self.ways(0, s)
    
    def ways(self, i, s):
        if (i == len(s)):
            return 1
        
        if (s[i] == "0"):
            return 0
        
        if (i == len(s)-1):
            return 1
        
        return self.ways(i+1, s) + (self.ways(i+2, s) if (int(s[i:i+2]) <= 26) else 0)

# Optimized: Memoization
class Solution:
    def __init__(self):
        self.pos = {}
    
    def numDecodings(self, s: str) -> int:
        if (not s):
            return 0
        return self.ways(0, s)
    
    def ways(self, i, s):
        if (i == len(s)):
            return 1
        
        if (s[i] == "0"):
            return 0
        
        if (i in self.pos):
            return self.pos[i]
        
        if (i == len(s)-1):
            return 1
        
        self.pos[i] = self.ways(i+1, s) + (self.ways(i+2, s) if (int(s[i:i+2]) <= 26) else 0)
        return self.pos[i]
        
        # Recursion here is two part. 
        # Jump once for a single digit possibility. 
        # Jump twice for a double digit possibility. (Need to check if is within range)
        self.memo[i] = self.helper(i+1, s) + (self.helper(i+2, s) if (int(s[i:i+2]) <= 26) else 0)
        return self.memo[i]
"""
Testcases:
["flower","flow","flight"]
[]
[""]
["a"]
["elephant","feel","eel"]
["aac","a","ccc"]
["c","c"]
["aa","a"]
["acc","aaa","aaba"] --> failed
"""
class prob_14:
    def longestCommonPrefix(self, strs):
        # Edge cases
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        for i in range(1, len(strs)):
            leftover = self._difference(strs[i-1], strs[i])
            if not leftover:
                return ""
        return leftover
    
    # Helper function
    def _difference(self, word1, word2):
        if word1 == word2:
            return word1
        temp_str = ""
        i = 1 
        length = min(len(word1), len(word2))
        word1 = word1[:length]
        word2 = word2[:length]
        while i <= length:
            if word1[:-i] == word2[:-i]:
                temp_str = word1[:-i]
                return temp_str
            else:
                temp_str = ""
            i += 1
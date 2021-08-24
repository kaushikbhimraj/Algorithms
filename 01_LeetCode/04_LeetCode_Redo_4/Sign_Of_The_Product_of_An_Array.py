class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 0
        for num in nums:
            if num == 0:
                sign = -1
                break
            if num < 0:
                sign += 1
 
        if (sign == -1):
            return 0
        elif (not sign % 2):
            return 1
        elif (sign % 2):
            return -1
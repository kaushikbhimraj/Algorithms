class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if (len(nums) <= 1):
            return []
        
        output = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            val = nums[i]
            l = i + 1
            r = n - 1
            while (l < r):
                if (nums[l]+nums[r] == -1 * val):
                    output.add((val, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif (nums[l]+nums[r] > -1 * val):
                    r -= 1
                else:
                    l += 1
        return [list(a) for a in output]